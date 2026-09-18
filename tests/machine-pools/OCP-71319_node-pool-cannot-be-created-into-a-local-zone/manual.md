# Test

## Step
Prepare a hosted cluster in a VPC with a local zone

## Expect

## Step
Create a node pool with a subnet from the local zone.

## Expect
This should fail

```
> rosa create machinepool -c $CLUSTER_NAME --name np-fail --replicas 2 --subnet <subnet-localzone>
```
