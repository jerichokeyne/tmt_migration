# Test

## Step
Prepare a ready ROSA cluster

## Expect

## Step
run command to check the machinepool help message  
$ rosa create machinepool -h

## Expect
- The flags use-spot-instances and spot-max-price are hidden for now.  
(They should be added before official release/announce)

## Step
List the machinepool of the cluster

## Expect
- There is no SPOT INSTANCES column in the list for the cluster have no spot machinepool

## Step
Crete a spot machine pool to the cluster via command  
$ rosa create machinepool spot1 --spot-max-price 10.2 -c sdqe-m-rosa --replicas 1

## Expect
- The machinepool will be created successfully  
- The list machinepool command will output

## Step
List the machinepool to check  
$ rosa list machinepool -c <cluster name>

## Expect
- The machinepool will be listed successfully  
- There will be column shows SPOT INSTANCES  
- The "SPOT INSTANCES" for the new created machinepool should be Yes(max $10.2)  
- The Default machinepool of the SPOT INSTANCES should show "N/A"  
- The machinepool output should be like below  
[xueli@xueli-work linux]$ rosa list machinepools -c sdqe-m-rosa  
ID AUTOSCALING REPLICAS INSTANCE TYPE LABELS TAINTS AVAILABILITY ZONES SPOT INSTANCES  
Default Yes 2-6 m5.xlarge us-east-2a N/A  
xuelimspot No 1 m5.xlarge us-east-2a Yes (on-demand)  
xuelimspot2 No 2 m5.xlarge us-east-2a Yes (max $10)  
xuelimspot3 Yes 2-2 m5.xlarge us-east-2a Yes (max $10)  
xuelinspot4 No 2 m5.xlarge us-east-2a No  
xuelimspot4 No 1 m5.xlarge us-east-2a Yes (on-demand)  
spot1 No 1 m5.xlarge us-east-2a Yes (max $10.2)

## Step
Create another machinepool without spot-max-price set and list the machinepool to check  
$ rosa create machinepool nspot1  --replicas 1

## Expect
- The machinepool will be created successfully  
- The SPOT INSTANCES of the machinepool should be "No"

## Step
Create another machinepool with use-spot-instances but no spot-max-price set and list the machinepool to check  
$ rosa create machinepool nspot1  --replicas 1 --use-spot-instances

## Expect
- The machinepool will be created successfully  
- The SPOT INSTANCES of the machinepool should be "Yes(On-demand)"
