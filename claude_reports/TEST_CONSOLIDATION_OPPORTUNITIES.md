# Test Consolidation Opportunities

## Goal

Reduce the number of ROSA CLI test cases without materially reducing feature
coverage. The review covers all 395 test cases and treats interactive, manual,
and automatic mode as separate test purposes when the mode changes the CLI
contract being tested.

This report is based on test metadata and manual procedures, not execution
history or ROSA source coverage instrumentation. Retain requirement links and
unique assertions when consolidating any candidate.

## Expected Reduction

- Low-risk first wave: 21 tests, reducing the suite from 395 to about 374.
- Broader consolidation: up to 44 tests, reducing the suite to about 351.
- The broader figure includes medium-risk merges that should be reviewed with
  ROSA feature owners before implementation.

## Consolidation Rules

- Keep interactive, manual, and automatic-mode tests separate when the mode is
  the test's primary behavior.
- Combine command-mode happy paths and validations for the same resource,
  topology, and lifecycle.
- Combine CRUD verb tests into one lifecycle test when the resource state is
  naturally shared.
- Preserve separate tests for different resource types, cluster topologies, or
  day-1 versus day-2 interfaces unless the combined lifecycle is intentional.

## Low-Risk First Wave

### Exact or Strict-Subset Duplicates

1. Combine `OCP-57410` into `OCP-75504` under `tests/operator-roles`.
   The two 88-line manuals are identical. Reduction: 1.
2. Combine `OCP-74761` into `OCP-60956` under `tests/operator-roles`.
   The former is a strict subset of the latter's BYO OIDC shared-provider
   deletion workflow. Retain the in-use-provider rejection assertion.
   Reduction: 1.
3. Combine disabled `OCP-55729` into `OCP-34950` under `tests/regions`.
   The metadata already declares it a duplicate. Retain its HCP cluster
   creation assertion if still required. Reduction: 1.
4. Combine `OCP-42053` into `OCP-72174` under `tests/instance-types`.
   Retain the authenticated baseline list assertion. Reduction: 1.
5. Combine `OCP-55995` into `OCP-52690` under `tests/general`.
   Retain the different-version account-role update assertion. Reduction: 1.

### Same Feature and Lifecycle

1. Combine `OCP-74408`, `OCP-74556`, `OCP-74433`, and `OCP-86375` into
   `OCP-74408` under `tests/clusters`.
   Retain create, describe, edit, malformed ARN, classic-cluster rejection,
   protected root-principal rejection, and no-mutation assertions.
   Reduction: 3.
2. Combine `OCP-57092` and `OCP-57091` into `OCP-57092` under
   `tests/clusters`.
   Retain interactive default-machine-pool label success and validation cases.
   Reduction: 1.
3. Combine `OCP-57103` and `OCP-57104` into `OCP-57103` under
   `tests/machine-pools`.
   Retain label/taint set, clear, malformed, duplicate, oversize, reserved,
   and no-mutation-after-rejection assertions. Reduction: 1.
4. Combine `OCP-57102` and `OCP-57105` into `OCP-57102` under
   `tests/machine-pools`.
   Retain the same command-mode label/taint validation matrix. Reduction: 1.
5. Combine `OCP-63178` and `OCP-63179` into `OCP-63178` under
   `tests/machine-pools`.
   Retain attach, replace, clear, duplicate, and nonexistent tuning-config
   behavior. Reduction: 1.
6. Combine `OCP-73765` and `OCP-73766` into `OCP-73765` under
   `tests/machine-pools`.
   Retain one-config-limit, nonexistent-config, and in-use-config protections.
   Reduction: 1.
7. Combine `OCP-43252` into `OCP-43251` under `tests/machine-pools`.
   Retain invalid spot price and explicitly-disabled spot validation. Reduction: 1.
8. Combine `OCP-68219` into `OCP-68173` under `tests/machine-pools`.
   Retain non-BYO-VPC, Red Hat-managed security group, VPC mismatch, and
   minimum-version rejections. Reduction: 1.
9. Combine `OCP-73672` into `OCP-64494` under `tests/clusters`.
   The broader interactive audit-log workflow already contains the validation
   matrix. Retain invalid ARN, trust relationship, missing role, and classic
   cluster rejection cases. Reduction: 1.
10. Combine `OCP-38778` into `OCP-32987` under `tests/clusters`.
    Retain missing, nonexistent, ambiguous ID, and unknown-flag cases.
    Reduction: 1.
11. Combine `OCP-74225` into `OCP-73449` under `tests/policy`.
    The validation coverage is a subset of the automatic attach/detach test.
    Keep manual-mode `OCP-74224` separate. Reduction: 1.
12. Combine `OCP-72602` into `OCP-72536` under `tests/external-auth-provider`.
    Retain disabled-feature, required-field, and non-HCP rejection cases.
    Keep interactive `OCP-72601` separate. Reduction: 1.
13. Combine `OCP-74468` into `OCP-67348` under `tests/autoscalers`.
    Retain already-existing-autoscaler and update-state validations. Reduction: 1.
14. Combine `OCP-73754` into `OCP-73753` under `tests/kubeletconfigs`.
    Retain invalid name/PID limit, duplicate, and missing-resource checks.
    Reduction: 1.
15. Combine `OCP-75052` into `OCP-73538` under `tests/ingresses`.
    Retain missing-cluster and nonexistent-ingress-ID errors. Reduction: 1.
