# Setup
```bash
rosa create cluster -c ${name}aa --region ${region} --version ${version}-${channel_group} --channel-group ${channel_group} --role-arn arn:aws:iam::${aws_account_id}:role/OSDCCSAdmin --tags cluster-name:${name},cluster-version:${version}-${channel_group} ${roles} --external-id "<external_id>"
```

# Test

## Step
Check help message.

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
Check the validation for `rosa create user-role`.

- Create an user-role with invalid mode.
- Create an user-role with invalid permision boundady.
- Create an user-role with the permision boundady under another aws account.
- Create another user-role with the existed prefix.

## Expect
Should fail with readable error message.

## Step
Check the validation for `rosa unlink user-role`.

- Unlink user-role with not-exist role.
- Unlink user-role with the role arn in incorrect format.

## Expect
Should fail with readable error message.

## Step
Check the validation for `rosa link user-role`.

- Link user-role with the role arn in incorrect format.

## Expect
Should fail with readable error message.
