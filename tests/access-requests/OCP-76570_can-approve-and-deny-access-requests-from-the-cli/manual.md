# Test

## Step
1. Check the help message
```bash
rosa create decision -h
```

## Expect
```
Create a decision for an Access Request

Usage:
  rosa create decision [flags]

Examples:
  # Create a decision for an Access Request to approve it
  rosa create decision --access-request <access_request_id> --decision Approved


Flags:
  -a, --access-request string   ID of the Access Request to add decision (required).
  -d, --decision string         Decision created for the Access Request, valid values are 'Approved' or 'Denied' (required).
  -h, --help                    help for decision
  -j, --justification string    Justification for the decision, required if decision is 'Denied'.

Global Flags:
      --color string     Surround certain characters with escape sequences to display them in color on the terminal. Allowed options are [auto never always] (default "auto")
      --debug            Enable debug mode.
      --profile string   Use a specific AWS profile from your credential file.
      --region string    Use a specific AWS region, overriding the AWS_REGION environment variable. (DEPRECATED: Region flag will be removed from this command in future versions)
  -y, --yes              Automatically answer yes to confirm operation.
```

## Step
2. Create a ROSA/ROSA HCP cluster

## Expect

## Step
3. Add the "capability.cluster.enable_access_protection" label to the cluster's subscription

