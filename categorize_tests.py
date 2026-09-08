#!/usr/bin/env python3
"""Suggest folder categorization for migrated tmt test cases.

Analyzes test case titles and step content to suggest a category folder,
then outputs a CSV that can be reviewed and adjusted before applying.

Usage:
    python3 categorize_tests.py                  # Generate suggestions CSV
    python3 categorize_tests.py --apply mapping.csv  # Apply a reviewed CSV
"""

import argparse
import csv
import os
import re
import shutil


TESTS_DIR = "tests"

RESOURCE_PATTERNS = [
    # Sub-resources (higher priority — matched before generic "cluster")
    (r"\bautoscaler\b", "autoscalers"),
    (r"\bautonode\b", "autoscalers"),
    (r"\bautoscaling\b", "autoscalers"),
    (r"\bmax.?node", "autoscalers"),
    (r"\bmachine[- ]?pool", "machine-pools"),
    (r"\bnode[- ]?pool", "machine-pools"),
    (r"\bdefault.*(worker|mp)\b", "machine-pools"),
    (r"\bspot.*(pool|instance)", "machine-pools"),
    (r"\bvolume[- ]size", "machine-pools"),
    (r"\bwin-li\b", "machine-pools"),
    (r"\bcapacity.reservation", "machine-pools"),
    (r"\bidp\b", "idps"),
    (r"\bhtpasswd\b", "idps"),
    (r"\bidentity.provider", "idps"),
    (r"\bcreate.*idps?\b", "idps"),
    (r"\bdelete.*idps?\b", "idps"),
    (r"\blist.*idps?\b", "idps"),
    (r"\baccount[- ]?role", "account-roles"),
    (r"\boperator[- ]?role", "operator-roles"),
    (r"\brole.arn\b.*operator", "operator-roles"),
    (r"\bocm[- ]?role", "ocm-roles"),
    (r"\buser[- ]?role", "user-roles"),
    (r"\boidc", "oidc"),
    (r"\bingress", "ingresses"),
    (r"\bupgrad(?:e|ing)\b", "upgrades"),
    (r"\bupgrade.*(policy|cluster|roles)", "upgrades"),
    (r"\bchannel[- ]group", "upgrades"),
    (r"\baddon\b", "addons"),
    (r"\btuning[- ]?config", "tuning-configs"),
    (r"\bkubelet[- ]?config", "tuning-configs"),
    (r"\bpodpidlimit\b", "tuning-configs"),
    (r"\bexternal[- ]?auth", "external-auth"),
    (r"\bbreak[- ]?glass", "external-auth"),
    (r"\blog[- ]forward", "log-forwarders"),
    (r"\baudit[- ]?log\b", "log-forwarders"),
    (r"\bshared[- ]?vpc\b", "shared-vpc"),
    (r"\biam[- ]?service[- ]?account", "iam-service-accounts"),
    (r"\bimage[- ]?mirror\b", "image-mirrors"),
    (r"\bregist(?:ry|ries)\b", "registries"),
    (r"\bnetwork[- ]?verif", "network"),
    (r"\bnetwork[- ]?resource", "network"),
    (r"\bsubnet", "network"),
    (r"\bcidr\b", "network"),
    (r"\bzero[- ]?egress\b", "network"),
    (r"\bsecurity[- ]?group", "security-groups"),
    (r"\badditional[- ]?security", "security-groups"),
    (r"\bcreate.*admin\b", "admins"),
    (r"\bdelete.*admin\b", "admins"),
    (r"\bdescribe.*admin\b", "admins"),
    (r"\badmin.*user\b", "admins"),
    (r"\bgrant.*user\b", "users"),
    (r"\brevoke.*user\b", "users"),
    (r"\baccess[- ]?request", "access-requests"),
    (r"\badditional.*allowed.*principal", "clusters"),
    (r"\bdelete[- ]?protection\b", "clusters"),
    (r"\bbilling[- ]?account\b", "clusters"),
    (r"\bhibernate\b", "clusters"),
    (r"\bresume.*cluster\b", "clusters"),
    (r"\bworkload.monitor", "clusters"),
    (r"\bproxy\b", "clusters"),
    (r"\bdomain\b", "dns"),
    (r"\bdns\b", "dns"),
    (r"\bload[- ]?balancer\b", "ingresses"),
    (r"\broute\b", "ingresses"),
    (r"\bfedramp\b", "fedramp"),
    (r"\brosa init\b", "init"),
    (r"\binit\b.*rosa\b", "init"),
    (r"\brosa.*init\b", "init"),
    (r"\blogout\b", "auth"),
    (r"\blogin\b", "auth"),
    (r"\brosa token\b", "auth"),
    (r"\brosa config\b", "config"),
    (r"\bkeyring\b", "config"),
    (r"\blist.*version", "general"),
    (r"\bversion\b(?!.*creat)", "general"),
    (r"\blist[- ]?region", "regions"),
    (r"\bavailable.region", "regions"),
    (r"\binstance[- ]?type", "instance-types"),
    (r"\blist.*command.*-o\b", "general"),
    (r"\busability\b", "general"),
    (r"\bregression\b", "general"),
    (r"\binteroperability\b", "general"),
    (r"\bpermission\b.*\bquota\b", "general"),
    (r"\b(profile|debug|-v)\b.*flag", "general"),
    (r"\bcertificate.*expir", "general"),
    (r"\bosl\b.*message", "general"),
    (r"\bsdn.*ovn\b", "clusters"),
    (r"\battach.*polic", "clusters"),
    (r"\bdetach.*polic", "clusters"),
    (r"\btrust.polic", "clusters"),
    (r"\bcreate.*cluster\b", "clusters"),
    (r"\bedit.*cluster\b", "clusters"),
    (r"\bdescribe.*cluster\b", "clusters"),
    (r"\bdelete.*cluster\b", "clusters"),
    (r"\bprivate[- ]?link\b", "clusters"),
    (r"\bfips\b", "clusters"),
    (r"\bsts\b.*cluster", "clusters"),
    (r"\bnon-sts\b", "clusters"),
    (r"\bhypershift.*cluster\b", "clusters"),
    (r"\bhosted.*cluster\b", "clusters"),
    (r"\bcluster.*creation\b", "clusters"),
    (r"\baws.*security.*token\b", "clusters"),
    (r"\bbyok\b", "clusters"),
    (r"\bkms\b", "clusters"),
    (r"\betcd.*encrypt", "clusters"),
    (r"\bimdsv2\b", "clusters"),
    (r"\brosa.*cluster\b", "clusters"),
    (r"\bcluster\b", "clusters"),
    (r"\b(moa|rosa)\b", "clusters"),
]

