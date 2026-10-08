# Test

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

Global Flags:
      --color string     Surround certain characters with escape sequences to display them in color on the terminal. Allowed options are [auto never always] (default "auto")
      --debug            Enable debug mode.
      --profile string   Use a specific AWS profile from your credential file.
      --region string    Use a specific AWS region, overriding the AWS_REGION environment variable. (DEPRECATED: Region flag will be removed from this command in future versions)
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
- Choosing `Y` for both Hosted CP and classic account roles creates account roles for both

```
$ ./rosa create account-roles -i
I: Logged in as 'ocmqe-jkeyne' on 'https://api.stage.openshift.com'
I: Validating AWS credentials...
I: AWS credentials are valid!
I: Validating AWS quota...
I: AWS quota ok. If cluster installation fails, validate actual AWS resource usage against https://docs.openshift.com/rosa/rosa_getting_started/rosa-required-aws-service-quotas.html
I: Verifying whether OpenShift command-line tool is available...
I: Current OpenShift Client Version: 4.22.17
I: Creating account roles
? Role prefix: jkeyne
? Permissions boundary ARN (optional): 
? Path (optional): /test/path/
? STS external ID (optional): 
? Role creation mode: auto
? Create Classic account roles: Yes
? Create Hosted CP account roles: No
I: Creating classic account roles using 'arn:aws:iam::090777400063:user/jkeyne'
I: Attached trust policy to role 'jkeyne-Installer-Role(https://console.aws.amazon.com/iam/home?#/roles/jkeyne-Installer-Role)': {"Version": "2012-10-17", "Statement": [{"Action": ["sts:AssumeRole"], "Effect": "Allow", "Principal": {"AWS": ["arn:aws:iam::644306948063:role/RH-Managed-OpenShift-Installer"]}}]}
I: Created role 'jkeyne-Installer-Role' with ARN 'arn:aws:iam::090777400063:role/test/path/jkeyne-Installer-Role'
W: If policies created are not attached, or are missing, try re-running "rosa create account-roles" with "force-policy-creation"
I: Attached policy 'arn:aws:iam::090777400063:policy/test/path/jkeyne-Installer-Role-Policy' to role 'jkeyne-Installer-Role(https://console.aws.amazon.com/iam/home?#/roles/jkeyne-Installer-Role)'

I: Attached trust policy to role 'jkeyne-ControlPlane-Role(https://console.aws.amazon.com/iam/home?#/roles/jkeyne-ControlPlane-Role)': {"Version": "2012-10-17", "Statement": [{"Action": ["sts:AssumeRole"], "Effect": "Allow", "Principal": {"Service": ["ec2.amazonaws.com"]}}]}
I: Created role 'jkeyne-ControlPlane-Role' with ARN 'arn:aws:iam::090777400063:role/test/path/jkeyne-ControlPlane-Role'
W: If policies created are not attached, or are missing, try re-running "rosa create account-roles" with "force-policy-creation"
I: Attached policy 'arn:aws:iam::090777400063:policy/test/path/jkeyne-ControlPlane-Role-Policy' to role 'jkeyne-ControlPlane-Role(https://console.aws.amazon.com/iam/home?#/roles/jkeyne-ControlPlane-Role)'

I: Attached trust policy to role 'jkeyne-Worker-Role(https://console.aws.amazon.com/iam/home?#/roles/jkeyne-Worker-Role)': {"Version": "2012-10-17", "Statement": [{"Action": ["sts:AssumeRole"], "Effect": "Allow", "Principal": {"Service": ["ec2.amazonaws.com"]}}]}
I: Created role 'jkeyne-Worker-Role' with ARN 'arn:aws:iam::090777400063:role/test/path/jkeyne-Worker-Role'
W: If policies created are not attached, or are missing, try re-running "rosa create account-roles" with "force-policy-creation"
I: Attached policy 'arn:aws:iam::090777400063:policy/test/path/jkeyne-Worker-Role-Policy' to role 'jkeyne-Worker-Role(https://console.aws.amazon.com/iam/home?#/roles/jkeyne-Worker-Role)'

I: Attached trust policy to role 'jkeyne-Support-Role(https://console.aws.amazon.com/iam/home?#/roles/jkeyne-Support-Role)': {"Version": "2012-10-17", "Statement": [{"Action": ["sts:AssumeRole"], "Effect": "Allow", "Principal": {"AWS": ["arn:aws:iam::644306948063:role/RH-Technical-Support-13849960"]}}]}
I: Created role 'jkeyne-Support-Role' with ARN 'arn:aws:iam::090777400063:role/test/path/jkeyne-Support-Role'
W: If policies created are not attached, or are missing, try re-running "rosa create account-roles" with "force-policy-creation"
I: Attached policy 'arn:aws:iam::090777400063:policy/test/path/jkeyne-Support-Role-Policy' to role 'jkeyne-Support-Role(https://console.aws.amazon.com/iam/home?#/roles/jkeyne-Support-Role)'
```

## Step
Set flags, then enter interactive mode.

## Expect
- Flag values are the defaults in prompts.
- With `--hosted-cp`, `Create Classic account roles` is not asked; with `--classic`, `Create Hosted CP account roles` is not asked.

## Step
Create account roles while not logged in to ROSA CLI.

## Expect
Can't create account roles without being logged in

```
$ rosa logout
$ rosa create account-roles -i
E: Failed to create OCM connection: Not logged in, run the 'rosa login' command
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
E: Failed to create AWS client: invalid AWS Credentials: operation error STS: GetCallerIdentity, exceeded maximum number of attempts, 12, https response error StatusCode: 403, RequestID: fd48fcd1-81cf-47ae-9443-1865c63dc585, api error InvalidClientTokenId: The security token included in the request is invalid..
 For help configuring your credentials, see https://docs.openshift.com/rosa/rosa_install_access_delete_clusters/rosa_getting_started_iam/rosa-config-aws-account.html#rosa-configuring-aws-account_rosa-config-aws-account
```
