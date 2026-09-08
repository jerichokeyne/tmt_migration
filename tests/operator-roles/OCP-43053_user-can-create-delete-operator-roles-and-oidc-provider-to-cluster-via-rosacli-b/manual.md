# Setup
$ rosa create cluster -c ${name}aa --region ${region} --version ${version}-${channel_group} --channel-group ${channel_group} --role-arn arn:aws:iam::${aws_account_id}:role/OSDCCSAdmin --tags cluster-name:${name},cluster-version:${version}-${channel_group} ${roles} --external-id "<external_id>"

# Test

## Step
Get the latest version of rosacli

## Expect
Support sts from version 1.0.6

## Step
Run command to check the help message  
$ rosa create operator-roles -h

## Expect
- The usage should output  
- The usage should be clear and correct  
[xueli@xueli-work ~]$ rosa create operator-roles -h  
Create cluster-specific operator IAM roles based on your cluster configuration.  
  
  
Usage:  
rosa create operator-roles [flags]  
  
  
Aliases:  
operator-roles, operatorroles  
  
  
Examples:  
\# Create default operator roles for cluster named "mycluster"  
rosa create operator-roles --cluster=mycluster  
  
  
\# Create operator roles with a specific permissions boundary  
rosa create operator-roles -c mycluster --permissions-boundary arn:aws:iam::123456789012:policy/perm-boundary  
  
  
Flags:  
-c, --cluster string Name or ID of the cluster to create the roles for (required).  
-h, --help help for operator-roles  
-i, --interactive Enable interactive mode.  
--mode string How to perform the operation. Valid options are:  
auto: Roles will be created using the current AWS account  
manual: Role files will be saved in the current directory (default "auto")  
--permissions-boundary string The ARN of the policy that is used to set the permissions boundary for the operator roles.  
--prefix string User-defined prefix for generated AWS operator policies. Leave empty to attempt to find them automatically.  
  
  
Global Flags:  
--debug Enable debug mode.  
--profile string Use a specific AWS profile from your credential file.  
--region string Use a specific AWS region, overriding the AWS_REGION environment variable.  
-y, --yes Automatically answer yes to confirm operation.

## Step
Run command to check the help message  
$ rosa create oidc-provider -h

## Expect
- The usage should output  
- The usage should be clear and correct  
[xueli@xueli-work rosa]$ rosa create oidc-provider -h  
Create OIDC provider for operators to authenticate against in an STS cluster.  
  
Usage:  
rosa create oidc-provider [flags]  
  
Aliases:  
oidc-provider, oidcprovider  
  
Examples:  
\# Create OIDC provider for cluster named "mycluster"  
rosa create oidc-provider --cluster=mycluster  
  
Flags:  
-c, --cluster string Name or ID of the cluster to create the roles for (required).  
-h, --help help for oidc-provider  
-i, --interactive Enable interactive mode.  
--mode string How to perform the operation. Valid options are:  
auto: Roles will be created using the current AWS account  
manual: Role files will be saved in the current directory (default "auto")  
  
Global Flags:  
--debug Enable debug mode.  
--profile string Use a specific AWS profile from your credential file.  
-y, --yes Automatically answer yes to confirm operation.

## Step
Prepare accounts on AWS via command  
$rosa create account-roles

## Expect
The accounts will be prepared successfully

## Step
Create rosa cluster with the command output by last step

## Expect

## Step
Input prefix for operator-roles with a valid string like "rosa1"

## Expect
The cluster will be created successfully

## Step
Create operator-roles via rosa  
$ rosa create operator-roles -c <clustername> --prefix <policy prefix> --mode auto -y --permissions-boundary <boundary policy>