16. Combine `OCP-71174` into `OCP-65798` under `tests/ingresses`.
    Retain the HCP rejection for `--default-ingress-route-selector`.
    Reduction: 1.

## Medium-Risk Consolidations

### Large Lifecycle Tests

1. Combine `OCP-56778`, `OCP-56783`, and `OCP-56786` into `OCP-56782` under
   `tests/machine-pools`. Reduction: 3.
   Retain list, create, edit, describe, delete, missing-resource, cannot-delete-
   final-NodePool, replica-bound, autoscaling-conflict, and HCP-only checks.
2. Combine `OCP-59530`, `OCP-60688`, and `OCP-75210` into `OCP-59530` under
   `tests/clusters`. Reduction: 2.
   Retain managed/unmanaged OIDC, role reuse and incompatibility, HCP OIDC
   requirement, and cleanup. The shared procedures are materially identical.
3. Combine `OCP-60084` into `OCP-60083` under `tests/clusters`. Reduction: 1.
   Retain all KMS ARN error cases and classic-cluster compatibility.
4. Combine `OCP-79227` into `OCP-79226` under `tests/clusters`. Reduction: 1.
   Retain scheduled, in-progress, and complete migration states plus JSON/YAML
   output assertions.
5. Combine `OCP-63169` and `OCP-63174` into `OCP-63164` under
   `tests/tuning-configs`. Reduction: 2.
   Retain invalid and duplicate names, malformed files, quota, nonexistent
   updates, and invalid update specs.
6. Combine `OCP-68835` and `OCP-68836` into `OCP-68828` under
   `tests/kubeletconfigs`. Reduction: 2.
   Retain update/delete-before-create, confirmation, `--yes`, post-delete, and
   HCP-rejection coverage.

### Shared Command Coverage

1. Combine `OCP-81295` into `OCP-77140` under `tests/network`. Reduction: 1.
   Retain default templates, no-argument defaults, AZ combinations, tags,
   verifier output, cluster consumption, local templates, and manual mode.
2. Combine `OCP-73814` into `OCP-62929` under `tests/upgrades`. Reduction: 1.
   Retain invalid cluster/date/time, schedule constraints, invalid cron, and
   unsupported HCP node-drain cases.
3. Combine `OCP-38787` into `OCP-38785` under `tests/upgrades`. Reduction: 1.
   Retain missing-cluster, no-scheduled-upgrade, and unsupported interactive
   behavior.
4. Combine `OCP-38827` and `OCP-77095` into `OCP-57094` under
   `tests/upgrades`. Reduction: 2.
   Retain no-upgrade, scheduled/started/completed, UI-created-policy visibility,
   missing-cluster, unsupported flags, debug, and profile cases.
5. Combine `OCP-74402` into `OCP-73731` under `tests/upgrades`. Reduction: 1.
   Retain arbitrary-policy preservation and account-role-only deletion behavior.
6. Combine `OCP-77016`, `OCP-76773`, and `OCP-76570` into `OCP-77016` under
   `tests/access-requests`. Reduction: 2.
   Retain describe formats/errors, decision validation, and list state filtering
   and ordering. This becomes an access-request state-machine test.
7. Combine `OCP-38810` and `OCP-62088` into a parameterized version-list test.
   Reduction: 1. Retain classic and HCP channel/default-version distinctions.
8. Combine `OCP-43067` into `OCP-43070` under `tests/account-roles`.
   Reduction: 1. Retain prefix, mode, boundary, and manual-force validations.
9. Combine `OCP-52419` and `OCP-52580` into `OCP-52419` under
   `tests/user-roles`. Reduction: 1. Retain invalid mode, boundary, prefix, and
   malformed link/unlink cases.
10. Combine `OCP-60971` and `OCP-63826` only after extracting common BYO OIDC
    pre-cluster setup. Reduction: 1. Retain list/inheritance, automatic mode,
    and negative validations.
11. Combine day-1 `OCP-86415` with day-2 `OCP-86448` under
    `tests/log-forwarders`. Reduction: 1. Retain day-1 CloudWatch/S3 matrices,
    YAML/backend failures, and day-2 CRUD. This is appropriate only if a single
    longer HCP end-to-end lifecycle is acceptable.
12. Combine OIDC validation `OCP-43046` into `OCP-70859` under
    `tests/operator-roles`. Reduction: 1. Normalize the legacy procedure first,
    then retain all cluster-state and identifier-selection errors.

## Not Recommended

- Do not merge interactive-only, manual-only, or automatic-only tests where
  input prompts, generated commands, or confirmation behavior is the feature.
- Keep day-1 and day-2 log-forwarding tests separate if independent failure
  diagnosis is more important than reducing one test.
- Keep create versus edit proxy tests and `--channel` versus `--channel-group`
  tests separate because their CLI contracts differ.
- Keep tests for different resources, even when their workflows look similar:
  account roles versus operator roles, OCM roles versus user roles, and classic
  versus Hosted Control Plane behavior.

## Implementation Sequence

1. Start with the five exact or strict-subset duplicates.
2. Merge the 16 same-feature low-risk cases while preserving requirement links.
3. Run the consolidated tests against `~/work/repos/rosa` before retiring IDs.
4. Review medium-risk lifecycle merges with the relevant ROSA feature owner.
5. Keep retired test IDs discoverable in metadata or issue links for traceability.
