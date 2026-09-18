# Test

## Step

Log in with rosacil and prepare account-roles with the low version 4.9

## Expect

## Step

Create a 4.9.z cluster which has an upgrade path to 4.10.z

## Expect

## Step

Check the help message of `rosa upgrade`, `rosa upgrade account-roles`, and `rosa upgrade operator-roles`.

## Expect

```bash
rosa upgrade -h
```

```
Upgrade a resource

Usage:
rosa upgrade [command]

Available Commands:
account-roles Upgrade account-wide IAM roles to the latest version.
cluster Upgrade cluster
operator-roles Upgrade operator IAM roles for a cluster.
roles          Upgrade cluster-specific IAM roles for a target OpenShift version.

Flags:
  -h, --help             help for upgrade
  -i, --interactive      Enable interactive mode.
      --profile string   Use a specific AWS profile from your credential file.
      --region string    Use a specific AWS region, overriding the AWS_REGION environment variable.

Global Flags:
      --color string   Surround certain characters with escape sequences to display them in color on the terminal. Allowed options are [auto never always] (default "auto")
      --debug          Enable debug mode.

Use "rosa upgrade [command] --help" for more information about a command.
```

```bash
rosa upgrade account-roles -h
```

```
Upgrade account-wide IAM roles to the latest version before upgrading your cluster.

Usage:
rosa upgrade account-roles [flags]

Aliases:
account-roles, account-role, accountroles, policies

Examples:
  # Upgrade account roles for ROSA STS clusters
rosa upgrade account-roles

Flags:
  -h, --help             help for account-roles
      --hosted-cp        Enable the use of Hosted Control Planes
  -i, --interactive      Enable interactive mode.
  -m, --mode string      How to perform the operation. Valid options are:
                         auto: Resource changes will be automatic applied using the current AWS account
                         manual: Commands necessary to modify AWS resources will be output to be run manually
  -p, --prefix string    User-defined prefix for all generated AWS resources
      --version string   Version of OpenShift that will be used to setup policy tag, for example "4.11"
  -y, --yes              Automatically answer yes to confirm operation.

Global Flags:
      --color string     Surround certain characters with escape sequences to display them in color on the terminal. Allowed options are [auto never always] (default "auto")
      --debug            Enable debug mode.
      --profile string   Use a specific AWS profile from your credential file.
      --region string    Use a specific AWS region, overriding the AWS_REGION environment variable. (DEPRECATED: Region flag will be removed from this command in future versions)
```

```bash
rosa upgrade operator-roles -h
```

```
Upgrade cluster-specific operator IAM roles to latest version.

Usage:
rosa upgrade operator-roles [flags]

Aliases:
operator-roles, operator-role, operatorroles

Examples:
  # Upgrade cluster-specific operator IAM roles
rosa upgrade operators-roles

Flags:
  -c, --cluster string   Name or ID of the cluster.
  -h, --help             help for operator-roles
  -i, --interactive      Enable interactive mode.
  -m, --mode string      How to perform the operation. Valid options are:
                         auto: Resource changes will be automatic applied using the current AWS account
                         manual: Commands necessary to modify AWS resources will be output to be run manually
      --version string   Version of OpenShift that the cluster will be upgraded to
  -y, --yes              Automatically answer yes to confirm operation.

Global Flags:
      --color string     Surround certain characters with escape sequences to display them in color on the terminal. Allowed options are [auto never always] (default "auto")
      --debug            Enable debug mode.
      --profile string   Use a specific AWS profile from your credential file.
      --region string    Use a specific AWS region, overriding the AWS_REGION environment variable. (DEPRECATED: Region flag will be removed from this command in future versions)
```

## Step

Upgrade account-roles with --mode manual

## Expect

