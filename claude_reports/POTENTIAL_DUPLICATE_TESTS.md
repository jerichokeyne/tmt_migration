# Potential Duplicate Test Cases

## Scope and Method

Reviewed all 395 test cases under `tests/**/main.fmf` and their associated `manual.md` files.

Candidates were identified by comparing test summaries, documented commands, prerequisites, expected output, and manual workflows. This report records overlap candidates for human review; it does not establish that either test can be deleted without preserving unique coverage.

Tests that differ only by interactive, manual, or automatic mode are excluded. Clear happy-path and validation-only pairs are also excluded unless one test substantially repeats the other's scenarios.

## High Confidence

### OCP-57410 and OCP-75504: Identical operator-role lifecycle tests

Paths:

- `tests/operator-roles/OCP-57410_create-delete-clusters-operator-roles-with-managed-operator-roles-policies/`
- `tests/operator-roles/OCP-75504_create-delete-clusters-operator-roles-with-managed-operator-roles-policies-in-ma/`

Both manuals are identical, covering automatic and manual creation, Hosted Control Planes, list/describe, and deletion of managed operator roles. The summary suffix in `OCP-75504` does not correspond to a substantive coverage difference.

Suggested review: retain one test, or split any necessary mode-specific assertions into distinct tests before removing the duplicate.

### OCP-60956 and OCP-74761: BYO OIDC operator-role deletion

Paths:

- `tests/operator-roles/OCP-60956_delete-byo-operator-roles-oidc-via-rosacli-by-command/`
- `tests/operator-roles/OCP-74761_delete-in-used-byo-operator-roles-oidc-via-rosacli-by-command/`

`OCP-74761` repeats `OCP-60956`'s shared-OIDC-provider scenario: two clusters share an OIDC provider and operator roles, one cluster is deleted, deletion of the still-in-use provider must fail, and nonexistent-resource deletion is covered. `OCP-60956` additionally covers the single-cluster lifecycle and URL validation.

Suggested review: consolidate the shared-provider scenario into `OCP-60956` and refocus or retire `OCP-74761`.

### OCP-64494 and OCP-73672: HCP audit-log forwarding validation

Paths:

- `tests/clusters/OCP-64494_create-and-edit-hosted-cp-cluster-with-auditlog-forwarding-enabled-disabled-via/`
- `tests/clusters/OCP-73672_validation-for-create-hosted-cp-cluster-with-auditlog-forwarding-enabled-disable/`

The invalid or missing ARN, invalid trust relationship, and wrong-cluster-type cases in `OCP-73672` are wholly covered by the validation section of `OCP-64494`. `OCP-64494` also covers interactive create/edit/describe happy paths.

Suggested review: remove the repeated validation section from one test. Do not delete `OCP-64494` as a whole.

### OCP-81295 and OCP-77140: Network-resource default templates

Paths:

- `tests/network/OCP-81295_create-network-resources-with-default-template-should-be-successful-via-rosa-cli/`
- `tests/network/OCP-77140_create-network-resources-with-local-template-should-be-successful-via-rosa-cli/`

Both cover successful default-template flows: three availability zones, two availability zones plus tags, cluster creation from generated subnets, and explicit availability-zone behavior. `OCP-81295` uniquely covers no-argument defaults. `OCP-77140` uniquely covers manual mode, local custom templates, `OCM_TEMPLATE_DIR`, and template-directory override flags.

Suggested review: share or consolidate the default-template scenarios while retaining `OCP-77140`'s local-template coverage.

### OCP-55729 and OCP-34950: Region listing

Paths:

- `tests/regions/OCP-55729_list-regions-via-rosacli-command/`
- `tests/regions/OCP-34950_available-regions-can-be-listed-by-rosa-cli/`

`OCP-55729/main.fmf` explicitly identifies itself as a duplicate of `OCP-34950` and is disabled. Both cover normal and `--hosted-cp` region listing. `OCP-34950` additionally covers help, multi-AZ filtering, API provenance, output formats, and errors. `OCP-55729` adds an HCP cluster creation use of a supported region.

Suggested review: retire `OCP-55729`, or retain only its distinct cluster-creation assertion.

### OCP-55995 and OCP-52690: General ROSA CLI usability

Paths:

- `tests/general/OCP-55995_common-usability-testing-for-managed-service-on-rosa-client/`
- `tests/general/OCP-52690_common-usability-testing-for-rosacli/`

