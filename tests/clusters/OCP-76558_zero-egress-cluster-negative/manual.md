# Setup
Ensure that AWS account organization has the capabilities:  
  
capability.organization.pin_to_shard  
capability.organization.hcp_enable_zero_egress  
  
Clone terraform file from: https://github.com/dustman9000/rosa-hcp-zero-egress-terraform.git  
  
provision shard: 88d699d7-7821-11ee-8b13-0a580a82022a

# Test

## Step
1. Attempt to create cluster with invalid property value set for zero_egress  
  
rosa create cluster --properties zero_egress:invalid

## Expect
Error message (bug currently preventing error message)

## Step
2. Create a zero_egress cluster

## Expect
Cluster creation succeeds

## Step
3. Attempt to change zero_egress property

## Expect
Failed to execute root command: unknown flag: --properties

## Step
4. Attempt to upgrade zero_egress cluster

## Expect
E: Failed to schedule upgrade for cluster 'my-hcp-cluster': status is 400, identifier is '400', code is 'CLUSTERS-MGMT-400', at '2024-10-01T20:46:10Z' and operation identifier is 'c5571e78-9b35-4562-8fa8-c9323f566e0d': Control Plane upgrade of a zero egress enabled cluster is not supported
