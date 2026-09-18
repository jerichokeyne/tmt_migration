# Test

## Step

1. Log in to ROSA CLI and create and link an OCM role. Confirm that no user role is linked.

## Expect

## Step

1. Create an STS cluster through ROSA CLI.

## Expect

It succeeds.

## Step

1. Test these actions:
   - Create, edit, and delete a cluster.
   - Create, edit, and delete a machine pool.
   - Create, edit, and delete an IDP.
   - Other operations.

## Expect

It succeeds.

## Step

1. Repeat steps 1 through 3 with an account that has no OCM role.

## Expect

It succeeds.