CLUSTER_SUBRESOURCE_PRIORITY = [
    "machine-pools", "idps", "upgrades", "account-roles", "operator-roles",
    "ocm-roles", "user-roles", "oidc", "ingresses", "addons", "tuning-configs",
    "external-auth", "log-forwarders", "shared-vpc", "iam-service-accounts",
    "image-mirrors", "registries", "network", "security-groups", "admins",
    "users", "access-requests", "dns", "fedramp", "autoscalers",
]


def suggest_category(title):
    """Suggest a category folder based on the test case title."""
    title_lower = title.lower()

    matches = []
    for pattern, category in RESOURCE_PATTERNS:
        if re.search(pattern, title_lower):
            matches.append(category)

    if not matches:
        return "uncategorized"

    for priority_cat in CLUSTER_SUBRESOURCE_PRIORITY:
        if priority_cat in matches:
            return priority_cat

    return matches[0]


def generate_csv(output_file):
    """Scan all test cases and generate a categorization CSV."""
    rows = []

    for subdir in sorted(os.listdir(TESTS_DIR)):
        subdir_path = os.path.join(TESTS_DIR, subdir)
        if not os.path.isdir(subdir_path):
            continue
        for test_dir in sorted(os.listdir(subdir_path)):
            fmf_path = os.path.join(subdir_path, test_dir, "main.fmf")
            if not os.path.exists(fmf_path):
                continue

            with open(fmf_path) as f:
                content = f.read()

            summary_match = re.search(r'^summary:\s*"(.+)"', content, re.MULTILINE)
            summary = summary_match.group(1) if summary_match else test_dir

            id_match = re.search(r"^id:\s*(\S+)", content, re.MULTILINE)
            test_id = id_match.group(1) if id_match else ""

            current_folder = subdir
            suggested = suggest_category(summary)

            rows.append({
                "test_id": test_id,
                "current_folder": current_folder,
                "suggested_folder": suggested,
                "summary": summary,
                "test_dir_name": test_dir,
            })

    with open(output_file, "w", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["test_id", "current_folder", "suggested_folder", "summary", "test_dir_name"],
        )
        writer.writeheader()
        writer.writerows(rows)

    by_category = {}
    changes = 0
    for row in rows:
        cat = row["suggested_folder"]
        by_category.setdefault(cat, []).append(row)
        if row["current_folder"] != row["suggested_folder"]:
            changes += 1

    print(f"Generated {output_file} with {len(rows)} test cases")
    print(f"{changes} would be moved, {len(rows) - changes} already in the right folder")
    print()
    print("Category distribution:")
    for cat, items in sorted(by_category.items(), key=lambda x: -len(x[1])):
        print(f"  {cat}: {len(items)}")


def apply_csv(csv_file):
    """Apply categorization from a reviewed CSV by moving test directories."""
    with open(csv_file) as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    moved = 0
    skipped = 0
    for row in rows:
        current = os.path.join(TESTS_DIR, row["current_folder"], row["test_dir_name"])
        target_folder = os.path.join(TESTS_DIR, row["suggested_folder"])
        target = os.path.join(target_folder, row["test_dir_name"])

        if current == target:
            skipped += 1
            continue

        if not os.path.exists(current):
            print(f"  SKIP (not found): {current}")
            skipped += 1
            continue

        os.makedirs(target_folder, exist_ok=True)
        shutil.move(current, target)
        moved += 1
        print(f"  {row['test_id']}: {row['current_folder']} -> {row['suggested_folder']}")

    print(f"\nMoved {moved} test cases, {skipped} unchanged")


def main():
    parser = argparse.ArgumentParser(
        description="Categorize migrated tmt test cases into folders"
    )
    parser.add_argument(
        "--apply",
        metavar="CSV_FILE",
        help="Apply categorization from a reviewed CSV file",
    )
    parser.add_argument(
        "--output",
        default="categorization.csv",
        help="Output CSV filename (default: categorization.csv)",
    )
    args = parser.parse_args()

    if args.apply:
        apply_csv(args.apply)
    else:
        generate_csv(args.output)


if __name__ == "__main__":
    main()
