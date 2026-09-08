#!/usr/bin/env python3
"""Migrate Polarion manual test cases to tmt format.

Queries Polarion for manual test cases matching given criteria,
converts them to tmt's main.fmf + manual.md format, and writes
them under tests/<subcomponent>/.

Images embedded in test steps are downloaded and saved alongside
the manual.md, with markdown references updated to local paths.
"""

import argparse
import os
import re
from dataclasses import dataclass

import html2text
import requests
from pylero.work_item import TestCase

POLARION_BASE = (
    "https://polarion.engineering.redhat.com/polarion/#/project/OSE/workitem?id="
)
JIRA_BASE = "https://redhat.atlassian.net/browse/"


@dataclass
class Link:
    link_type: str
    link_location: str


def resolve_jira_ids(jira_ids):
    """Resolve a set of Jira IDs to their current keys and titles via the Jira REST API.

    Returns a dict mapping original_id -> {"key": current_key}.
    IDs that can't be resolved map to themselves.
    """
    if not jira_ids:
        return {}

    token = os.environ.get("JIRA_API_TOKEN") or os.environ.get("ATLASSIAN_API_TOKEN")
    email = os.environ.get("JIRA_EMAIL") or os.environ.get("ATLASSIAN_EMAIL")

    if not token or not email:
        print(
            "  NOTE: Set JIRA_API_TOKEN and JIRA_EMAIL env vars to resolve migrated Jira keys."
        )
        print("  Using original Polarion IDs as-is.")
        return {jid: {"key": jid} for jid in jira_ids}

    resolved = {}
    session = requests.Session()
    session.auth = (email, token)
    session.headers["Accept"] = "application/json"

    cloud_url = "https://redhat.atlassian.net/rest/api/3/issue/"

    print(f"  Resolving {len(jira_ids)} Jira IDs...")
    for jid in jira_ids:
        try:
            resp = session.get(
                f"{cloud_url}{jid}", params={"fields": "summary"}, timeout=10
            )
            if resp.status_code == 200:
                data = resp.json()
                resolved[jid] = {"key": data["key"]}
            else:
                resolved[jid] = {"key": jid}
        except requests.RequestException:
            resolved[jid] = {"key": jid}

    migrated = sum(1 for k, v in resolved.items() if k != v["key"])
    print(f"  Resolved {len(resolved)} IDs ({migrated} migrated to new keys)")
    return resolved


def preprocess_html(html_content):
    """Convert Polarion's inline-style HTML to semantic tags before markdown conversion.

    Polarion uses inline styles instead of semantic tags for formatting:
      - font-family: Courier New  ->  <code>
      - text-decoration: line-through  ->  <del>
      - font-weight: bold  ->  <strong>
    """
    # Monospace font -> <code> (Polarion uses this for code since it has no code blocks)
    # Run this FIRST so strikethrough/bold inside code spans get nested correctly
    html_content = re.sub(
        r'<span\b([^>]*?)style="([^"]*?)font-family:\s*&#39;Courier New&#39;[^"]*?"([^>]*)>(.*?)</span>',
        r"<code>\4</code>",
        html_content,
        flags=re.DOTALL,
    )
    html_content = re.sub(
        r"<span\b([^>]*?)style=\"([^\"]*?)font-family:\s*'Courier New'[^\"]*?\"([^>]*)>(.*?)</span>",
        r"<code>\4</code>",
        html_content,
        flags=re.DOTALL,
    )

    # Strikethrough: style="text-decoration: line-through;" -> <del>
    # First, replace <br/> inside strikethrough spans with a placeholder so the
    # markdown ~~markers~~ don't get split across lines (which breaks rendering).
    def collapse_strikethrough_breaks(match):
        inner = match.group(5)
        inner = re.sub(r"<br\s*/?>", " ", inner)
        return f"<del>{inner}</del>"

    html_content = re.sub(
        r'<span\b([^>]*?)style="([^"]*?)text-decoration:\s*line-through;?([^"]*?)"([^>]*)>(.*?)</span>',
        collapse_strikethrough_breaks,
        html_content,
        flags=re.DOTALL,
    )

    # Bold -> <strong>
    html_content = re.sub(
        r'<span\b([^>]*?)style="([^"]*?)font-weight:\s*bold;?([^"]*?)"([^>]*)>(.*?)</span>',
        r"<strong>\5</strong>",
        html_content,
        flags=re.DOTALL,
    )

    # Clean up nested empty code/del/strong from the transforms
    html_content = re.sub(r"<(code|del|strong)>\s*</\1>", "", html_content)

    return html_content


