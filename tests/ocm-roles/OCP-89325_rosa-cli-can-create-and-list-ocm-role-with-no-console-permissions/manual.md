# Test

## Step

1. Run `rosa list ocm-roles` and confirm the OCM-role list includes a `CONSOLE ACCESS` column.

```bash
rosa list ocm-roles
```

## Expect

```
I: Fetching ocm roles
ROLE NAME ROLE ARN LINKED ADMIN AWS Managed CONSOLE ACCESS
rosacli-ocm-role-stage-OCM-Role-13849960 arn:aws:iam::090777400063:role/test/rosacli-ocm-role-stage-OCM-Role-13849960 No Yes No Yes
```

## Step

1. Run the list command with JSON and YAML output. Confirm valid output includes `NoConsole` with a value of `No` or `Yes`.

```bash
rosa list ocm-roles -o json
rosa list ocm-roles -o yaml
```

## Expect

```json
[
  {
    "RoleName": "rosacli-ocm-role-stage-OCM-Role-13849960",
    "RoleARN": "arn:aws:iam::090777400063:role/test/rosacli-ocm-role-stage-OCM-Role-13849960",
    "Linked": "No",
    "Admin": "Yes",
    "NoConsole": "No"
  }
]
```

```yaml
- Admin: "Yes"
  Linked: "No"
  NoConsole: "No"
  RoleARN: arn:aws:iam::090777400063:role/test/rosacli-ocm-role-stage-OCM-Role-13849960
  RoleName: rosacli-ocm-role-stage-OCM-Role-13849960
```

## Step

1. Create an OCM role with `--no-console`. Confirm the IAM role has the `rosa_no_console_role=true` tag.

```bash
rosa create ocm-role --mode auto -y --prefix 'jkeyne' --no-console
```

## Expect

```
I: Creating ocm role
W: This OCM role cannot be used to provision clusters via console.redhat.com
I: Creating role using 'arn:aws:iam::090777400063:user/jkeyne'
I: Attached trust policy to role 'jkeyne-OCM-Role-13849960(https://console.aws.amazon.com/iam/home?#/roles/jkeyne-OCM-Role-13849960)': {"Version": "2012-10-17", "Statement": [{"Action": ["sts:AssumeRole"], "Effect": "Allow", "Condition": {"StringEquals": {"sts:ExternalId": "1jlfDskrR39egznAq3T18Ul0Xxv"}}, "Principal": {"AWS": ["arn:aws:iam::644306948063:role/RH-Managed-OpenShift-Installer"]}}]}
I: Created role 'jkeyne-OCM-Role-13849960' with ARN 'arn:aws:iam::090777400063:role/jkeyne-OCM-Role-13849960'
I: Attached policy 'arn:aws:iam::090777400063:policy/jkeyne-OCM-Role-13849960-NoConsole-Policy' to role 'jkeyne-OCM-Role-13849960(https://console.aws.amazon.com/iam/home?#/roles/jkeyne-OCM-Role-13849960)'
I: Linking OCM role
I: Successfully linked role-arn 'arn:aws:iam::090777400063:role/jkeyne-OCM-Role-13849960' with organization account '1jlfDskrR39egznAq3T18Ul0Xxv'
```

```bash
rosa list ocm-roles
aws iam get-role --role-name jkeyne-OCM-Role-13849960 --output json | jq -r '.Role.Tags[] | select(.Key == "rosa_no_console_role")'
```

```
I: Fetching ocm roles
ROLE NAME ROLE ARN LINKED ADMIN AWS Managed CONSOLE ACCESS
jkeyne-OCM-Role-13849960 arn:aws:iam::090777400063:role/jkeyne-OCM-Role-13849960 Yes No No No
rosacli-ocm-role-stage-OCM-Role-13849960 arn:aws:iam::090777400063:role/test/rosacli-ocm-role-stage-OCM-Role-13849960 No Yes No Yes
```

```json
{
  "Key": "rosa_no_console_role",
  "Value": "true"
}
```

## Step

1. Run `rosa create ocm-role -i`. Confirm it prompts `? Create OCM role with minimal permissions (no console access): [? for help] (y/N)` and selecting yes creates the same role as the previous step.

```bash
rosa create ocm-role -i
```

## Expect

```
I: Creating ocm role
? Role prefix: jkeyne
? Enable admin capabilities for the OCM role: No
? Create OCM role with minimal permissions (no console access): Yes
W: This OCM role cannot be used to provision clusters via console.redhat.com
? Permissions boundary ARN (optional):
? Role Path (optional):
? Role creation mode: auto
I: Creating role using 'arn:aws:iam::090777400063:user/jkeyne'
? Create the 'jkeyne-OCM-Role-13849960' role? Yes
I: Attached trust policy to role 'jkeyne-OCM-Role-13849960(https://console.aws.amazon.com/iam/home?#/roles/jkeyne-OCM-Role-13849960)': {"Version": "2012-10-17", "Statement": [{"Action": ["sts:AssumeRole"], "Effect": "Allow", "Condition": {"StringEquals": {"sts:ExternalId": "1jlfDskrR39egznAq3T18Ul0Xxv"}}, "Principal": {"AWS": ["arn:aws:iam::644306948063:role/RH-Managed-OpenShift-Installer"]}}]}
I: Created role 'jkeyne-OCM-Role-13849960' with ARN 'arn:aws:iam::090777400063:role/jkeyne-OCM-Role-13849960'
I: Attached policy 'arn:aws:iam::090777400063:policy/jkeyne-OCM-Role-13849960-NoConsole-Policy' to role 'jkeyne-OCM-Role-13849960(https://console.aws.amazon.com/iam/home?#/roles/jkeyne-OCM-Role-13849960)'
I: Linking OCM role
? OCM Role ARN: arn:aws:iam::090777400063:role/jkeyne-OCM-Role-13849960
? Link the 'arn:aws:iam::090777400063:role/jkeyne-OCM-Role-13849960' role with organization '1jlfDskrR39egznAq3T18Ul0Xxv'? Yes
I: Successfully linked role-arn 'arn:aws:iam::090777400063:role/jkeyne-OCM-Role-13849960' with organization account '1jlfDskrR39egznAq3T18Ul0Xxv'
```

```bash
aws iam get-role --role-name jkeyne-OCM-Role-13849960 --output json | jq -r '.Role.Tags[] | select(.Key == "rosa_no_console_role")'
```

```json
{
  "Key": "rosa_no_console_role",
  "Value": "true"
}
```
