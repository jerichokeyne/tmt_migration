# Test

## Step
Prepare a rosa cluster

## Expect

## Step
Check the create machinepool message  
$ rosa create machinepool -h

## Expect
There is   
--disk-size string Root disk size with a suffix like GiB or TiB

## Step
Create a machinepool with the disk size  
$ rosa create machinepool -c <cluster> --name xueli --replicas 3 --instance-type r5.xlarge --disk-size "200 GiB"

## Expect
The machinepool will be created

## Step
List the created machine pool  
$ rosa list machinepool -c <cluster>

## Expect
The created machinepool can be listed  
The volume size shows correctly  
The workers created without volume size shows DISK SIZE "300GiB"  
~~The workers not created with volume size shows "default"~~

## Step
Describe the created machine pool  
$ rosa describe machinepool <machinepool> -c <cluster>

## Expect
It returns the correct DISK SIZE.

## Step
Launch cluster console to check

## Expect
The nodes are created with correct volume size

## Step
Create another machinepool with volume size 0.5TiB  
lixue@Xue-Lis-MacBook-Pro ~ % rosa create machinepool -c xueli --disk-size 0.5TiB --replicas 3 --name xueliadd2

## Expect
It will create successfully. When list the machinepools, it will show 512 GiB for the machinepool  
lixue@Xue-Lis-MacBook-Pro ~ % rosa list machinepools -c xueli  
ID AUTOSCALING REPLICAS INSTANCE TYPE LABELS TAINTS AVAILABILITY ZONES SUBNETS SPOT INSTANCES DISK SIZE   
xuelimp No 1 m5.xlarge us-west-2a No ~~default~~ 300GiB  
xuelimp2 No 3 m5.xlarge us-west-2a No ~~default~~ 300GiB  
xueliadd2 No 3 m5.xlarge us-west-2a No 512 GiB
