# Setup
rosa create cluster --hosted-cp --default-ingress-route-selector 10.0.0.1  
I: Enabling interactive mode  
? Cluster name: jf-test  
? Deploy cluster with Hosted Control Plane: Yes  
? Billing Account: 301721915996  
I: Using '301721915996' as billing account.  
? OpenShift version (default = '4.14.8'): 4.14.8  
W: More than one Installer role found  
? Installer role ARN (default = 'arn:aws:iam::301721915996:role/ManagedOpenShift-HCP-ROSA-Installer-Role'): arn:aws:iam::301721915996:role/jf2-HCP-ROSA-Installer-Role  
I: Using arn:aws:iam::301721915996:role/jf2-HCP-ROSA-Support-Role for the Support role  
I: Using arn:aws:iam::301721915996:role/jf2-HCP-ROSA-Worker-Role for the Worker role  
? External ID (optional):  
? Operator roles prefix: jf-test-d0i7  
? OIDC Configuration ID (default = '28ulrg53nnq0buccflc6hju776qhfim1 | https://oidc.os1.devshift.org/28ulrg53nnq0buccflc6hju776qhfim1'): 28uucir7atd3rlnmh96ajqckccondq2j | https://oidc.os1.devshift.org/28uucir7atd3rlnmh96ajqckccondq2j  
? Tags (optional):  
? AWS region (default = 'us-east-1'): us-west-2  
? PrivateLink cluster: No  
? Machine CIDR: 10.0.0.0/16  
? Service CIDR: 172.30.0.0/16  
? Pod CIDR: 10.128.0.0/14  
W: The following subnets were excluded because they belong to a VPC that is managed by Red Hat: [subnet-01643310ee0998e68, subnet-01aa1cc34ac52508c, subnet-02efd82885705aef2, subnet-032021b5c715d06f2, subnet-041a8604333923911, subnet-07a3d902ddfb04cec, subnet-07ac0846f6b22d6dd, subnet-088898abe9109f671]  
? Subnet IDs (optional): subnet-07ae3bb174cf0f333 ('rosa-cluster-vpc-public-usw2-az1','vpc-01cf2a5dc7e221c79','us-west-2a', Owner ID: '301721915996'), subnet-0fb8fd52d7fb98f1e ('rosa-cluster-vpc-private-usw2-az1','vpc-01cf2a5dc7e221c79','us-west-2a', Owner ID: '301721915996')  
? Enable Customer Managed key: No  
? Compute nodes instance type (optional, choose 'Skip' to skip selection. The default value will be provided; default = 'm5.xlarge'): m5.xlarge  
? Enable autoscaling: No  
? Compute nodes: 2  
? Host prefix: 23  
? Encrypt etcd data: No  
? Disable Workload monitoring: No  
? Use cluster-wide proxy: No  
? Additional trust bundle file path (optional):  
? Enable audit log forwarding to AWS CloudWatch: No  
E: Updating default ingress settings is not supported for Hosted Control Plane clusters

# Test

## Step
1. Test for HCP cluster creation using --default-ingress-route-selector flag

## Expect
Error stating: Updating default ingress settings is not supported for Hosted Control Plane clusters