The commands used to upgrade the account-roles are prompted.
Log in aws console to check the account-roles and policies tagged with the default openshift version(X.Y) after running all the commnads. the example is as bellow:
[root@yuwan rosa]# ./rosa upgrade account-roles --prefix cy48 --mode manual
I: All policy files saved to the current directory
I: Run the following commands to upgrade the account role policies:
aws iam create-policy-version \
--policy-arn arn:aws:iam::301721915996:policy/cy48-Installer-Role-Policy \
--policy-document file://sts_installer_permission_policy.json \
--set-as-default
aws iam tag-policy \
--tags Key=rosa_openshift_version,Value=4.9 \
--policy-arn arn:aws:iam::301721915996:policy/cy48-Installer-Role-Policy
aws iam tag-role \
--tags Key=rosa_openshift_version,Value=4.9 \
--role-name cy48-Installer-Role
aws iam create-policy-version \
--policy-arn arn:aws:iam::301721915996:policy/cy48-ControlPlane-Role-Policy \
--policy-document file://sts_instance_controlplane_permission_policy.json \
--set-as-default
aws iam tag-policy \
--tags Key=rosa_openshift_version,Value=4.9 \
--policy-arn arn:aws:iam::301721915996:policy/cy48-ControlPlane-Role-Policy
aws iam tag-role \
--tags Key=rosa_openshift_version,Value=4.9 \
--role-name cy48-ControlPlane-Role
aws iam create-policy-version \
--policy-arn arn:aws:iam::301721915996:policy/cy48-Worker-Role-Policy \
--policy-document file://sts_instance_worker_permission_policy.json \
--set-as-default
aws iam tag-policy \
--tags Key=rosa_openshift_version,Value=4.9 \
--policy-arn arn:aws:iam::301721915996:policy/cy48-Worker-Role-Policy
aws iam tag-role \
--tags Key=rosa_openshift_version,Value=4.9 \
--role-name cy48-Worker-Role
aws iam create-policy-version \
--policy-arn arn:aws:iam::301721915996:policy/cy48-Support-Role-Policy \
--policy-document file://sts_support_permission_policy.json \
--set-as-default
aws iam tag-policy \
--tags Key=rosa_openshift_version,Value=4.9 \
--policy-arn arn:aws:iam::301721915996:policy/cy48-Support-Role-Policy
aws iam tag-role \
--tags Key=rosa_openshift_version,Value=4.9 \
--role-name cy48-Support-Role
aws iam create-policy-version \
--policy-arn arn:aws:iam::301721915996:policy/cy48-openshift-ingress-operator-cloud-credentials \
--policy-document file://openshift_ingress_operator_cloud_credentials_policy.json \
--set-as-default
aws iam tag-policy \
--tags Key=rosa_openshift_version,Value=4.9 \
--policy-arn arn:aws:iam::301721915996:policy/cy48-openshift-ingress-operator-cloud-credentials
aws iam create-policy-version \
--policy-arn arn:aws:iam::301721915996:policy/cy48-openshift-cluster-csi-drivers-ebs-cloud-credentials \
--policy-document file://openshift_cluster_csi_drivers_ebs_cloud_credentials_policy.json \
--set-as-default
aws iam tag-policy \
--tags Key=rosa_openshift_version,Value=4.9 \
--policy-arn arn:aws:iam::301721915996:policy/cy48-openshift-cluster-csi-drivers-ebs-cloud-credentials
aws iam create-policy-version \
--policy-arn arn:aws:iam::301721915996:policy/cy48-openshift-machine-api-aws-cloud-credentials \
--policy-document file://openshift_machine_api_aws_cloud_credentials_policy.json \
--set-as-default
aws iam tag-policy \
--tags Key=rosa_openshift_version,Value=4.9 \
--policy-arn arn:aws:iam::301721915996:policy/cy48-openshift-machine-api-aws-cloud-credentials
aws iam create-policy-version \
--policy-arn arn:aws:iam::301721915996:policy/cy48-openshift-cloud-credential-operator-cloud-credential-operat \
--policy-document file://openshift_cloud_credential_operator_cloud_credential_operator_iam_ro_creds_policy.json \
--set-as-default
aws iam tag-policy \
--tags Key=rosa_openshift_version,Value=4.9 \
--policy-arn arn:aws:iam::301721915996:policy/cy48-openshift-cloud-credential-operator-cloud-credential-operat
aws iam create-policy-version \
--policy-arn arn:aws:iam::301721915996:policy/cy48-openshift-image-registry-installer-cloud-credentials \
--policy-document file://openshift_image_registry_installer_cloud_credentials_policy.json \
--set-as-default
aws iam tag-policy \
--tags Key=rosa_openshift_version,Value=4.9 \
--policy-arn arn:aws:iam::301721915996:policy/cy48-openshift-image-registry-installer-cloud-credentials
[root@yuwan rosa]#

