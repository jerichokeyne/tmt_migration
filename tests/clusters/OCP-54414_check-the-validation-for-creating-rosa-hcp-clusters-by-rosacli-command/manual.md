# Test

## Step
Check the validation for subnet_ids flag when creating Hypershift cluster:  
1. without setting subnet_ids  
2. with one private subnet_id  
3. with one public subnet_id  
4. with the private and public subnet_ids which are Not in the same region of the cluster  
5. The version < 4.14   
If hypershift-enable-additional-minimal-version enable, the minimal version is 4.14.x  
If not enable, the minimal version is 4.12(Used for IBM LH users))

## Expect
It should fail with readable error message

## Step
Repeat step1~2 to check the validations for multi-az cluster

## Expect

## Step
create a multi-az ROSA Hypershift cluster with the autoscaling by setting the illegal 'min_replicas' or 'max_replicas' value.  
For the default machinepool:  
1. min_replicas or min_replicas are not the number of replicas be a multiple of 3  
2. min_replicas<2  
3. min_replicas >= max_replicas  
4.without 'min_replicas' and 'max_replicas' value

## Expect

## Step
create a multi-az ROSA Hypershift cluster:  
1. when no billing accounts added in interactive mode  
2. with empty billing-account option  
3. with invalid billing-account option  
  
~~Note: the validation should work under capability.organization.enforce_rosa_hcp_billing and the billing account id is hidden in interactive mode and help doc before the end_date in `ocm get /api/clusters_mgmt/v1/products/rosa/technology_previews/hcp-billing`, after the end_date the billing account id should show in the interactive mode~~

## Expect
1. E: No valid billing account associated. Go to <https://console.aws.amazon.com/rosa/home#/get-started> to enable ROSA with HCP for your intended billing account. You must have a valid billing account associated to continue.  
2. Failed to execute root command: flag needs an argument: --billing-account  
3. E: Failed to create cluster: Got error response - http 400 from account manager: BillingMarketplaceAccount 765374464689 not linked to organization 1TBZNa7kLQTshFFKjV2AVpY4Vjm at the aws marketplace

## Step
Create Hypershift with the account which org has no 'capability.organization.hypershift' capability

## Expect
It should fail with readable error.

## Step
Create Hypershift with rosa version is lower than minimal version  
(Note: here is the minimal version :<https://gitlab.cee.redhat.com/service/uhc-clusters-service/-/blame/master/pkg/models/clusters.go#L753> )

## Expect
It should fail with a readable error.  
E: Failed to create cluster: Creating hosted control plane cluster requires ROSA 1.2.31 or higher. Go to <https://console.redhat.com/openshift/downloads#tool-rosa> to download the latest version

## Step
Create Hypershift with non-managed policies (disable toggle :preflight-hosted-cp-managed-policies )

## Expect
It should fail with readable error.  
{  
"kind":"Error",  
"id":"400",  
"href":"/api/clusters_mgmt/v1/errors/400",  
"code":"CLUSTERS-MGMT-400",  
"reason":"Role 'arn:aws:iam::301721915996:role/sdq-ci-eunkl-Installer-Role' has unmanaged policies. Creating a hosted CP cluster with unmanaged policies isn't supported. Please create a new set of account roles with AWS managed policies with 'rosa create account-roles --hosted-cp'. The minimal ROSA CLI version that supports AWS managed policies is '1.2.30'. For more information see: https://docs.openshift.com/rosa/rosa_hcp/rosa-hcp-sts-creating-a-cluster-quickly.html#rosa-sts-creating-account-wide-sts-roles-and-policies_rosa-hcp-sts-creating-a-cluster-quickly",  
"operation_id":"6424bfea-918b-4c8d-a0e1-12a2d59e78ad"  
}

## Step
Create HCP cluster with account roles and operator roles that policies type are not same:managed/unmanaged policies  
(Toggle:preflight-operator-role-managed-policies)  
--only with operator_role_prefix  
--only with operator_iam_roles  
-- role with path

## Expect
It should fail with readable error  
{  
"kind":"Error",  
"id":"400",  
"href":"/api/clusters_mgmt/v1/errors/400",  
"code":"CLUSTERS-MGMT-400",  
"reason":"Role 'arn:aws:iam::301721915996:role/sdq-ci-fjfer-Installer-Role' has classic unmanaged policies. Operator role 'arn:aws:iam::301721915996:role/ying-op-kube-system-kms-provider' has hosted CP managed policies. Creating a cluster with unmatched managed policies isn't allowed. Please create a new set of operator roles with Classic ROSA policies",  
"operation_id":"fb98d511-dfa9-407b-b614-7857fc254606"  
}  
Or  
Please create a new set of operator roles with AWS managed policies

## Step
Create HCP cluster with account roles type that are not inconsistent  
(Manual simulate: rosa_hcp_policies: true/false)

## Expect
It should fail with readable error  
{  
"kind":"Error",  
"id":"400",  
"href":"/api/clusters_mgmt/v1/errors/400",  
"code":"CLUSTERS-MGMT-400",  
"reason":"Account role 'arn:aws:iam::301721915996:role/sdq-ci-fjfer-Installer-Role' has managed policies. Account role 'arn:aws:iam::301721915996:role/sdq-ci-fjfer-Support-Role' has unmanaged policies. Please create a new set of account roles with the same policy type.",  
"operation_id":"458ba2d3-38c7-4981-b15f-4987eb5ed70e"  
}

## Step
Add the capability "capability.organization.hypershift_disable" to your organization(OCM-5427)  
With capability, Create ROSA HCP cluster  
Without capability, Create ROSA HCP cluster

## Expect
It will be successful with capability, Create ROSA HCP cluster  
It will be failed without capability, Create ROSA HCP cluster with error message  
"Creating Hosted Control Plane clusters capability is disabled"
