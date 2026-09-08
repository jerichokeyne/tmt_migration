# Test

## Step
Prepare a hcp cluster

## Expect

## Step
Check the help message of craete machinepool command  
rosa create machinepool --help

## Expect
--ec2-metadata-http-tokens string Should cluster nodes use both v1 and v2 endpoints or just v2 endpoint of EC2 Instance Metadata Service (IMDS)This flag is only supported for Hosted Control Planes.

## Step
Create a machinepool to the cluster in the interactive mode by setting the value of "Configure the use of IMDSv2 for ec2 instances" as optional  
$ rosa create machinepool -c aaraj-hcp -i  
? Machine pool name: test  
? OpenShift version (default = '4.16.2'): 4.16.2  
? Select subnet for a hosted machine pool: No  
? AWS availability zone (default = 'us-west-2a'): us-west-2a  
? Enable autoscaling: No  
? Replicas: 1  
? Labels (optional):   
? Taints (optional):   
? Tags (optional):   
I: Checking available instance types for machine pool 'test'  
? Instance type (default = 'm5.xlarge'): m5.xlarge  
? Autorepair: Yes  
W: No kubelet configs available for cluster '2cmeo59llnu4er51uoa36pfn33bcfh4q'. Any kubelet config in input will be ignored  
? Should cluster nodes use both v1 and v2 endpoints or just v2 endpoint of EC2 Instance Metadata Service (IMDS)This flag is only supported for Hosted Control Planes.  
? Configure the use of IMDSv2 for ec2 instances (default = 'optional'): [Use arrows to move, type to filter, ? for more help]  
> optional  
required  
? Configure the use of IMDSv2 for ec2 instances (default = 'optional'): optional

## Expect
The default value must be shown optional.  
The machinepool should be created successfully.

## Step
Describe the machinepool to the cluster that we created above  
$ rosa describe machinepool -c aaraj-hcp test

## Expect
The value for EC2 Metadata Http Tokens must be optional as set in step 2.  
ID: test  
Cluster ID: 2cmeo59llnu4er51uoa36pfn33bcfh4q  
Autoscaling: No  
Desired replicas: 1  
Current replicas: 0  
Instance type: m5.xlarge  
Labels:   
Tags: api.openshift.com/environment=staging, api.openshift.com/id=2cmeo59llnu4er51uoa36pfn33bcfh4q, api.openshift.com/legal-entity-id=1jlfDskrR39egznAq3T18Ul0Xxv, api.openshift.com/name=aaraj-hcp, api.openshift.com/nodepool-hypershift=aaraj-hcp-test, api.openshift.com/nodepool-ocm=test, red-hat-clustertype=rosa, red-hat-managed=true  
Taints:   
Availability zone: us-west-2a  
Subnet: subnet-026da85fa352a29ec  
Version: 4.16.2  
EC2 Metadata Http Tokens: optional  
Autorepair: Yes  
Tuning configs:   
Kubelet configs:   
Additional security group IDs:   
Node drain grace period:   
Management upgrade:   
- Type: Replace  
- Max surge: 1  
- Max unavailable: 0  
Message: Minimum availability requires 1 replicas, current 0 available

## Step
Create a machinepool to the cluster in the interactive mode by setting the value of "Configure the use of IMDSv2 for ec2 instances" as required  
$ rosa create machinepool -c aaraj-hcp -i  
? Machine pool name: test1  
? OpenShift version (default = '4.16.2'): 4.16.2  
? Select subnet for a hosted machine pool: No  
? AWS availability zone (default = 'us-west-2a'): us-west-2a  
? Enable autoscaling: No  
? Replicas: 1  
? Labels (optional):   
? Taints (optional):   
? Tags (optional):   
I: Checking available instance types for machine pool 'test1'  
? Instance type (default = 'm5.xlarge'): m5.xlarge  
? Autorepair: Yes  
W: No kubelet configs available for cluster '2cmeo59llnu4er51uoa36pfn33bcfh4q'. Any kubelet config in input will be ignored  
? Configure the use of IMDSv2 for ec2 instances (default = 'optional'): required

## Expect
The machinepool should be created successfully.

## Step
Describe the machinepool to the cluster that we created above  
$ rosa describe machinepool -c aaraj-hcp test1

## Expect
The value for EC2 Metadata Http Tokens must be optional as set in step 4.  
ID: test1  
Cluster ID: 2cmeo59llnu4er51uoa36pfn33bcfh4q  
Autoscaling: No  
Desired replicas: 1  
Current replicas: 0  
Instance type: m5.xlarge  
Labels:   
Tags: api.openshift.com/id=2cmeo59llnu4er51uoa36pfn33bcfh4q, api.openshift.com/legal-entity-id=1jlfDskrR39egznAq3T18Ul0Xxv, api.openshift.com/name=aaraj-hcp, api.openshift.com/nodepool-hypershift=aaraj-hcp-test1, api.openshift.com/nodepool-ocm=test1, red-hat-clustertype=rosa, red-hat-managed=true, api.openshift.com/environment=staging  
Taints:   
Availability zone: us-west-2a  
Subnet: subnet-026da85fa352a29ec  
Version: 4.16.2  
EC2 Metadata Http Tokens: required  
Autorepair: Yes  
Tuning configs:   
Kubelet configs:   
Additional security group IDs:   
Node drain grace period:   
Management upgrade:   
- Type: Replace  
- Max surge: 1  
- Max unavailable: 0  
Message: Minimum availability requires 1 replicas, current 0 available