NOTE: When upgrade to 4.10.* there is a new operator policy will be created 'openshift-cluster-csi-drivers-storage-ebs-cloud-cred' and the the permissions should be same with the one changed in <https://github.com/openshift/rosa/pull/610/files> There should be the command to create it.

## Step

Check the validation during upgrade account-roles

1. Upgrade one up-to-date version account roles
2. Upgrade account-roles with non-existed prefix
3. Upgrade with invalid mode.

## Expect

[root@yuwan rosa]# ./rosa upgrade account-roles --prefix cy48 --mode manual
I: Account role with the prefix 'cy48' is already up-to-date.
[root@yuwan rosa]# ./rosa upgrade account-roles --prefix cy4111 --mode auto
E: Roles with the prefix'cy4111' not found
[root@yuwan rosa]# ./rosa upgrade account-roles --prefix cf47 --mode aaa
E: Invalid mode. Allowed values are [auto manual]

## Step

Repeat to upgrade the account-roles via the command manual mode

## Expect

The results are same as the one via interactive mode

## Step

Create one sts cluster with the account-roles in low version 4.9

## Expect

## Step

Try to upgrade operator-roles with --mode manual with setting the cluster upgrading version

## Expect

The commands used to upgrade the operator-roles are prompted.
Log in aws console to check the policies tagged with the default openshift version(X.Y) after running all the commnads.

NOTE: When upgrade to 4.10.* there is a new operator policy will be created 'openshift-cluster-csi-drivers-storage-ebs-cloud-cred' and the the permissions should be same with the one changed in <https://github.com/openshift/rosa/pull/610/files> There should be the command to create it.

The operator-role and policy which is new added for 4.10.z cluster will be created.

The new added role and policy should contains 'red-hat-managed=true' tag

## Step

Upgrade operator-roles with --version flag:
Test steps:

1. Create one account-role of the version 4.9
2. Create one sts cluster of version 4.9.z which has a upgrade path to 4.10.z
3. Upgrade the account-roles
4. Upgrade the operator-role with --version <new_openshift_upgrade_version_4.x.y>
5. Upgrade the cluster

## Expect

4. The new added operator-role for the 4.10.z cluster is created.
5. The cluster will pass the operator-roles/account-roles validation and finish the upgrade policy schedule directly

## Step

Check the validation during upgrade account-roles

1. Upgrade operator-roles with one up-to-date version account roles
2. Upgrade operator-roles with non-existed cluster id
3. Upgrade with invalid mode.
4. Upgrade an up-to-date version operator-roles

## Expect

1.[root@yuwan rosa]# ./rosa upgrade operator-roles -c 1ob55vakao63mgh2dmss3mkplnt28fd8
I: Account roles with prefix 'cy48' need to be upgraded before operator roles. Roles can be upgraded with the following command :
rosa upgrade account-roles --prefix cy48
2.[root@yuwan rosa]# ./rosa upgrade operator-roles -c 1ob55vakao63m --mode auto
E: Failed to get cluster '1ob55vakao63m': There is no cluster with identifier or name '1ob55vakao63m'
3.E: Invalid mode. Allowed values are [auto manual]
4.[root@yuwan rosa]# ./rosa upgrade operator-roles -c 1ob55vakao63mgh2dmss3mkplnt28fd8 --mode auto
I: Operator roles associated with the cluster '1ob55vakao63mgh2dmss3mkplnt28fd8' is already up-to-date.

## Step

Repeat to upgrade the operator-roles via the command manual mode.

## Expect

The results are same as the above one

## Step

Update the cluster to 4.10.z

## Expect

It should succeed

## Step

Repeat all above steps from the Y-1 version to latest Y stream version

## Expect
