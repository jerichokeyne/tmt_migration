# Test

## Step
Prepare a hosted cp cluster

## Expect

## Step
Try to edit the machinepool with the name that is not present in the cluster.  
$ rosa edit machinepool -c aaraj-hcp --replicas 3 aaraj

## Expect
E: Machine pool 'aaraj' does not exist for hosted cluster 'aaraj-hcp'

## Step
Create a new machinepool to the cluster  
$ rosa create machinepool -c aaraj-hcp --replicas 3 --name mp-4597

## Expect
I: Checking available instance types for machine pool 'mp-4597'  
I: Machine pool 'mp-4597' created successfully on hosted cluster 'aaraj-hcp'  
I: To view the machine pool details, run 'rosa describe machinepool --cluster aaraj-hcp --machinepool mp-4597'  
I: To view all machine pools, run 'rosa list machinepools --cluster aaraj-hcp'

## Step
Try to edit the replicas of the machinepool with negative value  
$ rosa edit machinepool mp-4597 -c aaraj-hcp --replicas -9

## Expect
E: The number of machine pool replicas needs to be a non-negative integer

## Step
Try to edit the machinepool with --min-replicas flag when autoscaling is disabled for the machinepool.  
$ rosa edit machinepool -c aaraj-hcp mp-4597 --min-replicas 2

## Expect
E: Failed to get autoscaling or replicas: 'Autoscaling is not enabled on machine pool 'mp-4597'. can't set min or max replicas'

## Step
Try to edit the machinepool with --max-replicas flag when autoscaling is disabled for the machinepool.  
$ rosa edit machinepool -c aaraj-hcp mp-4597 --max-replicas 5

## Expect
E: Failed to get autoscaling or replicas: 'Autoscaling is not enabled on machine pool 'mp-4597'. can't set min or max replicas'

## Step
Edit the machinepool to autoscaling mode  
$ rosa edit machinepool -c aaraj-hcp mp-4597 --enable-autoscaling --min-replicas 2 --max-replicas 6

## Expect
I: Updated machine pool 'mp-4597' on hosted cluster 'aaraj-hcp'

## Step
Check that machinepool is in autoscaling mode  
$ rosa list machinepools -c aaraj-hcp

## Expect
ID AUTOSCALING REPLICAS INSTANCE TYPE LABELS TAINTS AVAILABILITY ZONE SUBNET VERSION AUTOREPAIR   
mp-4597 Yes 3/2-6 m5.xlarge us-west-2a subnet-031b3114d26f325c9 4.15.9 Yes   
workers No 2/2 m5.xlarge us-west-2a subnet-031b3114d26f325c9 4.15.9 Yes

## Step
Try to edit machinepool with negative min_replicas value.  
$ rosa edit machinepool -c aaraj-hcp mp-4597 --min-replicas -3

## Expect
E: The number of machine pool min-replicas needs to be greater than zero

## Step
Try to edit machinepool with --replicas flag when the autoscaling is enabled for the machinepool.  
$ rosa edit machinepool -c aaraj-hcp mp-4597 --replicas 3

## Expect
E: Failed to get autoscaling or replicas: 'Autoscaling enabled on machine pool 'mp-4597'. can't set replicas'
