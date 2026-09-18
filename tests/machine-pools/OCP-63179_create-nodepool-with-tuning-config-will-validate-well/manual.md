# Test

## Step
Prepare a hosted cluster

## Expect

## Step
Create 3 tuning configs to the cluster

    See

## Expect
Tuned configs created successfully

## Step
Create a nodepool with the non-existing tuning config

## Expect
```
E: Failed to add machine pool to hosted cluster 'am-hp0105': Tuning config with name 'asd' does not exist for cluster '23el6sntvmglp4qi1picvel80cvqtni3'
```

## Step
Create nodepool with duplicate tuning config

## Expect
Error

## Step
Create a nodepool

## Expect

## Step
Update the nodepool with non-existing tuning config set in the body

## Expect
```
E: Failed to edit machine pool to hosted cluster 'am-hp0105': Tuning config with name 'asd' does not exist for cluster '23el6sntvmglp4qi1picvel80cvqtni3'
```

## Step
Update with duplicate tuning config

## Expect
Error
