# Test

## Step
1. Check the help message

```bash
rosa list access-requests -h
```

## Expect
```
List Access Requests in Pending or Approved status. If '--cluster' flag is used, list all Access Requests in any status for the specified cluster.

Usage:
  rosa list access-request [flags]

Aliases:
  access-request, accessrequest, accessrequests, access-requests

Examples:
  # List all Access Requests for cluster 'foo'
  rosa list access-request --cluster foo


Flags:
  -c, --cluster string   Name or ID of the cluster.
  -h, --help             help for access-request
  -o, --output string    Output format. Allowed formats are [json yaml]

Global Flags:
      --color string     Surround certain characters with escape sequences to display them in color on the terminal. Allowed options are [auto never always] (default "auto")
      --debug            Enable debug mode.
      --profile string   Use a specific AWS profile from your credential file.
      --region string    Use a specific AWS region, overriding the AWS_REGION environment variable. (DEPRECATED: Region flag will be removed from this command in future versions)
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
5. List pending access requests

```bash
rosa list access-request
rosa list access-request -c ${CLUSTER_ID}
```

## Expect
```
$ rosa list access-request
STATE    ID                           CLUSTER ID                        UPDATED AT
Pending  3JSaqiYQOCTM2G1ElOSBiqA6GPZ  2ss7bulenrhb4cackpfsmoaliqocoleh  Thu Sep 17 14:58:35 UTC 2026
I: Run the following command to approve or deny the Access Request:

   rosa create decision --access-request <ID> --decision Approved
   rosa create decision --access-request <ID> --decision Denied --justification "justification"
```

```
$ rosa list access-request -c 2ss7bulenrhb4cackpfsmoaliqocoleh
STATE    ID                           CLUSTER ID                        UPDATED AT
Pending  3JSaqiYQOCTM2G1ElOSBiqA6GPZ  2ss7bulenrhb4cackpfsmoaliqocoleh  Thu Sep 17 14:58:35 UTC 2026
I: Run the following command to approve or deny the Access Request:

   rosa create decision --access-request 3JSaqiYQOCTM2G1ElOSBiqA6GPZ --decision Approved
   rosa create decision --access-request 3JSaqiYQOCTM2G1ElOSBiqA6GPZ --decision Denied --justification "justification"
```

## Step
6. Approve the pending access request

```bash
rosa create decision --access-request=${ACCESS_REQUEST_ID} --decision Approved
```

## Expect
```
I: Successfully created the decision for Access Request '2nZS9zZPUMQPm4EuqN0xV0ATkDs'
```

## Step
7. List the approved access requests
```bash
rosa list access-request
rosa list access-request -c ${CLUSTER_ID}
```

## Expect
STATE    ID                           CLUSTER ID                        UPDATED AT
Approved 2nZS9zZPUMQPm4EuqN0xV0ATkDs  2efdhq5agtt3l3f7grhdhn47pli540n4  Thu Oct 17 15:30:13 UTC 2024

## Step
8. Deny the access request

```bash
rosa create decision --access-request=${ACCESS_REQUEST_ID} --decision Denied --justification Testing
```

## Expect
```
I: Successfully created the decision for Access Request '2nZS9zZPUMQPm4EuqN0xV0ATkDs'
```

## Step
9. List the access requests

```bash
rosa list access-request
```

## Expect
```
I: There are no Access Requests in Pending or Approved status.
```

## Step
10. List the access requests for the cluster

```bash
rosa list access-request -c ${CLUSTER_ID}
```

## Expect
```
STATE    ID                           CLUSTER ID                        UPDATED AT
Denied   2nZS9zZPUMQPm4EuqN0xV0ATkDs  2efdhq5agtt3l3f7grhdhn47pli540n4  Thu Oct 17 15:30:38 UTC 2024
```

## Step
11. Create a second cluster and access requests for both clusters

## Expect

## Step
12. List the access requests, and make sure that when using no cluster ID that both access requests show up, and you can filter by either cluster ID

### All clusters
```bash
rosa list access-request
```

### Cluster 1
```bash
rosa list access-request -c $CLUSTER_ID1
```

### Cluster 2
```bash
rosa list access-request -c $CLUSTER_ID2
```

## Expect

### All clusters
```
STATE    ID                           CLUSTER ID                        UPDATED AT
Pending  2ncd23fnkP4S6oNfBnZZU0OfU7z  2eg3rvgtm18l3j1sqg79fnn1q421etlu  Fri Oct 18 18:28:07 UTC 2024
Pending  2ncd1AAhrP500aemibnECp4NoYU  2efdhq5agtt3l3f7grhdhn47pli540n4  Fri Oct 18 18:28:00 UTC 2024
I: Run the following command to approve or deny the Access Request:

   rosa create decision --access-request <ID> --decision Approved
   rosa create decision --access-request <ID> --decision Denied --justification "justification"
```

### Cluster 1
```
STATE    ID                           CLUSTER ID                        UPDATED AT
Pending  2ncd1AAhrP500aemibnECp4NoYU  2efdhq5agtt3l3f7grhdhn47pli540n4  Fri Oct 18 18:28:00 UTC 2024
Denied   2nZS9zZPUMQPm4EuqN0xV0ATkDs  2efdhq5agtt3l3f7grhdhn47pli540n4  Thu Oct 17 15:30:38 UTC 2024
I: Run the following command to approve or deny the Access Request:

   rosa create decision --access-request 2ncd1AAhrP500aemibnECp4NoYU --decision Approved
   rosa create decision --access-request 2ncd1AAhrP500aemibnECp4NoYU --decision Denied --justification "justification"
```

### Cluster 2
```
STATE    ID                           CLUSTER ID                        UPDATED AT
Pending  2ncd23fnkP4S6oNfBnZZU0OfU7z  2eg3rvgtm18l3j1sqg79fnn1q421etlu  Fri Oct 18 18:28:07 UTC 2024
I: Run the following command to approve or deny the Access Request:

   rosa create decision --access-request 2ncd23fnkP4S6oNfBnZZU0OfU7z --decision Approved
   rosa create decision --access-request 2ncd23fnkP4S6oNfBnZZU0OfU7z --decision Denied --justification "justification"
```

## Step
13. Approve one access request

```
rosa create decision --access-request ${ACCESS_REQUEST_ID} --decision Approved
```

## Expect

## Step
14. List the access requests to make sure that the approved one shows up after the pending request in the list

```bash
rosa list access-request
```

## Expect
```
STATE    ID                           CLUSTER ID                        UPDATED AT
Pending  2ncd1AAhrP500aemibnECp4NoYU  2efdhq5agtt3l3f7grhdhn47pli540n4  Fri Oct 18 18:28:00 UTC 2024
Approved 2ncd23fnkP4S6oNfBnZZU0OfU7z  2eg3rvgtm18l3j1sqg79fnn1q421etlu  Fri Oct 18 18:31:38 UTC 2024
I: Run the following command to approve or deny the Access Request:

   rosa create decision --access-request <ID> --decision Approved
   rosa create decision --access-request <ID> --decision Denied --justification "justification"
```

## Step
15. List access requests for a cluster that doesn't exist

```bash
rosa list access-request -c invalid
```

## Expect
```
E: There is no cluster with identifier or name 'invalid'
```
