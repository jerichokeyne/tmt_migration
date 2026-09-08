# Test

## Step
Create a private Hypershift cluster

## Expect
Checklist:  
- Cluster ready  
- Describe cluster and check it is marked as private  
- Machinepool ready  
- Cluster Operators ready (use `How to access private cluster document` in description)

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