## Expect
- The roles will be created and output to console with arn.  
- The version tag should be same with the default openshift version(X.Y)  
[xueli@xueli-work rosa]$ rosa create operator-roles -c xuelirosa4 --prefix ManagedOpenShift -y --mode auto  
I: Creating roles using 'arn:aws:iam::301721915996:user/xueli'  
I: Created role 'dkljakldjsf-openshift-machine-api-aws-cloud-credentials' with ARN 'arn:aws:iam::301721915996:role/dkljakldjsf-openshift-machine-api-aws-cloud-credentials'  
I: Created role 'dkljakldjsf-openshift-cloud-credential-operator-cloud-credential' with ARN 'arn:aws:iam::301721915996:role/dkljakldjsf-openshift-cloud-credential-operator-cloud-credential'  
I: Created role 'dkljakldjsf-openshift-image-registry-installer-cloud-credentials' with ARN 'arn:aws:iam::301721915996:role/dkljakldjsf-openshift-image-registry-installer-cloud-credentials'  
I: Created role 'dkljakldjsf-openshift-ingress-operator-cloud-credentials' with ARN 'arn:aws:iam::301721915996:role/dkljakldjsf-openshift-ingress-operator-cloud-credentials'  
I: Created role 'dkljakldjsf-openshift-cluster-csi-drivers-ebs-cloud-credentials' with ARN 'arn:aws:iam::301721915996:role/dkljakldjsf-openshift-cluster-csi-drivers-ebs-cloud-credentials'

## Step
Launch AWS to check the roles

## Expect
-The roles should exist on AWS  
- All of the roles created should have the indicated permission boundary

## Step
Create oidc-provider via rosa for the cluster  
$ rosa create oidc-provider -c xuelirosa4 -y

## Expect
The provider will be created with arn output to console  
[xueli@xueli-work rosa]$ rosa create oidc-provider -c xuelirosa4 -y  
? Role creation mode: auto  
I: Creating OIDC provider using 'arn:aws:iam::301721915996:user/xueli'  
I: Created OIDC provider with ARN 'arn:aws:iam::301721915996:oidc-provider/rh-oidc.s3.us-east-1.amazonaws.com/1m66gp3jjlt1e7lmhbrddssd0694odbu'

## Step
Launch AWS to check the provider and the roles

## Expect
- The provider existing in AWS  
- The operator roles created before will be attached the oidc provider as trust relationship

## Step
Repeat above steps with --mode manual

## Expect
- The output for opertor-roles will be like below.  
- The version tag should be same with the default openshift version(X.Y)  
[xueli@xueli-work tmp]$ rosa create operator-roles -c xuelirosa5 --mode manual --prefix xuelirosa5  
I: Run the following commands to create the operator roles:  
  
aws iam create-role \  
--role-name dkljakldjsf-openshift-ingress-operator-cloud-credentials \  
--assume-role-policy-document file://operator_ingress_operator_cloud_credentials_policy.json \  
--tags Key=rosa_cluster_id,Value=1m67g3tjn36j45ie90p1cp74khh0dhc4 Key=rosa_openshift_version,Value=4.7 Key=rosa_role_prefix,Value=xuelirosa5 Key=operator_namespace,Value=openshift-ingress-operator Key=operator_name,Value=cloud-credentials  
  
aws iam attach-role-policy \  
--role-name dkljakldjsf-openshift-ingress-operator-cloud-credentials \  
--policy-arn arn:aws:iam::301721915996:policy/xuelirosa5-openshift-ingress-operator-cloud-credentials  
  
aws iam create-role \  
--role-name dkljakldjsf-openshift-cluster-csi-drivers-ebs-cloud-credentials \  
--assume-role-policy-document file://operator_cluster_csi_drivers_ebs_cloud_credentials_policy.json \  
--tags Key=rosa_cluster_id,Value=1m67g3tjn36j45ie90p1cp74khh0dhc4 Key=rosa_openshift_version,Value=4.7 Key=rosa_role_prefix,Value=xuelirosa5 Key=operator_namespace,Value=openshift-cluster-csi-drivers Key=operator_name,Value=ebs-cloud-credentials  
  
