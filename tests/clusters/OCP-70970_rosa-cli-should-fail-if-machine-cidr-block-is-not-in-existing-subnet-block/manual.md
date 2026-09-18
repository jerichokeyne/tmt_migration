# Test

## Step

Prepare a VPC with subnet in 10.0.1.0/24

## Expect

## Step

Create a hosted cluster with machine cidr 192.168.1.0/23

## Expect

CLI should fail with error message
'E: All Hosted Control Plane clusters need a pre-configured VPC. Please check: https://docs.openshift.com/rosa/rosa_hcp/rosa-hcp-sts-creating-a-cluster-quickly.html#rosa-hcp-creating-vpc'

## Step

Create a hosted cluster with machine cidr 192.168.1.0/23 in interactive mode

## Expect

CLI should fail with error message
'E: All Hosted Control Plane clusters need a pre-configured VPC. Please check: https://docs.openshift.com/rosa/rosa_hcp/rosa-hcp-sts-creating-a-cluster-quickly.html#rosa-hcp-creating-vpc'
