# Test

## Step
Log in with rosacil and prepare account-roles with the low version 4.7

## Expect

## Step
Check the help message of 'create cluster'

## Expect
There is bellow help message:  
-m, --mode string How to perform the operation. Valid options are:  
auto: Resource changes will be automatic applied using the current AWS account  
  
manual: Commands necessary to modify AWS resources will be output to be run manually

## Step
Create a STS cluster which has available upgrade version with some higher Y-version with the account-roles

## Expect

## Step
Try to upgrade the cluster without --mode

## Expect
1. There is a step of 'Ensuring cluster roles and policies are compatible with upgrade.'  
2. The cluster fails to upgrade with bellow message.  
  
I: Ensuring cluster roles and policies are compatible with upgrade.  
I: Cluster Roles are not valid with upgrade version 4.8.17. Run the following command(s) to upgrade Cluster Roles:  
rosa upgrade account-roles --prefix cf47  
rosa upgrade operator-roles --cluster 1ob7c0nb286m6ima34ef3gn6kqi51nm1  
[root@yuwan rosa]#

## Step
Try to upgrade the cluster with --mode auto

## Expect
1. There is a step of Ensuring cluster roles and policies are compatible with upgrade. and if the version is not compatible, the options to upgrade the account-roles prompted.  
2. There a step if 'I: Preparing to upgrade operator roles.' and the options to upgrade the operator roles prompted if not compatible.  
  
[root@yuwan rosa]# ./rosa upgrade cluster -c 1ob4ubhaellt2k3sq45239eoafpbf528 --version 4.8.17 --mode auto  
I: Ensuring cluster roles and policies are compatible with upgrade.  
I: Preparing to upgrade account roles.  
I: Starting to upgrade the policies  
? Upgrade the 'dq47-Installer-Role' role polices to version 4.9? Yes  
I: Upgraded policy with ARN 'arn:aws:iam::301721915996:policy/dq47-Installer-Role-Policy' to version '4.9'  
? Upgrade the 'dq47-ControlPlane-Role' role polices to version 4.9? Yes  
I: Upgraded policy with ARN 'arn:aws:iam::301721915996:policy/dq47-ControlPlane-Role-Policy' to version '4.9'  
? Upgrade the 'dq47-Worker-Role' role polices to version 4.9? Yes  
I: Upgraded policy with ARN 'arn:aws:iam::301721915996:policy/dq47-Worker-Role-Policy' to version '4.9'  
? Upgrade the 'dq47-Support-Role' role polices to version 4.9? Yes  
I: Upgraded policy with ARN 'arn:aws:iam::301721915996:policy/dq47-Support-Role-Policy' to version '4.9'  
? Upgrade the operator role policies to version 4.9? Yes  
I: Upgraded policy with ARN 'arn:aws:iam::301721915996:policy/dq47-openshift-ingress-operator-cloud-credentials' to version '4.9'  
I: Upgraded policy with ARN 'arn:aws:iam::301721915996:policy/dq47-openshift-cluster-csi-drivers-ebs-cloud-credentials' to version '4.9'  
I: Upgraded policy with ARN 'arn:aws:iam::301721915996:policy/dq47-openshift-machine-api-aws-cloud-credentials' to version '4.9'  
I: Upgraded policy with ARN 'arn:aws:iam::301721915996:policy/dq47-openshift-cloud-credential-operator-cloud-credential-operat' to version '4.9'  
I: Upgraded policy with ARN 'arn:aws:iam::301721915996:policy/dq47-openshift-image-registry-installer-cloud-credentials' to version '4.9'  
I: Preparing to upgrade operator roles.  
I: Starting to upgrade the policies  
? Upgrade the 'yw-1108-sts1-d1j0-openshift-machine-api-aws-cloud-credentials' operator role policy to version 4.9? Yes  
I: Upgraded policy with ARN 'arn:aws:iam::301721915996:policy/dq47-openshift-machine-api-aws-cloud-credentials' to version '4.9'  
? Upgrade the 'yw-1108-sts1-d1j0-openshift-cloud-credential-operator-cloud-cred' operator role policy to version 4.9? Yes  
I: Upgraded policy with ARN 'arn:aws:iam::301721915996:policy/dq47-openshift-cloud-credential-operator-cloud-credential-operat' to version '4.9'  
? Upgrade the 'yw-1108-sts1-d1j0-openshift-image-registry-installer-cloud-crede' operator role policy to version 4.9? Yes  
I: Upgraded policy with ARN 'arn:aws:iam::301721915996:policy/dq47-openshift-image-registry-installer-cloud-credentials' to version '4.9'  
? Upgrade the 'yw-1108-sts1-d1j0-openshift-ingress-operator-cloud-credentials' operator role policy to version 4.9? Yes  
I: Upgraded policy with ARN 'arn:aws:iam::301721915996:policy/dq47-openshift-ingress-operator-cloud-credentials' to version '4.9'  
? Upgrade the 'yw-1108-sts1-d1j0-openshift-cluster-csi-drivers-ebs-cloud-creden' operator role policy to version 4.9? Yes  
I: Upgraded policy with ARN 'arn:aws:iam::301721915996:policy/dq47-openshift-cluster-csi-drivers-ebs-cloud-credentials' to version '4.9'  
? Please input desired date in format yyyy-mm-dd: 2021-11-08  
? Please input desired UTC time in format HH:mm: 07:03  
? Node draining: 15 minutes  
I: Upgrade successfully scheduled for cluster '1ob4ubhaellt2k3sq45239eoafpbf528'  
[root@yuwan rosa]#  
  