You can get the subscription ID by running (replace CLUSTER_ID with your cluster's ID):
```bash
subscription_id=$(ocm get /api/accounts_mgmt/v1/subscriptions -p search="cluster_id is 'CLUSTER_ID'" | jq -r .items[0].id)
```

You can then add the label by running this command logged in as the super admin account:
```bash
echo '{"kind": "Label", "internal": true, "key": "capability.cluster.enable_access_protection", "value": "true"}' | ocm post "/api/accounts_mgmt/v1/subscriptions/$subscription_id/labels"
```

## Expect
```json
{
  "created_at": "2024-10-02T19:29:43.474234Z",
  "href": "/api/accounts_mgmt/v1/subscriptions/2mtXwNcCC0bh3ST9cvI4tst8Lw8/labels/capability.cluster.enable_access_protection",
  "id": "2mtYY6Fuj0B8nlLkrLl4MSyTqcR",
  "internal": true,
  "key": "capability.cluster.enable_access_protection",
  "kind": "Label",
  "subscription_id": "2mtXwNcCC0bh3ST9cvI4tst8Lw8",
  "updated_at": "2024-10-02T19:31:20.879347Z",
  "value": "true"
}
```

## Step
4. Create an access request (if your account can't make an access request, try with the org admin account)

You can create an access request by running this (replace CLUSTER_ID with your cluster's ID, and if needed you can replace `SDAINT-9253` with another JIRA ticket in the SDAINT project):
```bash
echo "{\"justification\": \"Testing\", \"cluster_id\": \"${CLUSTER_ID}\", \"internal_support_case_id\": \"SDAINT-9253\"}" | ocm post /api/access_transparency/v1/access_requests
```

## Expect
```json
{
  "cluster_id": "2e5kvtptta5s8i4h9coadjp8i47kvivh",
  "created_at": "2024-10-02T19:31:21.481968Z",
  "deadline": "72h",
  "deadline_at": "2024-10-05T19:31:21.481968Z",
  "duration": "8h",
  "href": "/api/access_transparency/v1/access_requests/2mtYkOxGjMtoAGWfRb5Hst3t6Co",
  "id": "2mtYkOxGjMtoAGWfRb5Hst3t6Co",
  "internal_support_case_id": "SDAINT-9253",
  "justification": "Testing",
  "kind": "AccessRequest",
  "organization_id": "1OAqHo0k19kyq7Xt7I1Zqb8Ok4K",
  "requested_by": "sdqe-admin01",
  "status": {
    "state": "Pending"
  },
  "subscription_id": "2mtXwNcCC0bh3ST9cvI4tst8Lw8",
  "support_case_id": "",
  "updated_at": "2024-10-02T19:31:21.481968Z"
}
```

## Step
5. Try to approve the access request with and without a justification

```bash
rosa create decision -a ${ACCESS_REQUEST_ID} -d Approved

rosa create decision -a ${ACCESS_REQUEST_ID} -d Approved -j test
```

## Expect
```
I: Successfully created the decision for access request '2mtYkOxGjMtoAGWfRb5Hst3t6Co'
```

You can run `ocm get /api/access_transparency/v1/access_requests/${ACCESS_REQUEST_ID}` to get more info (you should see the justification if you set it):
```json
{
  "cluster_id": "2e5kvtptta5s8i4h9coadjp8i47kvivh",
  "created_at": "2024-10-02T19:29:58.313733Z",
  "deadline": "72h",
  "deadline_at": "2024-10-05T19:29:58.313733Z",
  "decisions": [
    {
      "created_at": "2024-10-02T19:30:29.660174Z",
      "decided_by": "sdqe-admin01",
      "decision": "Approved",
      "href": "/api/access_transparency/v1/access_requests/2mtYZx9fFOuy1y67sRrVmLL5w5q/decisions/2mtYdtAcxaEYwbbP7iSgdFCAqqy",
      "id": "2mtYdtAcxaEYwbbP7iSgdFCAqqy",
      "justification": "test",
      "kind": "Decision",
      "updated_at": "2024-10-02T19:30:29.660174Z"
    }
  ],
  "duration": "8h",
  "href": "/api/access_transparency/v1/access_requests/2mtYZx9fFOuy1y67sRrVmLL5w5q",
  "id": "2mtYZx9fFOuy1y67sRrVmLL5w5q",
  "internal_support_case_id": "SDAINT-9253",
  "justification": "Testing",
  "kind": "AccessRequest",
  "organization_id": "1OAqHo0k19kyq7Xt7I1Zqb8Ok4K",
  "requested_by": "sdqe-admin01",
  "status": {
    "expires_at": "2024-10-03T03:30:29.660174Z",
    "state": "Approved"
  },
  "subscription_id": "2mtXwNcCC0bh3ST9cvI4tst8Lw8",
  "support_case_id": "",
  "updated_at": "2024-10-02T19:30:29.665909Z"
}
```

## Step
6. Deny the access request

```bash
rosa create decision -a ${ACCESS_REQUEST_ID} -d Denied -j test
```

## Expect
```
I: Successfully created the decision for access request '2mtYkOxGjMtoAGWfRb5Hst3t6Co'
```

You can run `ocm get /api/access_transparency/v1/access_requests/${ACCESS_REQUEST_ID}` to get more info:
```json
{
  "cluster_id": "2e5kvtptta5s8i4h9coadjp8i47kvivh",
  "created_at": "2024-10-02T19:29:58.313733Z",
  "deadline": "72h",
  "deadline_at": "2024-10-05T19:29:58.313733Z",
  "decisions": [
    {
      "created_at": "2024-10-02T19:30:29.660174Z",
      "decided_by": "sdqe-admin01",
      "decision": "Approved",
      "href": "/api/access_transparency/v1/access_requests/2mtYZx9fFOuy1y67sRrVmLL5w5q/decisions/2mtYdtAcxaEYwbbP7iSgdFCAqqy",
      "id": "2mtYdtAcxaEYwbbP7iSgdFCAqqy",
      "justification": "test",
      "kind": "Decision",
      "updated_at": "2024-10-02T19:30:29.660174Z"
    },
    {
      "created_at": "2024-10-02T19:30:56.374494Z",
      "decided_by": "sdqe-admin01",
      "decision": "Denied",
      "href": "/api/access_transparency/v1/access_requests/2mtYZx9fFOuy1y67sRrVmLL5w5q/decisions/2mtYhIkcglLQnxjaHLH8aTjjfJw",
      "id": "2mtYhIkcglLQnxjaHLH8aTjjfJw",
      "justification": "test",
      "kind": "Decision",
      "updated_at": "2024-10-02T19:30:56.374494Z"
    }
  ],
  "duration": "8h",
  "href": "/api/access_transparency/v1/access_requests/2mtYZx9fFOuy1y67sRrVmLL5w5q",
  "id": "2mtYZx9fFOuy1y67sRrVmLL5w5q",
  "internal_support_case_id": "SDAINT-9253",
  "justification": "Testing",
  "kind": "AccessRequest",
  "organization_id": "1OAqHo0k19kyq7Xt7I1Zqb8Ok4K",
  "requested_by": "sdqe-admin01",
  "status": {
    "state": "Denied"
  },
  "subscription_id": "2mtXwNcCC0bh3ST9cvI4tst8Lw8",
  "support_case_id": "",
  "updated_at": "2024-10-02T19:30:56.378277Z"
}
```

## Step
7. Make sure you can't deny without a justification

```bash
rosa create decision -a ${ACCESS_REQUEST_ID} -d Denied
```

## Expect
```
E: Non-empty value is required for 'justification' if 'decision' is set as 'Denied'
```

## Step
8. Make sure that if the access request is expired/denied you can't still approve the access request

```bash
rosa create decision -a ${ACCESS_REQUEST_ID} -d Approved
```

## Expect
```
E: status is 400, identifier is '21', code is 'OCM-ATS-21' and operation identifier is '2mtYj14uAiQ9kiTYLdo2wzRIXdF': The Access Request '2mtYZx9fFOuy1y67sRrVmLL5w5q' for this Decision is 'Denied' and new decisions cannot be made
```

## Step
9. Make sure that if the access request is expired/denied you can't still deny the access request

```bash
rosa create decision -a ${ACCESS_REQUEST_ID} -d Denied -j test
```

## Expect
```
E: status is 400, identifier is '21', code is 'OCM-ATS-21' and operation identifier is '2mtdrWOyxSsF3nmxDrfai8hcOX2': The Access Request '2mtYkOxGjMtoAGWfRb5Hst3t6Co' for this Decision is 'Denied' and new decisions cannot be made
```

## Step
10. Make sure that providing an invalid decision creates an error

```bash
rosa create decision -a ${ACCESS_REQUEST_ID} -d Invalid
```

## Expect
```
E: Invalid 'decision' value: 'Invalid', should be one of 'Approved', 'Denied'
```

## Step
11. Make sure that providing an access request id that doesn't exist creates an error

```bash
rosa create decision -a invalid -d Denied -j test
rosa create decision -a invalid -d Approved
```

## Expect
```
E: status is 404, identifier is '7', code is 'OCM-ATS-7' and operation identifier is '2mteCb2B3vcca1Fjh26q3g4kDSL': AccessRequest with id='invalid' not found
```

## Step
12. Try to make a decision without the access request ID

```bash
rosa create decision -d Approved
```

## Expect
```
Error: required flag(s) "access-request" not set
```

Also the help message should be displayed

## Step
13. Try to make a decision without specifying the decision

```bash
rosa create decision -a ${ACCESS_REQUEST_ID}
```

## Expect
```
Error: required flag(s) "decision" not set
```

Also the help message should be displayed
