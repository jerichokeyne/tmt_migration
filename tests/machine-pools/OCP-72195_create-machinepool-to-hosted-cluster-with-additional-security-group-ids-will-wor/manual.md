# Test

## Step
Prepare a hosted cluster

## Expect

## Step
Prepare some security groups to the cluster vpc

## Expect

## Step
Create machinepool with security groups set  
$ rosa create machinepool --name test -c <cluster id> --additional-security-group-ids <sg ids>

## Expect
The machinepool will be created successfully

## Step
Check the machinepool detail by   
$ rosa describe machinepool test -c <cluster>

## Expect
There will be output of machinepool shows the security groups  
lixue@Xue-Lis-MacBook-Pro SHARED_DIR % rosa describe machinepool workers-0 -c 29ren0qudb8fk9k519uu9nsj8jtfhnla  
  
ID: test  
Cluster ID: 29ren0qudb8fk9k519uu9nsj8jtfhnla  
Autoscaling: Yes  
Desired replicas: 1-2  
Current replicas: 1  
Instance type: m5.xlarge  
Labels:   
Taints:   
Availability zone: us-west-2b  
Subnet: subnet-0242db861e168433d  
Version: 4.15.0-0.nightly-2024-03-06-210910  
Autorepair: Yes  
Tuning configs:   
Message:   
Additional security group IDs: sg-06dff8bf9f0b84f73, sg-0c096260b7d3654bf, sg-07fc9d944fd82ef8d

## Step
Find another machinepool without security groups and describe it  
$ rosa describe machinepool <mp> -c <cluster>

## Expect
The output of machinepool shows empty security groups  
lixue@Xue-Lis-MacBook-Pro SHARED_DIR % rosa describe machinepool workers-0 -c 29ren0qudb8fk9k519uu9nsj8jtfhnla  
  
ID: workers-0  
Cluster ID: 29ren0qudb8fk9k519uu9nsj8jtfhnla  
Autoscaling: Yes  
Desired replicas: 1-2  
Current replicas: 1  
Instance type: m5.xlarge  
Labels:   
Taints:   
Availability zone: us-west-2b  
Subnet: subnet-0242db861e168433d  
Version: 4.15.0-0.nightly-2024-03-06-210910  
Autorepair: Yes  
Tuning configs:   
Message:   
Additional security group IDs:
