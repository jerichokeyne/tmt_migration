# Setup

[SDA] Create, link, and delete user and OCM roles across the account and organization.

# Test

## Step

1. Log in to ROSA CLI as `not-org-admin-RH-user1`.

## Expect

## Step

1. Create an OCM role in auto mode.

```bash
rosa create ocm-role --prefix <prefix> --mode auto -y
```

## Expect

- The OCM role is created on AWS.
- Linking the role fails with a readable error message.

## Step

1. Link the OCM role created in step 2.

## Expect

It fails with a readable error message.

## Step

1. Log in to ROSA CLI as `org-admin-RH-user1`.

## Expect

## Step

1. Link the OCM role created in step 2.

## Expect

It succeeds.

## Step

1. Link a second OCM role under the same AWS account.

## Expect

It fails with a readable error message.

## Step

1. Link a second OCM role under a different AWS account.

## Expect

It succeeds.

## Step

1. Log in to ROSA CLI as `not-org-admin-RH-user1`.

## Expect

## Step

1. Create a user role without linking it.

## Expect

## Step

1. Log in to ROSA CLI as `not-org-admin-RH-user2`, which is in the same organization as `not-org-admin-RH-user1`.

## Expect

## Step

1. Link the user role created in step 9.

## Expect

It succeeds.

## Step

1. Log in to ROSA CLI as `not-org-admin-RH-user3`, which is not in the same organization as `not-org-admin-RH-user1`.

## Expect

## Step

1. Link the user role created in step 9.

## Expect

It fails with a readable error message.
