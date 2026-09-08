# Test

## Step
Log in the rosa tool and prepare one multi zone ready cluster

## Expect

## Step
Run command to edit the machine pools  
$ rosa edit machinepool

## Expect
- It will show Error: required flag(s) "cluster" not set

## Step
edit machine pool with invalid value  
$ rosa edit machinepool -c xueli-rosa --replicas -9 aaa

## Expect
Failed with error:  
~~Failed to add machine pool to cluster 'xueli-rosa': identifier is '400', code is 'CLUSTERS-MGMT-400' and operation identifier is '1ie6b9sokkd6n3461t9g9rafu928s56r': Attribute 'replicas' must be a non-negative integer.~~  
E: The number of machine pool replicas needs to be a non-negative integer(OCM-4597)

## Step
Set replicas and enable-autoscaling at the same time  
$ rosa edit machinepool <machinepool name> -c xueli-rosa --min-replicas 3--max-replicas 3 --enable-autoscaling --replicas 0

## Expect
Failed with error:  
~~Replicas can 't be set when autoscaling is enabled~~  
E: Failed to get autoscaling or replicas: 'Autoscaling enabled on machine pool 'worker'. can't set replicas'(OCM-4597)

## Step
Set min-replicas large than max-replicas  
$ rosa edit machinepool <machinepool name> -c xueli-rosa --min-replicas 9 --max-replicas 3 -enable-autoscalingedit

## Expect
Failed with error:  
E: Failed to update machine pool 'mp-4597' on cluster 'aaraj-classic': Attribute 'autoscaling.min_replicas' must be less than or equal to 'autoscaling.max_replicas'.(OCM-4597)

## Step
set min-replicas and max-replicas without set --enable-autoscaling  
$ rosa edit machinepool <machinepool name> -c xueli-rosa --min-replicas 9 --max-replicas 3

## Expect
Failed with error  
~~E: Autoscaling must be enabled in order to set min and max replicas~~  
E: Failed to get autoscaling or replicas: 'Autoscaling is not enabled on machine pool 'worker'. can't set min or max replicas'(OCM-4597)

## Step
set min-replicas and max-replicas not multiple 3 for multi-az  
$ rosa edit machinepool <machinepool name> -c xueli-rosa --min-replicas 4 --enable-autoscaling -- max-replica 5

## Expect
Failed with error:  
~~E: Multi AZ clusters require that the replicas be a multiple of 3~~  
E: Multi AZ clusters require that the number of MachinePool replicas be a multiple of 3(OCM-4597)

## Step
Check other options should work  
--debug  
--profile  
-v  
--yes

## Expect
