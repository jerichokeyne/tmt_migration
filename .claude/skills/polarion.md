---
name: polarion
description: Query Polarion test cases via pylero. Use when the user asks to look up, search, inspect, or fetch data from Polarion work items — including test case fields, test steps, attachments, linked items, or any Lucene query against the OSE project.
---

# Polarion Query Skill

Use `python3 -c "..."` to run pylero queries. The pylero config is already set up — no auth setup needed.

## Quick Patterns

### Fetch a single test case (all fields)
```python
from pylero.work_item import TestCase
tc = TestCase(work_item_id="OCP-12345", project_id="OSE")
```

### Query test cases (returns partially-populated objects)
```python
from pylero.work_item import TestCase
results = TestCase.query("subcomponent.KEY:moacli AND NOT status:inactive", project_id="OSE", limit=10)
# Each result has .uri and requested fields only
# For full data, re-fetch: tc = TestCase(uri=item.uri)
```

### Count without fetching
```python
count = TestCase.get_query_result_count("status:approved", project_id="OSE")
```

## TestCase.query() Signature
```python
TestCase.query(
    query,                    # Lucene query string (type:testcase AND project.id:OSE appended automatically)
    fields=["work_item_id"], # fields to populate on returned objects
    sort="work_item_id",     # sort field
    limit=-1,                # max results (-1 = all)
    project_id=None,         # override default project
)
```

## Lucene Query Syntax
- `"title:OCP-12345"` — by title
- `"status:approved"` — by status (values: draft, approved, inactive, needsupdate)
- `"subcomponent.KEY:moacli"` — by subcomponent
- `"caseautomation.KEY:(manualonly notautomated)"` — OR within a field
- `"severity:critical AND priority:high"` — combined
- `""` (empty string) — all test cases in the project
- `"created:[20240101 TO 20240601]"` — date range
- `"title:*login*"` — wildcard
- `"NOT status:inactive"` — negation
- `"NOT tags:ExcludeManual"` — exclude by tag

## Field Reference

### Core fields
| Field | Type | Example value |
|---|---|---|
| `work_item_id` | str | `"OCP-12345"` |
| `title` | str | `"[OCM-208] Create cluster..."` |
| `description` | str (HTML) | `"<p>...</p>"` |
| `status` | str | `"draft"`, `"approved"`, `"inactive"`, `"needsupdate"` |
| `type` | str | `"testcase"` |
| `author` | str | `"jkeyne"` (user ID) |
| `assignee` | list[User] | `[<User>]` — access `.user_id`, `.name`, `.email` |
| `runner` | str | `"jkeyne"` (user ID) |
| `created` | datetime | |
| `updated` | datetime | |
| `uri` | str | internal URI for re-fetching |

### Test metadata
| Field | Type | Values |
|---|---|---|
| `caseautomation` | str | `"automated"`, `"manualonly"`, `"notautomated"` |
| `caseimportance` | str | `"critical"`, `"high"`, `"medium"`, `"low"` |
| `caselevel` | str | `"component"`, `"system"` |
| `casecomponent` | str | `"clustermanager"` etc. |
| `subcomponent` | str | `"moacli"` etc. |
| `subteam` | str | team name |
| `testtype` | str | `"functional"` etc. |
| `caseposneg` | str | `"positive"`, `"negative"` |
| `priority` | str | |
| `severity` | str | |
| `tier` | — | (not a direct field; derived from `caseimportance`) |

### Tags and products
| Field | Type | Notes |
|---|---|---|
| `tags` | str or None | Space-separated: `"smoke fr aset0813"` — split with `re.split(r"[,\s]+", str(tc.tags))` |
| `products` | list[str] | `["rosa", "rosahcp", "ocm"]` — `"rosa"` = classic, `"rosahcp"` = HCP |
| `trello` | str | Jira/Trello IDs, space-separated: `"OCM-9613 OCM-17611"` |
| `version` | list[str] | OCP versions: `["4_14", "4_15", "4_16"]` |
| `customerscenario` | bool | |
| `day2operation` | bool | |

### Relationships
| Field | Type | Notes |
|---|---|---|
| `linked_work_items` | list[LinkedWorkItem] | `.work_item_id`, `.role` (e.g., `"relates_to"`) |
| `linked_work_items_derived` | list | Reverse links |
| `plannedin` | list | Planned-in iterations |

### Setup / Teardown
| Field | Type | Notes |
|---|---|---|
| `setup` | str or None | HTML content — preconditions |
| `teardown` | str or None | HTML content — cleanup steps |

### Test Steps
```python
tc.test_steps              # TestSteps object, can be None
tc.test_steps.steps        # list of TestStep objects
# Each step has .values — a list of Text objects:
#   values[0].content = step description (HTML, can be None)
#   values[1].content = expected result (HTML, can be None)
```

### Attachments
```python
tc.attachments             # list of Attachment objects
# Each attachment:
#   .attachment_id   — e.g., "1-screenshot-20210520-123954.png"
#   .file_name       — e.g., "screenshot-20210520-123954.png"
#   .url             — direct download URL
#   .title           — human-friendly name
#   .length          — file size in bytes
```
Images in test steps reference attachments as `src="workitemimg:<attachment_id>"`.

### Environment fields (all prefixed `env_`)
These are list or str fields for test environment metadata: `env_iaas_cloud_provider`, `env_network_plugin`, `env_install_method`, `env_os`, `env_enable_fips`, `env_private_cluster`, `env_hypershift_hosted_cluster`, etc.

## Common Query Recipes

```python
# All manual moacli test cases (excluding inactive and ExcludeManual)
TestCase.query(
    "subcomponent.KEY:moacli AND NOT status:inactive"
    " AND caseautomation.KEY:(manualonly notautomated)"
    " AND NOT tags:ExcludeManual",
    project_id="OSE"
)

# All test cases for a specific Jira story
TestCase.query("trello:OCM-12345", project_id="OSE")

# All critical automated test cases
TestCase.query("caseimportance:critical AND caseautomation.KEY:automated", project_id="OSE")

# All test cases updated in the last month
TestCase.query("updated:[20260701 TO 20260801]", project_id="OSE")

# Fetch specific fields without full re-fetch
TestCase.query("subcomponent.KEY:moacli", fields=["work_item_id", "title", "status", "trello"], project_id="OSE")
```

## Tips
- `TestCase.query()` auto-appends `type:testcase AND project.id:<project>` — don't include those yourself.
- Results from `query()` are partially populated. For full field access, re-fetch with `TestCase(uri=item.uri)`.
- `str()` values from pylero are `suds.sax.text.Text` — they behave like strings but cast with `str()` if needed.
- `tags` is a single string (space or comma separated), NOT a list.
- `products` IS a list of strings.
- `assignee` is a list of User objects; access `.user_id` for the ID string.
- HTML fields (`description`, `setup`, `teardown`, step content) need conversion for human-readable output.
