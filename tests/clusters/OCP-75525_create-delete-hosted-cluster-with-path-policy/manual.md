# Test

## Step
Prepare account-roles with role path and policy path

## Expect

## Step
Create Hypershift cluster with the account-roles in step1 and set the operator role/policy path

## Expect
Checklist:  
- Cluster ready  
- Describe cluster and check account/operator roles contain the given path  
- Machinepool ready  
- Cluster Operators ready

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
