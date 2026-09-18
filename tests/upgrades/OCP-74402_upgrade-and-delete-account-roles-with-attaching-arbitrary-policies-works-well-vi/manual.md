# Test

## Step

Create account-roles in lower version.

```bash
rosa create account-roles --version 4.14 --prefix oa-414 --mode auto -y
```

## Expect

Expect each role to have an attached policy as below:

```
I: Attached trust policy to role 'oa-414-Installer-Role(https://console.aws.amazon.com/iam/home?#/roles/oa-414-Installer-Role)': {"Version": "2012-10-17", "Statement": [{"Action": ["sts:AssumeRole"], "Effect": "Allow", "Principal": {"AWS": ["arn:aws:iam::896164604406:role/RH-Managed-OpenShift-Installer"]}}]}
I: Created role 'oa-414-Installer-Role' with ARN 'arn:aws:iam::301721915996:role/oa-414-Installer-Role'
I: Attached policy 'arn:aws:iam::301721915996:policy/oa-414-Installer-Role-Policy' to role 'oa-414-Installer-Role(https://console.aws.amazon.com/iam/home?#/roles/oa-414-Installer-Role)'
I: Creating hosted CP account roles using 'arn:aws:iam::301721915996:user/oaharoni'
I: Attached trust policy to role 'oa-414-HCP-ROSA-Installer-Role(https://console.aws.amazon.com/iam/home?#/roles/oa-414-HCP-ROSA-Installer-Role)': {"Version": "2012-10-17", "Statement": [{"Action": ["sts:AssumeRole"], "Effect": "Allow", "Principal": {"AWS": ["arn:aws:iam::896164604406:role/RH-Managed-OpenShift-Installer"]}}]}
I: Created role 'oa-414-HCP-ROSA-Installer-Role' with ARN 'arn:aws:iam::301721915996:role/oa-414-HCP-ROSA-Installer-Role'
I: Attached policy 'ROSAInstallerPolicy(https://docs.aws.amazon.com/aws-managed-policy/latest/reference/ROSAInstallerPolicy)' to role 'oa-414-HCP-ROSA-Installer-Role(https://console.aws.amazon.com/iam/home?#/roles/oa-414-HCP-ROSA-Installer-Role)'
```

Additionally, ensure that the trust policies output the content of their policy. The Roles should include a link to their AWS Console page. Managed permissions policies should instead link to their public AWS Docs page.

## Step

Detach and Delete ~~some operator-roles polcies and~~ account-roles policies from the roles + and also attach some arbitrary polcies on ~~some operator-role and~~ account-roles to make sure some ~~operator-role and~~ account-roles attaching arbitrary policies

## Expect

## Step

Upgrade account roles in auto mode

## Expect

- All roles and redhat-managed policies are upgrade to the latest version
- No any changes on the arbitrary policies

Like in step 1, expect each role to have an attached policy as below:

```
I: Attached trust policy to role 'oa-414-Installer-Role(https://console.aws.amazon.com/iam/home?#/roles/oa-414-Installer-Role)': {"Version": "2012-10-17", "Statement": [{"Action": ["sts:AssumeRole"], "Effect": "Allow", "Principal": {"AWS": ["arn:aws:iam::896164604406:role/RH-Managed-OpenShift-Installer"]}}]}
I: Created role 'oa-414-Installer-Role' with ARN 'arn:aws:iam::301721915996:role/oa-414-Installer-Role'
I: Attached policy 'arn:aws:iam::301721915996:policy/oa-414-Installer-Role-Policy' to role 'oa-414-Installer-Role(https://console.aws.amazon.com/iam/home?#/roles/oa-414-Installer-Role)'
```

Additionally, ensure that the trust policies output the content of their policy, or a link to the docs page if they are an AWS managed policy. The Roles should also always include a link to their AWS Console page.

## Step

Delete account-roles ~~and operator-roles~~ which are attaching arbitrary poliies in auto mode

## Expect

- All not-arbitrary policies are deleted from AWS
- arbitrary policies are detached and not be deleted.

## Step

Repeat step 1 then attach only one policy on one account roles, the repeat step 3 4 (one time test step).

## Expect

The result should be same