Both cover deletion confirmation, complete operation workflows, operation-result messages, retries after network failures, and race-condition retries. `OCP-52690` adds command inventories, invalid interactive-input recovery, and rollback; `OCP-55995` adds account-role upgrade usability.

Suggested review: move the two unique assertions to one canonical general-usability test and eliminate repeated core checks.

### OCP-59551 and OCP-74661: Forced operator-role recreation

Paths:

- `tests/account-roles/OCP-59551_force-to-create-operator-roles-and-account-roles-to-ensure-the-policies-action-u/`
- `tests/operator-roles/OCP-74661_force-to-create-operator-roles-which-were-created-with-cluster-to-ensure-the-pol/`

Both test forced recreation of existing operator roles after policy actions or policies are removed, including IAM path coverage. `OCP-59551` also retains distinct account-role scenarios.

Suggested review: retain the operator-role flow in `OCP-74661` and remove or reference the duplicated operator-role subsection in `OCP-59551`.

## Medium Confidence

### OCP-60971 and OCP-63826: Pre-cluster operator-role creation

Paths:

- `tests/operator-roles/OCP-60971_create-operator-roles-prior-to-cluster-creation/`
- `tests/operator-roles/OCP-63826_create-list-operator-roles-prior-to-cluster-creation-in-the-interactive-mode-and/`

Both prepare BYO OIDC, create pre-cluster operator roles using prefix, OIDC, and installer ARN inputs, repeat for Hosted Control Planes, cover manual execution, and validate cluster creation. `OCP-63826` adds list output and configuration inheritance; `OCP-60971` adds automatic-mode behavior and negative validations.

Suggested review: merge shared setup and core creation assertions; retain each test's distinct checks.

### OCP-84391 and OCP-84626: IAM service-account manual deletion

Paths:

- `tests/iam-service-accounts/OCP-84391_create-delete-list-decribe-iamserviceaccount-via-rosacli-by-command-in-auto-mode/`
- `tests/iam-service-accounts/OCP-84626_create-delete-iamserviceaccount-via-rosacli-by-command-in-manual-mode/`

`OCP-84391` already contains the manual deletion workflow and AWS detach/delete command assertions repeated by `OCP-84626`, including classic OIDC coverage. `OCP-84391` is a broader lifecycle test. `OCP-84626` documents manual creation options, but has no substantive expected result because manual creation is unsupported.

Suggested review: consolidate the manual deletion checks in the lifecycle test and refocus `OCP-84626` on unsupported manual creation behavior.

### OCP-43070 and OCP-61322: Hosted CP managed account-role lifecycle

Paths:

- `tests/account-roles/OCP-43070_create-list-delete-account-roles-via-rosacli/`
- `tests/account-roles/OCP-61322_create-delete-hypershift-account-roles-with-managed-policies/`

Both verify Hosted Control Plane account-role creation in automatic and manual modes, managed-policy attachment, list status, and automatic/manual deletion. `OCP-43070` is broader across default, classic, and Hosted Control Plane commands. `OCP-61322` adds Hosted Control Plane flags, version warnings, and invalid-delete coverage.

Suggested review: retain distinct Hosted Control Plane validations and consolidate common lifecycle assertions.

### OCP-67348 and OCP-74468: Autoscaler invalid-input validation

Paths:

- `tests/autoscalers/OCP-67348_validations-for-create-describe-edit-delete-autoscaler-via-rosacli/`
- `tests/autoscalers/OCP-74468_validations-for-create-describe-edit-delete-autoscaler-via-rosacli/`

Both validate missing `--cluster`, unknown flags, invalid interactive values, and maximum-less-than-minimum bounds. `OCP-67348` adds no-autoscaler operations, HCP rejection, and not-ready clusters. `OCP-74468` adds the already-existing autoscaler case and uses existing-autoscaler state for updates.

Suggested review: consolidate the shared invalid-input matrix while retaining state-specific cases.

### OCP-72174 and OCP-42053: Instance-type listing

Paths:

- `tests/instance-types/OCP-72174_as-a-user-of-rosa-cli-i-want-to-be-able-to-use-rosa-list-instance-types-to-fi/`
- `tests/instance-types/OCP-42053_instance-types-can-be-listed-by-rosa-cli/`

Both verify `rosa list instance-types` help and successful listing. `OCP-72174` adds role/region invocation, unsupported-region validation, and an interactive-mode invocation, which is excluded from duplicate consideration.

