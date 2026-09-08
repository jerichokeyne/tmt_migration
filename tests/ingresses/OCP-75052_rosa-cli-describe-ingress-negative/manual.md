# Setup
Prepare a cluster

# Test

## Step
1. Verify error if no cluster provided:  
'rosa describe ingress $ingressID'

## Expect
Failed to execute root command: required flag(s) "cluster" not set

## Step
2. Verify error if incorrect ingress ID is provided:  
'rosa describe ingress xxx -c $cluster'

## Expect
E: Failed to get ingress 'xxx' for cluster '27fd1e14gi4pkct19qo1jgbsodv22n5i'
