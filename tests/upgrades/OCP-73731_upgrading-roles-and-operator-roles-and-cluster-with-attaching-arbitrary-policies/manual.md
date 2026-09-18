# Test

## Step

Create one claissc STS cluster which has upgrade path, cluster3

## Expect

## Step

Detach and Delete some operator-roles polcies and account-roles policies from the roles + and also attach one arbitrary polcy on some operator-role and account-roles to make sure some operator-role and account-roles only attaching one arbitrary policy

## Expect

## Step

Upgrade roles and upgrade cluster in auto mode:

```bash
rosa upgrade roles
rosa upgrade cluster
```

## Expect

In auto mode:

- The deleted policies should be created
- All roles should be attached with the desired polcies.
- No change on the arbitray policies and the roles attached arbitray policies
- Expect to see output of policies being attached as expected, for example:

```
I: Attached policy 'arn:aws:iam::xxx:policy/oa-upgr-ControlPlane-Role-Policy' to role 'oa-upgr-ControlPlane-Role(https://console.aws.amazon.com/iam/home?#/roles/oa-upgr-ControlPlane-Role)'
```

Specifically, we are looking to see that the policy name appears as well as a URL to the IAM role for each upgraded role

## Step

Create one claissc STS cluster which has upgrade path, cluster4

## Expect

## Step

Detach and Delete some operator-roles polcies and account-roles policies from the roles + and also attach some arbitrary polcies on some operator-role and account-roles

## Expect

## Step

Upgrade roles and upgrade cluster in auto mode:

```bash
rosa upgrade roles
rosa upgrade cluster
```

## Expect

In auto mode:

- The deleted policies should be created
- All roles should be attached with the desired polcies.
- No change on the arbitray policies and the roles attached arbitray policies
