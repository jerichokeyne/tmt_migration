# Test

## Step
1. Check the help message  
  
rosa describe access-request -h

## Expect
Show details of an Access Request  
  
Usage:  
rosa describe access-request [flags]  
  
Aliases:  
access-request, accessrequest  
  
Examples:  
\# Describe an Access Request wit id <access_request_id>  
rosa describe access-request --id <access_request_id>  
  
  
Flags:  
-h, --help help for access-request  
--id string ID of the Access Request. (required).  
-o, --output string Output format. Allowed formats are [json yaml]  
  
Global Flags:  
--color string Surround certain characters with escape sequences to display them in color on the terminal. Allowed options are [auto never always] (default "auto")  
--debug Enable debug mode.  
--profile string Use a specific AWS profile from your credential file.  
--region string Use a specific AWS region, overriding the AWS_REGION environment variable. (DEPRECATED: Region flag will be removed from this command in future versions)

## Step
2. Create a ROSA/ROSA HCP cluster

## Expect

## Step
3. Add the "capability.cluster.enable_access_protection" label to the cluster's subscription  
  
You can get the subscription ID by running (replace CLUSTER_ID with your cluster's ID):  
subscription_id=$(ocm get /api/accounts_mgmt/v1/subscriptions -p search="cluster_id is 'CLUSTER_ID'" | jq -r .items[0].id)  
  
You can then add the label by running this command logged in as the super admin account:  
echo '{"kind": "Label", "internal": true, "key": "capability.cluster.enable_access_protection", "value": "true"}' | ocm post "/api/accounts_mgmt/v1/subscriptions/$subscription_id/labels"

## Expect
{  
"created_at":"2024-10-02T19:29:43.474234Z",  
"href":"/api/accounts_mgmt/v1/subscriptions/2mtXwNcCC0bh3ST9cvI4tst8Lw8/labels/capability.cluster.enable_access_protection",  
"id":"2mtYY6Fuj0B8nlLkrLl4MSyTqcR",  
"internal":true,  
"key":"capability.cluster.enable_access_protection",  
"kind":"Label",  
"subscription_id":"2mtXwNcCC0bh3ST9cvI4tst8Lw8",  
"updated_at":"2024-10-02T19:31:20.879347Z",  
"value":"true"  
}

## Step
4. Create an access request (if your account can't make an access request, try with the org admin account)  
  
You can create an access request by running this (replace CLUSTER_ID with your cluster's ID, and if needed you can replace SDAINT-9253 with another JIRA ticket in the SDAINT project):  
echo '{"justification": "Testing", "cluster_id": "CLUSTER_ID", "internal_support_case_id": "SDAINT-9253"}' | ocm post /api/access_transparency/v1/access_requests

## Expect
{  
"cluster_id":"2e5kvtptta5s8i4h9coadjp8i47kvivh",  
"created_at":"2024-10-02T19:31:21.481968Z",  
"deadline":"72h",  
"deadline_at":"2024-10-05T19:31:21.481968Z",  
"duration":"8h",  
"href":"/api/access_transparency/v1/access_requests/2mtYkOxGjMtoAGWfRb5Hst3t6Co",  
"id":"2mtYkOxGjMtoAGWfRb5Hst3t6Co",  
"internal_support_case_id":"SDAINT-9253",  
"justification":"Testing",  
"kind":"AccessRequest",  
"organization_id":"1OAqHo0k19kyq7Xt7I1Zqb8Ok4K",  
"requested_by":"sdqe-admin01",  
"status": {  
"state":"Pending"  
},  
"subscription_id":"2mtXwNcCC0bh3ST9cvI4tst8Lw8",  
"support_case_id":"",  
"updated_at":"2024-10-02T19:31:21.481968Z"  
}

## Step
5. Describe the access request  
  
rosa describe access-request --id=$ACCESS_REQUEST_ID

## Expect
ID: 2nFVxq5ki0ktsRtmhrSyGf98TVB  
Subscription ID: 2nAAQqLuLAUeo3Row1qEIWhDDjN  
Cluster ID: 2e9h3sh7nguvamnanq0nudpi38qrssr2  
Support Case ID:  
Requested By: sdqe-admin01  
Created At: Thu Oct 10 14:04:19 UTC 2024  
Respond By: Sun Oct 13 14:04:19 UTC 2024  
Request Duration: 8h  
Justification: Testing  
Status: Pending  
I: Run the following command to approve or deny the access request:  
  
rosa create decision --access-request 2nFVxq5ki0ktsRtmhrSyGf98TVB --decision Approved  
rosa create decision --access-request 2nFVxq5ki0ktsRtmhrSyGf98TVB --decision Denied

## Step
6. Check the output flag  
  
rosa describe access-request --id=$ACCESS_REQUEST_ID -o yaml  
rosa describe access-request --id=$ACCESS_REQUEST_ID -o json

## Expect
cluster_id: 2e9h3sh7nguvamnanq0nudpi38qrssr2  
created_at: "2024-10-10T14:04:19Z"  
deadline: 72h  
deadline_at: "2024-10-13T14:04:19Z"  
duration: 8h  
href: /api/access_transparency/v1/access_requests/2nFVxq5ki0ktsRtmhrSyGf98TVB  
id: 2nFVxq5ki0ktsRtmhrSyGf98TVB  
internal_support_case_id: SDAINT-9253  
justification: Testing  
kind: AccessRequest  
organization_id: 1OAqHo0k19kyq7Xt7I1Zqb8Ok4K  
requested_by: sdqe-admin01  
status:  
state: Pending  
subscription_id: 2nAAQqLuLAUeo3Row1qEIWhDDjN  
support_case_id: ""  
updated_at: "2024-10-10T14:04:19Z"  
  
  
{  
"kind": "AccessRequest",  
"id": "2nFVxq5ki0ktsRtmhrSyGf98TVB",  
"href": "/api/access_transparency/v1/access_requests/2nFVxq5ki0ktsRtmhrSyGf98TVB",  
"cluster_id": "2e9h3sh7nguvamnanq0nudpi38qrssr2",  
"created_at": "2024-10-10T14:04:19Z",  
"deadline": "72h",  
"deadline_at": "2024-10-13T14:04:19Z",  
"duration": "8h",  
"internal_support_case_id": "SDAINT-9253",  
"justification": "Testing",  
"organization_id": "1OAqHo0k19kyq7Xt7I1Zqb8Ok4K",  
"requested_by": "sdqe-admin01",  
"status": {  
"state": "Pending"  
},  
"subscription_id": "2nAAQqLuLAUeo3Row1qEIWhDDjN",  
"support_case_id": "",  
"updated_at": "2024-10-10T14:04:19Z"  
}

## Step
7. Try with an invalid access request ID  
  
rosa describe access-request --id=invalid

## Expect
E: The Access Request with id '2nFVxq5ki0ktsRtmhrSyGf98TV' does not exist

## Step
8. Make sure that the "--id" flag is required  
  
rosa describe access-request

## Expect
Error: required flag(s) "id" not set  
Usage:  
rosa describe access-request [flags]  
  
Aliases:  
access-request, accessrequest  
  
Examples:  
\# Describe an Access Request wit id <access_request_id>  
rosa describe access-request --id <access_request_id>  
  
  
Flags:  
-h, --help help for access-request  
--id string ID of the Access Request. (required).  
-o, --output string Output format. Allowed formats are [json yaml]  
  
Global Flags:  
--color string Surround certain characters with escape sequences to display them in color on the terminal. Allowed options are [auto never always] (default "auto")  
--debug Enable debug mode.  
--profile string Use a specific AWS profile from your credential file.  
--region string Use a specific AWS region, overriding the AWS_REGION environment variable.  
  
Failed to execute root command: required flag(s) "id" not set