NOTE: When upgrade to 4.10.* there is a new operator policy will be created 'openshift-cloud-network-config-controller-cloud' and user will be prompted with a message to create this new role

## Step
Try to upgrade the cluster with --mode manual

## Expect
It fails to upgrade the cluster with the commands to upgrade the account role/policies and operator roles.   
The cluster can be upgraded after run the commands manually.  
[root@yuwan rosa]# ./rosa upgrade cluster -c 1ob7c0nb286m6ima34ef3gn6kqi51nm1 --version 4.8.17 --mode manual  
I: Ensuring cluster roles and policies are compatible with upgrade.  
I: Preparing to upgrade account roles.  
I: All policy files saved to the current directory  
I: Run the following commands to upgrade the account role policies:  
aws iam create-policy-version \  
--policy-arn arn:aws:iam::301721915996:policy/cf47-Installer-Role-Policy \  
--policy-document file://sts_installer_permission_policy.json \  
--set-as-default  
aws iam tag-policy \  
--tags Key=rosa_openshift_version,Value=4.9 \  
--policy-arn arn:aws:iam::301721915996:policy/cf47-Installer-Role-Policy  
aws iam tag-role \  
--tags Key=rosa_openshift_version,Value=4.9 \  
--role-name cf47-Installer-Role  
aws iam create-policy-version \  
--policy-arn arn:aws:iam::301721915996:policy/cf47-ControlPlane-Role-Policy \  
--policy-document file://sts_instance_controlplane_permission_policy.json \  
--set-as-default  
aws iam tag-policy \  
--tags Key=rosa_openshift_version,Value=4.9 \  
--policy-arn arn:aws:iam::301721915996:policy/cf47-ControlPlane-Role-Policy  
aws iam tag-role \  
--tags Key=rosa_openshift_version,Value=4.9 \  
--role-name cf47-ControlPlane-Role  
aws iam create-policy-version \  
--policy-arn arn:aws:iam::301721915996:policy/cf47-Worker-Role-Policy \  
--policy-document file://sts_instance_worker_permission_policy.json \  
--set-as-default  
aws iam tag-policy \  
--tags Key=rosa_openshift_version,Value=4.9 \  
--policy-arn arn:aws:iam::301721915996:policy/cf47-Worker-Role-Policy  
aws iam tag-role \  
--tags Key=rosa_openshift_version,Value=4.9 \  
--role-name cf47-Worker-Role  
aws iam create-policy-version \  
--policy-arn arn:aws:iam::301721915996:policy/cf47-Support-Role-Policy \  
--policy-document file://sts_support_permission_policy.json \  
--set-as-default  
aws iam tag-policy \  
--tags Key=rosa_openshift_version,Value=4.9 \  
--policy-arn arn:aws:iam::301721915996:policy/cf47-Support-Role-Policy  
aws iam tag-role \  
--tags Key=rosa_openshift_version,Value=4.9 \  
--role-name cf47-Support-Role  
aws iam create-policy-version \  
--policy-arn arn:aws:iam::301721915996:policy/cf47-openshift-machine-api-aws-cloud-credentials \  
--policy-document file://openshift_machine_api_aws_cloud_credentials_policy.json \  
--set-as-default  
aws iam tag-policy \  
--tags Key=rosa_openshift_version,Value=4.9 \  
--policy-arn arn:aws:iam::301721915996:policy/cf47-openshift-machine-api-aws-cloud-credentials  
aws iam create-policy-version \  
--policy-arn arn:aws:iam::301721915996:policy/cf47-openshift-cloud-credential-operator-cloud-credential-operat \  
--policy-document file://openshift_cloud_credential_operator_cloud_credential_operator_iam_ro_creds_policy.json \  
--set-as-default  
aws iam tag-policy \  
--tags Key=rosa_openshift_version,Value=4.9 \  
--policy-arn arn:aws:iam::301721915996:policy/cf47-openshift-cloud-credential-operator-cloud-credential-operat  
aws iam create-policy-version \  
--policy-arn arn:aws:iam::301721915996:policy/cf47-openshift-image-registry-installer-cloud-credentials \  
--policy-document file://openshift_image_registry_installer_cloud_credentials_policy.json \  
--set-as-default  
aws iam tag-policy \  
--tags Key=rosa_openshift_version,Value=4.9 \  
--policy-arn arn:aws:iam::301721915996:policy/cf47-openshift-image-registry-installer-cloud-credentials  
aws iam create-policy-version \  
--policy-arn arn:aws:iam::301721915996:policy/cf47-openshift-ingress-operator-cloud-credentials \  
--policy-document file://openshift_ingress_operator_cloud_credentials_policy.json \  
--set-as-default  
aws iam tag-policy \  
--tags Key=rosa_openshift_version,Value=4.9 \  
--policy-arn arn:aws:iam::301721915996:policy/cf47-openshift-ingress-operator-cloud-credentials  
aws iam create-policy-version \  
--policy-arn arn:aws:iam::301721915996:policy/cf47-openshift-cluster-csi-drivers-ebs-cloud-credentials \  
--policy-document file://openshift_cluster_csi_drivers_ebs_cloud_credentials_policy.json \  
--set-as-default  
aws iam tag-policy \  
--tags Key=rosa_openshift_version,Value=4.9 \  
--policy-arn arn:aws:iam::301721915996:policy/cf47-openshift-cluster-csi-drivers-ebs-cloud-credentials  
I: Preparing to upgrade operator roles.  
I: Account roles with prefix 'cf47' need to be upgraded before operator roles. Roles can be upgraded with the following command :  
rosa upgrade account-roles --prefix cf47  
  
NOTE: When upgrade to 4.10.* there is a new operator policy will be created 'openshift-cloud-network-config-controller-cloud' and user will be prompted with a message to create this new role the command should contain the one to create the new role.

## Step
Upgrade cluster with the up-to-date account-roles but low version of operator-roles with --mode manual

## Expect
There should be the commands to upgrade the operator roles prompted.  
And the cluster can be upgrade after run the commands

## Step
Upgrade cluster with the up-to-date account-roles but low version of operator-roles with --mode auto

## Expect
The operator-roles should be upgraded automatically and the cluster upgrade procedure should be finished.

## Step
Repeat all above steps with the invalid mode

## Expect
There is some error message shown.  
E: Invalid mode. Allowed values are [auto manual]