Suggested review: retain the additional coverage in `OCP-72174` and remove or narrow duplicate baseline checks in `OCP-42053`.

### OCP-62088 and OCP-38810: OCP version listing

Paths:

- `tests/ocp-versions/OCP-62088_list-versions-can-work-correctly-for-hosted-cp-cluster-via-rosa-cli/`
- `tests/ocp-versions/OCP-38810_list-versions-can-work-correctly-via-rosa-cli/`

Both verify stable and candidate channel output and common global flags for `rosa list version(s)`. `OCP-62088` asserts Hosted Control Plane-specific eligibility/default behavior; `OCP-38810` covers help and unsupported `--interactive`.

Suggested review: parameterize shared list-version checks by cluster type, retaining the distinct flags and eligibility assertions.

### OCP-71912 and OCP-38854: Debug flag coverage

Paths:

- `tests/general/OCP-71912_test-support-for-debug-flag-for-commands-rosa-version-and-rosa-verify-rosa-clien/`
- `tests/general/OCP-38854_check-all-commands-with-the-profile-debug-v-flag-and-the-request-header/`

`OCP-38854` claims `--debug` coverage for all commands, including the `rosa version` and `rosa verify rosa-client` command/flag pairs in `OCP-71912`. `OCP-71912` specifically checks mirror-request debug output, while `OCP-38854` includes verbosity, profiles, and AWS-client User-Agent behavior.

Suggested review: clarify `OCP-38854`'s command matrix. Retain `OCP-71912` if it is the only test asserting request-level debug output.

### OCP-77016 and OCP-76570: Access-request decisions used as list setup

Paths:

- `tests/access-requests/OCP-77016_can-list-access-requests-from-the-cli/`
- `tests/access-requests/OCP-76570_can-approve-and-deny-access-requests-from-the-cli/`

`OCP-77016` approves and denies requests to create list states, duplicating the dedicated successful decision actions in `OCP-76570`. The list test also uniquely needs Pending/Approved/Denied states to check default visibility, filtering, ordering, and cluster scope. `OCP-76570` owns decision behavior and validation.

Suggested review: use shared setup or a fixture for state transitions. These are not candidates for whole-test removal.

### OCP-57091 and OCP-57104: Default machine-pool label validation corpus

Paths:

- `tests/clusters/OCP-57091_validate-default-mp-labels-option-for-rosa-cluster-creation-in-interactive-mode/`
- `tests/machine-pools/OCP-57104_validate-default-machine-pool-labels-with-rosacli-in-interactive-mode/`

The manuals repeat almost the same invalid-label corpus: malformed or empty keys, duplicate keys, length limits, non-`key=value` input, and reserved Kubernetes/OpenShift prefixes. The command surfaces differ: cluster-creation default labels versus editing the default machine pool.

Suggested review: share the invalid-label data set while retaining command-specific validation tests.

### OCP-66748 and OCP-66761: Autoscaler flags during cluster creation

Paths:

- `tests/autoscalers/OCP-66748_create-cluster-autoscaler-by-rosacli/`
- `tests/clusters/OCP-66761_validations-for-autoscaler-flags-during-creating-cluster-via-rosacli/`

Both create clusters with autoscaler flags and verify whether a cluster autoscaler exists and its API representation. `OCP-66748` focuses on valid/default behavior. `OCP-66761` focuses on invalid input and unsupported Hosted Control Plane behavior.

Suggested review: factor out the shared happy-path assertions; retain the validation matrix separately.

## Excluded Similar Tests

- Interactive, manual, and automatic mode variants are intentionally separate tests.
- Shared-VPC account-role and operator-role pairs target different resources and commands.
- OCM-role and user-role workflows target different resources despite similarly shaped command sequences.
- Day-1 versus day-2 log-forwarding cases use different interfaces and coverage scope.
- External-auth-provider, IDP, and cluster tests that share prerequisite setup are feature-consumer coverage, not duplicates.
- Similar zero-egress, Win-LI, MaxSurge/MaxUnavailable, and basic Hosted Control Plane tests differ in topology, interface, or end-to-end scope.

## Next Review Steps

1. Confirm the two high-confidence full or near-full duplicates first: `OCP-57410`/`OCP-75504` and `OCP-60956`/`OCP-74761`.
2. For partial duplicates, extract shared setup or validation matrices rather than deleting whole tests.
3. Update links, test metadata, and issue references before retiring any test case.
