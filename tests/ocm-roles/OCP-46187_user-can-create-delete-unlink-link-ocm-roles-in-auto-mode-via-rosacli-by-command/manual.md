# Setup

```bash
rosa create cluster -c ${name}aa --region ${region} --version ${version}-${channel_group} --channel-group ${channel_group} --role-arn arn:aws:iam::${aws_account_id}:role/OSDCCSAdmin --tags cluster-name:${name},cluster-version:${version}-${channel_group} ${roles} --external-id "<external_id>"
```

> Note: As of 2024-07-16, OCP-59406 is merged into this case. The managed policy for the OCM role is not yet available on AWS (`ROSAOCMPolicy`). Automation will be implemented after the managed policy is available.

# Test

## Step

1. Create the admin OCM role.

```bash
rosa create ocm-role --admin --permision-boundary <pb> --mode auto -y
```

## Expect

Confirm that the trust-policy output contains the policy and that the role output links to the AWS Console.

```
INFO: Creating role using 'arn:aws:iam::301721915996:user/yuwan'
I: Attached trust policy to role 'ManagedOpenShift-OCM-Role-13849960(https://console.aws.amazon.com/iam/home?#/roles/ManagedOpenShift-OCM-Role-13849960)': {"Version": "2012-10-17", "Statement": [{"Action": ["sts:AssumeRole"], "Effect": "Allow", "Condition": {"StringEquals": {"sts:ExternalId": "1kDmx7itdCqfKPXlaIihdT3CIZL"}}, "Principal": {"AWS": ["arn:aws:iam::896164604406:role/RH-Managed-OpenShift-Installer"]}}]}
INFO: Created role 'QEAuto-user-20220624-401-OCM-Role-12553207' with ARN 'arn:aws:iam::301721915996:role/QEAuto-user-20220624-401-OCM-Role-12553207'
I: Attached policy 'arn:aws:iam::301721915996:policy/ManagedOpenShift-OCM-Role-13849960-Policy' to role 'ManagedOpenShift-OCM-Role-13849960(https://console.aws.amazon.com/iam/home?#/roles/ManagedOpenShift-OCM-Role-13849960)'
INFO: Successfully linked role-arn 'arn:aws:iam::301721915996:role/QEAuto-user-20220624-401-OCM-Role-12553207' with organization account '1OAqHo0k19kyq7Xt7I1Zqb8Ok4K'
```

- The permission boundary is added.

## Step

1. List OCM roles.

```bash
rosa list ocm-role
```

## Expect

- The OCM role is displayed.
- All role parameters are shown.

## Step

1. Unlink the OCM role.

```bash
rosa unlink ocm-role --role-arn <rosa arn>
```

## Expect

```
INFO: Successfully unlinked role-arn 'arn:aws:iam::301721915996:role/QEAuto-user-20220624-401-OCM-Role-12553207' from organization account '1OAqHo0k19kyq7Xt7I1Zqb8Ok4K'
```

## Step

1. List OCM roles.

## Expect

The related item shows `Linked` as `No`.

## Step

1. Link the OCM role.

```bash
rosa link ocm-role --role-arn <rosa arn>
```

## Expect

```
INFO: Successfully linked role ARN 'arn:aws:iam::301721915996:role/QEAuto-user-20220624-401-OCM-Role-12553207' with account '1Pg8PstQKeyanR20qpwlvkEF9NC'
```

## Step

1. List OCM roles.

## Expect

The related item shows `Linked` as `Yes`.

## Step

1. Delete the OCM role in auto mode by command.

## Expect

The role is unlinked and deleted.

## Step

1. Create an OCM role with the default prefix, delete the role while retaining the policy, then create it again.

## Expect

The OCM role is created successfully (new checkpoint OCM-7881).

## Step

1. Create OCM roles with managed OCM role policies in auto mode.

```bash
rosa create ocm-role --managed-policies --mode auto
rosa create ocm-role --managed-policies --mode auto --admin
```

## Expect

- The OCM role is created on AWS and has the managed policy attached.
- With `--admin`, the OCM role has two managed policies attached: the OCM managed role policy and the admin OCM managed policy.
- The AWS roles are tagged with `rosa_managed_policies=true`.

## Step

1. Create an OCM role with the managed OCM role policy in manual mode.

```bash
rosa create ocm-role --managed-policies --mode manual
rosa create ocm-role --managed-policies --mode manual --admin
```

## Expect

- The prompted AWS commands do not create policies; they create roles and attach managed policies. With `--admin`, they include two policy-attachment commands.
- The AWS roles are tagged with `rosa_managed_policies=true`.
- After the commands run, the OCM role is created on AWS with the managed policies attached.

## Step

1. Repeat steps 1 and 2 with a path setting.

## Expect

## Step

1. Delete the managed OCM roles in auto mode.

## Expect

- The OCM roles are detached and deleted.
- The managed policies are not deleted.

## Step

1. Delete the managed OCM roles in manual mode.

## Expect

- AWS commands detach policies and delete roles.
- No AWS commands delete the managed policies.
