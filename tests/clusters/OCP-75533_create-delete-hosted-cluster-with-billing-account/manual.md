# Test

## Step

Create the Hypershift cluster with different --billing-account <account-id>

## Expect

Checklist:
- Cluster ready
- Describe cluster and check billing account information
- Machinepool ready
- Check machinepool instance type is correct

## Step

Delete the Hypershift cluster by `rosa delete cluster`

## Expect

- The cluster can be deleted
- All resource on AWS should be deleted.

## Step

Delete operator roles

## Expect

- The operator roles are deleted from AWS
- There are readable message shown about the role deletion

## Step

Delete oidc provider

## Expect

- The oidc-provider are deleted from AWS
- There are readable message shown about the oidc-provider deletion
