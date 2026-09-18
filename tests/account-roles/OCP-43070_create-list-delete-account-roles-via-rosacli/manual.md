# Setup

Role policies have all permissions defined in <https://github.com/openshift/managed-cluster-config/tree/master/resources/sts>.

# Test

## Step
Get the latest version of ROSA CLI and log in.

## Expect
STS is supported from version `1.0.6`.

## Step
Create default account roles in auto mode.

```bash
rosa create account-roles --prefix <prefix> --mode auto --path <path> -y
```

## Expect
- Account roles for the default OpenShift version (`X.Y`) are created.
- Seven roles are created: three for Hosted CP and four for classic STS clusters.
- Hosted CP roles have managed policies; classic STS roles have non-managed policies created automatically by ROSA CLI.
- Hosted CP roles use `<prefix>-HCP-ROSA-<role type>` and STS roles use `<prefix>-<role type>`.
- Output identifies the policy attached to each role and links roles to their AWS Console page.
- Trust-policy output includes policy contents; managed-policy output links to public AWS documentation.
- No message guides the user to create a cluster with the account roles (OCM-1755).
- The single-set hint is shown.

```
I: Attached policy 'arn:aws:iam::xxx:policy/test-Installer-Role-Policy' to role 'test-Installer-Role(https://console.aws.amazon.com/iam/home?#/roles/test-Installer-Role)'
I: Attached trust policy to role 'oa-417-Worker-Role(https://console.aws.amazon.com/iam/home?#/roles/oa-417-Worker-Role)': {"Version": "2012-10-17", "Statement": [{"Action": ["sts:AssumeRole"], "Effect": "Allow", "Principal": {"Service": ["ec2.amazonaws.com"]}}]}
I: Attached policy 'ROSAWorkerInstancePolicy(https://docs.aws.amazon.com/aws-managed-policy/latest/reference/ROSAWorkerInstancePolicy)' to role 'oa-417-HCP-ROSA-Worker-Role(https://console.aws.amazon.com/iam/home?#/roles/oa-417-HCP-ROSA-Worker-Role)'
I: By default, the create account-roles command creates two sets of account roles, one for classic ROSA clusters, and one for Hosted Control Plane clusters.
In order to create a single set, please set one of the following flags: --classic or --hosted-cp
```

Hosted CP role types are `Installer-Role`, `Support-Role`, and `Worker-Role`. Classic STS role types are `Installer-Role`, `Support-Role`, `Worker-Role`, and `ControlPlane-Role`. Hosted CP managed policies are `/service-role/ROSAInstallerPolicy`, `service-role/ROSASRESupportPolicy`, and `service-role/ROSAWorkerInstancePolicy`.

## Step
Create only Hosted CP account roles in auto mode.

```bash
rosa create account-roles --prefix <prefix> --mode auto --path <path> -y --hosted-cp
```

## Expect
- Only three Hosted CP account roles are created.
- They are attached to managed policies by default and mandatorily.
- Their names use `<prefix>-HCP-ROSA-<role type>`.
- Output identifies attached policies and links roles to the AWS Console.
- No message guides the user to create a cluster with the account roles (OCM-1755).

## Step
Create only classic STS account roles in auto mode.

```bash
rosa create account-roles --prefix <prefix> --mode auto --path <path> -y --classic
```

## Expect
- Four classic STS account roles are created.
- They have non-managed policies created automatically by ROSA CLI.
- Output identifies attached policies and links roles to the AWS Console.
- No message guides the user to create a cluster with the account roles (OCM-1755).

## Step
Repeat steps 2 and 4 with `--managed-policies`.

For Hosted CP account roles, only managed policies are supported. For classic roles, `--managed-policies` uses managed policies; the flag is hidden, classic managed policies must be prepared manually on AWS, and production does not support creating classic account roles with managed policies.

## Expect
Classic STS roles also have managed policies attached.

```
$ ./rosa create account-roles --hosted-cp --managed-policies=false --mode auto -y --prefix test
I: Logged in as 'sdqe-rosa' on 'https://api.stage.openshift.com'
E: Setting `hosted-cp` as unmanaged policies is not supported
```

The error is the same in staging and production (OCM-6570).

## Step
Repeat steps 2-4 with `--permissions-boundary`.

## Expect
- Account roles are created with the permissions boundary set.
- Other results are the same as steps 2-4.

## Step
Repeat steps 2-4 with `--version`.

## Expect
- Account roles are created with the version.
- Other results are the same as steps 2-4.

## Step
Repeat steps 2-7 with `--mode manual`.

## Expect
- AWS commands to create account roles are prompted.
- The commands execute successfully.
- Roles are created successfully; results are the same as steps 2-7.

## Step
Set manual mode and pipe output to a file.

```bash
rosa create account-roles --prefix aaaa --mode manual --permissions-boundary arn:aws:iam::301721915996:policy/xueli-openshift > file
```

## Expect
Only commands are written to the file, and the file executes without error.

## Step
Create account roles with `--force-policy-creation` in auto mode.

```bash
rosa create account-roles --mode auto -y -f
```

## Expect
Default roles are created or recreated while skipping the compatibility check.
