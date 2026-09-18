# Test

## Step

Prepare a vpc with tag red-hat-managed:true
Prepare subnets belongs to the vpc
some of them have label red-hat-managed:true
Some of them have no label red-hat-managed:true

## Expect

## Step

Create rosa cluster in interactive mode

## Expect

## Step

Choose create on existing vpc in interactive mode

## Expect

Check the listed subnets:
All subnets with red-hat-managed:true shouldn't be listed
There should be a warning like below
```
W: The following subnets were excluded because they belong to a VPC that is managed by Red Hat: [subnet-08c081cb90c201892, subnet-08fae84740150fef5, subnet-096a70a06abc5ab26, subnet-0fce128180b46d873]
```

## Step

Prepare a cluster with existing vpc

## Expect

## Step

Prepare a subnet with red-hat-managed:true

## Expect

## Step

Create machinepool of the cluster to a subnet in interactive mode

## Expect

Check the listed subnets:
All subnets with red-hat-managed:true shouldn't be listed
There should be a warning like below
```
W: The following subnets were excluded because they belong to a VPC that is managed by Red Hat: [subnet-08c081cb90c201892, subnet-08fae84740150fef5, subnet-096a70a06abc5ab26, subnet-0fce128180b46d873]
```