def html_to_markdown(html_content):
    """Convert Polarion HTML content to clean markdown."""
    if not html_content:
        return ""

    html_content = preprocess_html(html_content)

    converter = html2text.HTML2Text()
    converter.body_width = 0
    converter.unicode_snob = True
    converter.protect_links = True
    converter.wrap_links = False
    converter.single_line_break = True

    md = converter.handle(html_content)
    md = md.strip()
    md = re.sub(r"\n{3,}", "\n\n", md)
    # html2text escapes list markers to avoid list interpretation
    md = md.replace("\\-", "-")
    md = re.sub(r"(\d+)\\\.", r"\1.", md)
    # Escape leading # that aren't real headings — these are shell comments
    # or example prompts from Polarion content that html2text treats as headings
    md = re.sub(r"^(#+)", lambda m: "\\" + m.group(0), md, flags=re.MULTILINE)
    # Break setext-style headings: a line of -/= under text becomes h1/h2
    md = re.sub(r"^(-+|={3,})\s*$", lambda m: "\\" + m.group(0), md, flags=re.MULTILINE)
    return md


def slugify(text, max_len=80):
    """Convert a title to a filesystem-safe slug."""
    text = text.lower()
    text = re.sub(r"\[.*?\]\s*", "", text)
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = text.strip("-")
    if len(text) > max_len:
        text = text[:max_len].rstrip("-")
    return text


def build_attachment_map(tc):
    """Build a map from workitemimg IDs to attachment metadata."""
    att_map = {}
    if not tc.attachments:
        return att_map
    for att in tc.attachments:
        att_map[att.attachment_id] = {
            "file_name": att.file_name,
            "url": att.url,
        }
    return att_map


def rewrite_image_refs(html_content, att_map):
    """Replace workitemimg: src references with local file paths."""
    if not html_content:
        return html_content, []

    images_used = []

    def replace_src(match):
        img_id = match.group(1)
        if img_id in att_map:
            local_name = att_map[img_id]["file_name"]
            images_used.append(img_id)
            return f'src="{local_name}"'
        return match.group(0)

    updated = re.sub(r'src="workitemimg:([^"]+)"', replace_src, html_content)
    return updated, images_used


def print_image_instructions(images_to_download, att_map, test_dir, tc_id):
    """Print instructions for manually downloading image attachments."""
    missing = []
    for img_id in images_to_download:
        att = att_map[img_id]
        if not os.path.exists(os.path.join(test_dir, att["file_name"])):
            missing.append(att["file_name"])
    if not missing:
        return
    polarion_url = f"{POLARION_BASE}{tc_id}"
    print(f"    Images need manual download from: {polarion_url}")
    print(f"    Save to: {test_dir}/")
    for name in missing:
        print(f"      - {name}")


