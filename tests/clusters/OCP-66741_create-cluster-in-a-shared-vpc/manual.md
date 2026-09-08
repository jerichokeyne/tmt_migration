# Test

## Step
(For reference) Shared-VPC on ROSA  
<https://docs.google.com/presentation/d/1EdXUgmmYIU_grHpjRPysbdfXNKs-c_iMGSd19i-nCGY/edit#slide=id.g6445211f96_0_80>   
(For reference) Shared VPC STS cluster steps  
<https://docs.google.com/document/d/1cJbD_3OkIXTnmCFoKspFq89sXUfZo-blgRe8_o6xhOo/edit>

## Expect

## Step
Create shared-vpc cluster in auto away  
  
`rosa create cluster -m auto -y \  
**--cluster-name "${CLUSTER_NAME}" \  
--sts \  
--region "${REGION}" \  
--subnet-ids ${subnet_ids_comma} \  
--operator-roles-prefix "${CLUSTER_NAME}" \  
--oidc-config-id ${oidc_id} \  
--private-hosted-zone-id ${HOSTED_ZONE_ID} \  
--shared-vpc-role-arn \"${ROLE_ARN}\" \  
--base-domain ${CLUSTER_BASE_DOMAIN} \  
--role-arn \"${INSTALLER_ROLE_ARN}\" \`  
--controlplane-iam-role \"${MASTER_ROLE_ARN}\" \  
--support-role-arn \"${SUPPORT_ROLE_ARN}\" \  
--worker-iam-role \"${WORKER_ROLE_ARN}\" \  
--version "${VERSION_RAW_ID}" \  
--channel-group ${CHANNEL_GROUP} \**

## Expect
1. cluster is created successfully and healthy, refer to    
  
2. Private Hosted Zone info is listed  
`rosa describe cluster -c yunjiang-clia | grep -A 2 "Private Hosted Zone:"  
Private Hosted Zone:  
- ID: Z01722152SZBYLQH13HJ8  
- Role ARN: arn:aws:iam::641733028092:role/yunjiang-clia-shared-vpc-rol1`  
  
3. ingress policy is for shared VPC (with sts:AssumeRole)  
`cluster_name=yunjiang-clia  
ingress_role_name=$(rosa describe cluster -c ${cluster_name} -ojson | jq -r '.aws.sts.operator_iam_roles[] | select(.namespace=="openshift-ingress-operator") | .role_arn' | cut -d/ -f2)  
ingress_policy_arn=$(aws iam list-attached-role-policies --role-name yunjiang-clia-g6c6-openshift-ingress-operator-cloud-credentials | jq -r '.AttachedPolicies[0].PolicyArn')  
  
aws iam get-policy-version --version-id v1 --policy-arn $ingress_policy_arn  
{  
"PolicyVersion": {  
"Document": {  
"Version": "2012-10-17",  
"Statement": [  
{  
"Action": [  
"route53:ChangeResourceRecordSets"  
],  
"Effect": "Allow",  
"Resource": "*",  
"Condition": {  
"ForAllValues:StringLike": {  
"route53:ChangeResourceRecordSetsNormalizedRecordNames": [  
"*.devshift.org",  
"*.devshiftusgov.com",  
"*.openshiftapps.com",  
"*.openshiftusgov.com"  
]  
}  
}  
},  
{  
"Action": [  
"elasticloadbalancing:DescribeLoadBalancers",  
"route53:ListHostedZones",  
"tag:GetResources"  
],  
"Effect": "Allow",  
"Resource": "*"  
},  
{  
"Action": "sts:AssumeRole",  
"Effect": "Allow",  
"Resource": "arn:aws:iam::641733028092:role/yunjiang-clia-shared-vpc-rol1"  
}  
]  
},  
"VersionId": "v1",  
"IsDefaultVersion": false,  
"CreateDate": "2023-08-21T08:18:43+00:00"  
}  
}`

## Step
Day 2 operations:  
* Check web UI (will update details once UI is available )  
* Run regression tests, the cases for Shared VPC cluster is listed in <https://docs.google.com/spreadsheets/d/1BUrIIojyMrLk7iqyc07K-gK0Y08NI3e07Qa-Yjw8EQc/edit#gid=0>

## Expect
No issues

## Step
Create shared-vpc cluster (operator roles are created after create cluster) (waiting state)  
<https://issues.redhat.com/browse/OCM-3341>   
  
Using above command, but remove operator-roles-prefix and oidc param:  
rosa create cluster -m auto -y \  
**--cluster-name "${CLUSTER_NAME}" \  
--sts \  
--region "${REGION}" \  
--subnet-ids ${subnet_ids_comma} \  
~~--operator-roles-prefix "${CLUSTER_NAME}" \~~  
~~--oidc-config-id ${oidc_id} \~~  
--private-hosted-zone-id ${HOSTED_ZONE_ID} \  
--shared-vpc-role-arn \"${ROLE_ARN}\" \  
--base-domain ${CLUSTER_BASE_DOMAIN} \  
--role-arn \"${INSTALLER_ROLE_ARN}\" \**  
--controlplane-iam-role \"${MASTER_ROLE_ARN}\" \  
--support-role-arn \"${SUPPORT_ROLE_ARN}\" \  
--worker-iam-role \"${WORKER_ROLE_ARN}\" \  
--version "${VERSION_RAW_ID}" \  
--channel-group ${CHANNEL_GROUP}   
  
Create operator roles and oidc after creating cluster

## Expect
1. Describe cluster cluster will see:  
  
waiting (Operator Role(s) not found: Role name 'yunjiang-18a-o3i5-openshift-ingress-operator-cloud-credentials' does not exists for cluster '274dng9c4gse5ckbdongipmkv72p35eo')  
  
2. After creating operator roles:  
  
waiting (OIDC Provider not found: failed to assume role with web identity: operation error STS: AssumeRoleWithWebIdentity, https response error StatusCode: 400, RequestID: 8f6fdce9-f53c-4f0e-ae89-1ed2e2d0228b, InvalidIdentityToken: No OpenIDConnect provider found in your account for https://d3gt1gce2zmg3d.cloudfront.net/274dng9c4gse5ckbdongipmkv72p35eo)  
  
3. After creating OIDC  
  
waiting (Failed to verify ingress operator for shared VPC: Failed to assume role with ARN 'arn:aws:iam::641733028092:role/yunjiang-18a-shared-vpc-rol1': failed to assume role: operation error STS: AssumeRole, https response error StatusCode: 403, RequestID: 16f4c74e-c60a-4d30-a5e7-319de25bd0e2, api error AccessDenied: User: arn:aws:sts::301721915996:assumed-role/yunjiang-18a-o3i5-openshift-ingress-operator-cloud-credentials/OCM is not authorized to perform: sts:AssumeRole on resource: arn:aws:iam::641733028092:role/yunjiang-18a-shared-vpc-rol1)  
  
4. After adding ingress role to trust policy  
Cluster was created successfully.
