# Setup
Log in the rosa tool, create VPC with subnets and prepare one rosa hypershift ready cluster

# Test

## Step
Check nodes details

## Expect
As desired  
Nodes:  
- Compute (desired): 2  
- Compute (current): 0  
  
Or for an autoscaling cluster  
Nodes:  
- Compute (autoscaled): 2-3  
- Compute (current): 0

## Step
Run command to record the machine pools (would work with day1 autoscaling too)  
$ rosa list machinepool -c <cluster name>

## Expect
- The machine pools returned  
- Subnets are set  
- Autorepair is True  
- Autoscaling is as set  
- Nodepool name is "workers or workers-<number> for multi-az  
ID AUTOSCALING REPLICAS INSTANCE TYPE AVAILABILITY ZONE SUBNET NODEPOOL   
workers No 2 m5.xlarge us-west-2a subnet-093ef2e9cd69cb74d am-hp-workers

## Step
Run command to create machine pool with the created subnet  
$ rosa create machinepool -c <cluster name> --replicas 3 --instance-type m5.xlarge --name new-mp --subnet <subnetids>

## Expect
I: Machine pool 'new-mp' created successfully on hosted cluster '<cluster name>'  
I: To view all machine pools, run 'rosa list machinepools -c <cluster name>'

## Step
Check nodes details

## Expect
Nodes:  
- Compute (desired): 5  
- Compute (current): 0  
  
Or for an autoscaling cluster  
Nodes:  
- Compute (autoscaled): 5-6  
- Compute (current): 0

## Step
Check the machine pool with command  
$ rosa list machinepool -c <cluster name>

## Expect
The machine pool should be created and all of the information should exactly match the input  
ID AUTOSCALING REPLICAS INSTANCE TYPE AVAILABILITY ZONE SUBNET NODEPOOL   
workers No 2 m5.xlarge us-west-2a subnet-093ef2e9cd69cb74d am-hp-workers   
new-mp No 3 m5.xlarge us-west-2a subnet-093ef2e9cd69cb74d am-hp-workers1

## Step
Scale up and scale down the machinepool

## Expect
The result is as expected

## Step
Add autoscalling

## Expect
The machinepool updated as expected

## Step
Change the autorepair to False

## Expect
The machinepool updated as expected

## Step
Delete machinepool

## Expect
The machinepool deleted

## Step
Create another machinepool replicas 0

## Expect
It will succeed

## Step
Create another machinepool autoscaling but min_replicas 0

## Expect
It will fail that min_replicas cannot be 0

## Step
Repeat with multi-az cluster

## Expect

## Step
Repeat with autoscaling cluster

## Expect