def build_manual_md(tc, att_map):
    """Build the manual.md content from a TestCase's test steps.

    Returns (markdown_content, set_of_image_ids_used).
    """
    lines = []
    all_images = set()

    setup_html = str(tc.setup) if tc.setup else None
    if setup_html:
        setup_html, setup_imgs = rewrite_image_refs(setup_html, att_map)
        all_images.update(setup_imgs)
        setup_md = html_to_markdown(setup_html)
        if setup_md:
            lines.append("# Setup")
            lines.append(setup_md)
            lines.append("")

    lines.append("# Test")
    lines.append("")

    if not tc.test_steps or not tc.test_steps.steps:
        lines.append("No test steps defined in Polarion.")
        return "\n".join(lines) + "\n", all_images

    for step in tc.test_steps.steps:
        values = step.values
        step_html = values[0].content if len(values) > 0 else None
        expect_html = values[1].content if len(values) > 1 else None

        step_html, step_imgs = rewrite_image_refs(step_html, att_map)
        expect_html, expect_imgs = rewrite_image_refs(expect_html, att_map)
        all_images.update(step_imgs)
        all_images.update(expect_imgs)

        step_md = html_to_markdown(step_html)
        expect_md = html_to_markdown(expect_html)

        if step_md:
            lines.append("## Step")
            lines.append(step_md)
            lines.append("")

            lines.append("## Expect")
            if expect_md:
                lines.append(expect_md)
            lines.append("")

    teardown_html = str(tc.teardown) if tc.teardown else None
    if teardown_html:
        teardown_html, teardown_imgs = rewrite_image_refs(teardown_html, att_map)
        all_images.update(teardown_imgs)
        teardown_md = html_to_markdown(teardown_html)
        if teardown_md:
            lines.append("# Cleanup")
            lines.append(teardown_md)
            lines.append("")

    return "\n".join(lines).rstrip() + "\n", all_images


def build_main_fmf(tc, jira_map=None, test_dir="/"):
    """Build the main.fmf content from a TestCase."""
    title = tc.title or tc.work_item_id
    title = re.sub(r"\s+", " ", title).strip()
    description = title.replace('"', '\\"')
    summary = re.sub(r"^(\[.*?\]\s*)+", "", title).strip().replace('"', '\\"')

    lines = []
    lines.append(f'summary: "{summary}"')
    lines.append(f'description: "{description}"')
    lines.append(f"id: {tc.work_item_id}")

    importance = tc.caseimportance
    tier_map = {"critical": "0", "high": "1", "medium": "2", "low": "3"}
    tier = tier_map.get(importance, "2")
    lines.append(f'tier: "{tier}"')

    status = str(tc.status) if tc.status else ""
    if status in ("inactive"):
        lines.append("enabled: false")

    automation = tc.caseautomation
    tag_list = []
    links = []

    match automation:
        case "automated":
            lines.append("manual: false")
            links.append(Link("documented-by", f"/{test_dir}/manual.md"))
        case "manualonly":
            lines.append("manual: true")
            lines.append("test: manual.md")
            links.append(Link("documented-by", f"/{test_dir}/manual.md"))
        case "notautomated":
            lines.append("manual: true")
            lines.append("test: manual.md")
            links.append(Link("documented-by", f"/{test_dir}/manual.md"))
        case _:
            print(f"WARNING: Unknown automation status: {automation}")

    if automation:
        tag_list.append(automation)

    if tc.tags:
        tag_list.extend(re.split(r"[,\s]+", str(tc.tags)))

    products = tc.products if hasattr(tc, "products") and tc.products else []
    product_ids = [str(p) for p in products]
    if "rosa" in product_ids:
        tag_list.append("classic")
    if "rosahcp" in product_ids:
        tag_list.append("hcp")

    tag_list = [t.strip().lower() for t in tag_list if t.strip()]
    if tag_list:
        lines.append(f"tag: [{', '.join(tag_list)}]")

    if tc.author:
        lines.append(f"author: {tc.author}")

    if tc.assignee:
        assignees = []
        for a in tc.assignee:
            uid = a.user_id if hasattr(a, "user_id") else str(a)
            if uid:
                assignees.append(uid)
        if assignees:
            lines.append(f"contact: [{', '.join(assignees)}]")

    runner = tc.runner if hasattr(tc, "runner") else None
    if runner:
        lines.append(f"extra-runner: {runner}")

    if tc.linked_work_items:
        for lwi in tc.linked_work_items:
            role = lwi.role or "relates_to"
            role_label = role.replace("_", "-") if "_" in role else role
            if "relate" in role_label:
                role_label = "relates"
            links.append(Link(role_label, f"{POLARION_BASE}{lwi.work_item_id}"))

    if tc.trello:
        for ticket in re.split(r"[,\s]+", str(tc.trello)):
            old_ticket = ticket.strip()
            if jira_map is not None:
                info = jira_map.get(old_ticket, {"key", old_ticket})
                ticket_id = info["key"]
            else:
                ticket_id = old_ticket
            links.append(Link("verifies", f"{JIRA_BASE}{ticket_id}"))

    if links:
        lines.append("link:")
        for link in links:
            lines.append(f"  - {link.link_type}: {link.link_location}")

    return "\n".join(lines) + "\n"


