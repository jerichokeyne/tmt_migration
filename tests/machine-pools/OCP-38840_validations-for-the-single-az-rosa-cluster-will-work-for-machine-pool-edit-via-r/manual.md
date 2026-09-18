# Test

## Step
Log in the rosa tool and prepare one multi zone ready cluster

## Expect

## Step
Run command to edit the machine pools
```bash
rosa edit machinepool
```

## Expect
- It will show Error: required flag(s) "cluster" not set

## Step
edit machine pool with invalid value
```bash
rosa edit machinepool -c xueli-rosa --replicas -9 aaa
```

## Expect
~~Failed with error: Failed to add machine pool to cluster 'xueli-rosa': identifier is '400', code is 'CLUSTERS-MGMT-400' and operation identifier is '1ie6b9sokkd6n3461t9g9rafu928s56r': Attribute 'replicas' must be a non-negative integer.~~
```
E: The number of machine pool replicas needs to be a non-negative integer(OCM-4597)
```

## Step
Set replicas and enable-autoscaling at the same time
```bash
rosa edit machinepool <machinepool name> -c xueli-rosa --min-replicas 3--max-replicas 3 --enable-autoscaling --replicas 0
```

## Expect
Failed with error:
~~Replicas can 't be set when autoscaling is enabled ~~ E: Failed to get autoscaling or replicas: 'Autoscaling enabled on machine pool 'worker'. can't set replicas'(OCM-4597)

## Step
Set min-replicas large than max-replicas
```bash
rosa edit machinepool <machinepool name> -c xueli-rosa --min-replicas 9 --max-replicas 3 -enable-autoscalingedit
```

## Expect
Failed with error:
~~E: Failed to update machine pool 'mp-4597' on cluster 'aaraj-classic': Attribute 'autoscaling.min_replicas' must be less than or equal to 'autoscaling.max_replicas'.(OCM-4597) ~~ E: Min replicas must be less than max replicas (OCM-7180)

## Step
set min-replicas and max-replicas without set --enable-autoscaling
```bash
rosa edit machinepool <machinepool name> -c xueli-rosa --min-replicas 9 --max-replicas 3
```

## Expect
Failed with error
~~E: Autoscaling must be enabled in order to set min and max replicas~~ E: Failed to get autoscaling or replicas: 'Autoscaling is not enabled on machine pool 'worker'. can't set min or max replicas'(OCM-4597)

## Step
Try to edit the machinepool with the invalid identifier name.
```bash
rosa edit machinepool -c aaraj-classic $#_aaraj
```

## Expect
```
E: Expected a valid identifier for the machine pool
```

## Step
Try to edit the machinepool with the name not present in the cluster
```bash
rosa edit machinepool -c aaraj-classic --replicas 3 aaraj
```

## Expect
```
E: Failed to get machine pool 'aaraj' for cluster 'aaraj-classic'
```

## Step
Try to edit the machinepool with --min-replicas flag when autoscaling is disabled for the machinepool.
```bash
rosa edit machinepool -c aaraj-classic mp-4597 --min-replicas 2
```

## Expect
```
E: Failed to get autoscaling or replicas: 'Autoscaling is not enabled on machine pool 'mp-4597'. can't set min or max replicas'
```

## Step
Try to edit the machinepool with --max-replicas flag when autoscaling is disabled for the machinepool.
```bash
rosa edit machinepool -c aaraj-classic mp-4597 --max-replicas 5
```

## Expect
```
E: Failed to get autoscaling or replicas: 'Autoscaling is not enabled on machine pool 'mp-4597'. can't set min or max replicas'
```

## Step
Try to edit machinepool with negative min_replicas value.
```bash
rosa edit machinepool -c aaraj-classic mp-4597 --min-replicas -3 --enable-autoscaling
```

## Expect
~~E: The number of machine pool replicas needs to be a non-negative integer~~ E: Min replicas must be greater than zero when autoscaling is enabled(OCM-7180)

## Step
Try to edit machinepool with just --autorepair flag.
```bash
rosa edit machinepool -c aaraj-classic mp-4597 --autorepair=false
```

## Expect
```
E: Setting the `autorepair` flag is only supported for hosted clusters(OCM-4597)
```

## Step
Check other options should work
--debug
--profile
-v
--yes

## Expect
