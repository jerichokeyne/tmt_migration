# Test

## Step

Create one claissc STS cluster which has upgrade path, cluster1

## Expect

## Step

Detach some operator-roles polcies and account-roles policies from the roles

## Expect

## Step

Upgrade account-roles by `rosa upgrade account-roles --mode manual` and upgrade operator-roles by `rosa upgrade operator-roles --mode manual`

## Expect

The promoted command should contain:

- to upgrade the policies versions on both roles and policies
- to attach the policies to the roles which polcies are detached.

## Step

Delete some operator-roles polcies and account-roles policies of the account and operator roles

## Expect

## Step

Upgrade account-roles by `rosa upgrade account-roles --mode manual` and upgrade operator-roles by `rosa upgrade operator-roles --mode manual`

## Expect

The promoted command should contain:

- to upgrade the policies versions on both roles and policies
- to create the deleted polcies
- to attach the policies to the roles which polcies are deleted.

## Step

Create one claissc STS cluster which has upgrade path, cluster3

## Expect

## Step

Detach and Delete some operator-roles polcies and account-roles policies from the roles + and also attach one arbitrary polcy on some operator-role and account-roles to make sure some operator-role and account-roles only attaching one arbitrary policy

## Expect

## Step

Upgrade account-roles by `rosa upgrade account-roles --mode manual` and upgrade operator-roles by `rosa upgrade operator-roles --mode manual`

## Expect

The promoted command should contain:

- to upgrade the policies versions on both roles and policies
- to attach the policies to the roles which polcies are detached.
- No command for any operation on the arbitrary policies.

## Step

Create one claissc STS cluster which has upgrade path, cluster5

## Expect

## Step

Detach and delete some operator-roles polcies and account-roles policies from the roles

## Expect

## Step

Upgrade roles and upgrade cluster in manual:

```bash
rosa upgrade roles
rosa upgrade cluster
```

## Expect

In manual mode, the promoted command should contain:

- to upgrade the policies versions on both roles and policies
- to create the deleted polcies
- to attach the policies to the roles which polcies are deleted.

## Step

Create one claissc STS cluster which has upgrade path, cluster6

## Expect

## Step

Detach and Delete some operator-roles polcies and account-roles policies from the roles + and also attach one arbitrary polcy on some operator-role and account-roles to make sure some operator-role and account-roles only attaching one arbitrary policy

## Expect

## Step

Upgrade roles and upgrade cluster in manual:

```bash
rosa upgrade roles
rosa upgrade cluster
```

## Expect

In manual mode, the promoted command should contain:

- to upgrade the policies versions on both roles and policies
- to attach the policies to the roles which polcies are detached.
- No command for any operation on the arbitrary policies.

## Step

Repeat step 6~14 on the cluster which has account and operator roles has more than one arbitrary polcies attached

## Expect

The result should be same as above.

## Step

Delete account-roles and operator-roles in manual mode after the cluster is deleted

## Expect

Account-roles:

- Prompted AWS commands should not contains the ones to delete the arbitrary policies
- Prompted AWS commands can be executed to detach all attaching policies including arbitrary policies and delete the roles and not-arbitrary polcies.

Operator-roles:

- Prompted AWS commands should not contains the ones to delete the arbitrary policies
- Prompted AWS commands can be executed to detach all attaching policies including arbitrary policies and delete the roles and not-arbitrary polcies.

## Step

Repeat all above steps on hostecp clusters(account-roles and operator-roles)

## Expect

Results about arbitrary should be same.
Reuslts on the redhat managed policies don't need upgrade as they are using AWS managed policies
