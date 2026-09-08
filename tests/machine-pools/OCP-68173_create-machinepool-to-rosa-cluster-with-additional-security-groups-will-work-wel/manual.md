# Test

## Step
Run command to check help message  
$ rosa create machinepool -h

## Expect
There should be flag  
--security-group-ids stringArray Security Group IDs to be added to the machine pool

## Step
Prepare a cluster with byovpc

## Expect

## Step
Prepare customized security groups to the vpc

## Expect

## Step
Create a machinepool with --security-group-ids set  
% rosa create machinepool --name test --cluster-name xuelisg --security-group-ids <ids> --replicas 3

## Expect
The machinepool will be created

## Step
List the machinepool  
% rosa list machinepool -c xuelisg

## Expect
The created machinepool will be listed and the sg is listed in the column of the output  
lixue@Xue-Lis-MacBook-Pro rosa % rosa list machinepool -c xuelisg   
ID AUTOSCALING REPLICAS INSTANCE TYPE LABELS TAINTS AVAILABILITY ZONES SUBNETS SPOT INSTANCES DISK SIZE SG IDs  
worker No 2 m5.xlarge us-west-2c subnet-0d61a41423986be56 No 300 GiB [sg-08f1d3c305c402464]  
test No 3 m5.xlarge us-west-2c subnet-0d61a41423986be56 No 300 GiB [sg-08f1d3c305c402464]

## Step
Describe the machinepool

## Expect
There is security group for machinepool details  
lixue@Xue-Lis-MacBook-Pro rosa % rosa describe machinepool test -c xuelisg  
  
ID: test  
Cluster ID: 26o1b8eooiqkmr2kikp99ucis32fqmuq  
Autoscaling: No  
Replicas: 3  
Instance type: m5.xlarge  
Labels:   
Taints:   
Availability zones: us-west-2c  
Subnets: subnet-0d61a41423986be56  
Spot instances: No  
Disk size: 300 GiB  
Security Group IDs: [sg-08f1d3c305c402464]

## Step
Launch cluster console to check the machineset  
$ oc get machineset -o yaml -n openshift-machine-api

## Expect
The machineset has the security group
