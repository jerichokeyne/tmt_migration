# Test

## Step
Prepare a rosa cluster

## Expect

## Step
List the machinepools of the cluster
```bash
rosa list machinepool -c <cluster id>
```

## Expect
There will be a default worker pool be listed
lixue@Xue-Lis-MacBook-Pro rosa % rosa list machinepool -c 25o86o092v3l5p44fk3sc1em9ck29qih
```
ID AUTOSCALING REPLICAS INSTANCE TYPE LABELS TAINTS AVAILABILITY ZONES SUBNETS SPOT INSTANCES DISK SIZE
**worker** No 3 m5.xlarge us-east-1a, us-east-1c, us-east-1d subnet-077f024a0fbd86b02, subnet-0fdc7fed45d0d76ea, subnet-0cf9b655a55b4f416 No default
```

## Step
Scale up the default machinepool worker
```bash
rosa edit machinepool worker -c <cluster name> --replicas <replicas number>
```

## Expect
It will succeed

## Step
Describe the rosa cluster
```bash
rosa describe cluster -c <cluster id>
```

## Expect
The worker should be updated successfully

## Step
Edit the cluster
```bash
rosa edit machinepool Default -c <cluster name> --enbale-autoscaling --min-replicas 3 --max-replicas 4
```

## Expect
It will succeed

## Step
Check the machinepool of the cluster
```bash
rosa list machinepool -c <cluster id>
```

## Expect
The default worker is updated

## Step
Create an additional machinepool of the cluster
```bash
rosa create machinepool additional -c <cluster name>
```

## Expect
Check that the additional machinepool is created

## Step
Describe the cluster
```bash
rosa describe cluster -c <cluster name>
```

## Expect
The compute number should be total number of all the machinepools

## Step
Scale down the worker pool nodes to 0

## Expect
It will scale down succeed

## Step
Update the cluster to UWM enabled/disabled
```bash
rosa edit cluster -c <cluster name> --disable-workload-monitoring
```

## Expect
It will succeed

## Step
Delete the default machinepool
```bash
rosa delete machinepool worker -c <cluster>
```

## Expect

## Step
List the machinepool again
```bash
rosa list machinepool -c <cluster name>
```

## Expect
The default worker pool is not listed anymore
