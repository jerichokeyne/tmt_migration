# Test

## Step

1. Check the help messages.

```bash
rosa create -h
rosa create ocm-role -h
```

## Expect

```
ocm-role Create role used by Red Hat Hybrid Cloud Console
```

```
Create role used by Red Hat Hybrid Cloud Console to verify necessary roles and OIDC providers are in place.

Usage:
  rosa create ocm-role [flags]

Aliases:
  ocm-role, ocmrole

Examples:
  # Create default ocm-role for ROSA clusters using STS
  rosa create ocm-role

  # Create ocm-role with a specific permissions boundary
  rosa create ocm-role --permissions-boundary arn:aws:iam::123456789012:policy/perm-boundary

Flags:
      --admin                         Enable admin capabilities for the role
  -h, --help                          help for ocm-role
  -i, --interactive                   Enable interactive mode.
  -m, --mode string                   How to perform the operation. Valid options are:
                                      auto: Resource changes will be automatic applied using the current AWS account
                                      manual: Commands necessary to modify AWS resources will be output to be run manually
      --no-console                    Create OCM role with minimal permissions (cannot be used with console.redhat.com)
      --path string                   The arn path for the ocm role and policies
      --permissions-boundary string   The ARN of the policy that is used to set the permissions boundary for the OCM role.
      --prefix string                 User-defined prefix for all generated AWS resources (default "ManagedOpenShift")
  -y, --yes                           Automatically answer yes to confirm operation.

Global Flags:
      --color string     Surround certain characters with escape sequences to display them in color on the terminal. Allowed options are [auto never always] (default "auto")
      --debug            Enable debug mode.
      --profile string   Use a specific AWS profile from your credential file.
      --region string    Use a specific AWS region, overriding the AWS_REGION environment variable. (DEPRECATED: Region flag will be removed from this command in future versions)
```

## Step

1. Create the OCM role in auto mode through interactive mode.

> Note: The user needs the `OrganizationLabel` permission.

## Expect

Manual mode:

```
I: Creating ocm role
? Role prefix: ManagedOpenShift
? Enable admin capabilities for the OCM role (optional): Yes
? Permissions boundary ARN (optional):
? Role creation mode: manual
I: All policy files saved to the current directory
I: Run the following commands to create the ocm role and policies:
```

```bash
aws iam create-role \
  --role-name ManagedOpenShift-OCM-Role-12553207 \
  --assume-role-policy-document file://sts_ocm_trust_policy.json \
  --tags Key=rosa_role_prefix,Value=ManagedOpenShift Key=rosa_role_type,Value=OCM Key=rosa_environment,Value=staging Key=rosa_admin_role,Value=true

aws iam create-policy \
  --policy-name ManagedOpenShift-OCM-Role-12553207-Policy \
  --policy-document file://sts_ocm_permission_policy.json \
  --tags Key=rosa_role_prefix,Value=ManagedOpenShift Key=rosa_role_type,Value=OCM Key=rosa_environment,Value=staging

aws iam attach-role-policy \
  --role-name ManagedOpenShift-OCM-Role-12553207 \
  --policy-arn arn:aws:iam::301721915996:policy/ManagedOpenShift-OCM-Role-12553207-Policy

aws iam create-policy \
  --policy-name ManagedOpenShift-OCM-Role-12553207-Admin-Policy \
  --policy-document file://sts_ocm_admin_permission_policy.json \
  --tags Key=rosa_admin_role,Value=true

aws iam attach-role-policy \
  --role-name ManagedOpenShift-OCM-Role-12553207 \
  --policy-arn arn:aws:iam::301721915996:policy/ManagedOpenShift-OCM-Role-12553207-Admin-Policy

rosa link ocm-role --role-arn arn:aws:iam::301721915996:role/ManagedOpenShift-OCM-Role-12553207
```

Auto mode:

```
I: Creating ocm role
? Role prefix: yw4988i2
? Enable admin capabilities for the OCM role (optional): Yes
? Permissions boundary ARN (optional):
? Role creation mode: auto
I: Creating role using 'arn:aws:iam::301721915996:user/yuwan'
? Create the 'yw4988i2-OCM-Role' role? Yes
I: Created role 'yw4988i2-OCM-Role' with ARN 'arn:aws:iam::301721915996:role/yw4988i2-OCM-Role'
? Link the 'arn:aws:iam::301721915996:role/yw4988i2-OCM-Role' role with organization '1H9SY60bJWyoynWMsZzZEvtLFdI'? Yes
I: Successfully linked role-arn 'arn:aws:iam::301721915996:role/yw4988i2-OCM-Role' with organization account '1H9SY60bJWyoynWMsZzZEvtLFdI'
```

When interactive mode is called without all flags, parameters set through flags are prompted as defaults.

## Step

1. Repeat step 2 with an account that does not have `OrganizationLabel` permission.

## Expect

```
E: Unable to link role arn 'arn:aws:iam::301721915996:role/ywocmrole01-OCM-Role' with the organization id : '1OAqHo0k19kyq7Xt7I1Zqb8Ok4K' : identifier is '11', code is 'ACCT-MGMT-11' and operation identifier is 'bf96d87b-cb68-435e-9f23-12f6b0452cf5': Account with ID 1Pg91NjVkaKuxDvnp9iXQa8MlC3 denied access to perform create on OrganizationLabel with HTTP call POST /api/accounts_mgmt/v1/organizations/1OAqHo0k19kyq7Xt7I1Zqb8Ok4K/labels
```

## Step

1. Check validation for `--permissions-boundary`.

## Expect

```
X Sorry, your reply was invalid: Invalid ARN: arn: invalid prefix
```
