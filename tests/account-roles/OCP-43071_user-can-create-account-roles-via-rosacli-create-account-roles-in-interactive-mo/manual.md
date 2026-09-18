# Setup

```bash
rosa create cluster -c ${name}aa --region ${region} --version ${version}-${channel_group} --channel-group ${channel_group} --role-arn arn:aws:iam::${aws_account_id}:role/OSDCCSAdmin --tags cluster-name:${name},cluster-version:${version}-${channel_group} ${roles} --external-id "<external_id>"
```

# Test

## Step
Get the latest version of ROSA CLI.

## Expect
STS is supported from version `1.0.6`.

## Step
Check the help message.

```bash
rosa create account-roles --help
```

## Expect
```
Create account-wide Identity and Access Management (IAM) roles before creating your cluster.

Usage:
  rosa create account-roles [flags]

Aliases:
  account-roles, accountroles, roles, policies

Examples:
  # Create default account roles for ROSA clusters using STS
  rosa create account-roles

  # Create account roles with a specific permissions boundary
  rosa create account-roles --permissions-boundary arn:aws:iam::123456789012:policy/perm-boundary

Flags:
      --classic                        Create only classic Rosa account roles
      --external-id string             An optional unique identifier embedded in installer and support role trust policies when assuming those roles.
  -f, --force-policy-creation          Forces creation of policies skipping compatibility check
  -h, --help                           help for account-roles
      --hosted-cp                      Enable the use of Hosted Control Planes
  -i, --interactive                    Enable interactive mode.
  -m, --mode string                    How to perform the operation. Valid options are:
                                       auto: Resource changes will be automatic applied using the current AWS account
                                       manual: Commands necessary to modify AWS resources will be output to be run manually
      --path string                    The arn path for the account/operator roles as well as their policies
      --permissions-boundary string    The ARN of the policy that is used to set the permissions boundary for the account roles.
      --prefix string                  User-defined prefix for all generated AWS resources (default "ManagedOpenShift")
      --route53-role-arn string        Role ARN associated with the private hosted zone used for Hosted Control Plane cluster shared VPC, this role contains policies to be used with Route 53
      --version string                 Version of OpenShift that will be used to setup policy tag, for example "4.11"
      --vpc-endpoint-role-arn string   Role ARN associated with the shared VPC used for Hosted Control Plane clusters, this role contains policies to be used with the VPC endpoint
  -y, --yes                            Automatically answer yes to confirm operation.
```

## Step
Run interactive mode.

```bash
rosa create account-roles -i
```

## Expect
- Check all prompted options below.
- `Create Classic account roles` defaults to `Y`; `Create Hosted CP account roles` defaults to `N`.
- All options work and take effect after input.
- There is no guidance to create a cluster with the account roles: `I: To create a cluster with these roles, run the following command:` (OCM-1755).
- Choosing `Y` for both Hosted CP and classic account roles prints the single-set hint.

```
$ ./rosa create account-roles -i
I: Logged in as 'sdqe-rosa' on 'https://api.stage.openshift.com'
I: Validating AWS credentials...
I: AWS credentials are valid!
I: Validating AWS quota...
I: AWS quota ok. If cluster installation fails, validate actual AWS resource usage against https://docs.openshift.com/rosa/rosa_getting_started/rosa-required-aws-service-quotas.html
I: Verifying whether OpenShift command-line tool is available...
I: Current OpenShift Client Version: 4.7.13
I: Creating account roles
? Role prefix: yuwan-test3
? Permissions boundary ARN (optional):
? Path (optional): /asd/sf/
? Role creation mode: manual
? Create Classic account roles: No
? Create Hosted CP account roles (optional): No
```

## Step
Set flags, then enter interactive mode.

## Expect
- Flag values are the defaults in prompts.
- With `--hosted-cp`, `Create Classic account roles` is not asked; with `--classic`, `Create Hosted CP account roles` is not asked.

## Step
Create account roles while not logged in to ROSA CLI.

## Expect
Interactive mode prompts for a token.

```
$ ./rosa create account-roles
To login to your Red Hat account, get an offline access token at https://console.redhat.com/openshift/token/rosa
? Copy the token and paste it here: *********************************************************************************************************************************
I: Logged in as 'sdqe-regular01' on 'https://api.openshift.com'
I: Validating AWS credentials...
I: AWS credentials are valid!
I: Validating AWS quota...
I: AWS quota ok. If cluster installation fails, validate actual AWS resource usage against https://docs.openshift.com/rosa/rosa_getting_started/rosa-required-aws-service-quotas.html
I: Verifying whether OpenShift command-line tool is available...
I: Current OpenShift Client Version: 4.8.0-fc.2
I: Starting to create the account roles!
? OpenShift version to create account roles: 4.8..........
```

## Step
Create account roles with an account that has insufficient AWS quota.

## Expect
A warning is shown.

## Step
Create account roles without `oc` installed.

## Expect
```
W: OpenShift command-line tool is not installed.
```

## Step
Create account roles with invalid AWS credentials.

## Expect
```
E: Failed to create AWS client: SignatureDoesNotMatch: The request signature we calculated does not match the signature you provided. Check your AWS Secret Access Key and signing method. Consult the service documentation for details.
```
