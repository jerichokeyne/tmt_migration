# Test

## Step
Create a machinepool with interactive mode  
$ rosa create machinepool -c jf-hcp -i  
  
? Tags (optional): key1:value1,key2:value2

## Expect
I: Machine pool 'mp-1' created successfully on hosted cluster 'jf-hcp'  
I: To view the machine pool details, run 'rosa describe machinepool --cluster jf-hcp --machinepool mp-1'  
I: To view all machine pools, run 'rosa list machinepools --cluster jf-hcp'

## Step
Describe the machinepool  
$ rosa describe machinepool mp-1 -c jf-hcp

## Expect
ID: mp-1  
Cluster ID: 2b41lllf5988rrh45bde8t7q50adb4p6  
Autoscaling: No  
Desired replicas: 2  
Current replicas: 0  
Instance type: m5.xlarge  
Labels:  
Tags: api.openshift.com/legal-entity-id=1jlfDskrR39egznAq3T18Ul0Xxv, api.openshift.com/name=jf-hcp, api.openshift.com/nodepool-ocm=mp-1, key1=value1, key2=value2, red-hat-managed=true, api.openshift.com/environment=staging, api.openshift.com/id=2b41lllf5988rrh45bde8t7q50adb4p6, red-hat-clustertype=rosa, api.openshift.com/nodepool-hypershift=jf-hcp-mp-1, cluster-tag=cluster-value  
Taints:  
Availability zone: us-west-2a  
Subnet: subnet-0309526054864f01b  
Version: 4.15.6  
Autorepair: Yes  
Tuning configs:  
Additional security group IDs: sg-09360a53ee730ec37  
Node drain grace period:  
Message: Minimum availability requires 2 replicas, current 0 available

## Step
Attempt to create new machinepool with invalid tags  
$ rosa create machinepool -c jf-hcp -i  
  
? Tags (optional): test

## Expect
X Sorry, your reply was invalid: invalid tag format for tag '[test]'. Expected tag format: 'key:value'
