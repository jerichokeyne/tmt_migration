# Test

## Step
Create a Hypershift cluster with autoscaling  
  
--min-replicas 3 --max-replicas 6 --enable-autoscaling

## Expect
Checklist:  
- Cluster ready  
- Describe cluster and check the nodes information. It should show the autoscaling information  
- Machinepool ready  
- Check machinepool show the 3/6 autoscaling for replicas  
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