def migrate_test_case(tc, output_dir, jira_map=None):
    """Write a single test case as tmt files."""
    tc_id = tc.work_item_id
    title_slug = slugify(tc.title or "untitled")
    dir_name = f"{tc_id}_{title_slug}"

    subcomponent = tc.subcomponent or "general"
    test_dir = os.path.join(output_dir, subcomponent, dir_name)
    os.makedirs(test_dir, exist_ok=True)

    fmf_content = build_main_fmf(tc, jira_map=jira_map, test_dir=test_dir)
    fmf_path = os.path.join(test_dir, "main.fmf")
    with open(fmf_path, "w") as f:
        f.write(fmf_content)

    att_map = build_attachment_map(tc)
    md_content, images_used = build_manual_md(tc, att_map)

    md_path = os.path.join(test_dir, "manual.md")
    with open(md_path, "w") as f:
        f.write(md_content)

    if images_used:
        print_image_instructions(images_used, att_map, test_dir, tc_id)

    return test_dir, len(images_used)


def main():
    parser = argparse.ArgumentParser(
        description="Migrate Polarion manual test cases to tmt format"
    )
    parser.add_argument(
        "--query",
        default=(
            "subcomponent.KEY:moacli AND NOT status:inactive"
            # " AND caseautomation.KEY:(manualonly notautomated)"
            # " AND NOT tags:ExcludeManual"
        ),
        help="Polarion Lucene query string",
    )
    parser.add_argument(
        "--project", default="OSE", help="Polarion project ID (default: OSE)"
    )
    parser.add_argument(
        "--output-dir",
        default="tests",
        help="Output directory for generated tests (default: tests)",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=-1,
        help="Max number of test cases to fetch (-1 for all)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print what would be created without writing files",
    )
    args = parser.parse_args()

    print(f"Querying Polarion project '{args.project}'...")
    print(f"Query: {args.query}")
    print()

    results = TestCase.query(
        args.query,
        project_id=args.project,
        limit=args.limit,
        fields=["work_item_id", "trello"],
    )
    print(f"Found {len(results)} test cases")
    print()

    all_jira_ids = set()
    for item in results:
        if item.trello:
            for jid in re.split(r"[,\s]+", str(item.trello)):
                jid = jid.strip()
                if jid:
                    all_jira_ids.add(jid)

    jira_map = {}
    if all_jira_ids and not args.dry_run:
        jira_map = resolve_jira_ids(all_jira_ids)
        print()

    total_images = 0

    for i, item in enumerate(results, 1):
        tc = TestCase(uri=item.uri)
        step_count = (
            len(tc.test_steps.steps) if tc.test_steps and tc.test_steps.steps else 0
        )

        if args.dry_run:
            att_map = build_attachment_map(tc)
            has_images = any(
                re.search(r'src="workitemimg:', v.content or "")
                for s in (tc.test_steps.steps or [])
                for v in s.values
            )
            img_note = " [has images]" if has_images else ""
            print(
                f"[{i}/{len(results)}] {tc.work_item_id} - {tc.title} ({step_count} steps){img_note}"
            )
            continue

        test_dir, img_count = migrate_test_case(tc, args.output_dir, jira_map=jira_map)
        total_images += img_count
        img_note = f", {img_count} images" if img_count else ""
        print(
            f"[{i}/{len(results)}] {tc.work_item_id} -> {test_dir} ({step_count} steps{img_note})"
        )

    print()
    if args.dry_run:
        print("Dry run complete (no files written).")
    else:
        print(
            f"Done! Migrated {len(results)} test cases, {total_images} images need manual download."
        )


if __name__ == "__main__":
    main()
