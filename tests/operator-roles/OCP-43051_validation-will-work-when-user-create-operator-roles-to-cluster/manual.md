# Setup
$ rosa create cluster -c ${name}aa --region ${region} --version ${version}-${channel_group} --channel-group ${channel_group} --role-arn arn:aws:iam::${aws_account_id}:role/OSDCCSAdmin --tags cluster-name:${name},cluster-version:${version}-${channel_group} ${roles} --external-id "<external_id>"

# Test

## Step
Get the latest version of rosacli

## Expect
Support sts from version 1.0.6

## Step
Prepare three clusters   
1. A standard rosa cluster  
2. A sts cluster in status of installing not pending  
3. A sts cluster in status pending

## Expect
The cluster will be prepared successfully

## Step
Create operator-roles on standard rosa cluster  
$ rosa create operator-roles -c <standard cluster>

## Expect
There will be error output  
E: Cluster '<cluster name>' is not an STS cluster

## Step
Create operator-roles on non-pending rosa cluster  
$ rosa create operator-roles -c <standard cluster>

## Expect
There will be error output  
[xueli@xueli-work rosa]$ rosa create oidc-provider -c xuelirosa  
I: Cluster 'xuelirosa' is ready and does not need additional configuration.  
[xueli@xueli-work rosa]$ rosa create oidc-provider -c 1m64nrbojlma3b8dlocdmrsm7gskn2gr  
I: Cluster '1m64nrbojlma3b8dlocdmrsm7gskn2gr' is installing and does not need additional configuration.

## Step
Create operator-roles on-existing rosa cluster  
$ rosa create operator-roles -c <non-exsiting cluster>

## Expect
There will be error output   
[xueli@xueli-work rosa]$ rosa create oidc-provider -c xuelirosaaaaaaaa  
E: Failed to get cluster 'xuelirosaaaaaaaa': There is no cluster with identifier or name 'xuelirosaaaaaaaa'

## Step
Create operator-roles to sts cluster without -c indicating

## Expect
Correct error with usage will show

## Step
Create operator-roles without corresponding existing operator policies  
-- The prefix not match the prefix when run rosa init account

## Expect
There should be error message like below.  
[xueli@xueli-work rosa]$ rosa create operator-roles -c xuelirosa4 --prefix xuelirosa4 -y  
? Role prefix: xuelirosa4  
? Role creation mode: auto  
I: Creating roles using 'arn:aws:iam::301721915996:user/xueli'  
I: Created role 'dkljakldjsf-openshift-ingress-operator-cloud-credentials' with ARN 'arn:aws:iam::301721915996:role/dkljakldjsf-openshift-ingress-operator-cloud-credentials'  
E: There was an error creating the operator roles: NoSuchEntity: Policy arn:aws:iam::301721915996:policy/xuelirosa4-openshift-ingress-operator-cloud-credentials does not exist or is not attachable.  
status code: 404, request id: bb1cebf1-dbcd-42d1-95b9-d0f8c4651be9

## Step
Create operator-roles with invalid permissions-boundary  
--permissions-boundary invalid

## Expect
There should be error message like below  
[xueli@xueli-work ~]$ rosa create operator-roles -c xuelists3 --permissions-boundary invalid --mode auto -y  
E: Expected a valid policy ARN: arn: invalid prefix

## Step
Create operator-roles with non-existing permissions-boundary  
--permissions-boundary arn:aws:iam::301721915996:policy/non-existing

## Expect
[xueli@xueli-work ~]$ rosa create operator-roles -c xuelists3 --permissions-boundary arn:aws:iam::301721915996:policy/xuelinop --mode auto -y  
E: There was an error creating the operator roles: NoSuchEntity: Scope ARN: arn:aws:iam::301721915996:policy/xuelinop does not exist or is not attachable.  
status code: 404, request id: 205660d8-b37b-4565-8da1-a524ad7bfad4
