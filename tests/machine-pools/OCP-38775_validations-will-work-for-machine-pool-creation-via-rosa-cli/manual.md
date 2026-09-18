# Test

## Step
Log in the rosa tool and prepare one multi zone ready cluster

## Expect

## Step
Run command to create the machine pools
```bash
rosa create machinepool
```

## Expect
- It will show Error: required flag(s) "cluster" not set

## Step
Create machine pool with invalid value
```bash
rosa create machinepool -c xueli-rosa --replicas -9 --name aaa
```

## Expect
Failed with error:
Failed to add machine pool to cluster 'xueli-rosa': identifier is '400', code is 'CLUSTERS-MGMT-400' and operation identifier is '1ie6b9sokkd6n3461t9g9rafu928s56r': Attribute 'replicas' must be a non-negative integer.

## Step
Create machine pool with invalid name
```bash
rosa create machinepool -c xueli-rosa --replicas 0 --name %^#@
```

## Expect
Failed with error:
Expected a valid name for the machine pool

## Step
Create machine pool with invalid instance type:
```bash
rosa create machinepool -c xueli-rosa --replicas 0 --name aaa --instance-type custom-4-16384
```

## Expect
Failed with error:
```
E: Expected a valid machine type: A valid machine type number must be specified
Valid machine types: m5.xlarge r5.xlarge m5.2xlarge c5.2xlarge r5.2xlarge m5.4xlarge c5.4xlarge r5.4xlarge m5.8xlarge
```

## Step
Set replicas and enable-autoscaling at the same time
```bash
rosa create machinepool -c xueli-rosa --min-replicas 3--max-replicas 3 --name aaa --enable-autoscaling --replicas 0
```

## Expect
Failed with error:
Replicas can't be set when autoscaling is enabled

## Step
Set min-replicas large than max-replicas
```bash
rosa create machinepool -c xueli-rosa --min-replicas 9 --max-replicas 3 --name aaa -enable-autoscaling
```

## Expect
Failed with error:
max-replicas must be greater or equal to min-replicas

## Step
set min-replicas and max-replicas without set --enable-autoscaling
```bash
rosa create machinepool -c xueli-rosa --min-replicas 9 --max-replicas 3 --name aaa
```

## Expect
Failed with error
```
E: Autoscaling must be enabled in order to set min and max replicas
```

## Step
set min-replicas and max-replicas not multiple 3 for multi-az
```bash
rosa create machinepool -c xueli-rosa --min-replicas 4 --name aaa --enable-autoscaling -- max-replica 5
```

## Expect
Failed with error:
```
E: Multi AZ clusters require that the replicas be a multiple of 3
```

## Step
Check other options should work
--debug
--profile
-v
--yes

## Expect
