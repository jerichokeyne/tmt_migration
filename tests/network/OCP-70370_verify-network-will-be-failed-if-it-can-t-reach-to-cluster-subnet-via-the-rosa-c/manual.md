# Test

## Step
Prepare a ready ROSA cluster

## Expect

## Step
Edit the VPC to make the subnets network can't work well  
How to do:create a VPC,then add deny rules in VPC Network ACLs(eg:deny 443 port) and rule number is less than 100

## Expect

## Step
Verify network with cluster id

## Expect
-The result should be failed  
-For different cluster types, the domain list is different  
[https://gitlab.cee.redhat.com/service/osd-network-verifier-golden-ami/-/tree/master/build/config ](<https://gitlab.cee.redhat.com/service/osd-network-verifier-golden-ami/-/tree/master/build/config%A0>)

## Step
Check if --status-only and --watch works well and --region

## Expect

## Step
The network verification result will be sync to cluster inflight check  
rosa describe cluster <>

## Expect
-The failed result will be displayed in cluster description  
-There will be inflight check failed result in the response  

  * Inflight check ID
  * Inflight check Last Run time
  * Inflight check private subnets failed reason
  * A tip for rerun network verify command

./rosa describe cluster -c sdq-rosa-bpcjx  
Name: sdq-rosa-bpcjx  
ID: 27ccfk1shne5obr7vvqm84vnejc2okiq  
External ID:   
Control Plane: Customer Hosted  
OpenShift Version:   
Channel Group: stable  
DNS: Not ready  
AWS Account: 301721915996  
API URL:   
Console URL:   
Region: us-east-2  
Multi-AZ: true  
Nodes:  
- Control plane: 3  
- Infra: 3  
- Compute: 3  
Network:  
- Type: OVNKubernetes  
- Service CIDR: 172.30.0.0/16  
- Machine CIDR: 10.0.0.0/16  
- Pod CIDR: 10.128.0.0/14  
- Host Prefix: /23  
Workload Monitoring: Enabled  
Ec2 Metadata Http Tokens: optional  
State: error (Inflight checks failed. Check inflight checks API for details)  
Private: No  
Created: Nov 8 2023 05:00:02 UTC  
Details Page: https://qaprodauth.console.redhat.com/openshift/details/s/2XsZA9Qdv2bRknvzpp3CgatCMI6  
Provisioning Error Code: OCM4001  
Provisioning Error Message: Inflight checks failed. Get 'inflight_checks' endpoint for details.  
Failed Inflight Checks:  
ID: bc8afa3e-b679-44d9-aba4-a5496a5c6d19  
Last run: Nov 8 2023 05:03:22 UTC  
Invalid configurations on subnet 'subnet-0093e0e8e8bc28f28' have been identified:   
Details for 'Egress URL access issues':  
- quay-registry.s3.amazonaws.com:443  
Invalid configurations on subnet 'subnet-00f1df15c6d6bce33' have been identified:   
Details for 'Egress URL access issues':  
- events.us-east-2.amazonaws.com:443  
Invalid configurations on subnet 'subnet-09db3e4745f1952a4' have been identified:   
Details for 'Egress URL access issues':  
- ec2.us-east-2.amazonaws.com:443  
  
  
Please run `rosa verify network -c 27ccfk1shne5obr7vvqm84vnejc2okiq` after adjusting the cluster's network configuration to remove the warning

## Step
Remove the deny rule from AWS to make the subnets network is fine

## Expect
-The result will be sync to cluster inflight check  
-The passed result will not listed in clusters description

## Step
~~Verify network with subnet-ids~~  
with --hosted-cp   
without --hosted-cp

## Expect
-The result should be failed  
-For different cluster types, the domain list is different  
[https://gitlab.cee.redhat.com/service/osd-network-verifier-golden-ami/-/tree/master/build/config ](<https://gitlab.cee.redhat.com/service/osd-network-verifier-golden-ami/-/tree/master/build/config%A0>)

## Step
Check if --status-only and --watch works well and --region

## Expect

## Step
Repeat the above steps to a BYO VPC sts/non-sts/Hosted ROSA cluster

## Expect
