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
Create a machinepool to the cluster by setting the value of ec2_metadata_http_tokens to optional  
$ rosa create machinepool -c 2cn3brv872nucjaq5p6bcnguu0d9f89p --name test --replicas 3 --ec2-metadata-http-tokens optional

## Expect
I: Checking available instance types for machine pool 'test'  
I: Machine pool 'test' created successfully on hosted cluster '2cn3brv872nucjaq5p6bcnguu0d9f89p'  
I: To view the machine pool details, run 'rosa describe machinepool --cluster 2cn3brv872nucjaq5p6bcnguu0d9f89p --machinepool test'  
I: To view all machine pools, run 'rosa list machinepools --cluster 2cn3brv872nucjaq5p6bcnguu0d9f89p'

## Step
Describe the machinepool to the cluster that we created above  
$ rosa describe machinepool -c 2cn3brv872nucjaq5p6bcnguu0d9f89p test

## Expect
ID: test  
Cluster ID: 2cn3brv872nucjaq5p6bcnguu0d9f89p  
Autoscaling: No  
Desired replicas: 3  
Current replicas: 0  
Instance type: m5.xlarge  
Labels:   
Tags: api.openshift.com/environment=staging, api.openshift.com/legal-entity-id=1jlfDskrR39egznAq3T18Ul0Xxv, api.openshift.com/nodepool-hypershift=rosacli-ci-r3ca-test, api.openshift.com/nodepool-ocm=test, qe-managed=true, red-hat-clustertype=rosa, test-tag=tagvalue, api.openshift.com/id=2cn3brv872nucjaq5p6bcnguu0d9f89p, api.openshift.com/name=rosacli-ci-r3ca, red-hat-managed=true  
Taints:   
Availability zone: us-west-2a  
Subnet: subnet-013e2b2ef1d2a91c4  
Version: 4.16.4  
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
Message: Minimum availability requires 3 replicas, current 0 available

## Step
Create a machinepool to the cluster by setting the value of ec2_metadata_http_tokens to required  
$ rosa create machinepool -c 2cn3brv872nucjaq5p6bcnguu0d9f89p --name test2 --replicas 3 --ec2-metadata-http-tokens required

## Expect
I: Checking available instance types for machine pool 'test2'  
I: Machine pool 'test2' created successfully on hosted cluster '2cn3brv872nucjaq5p6bcnguu0d9f89p'  
I: To view the machine pool details, run 'rosa describe machinepool --cluster 2cn3brv872nucjaq5p6bcnguu0d9f89p --machinepool test2'  
I: To view all machine pools, run 'rosa list machinepools --cluster 2cn3brv872nucjaq5p6bcnguu0d9f89p'

## Step
Describe the machinepool to the cluster that we created above  
$ rosa describe machinepool -c 2cn3brv872nucjaq5p6bcnguu0d9f89p test2

## Expect
ID: test2  
Cluster ID: 2cn3brv872nucjaq5p6bcnguu0d9f89p  
Autoscaling: No  
Desired replicas: 3  
Current replicas: 0  
Instance type: m5.xlarge  
Labels:   
Tags: api.openshift.com/name=rosacli-ci-r3ca, red-hat-managed=true, test-tag=tagvalue, api.openshift.com/id=2cn3brv872nucjaq5p6bcnguu0d9f89p, api.openshift.com/legal-entity-id=1jlfDskrR39egznAq3T18Ul0Xxv, api.openshift.com/nodepool-ocm=test2, qe-managed=true, red-hat-clustertype=rosa, api.openshift.com/environment=staging, api.openshift.com/nodepool-hypershift=rosacli-ci-r3ca-test2  
Taints:   
Availability zone: us-west-2a  
Subnet: subnet-013e2b2ef1d2a91c4  
Version: 4.16.4  
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
Message: Minimum availability requires 3 replicas, current 0 available

## Step
Create a machinepool to the cluster by setting the value of ec2_metadata_http_tokens to empty string/no value  
$ rosa create machinepool -c 2cn3brv872nucjaq5p6bcnguu0d9f89p --name test3 --replicas 3 --ec2-metadata-http-tokens ""

## Expect
I: Checking available instance types for machine pool 'test3'  
I: Machine pool 'test3' created successfully on hosted cluster '2cn3brv872nucjaq5p6bcnguu0d9f89p'  
I: To view the machine pool details, run 'rosa describe machinepool --cluster 2cn3brv872nucjaq5p6bcnguu0d9f89p --machinepool test3'  
I: To view all machine pools, run 'rosa list machinepools --cluster 2cn3brv872nucjaq5p6bcnguu0d9f89p'

## Step
Describe the machinepool to the cluster that we created above  
$ rosa describe machinepool -c 2cn3brv872nucjaq5p6bcnguu0d9f89p test3  
  
**Note** : It takes optional as default value

## Expect
ID: test3  
Cluster ID: 2cn3brv872nucjaq5p6bcnguu0d9f89p  
Autoscaling: No  
Desired replicas: 3  
Current replicas: 0  
Instance type: m5.xlarge  
Labels:   
Tags: api.openshift.com/nodepool-hypershift=rosacli-ci-r3ca-test3, api.openshift.com/nodepool-ocm=test3, qe-managed=true, red-hat-clustertype=rosa, red-hat-managed=true, test-tag=tagvalue, api.openshift.com/legal-entity-id=1jlfDskrR39egznAq3T18Ul0Xxv, api.openshift.com/name=rosacli-ci-r3ca, api.openshift.com/environment=staging, api.openshift.com/id=2cn3brv872nucjaq5p6bcnguu0d9f89p  
Taints:   
Availability zone: us-west-2a  
Subnet: subnet-013e2b2ef1d2a91c4  
Version: 4.16.4  
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
Message: Minimum availability requires 3 replicas, current 0 available

## Step
Create a machinepool to the cluster by setting the value of ec2_metadata_http_tokens to invalid string  
$ rosa create machinepool -c 2cn3brv872nucjaq5p6bcnguu0d9f89p --name test3 --replicas 3 --ec2-metadata-http-tokens invalid

## Expect
I: Checking available instance types for machine pool 'test3'  
E: Expected a valid http tokens value : ec2-metadata-http-tokens value should be one of 'required', 'optional'
