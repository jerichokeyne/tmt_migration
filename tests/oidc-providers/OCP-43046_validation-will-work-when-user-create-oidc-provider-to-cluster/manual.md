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
Create oidc-provider on standard rosa cluster  
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
Create oidc-provider on-existing rosa cluster  
$ rosa create operator-roles -c <non-exsiting cluster>

## Expect
There will be error output   
[xueli@xueli-work rosa]$ rosa create oidc-provider -c xuelirosaaaaaaaa  
E: Failed to get cluster 'xuelirosaaaaaaaa': There is no cluster with identifier or name 'xuelirosaaaaaaaa'

## Step
Create oidc-provier with region setting

## Expect
$ ./rosa create oidc-provider -c 29u37uimscqjfh1puervht9b9a2fe01a --region us-east-2  
E: The '--region' flag is not available when creating the OIDC provider. OIDC provider is a global AWS IAM entity.(from OCM-6119)

## Step
~~Create oidc-provider to the pending sts cluster without operator-roles created~~

## Expect
~~There will be error output [xueli@xueli-work rosa]$ rosa create oidc-provider -c xuelirosa3 -i E: Unable to find all required IAM roles for operators: xuelirosa3-openshift-cloud-credential-operator-cloud-credential- xuelirosa3-openshift-image-registry-installer-cloud-credentials xuelirosa3-openshift-ingress-operator-cloud-credentials xuelirosa3-openshift-cluster-csi-drivers-ebs-cloud-credentials xuelirosa3-openshift-machine-api-aws-cloud-credentials See 'rosa create operator-roles --help'~~
