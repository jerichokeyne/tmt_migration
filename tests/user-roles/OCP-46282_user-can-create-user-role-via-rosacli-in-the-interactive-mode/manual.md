# Test

## Step
Check the help message.

```bash
rosa create -h
rosa create user-role -h
```

## Expect
```
Create a resource from stdin

Usage:
  rosa create [command]

Available Commands:
  account-roles          Create account-wide Identity and Access Management (IAM) roles before creating your cluster.
  admin                  Creates an admin user to login to the cluster
  autoscaler             Create an autoscaler for a cluster
  break-glass-credential Create a break glass credential for a cluster.
  cluster                Create cluster
  decision               Create a decision for an Access Request
  dns-domain             Create Domain Name System (DNS) domain.
  external-auth-provider Create an external authentication provider for a cluster.
  iamserviceaccount      Create IAM role for Kubernetes service account
  idp                    Add an identity provider (IDP) for a cluster
  image-mirror           Create image mirror for a cluster
  kubeletconfig          Create a custom kubeletconfig for a cluster
  log-forwarder          Create a log forwarder for a Hosted Control Plane cluster
  machinepool            Add machine pool to cluster
  network                Network AWS cloudformation stack
  ocm-role               Create role used by Red Hat Hybrid Cloud Console
  oidc-config            Create OpenID Connect (OIDC) config compliant with OIDC protocol.
  oidc-provider          Create OpenID Connect (OIDC) provider for an AWS Security Token Service (STS) cluster.
  operator-roles         Create Operator Identity and Access Management (IAM) roles for a cluster.
  spot-termination-queue Create Spot termination queue resources
  tuning-configs         Add tuning config
  user-role              Create user role to verify account association

Flags:
  -h, --help             help for create
      --profile string   Use a specific AWS profile from your credential file.
      --region string    Use a specific AWS region, overriding the AWS_REGION environment variable.
  -y, --yes              Automatically answer yes to confirm operation.

Global Flags:
      --color string   Surround certain characters with escape sequences to display them in color on the terminal. Allowed options are [auto never always] (default "auto")
      --debug          Enable debug mode.

Use "rosa create [command] --help" for more information about a command.
```

```
Create user role that allows Red Hat Hybrid Cloud Console to verify that users creating a cluster have access to the current AWS account.

Usage:
  rosa create user-role [flags]

Aliases:
  user-role, userrole

Examples:
  # Create user roles
  rosa create user-role

  # Create user role with a specific permissions boundary
  rosa create user-role --permissions-boundary arn:aws:iam::123456789012:policy/perm-boundary

Flags:
  -h, --help                          help for user-role
  -i, --interactive                   Enable interactive mode.
  -m, --mode string                   How to perform the operation. Valid options are:
                                      auto: Resource changes will be automatic applied using the current AWS account
                                      manual: Commands necessary to modify AWS resources will be output to be run manually
      --path string                   The arn path for the user role and policies.
      --permissions-boundary string   The ARN of the policy that is used to set the permissions boundary for the user role.
      --prefix string                 User-defined prefix for ocm-user role (default "ManagedOpenShift")
  -y, --yes                           Automatically answer yes to confirm operation.

Global Flags:
      --color string     Surround certain characters with escape sequences to display them in color on the terminal. Allowed options are [auto never always] (default "auto")
      --debug            Enable debug mode.
      --profile string   Use a specific AWS profile from your credential file.
      --region string    Use a specific AWS region, overriding the AWS_REGION environment variable. (DEPRECATED: Region flag will be removed from this command in future versions)
```

## Step
Create the user-role in the auto mode in the interactive mode.

NOTE: It needs the user which has 'AccountLabel' permission.

## Expect
```
-----manual mode------
[root@yuwan rosa]# ./rosa create user-role -i
I: Creating User role
? Role prefix: aa
? Permissions boundary ARN (optional):
? Role creation mode: auto
I: Creating ocm user role using 'arn:aws:iam::301721915996:user/yuwan'
? Create the 'aa-User-xueli_1-Role' role? Yes
I: Created role 'aa-User-xueli_1-Role' with ARN 'arn:aws:iam::301721915996:role/aa-User-xueli_1-Role'
I: Linking User role
? User Role ARN: arn:aws:iam::301721915996:role/aa-User-xueli_1-Role
? Link the 'arn:aws:iam::301721915996:role/aa-User-xueli_1-Role' role with account '1G9OXMM1oNIdUuatCH1FZJm2Nls'? Yes
I: Successfully linked role-arn 'arn:aws:iam::301721915996:role/aa-User-xueli_1-Role' with account '1G9OXMM1oNIdUuatCH1FZJm2Nls'
[root@yuwan rosa]#

-----auto mode------
[root@yuwan rosa]# ./rosa create user-role -i
I: Creating User role
? Role prefix: bb
? Permissions boundary ARN (optional):
? Role creation mode: manual
I: All policy files saved to the current directory
I: Run the following commands to create the account roles and policies:

aws iam create-role \
--role-name bb-User-xueli_1-Role \
--assume-role-policy-document file://sts_ocm_user_trust_policy.json \
--tags Key=rosa_role_prefix,Value=bb Key=rosa_role_type,Value=User Key=rosa_environment,Value=staging

rosa link user-role --role-arn arn:aws:iam::301721915996:role/bb-User-xueli_1-Role
[root@yuwan rosa]#
```

## Step
Repeat step2 with an acocunt which has no 'AccountLabel' permission.

## Expect
```
E: Unable to link role arn 'arn:aws:iam::301721915996:role/ManagedOpenShift-User-sdqe-regular01-Role' with the account id : '1Pg91NjVkaKuxDvnp9iXQa8MlC3' : identifier is '11', code is 'ACCT-MGMT-11' and operation identifier is 'b96a902a-53c4-4b0c-a34b-d60d6beceead': Account with ID 1Pg91NjVkaKuxDvnp9iXQa8MlC3 denied access to perform get on Account with HTTP call GET /api/accounts_mgmt/v1/accounts/1Pg91NjVkaKuxDvnp9iXQa8MlC3/labels
```

## Step
Check the validation for the validation for the `-permissions-boundary`.

## Expect
There should be validation for it.

```
X Sorry, your reply was invalid: Invalid ARN: arn: invalid prefix
```