aws iam attach-role-policy \  
--role-name dkljakldjsf-openshift-cluster-csi-drivers-ebs-cloud-credentials \  
--policy-arn arn:aws:iam::301721915996:policy/xuelirosa5-openshift-cluster-csi-drivers-ebs-cloud-credentials  
  
aws iam create-role \  
--role-name dkljakldjsf-openshift-machine-api-aws-cloud-credentials \  
--assume-role-policy-document file://operator_machine_api_aws_cloud_credentials_policy.json \  
--tags Key=rosa_cluster_id,Value=1m67g3tjn36j45ie90p1cp74khh0dhc4 Key=rosa_openshift_version,Value=4.7 Key=rosa_role_prefix,Value=xuelirosa5 Key=operator_namespace,Value=openshift-machine-api Key=operator_name,Value=aws-cloud-credentials  
  
aws iam attach-role-policy \  
--role-name dkljakldjsf-openshift-machine-api-aws-cloud-credentials \  
--policy-arn arn:aws:iam::301721915996:policy/xuelirosa5-openshift-machine-api-aws-cloud-credentials  
  
aws iam create-role \  
--role-name dkljakldjsf-openshift-cloud-credential-operator-cloud-credential \  
--assume-role-policy-document file://operator_cloud_credential_operator_cloud_credential_operator_iam_ro_creds_policy.json \  
--tags Key=rosa_cluster_id,Value=1m67g3tjn36j45ie90p1cp74khh0dhc4 Key=rosa_openshift_version,Value=4.7 Key=rosa_role_prefix,Value=xuelirosa5 Key=operator_namespace,Value=openshift-cloud-credential-operator Key=operator_name,Value=cloud-credential-operator-iam-ro-creds  
  
aws iam attach-role-policy \  
--role-name dkljakldjsf-openshift-cloud-credential-operator-cloud-credential \  
--policy-arn arn:aws:iam::301721915996:policy/xuelirosa5-openshift-cloud-credential-operator-cloud-credential-  
  
aws iam create-role \  
--role-name dkljakldjsf-openshift-image-registry-installer-cloud-credentials \  
--assume-role-policy-document file://operator_image_registry_installer_cloud_credentials_policy.json \  
--tags Key=rosa_cluster_id,Value=1m67g3tjn36j45ie90p1cp74khh0dhc4 Key=rosa_openshift_version,Value=4.7 Key=rosa_role_prefix,Value=xuelirosa5 Key=operator_namespace,Value=openshift-image-registry Key=operator_name,Value=installer-cloud-credentials  
  
aws iam attach-role-policy \  
--role-name dkljakldjsf-openshift-image-registry-installer-cloud-credentials \  
--policy-arn arn:aws:iam::301721915996:policy/xuelirosa5-openshift-image-registry-installer-cloud-credentials

## Step
Create the roles with the commands

## Expect
All of the roles created successfully

## Step
Create oidc-provider with --mode manual

## Expect
The output of create oidc-provider will be:  
[xueli@xueli-work tmp]$ rosa create oidc-provider -c xuelirosa5 --mode manual  
I: Run the following commands to create the OIDC provider:  
  
aws iam create-open-id-connect-provider \  
--url https://rh-oidc.s3.us-east-1.amazonaws.com/1m67g3tjn36j45ie90p1cp74khh0dhc4 \  
--client-id-list openshift sts.amazonaws.com \  
--thumbprint-list a9d53002e97e00e043244f3d170d6f4c414104fd

## Step
Run the command in the output

## Expect
The open-id provider will be created successfully

## Step
Delete the cluster

## Expect

## Step
Delete the operator-roles by command in the manual mode

## Expect
- The aws commands will be prompted.  
- The operator roles can be deleting by running the prompted aws commands.

## Step
Delete the oidc provider by command in the manual mode

## Expect
- The aws commands will be prompted.  
- The oidc provider can be deleting by running the prompted aws commands.
