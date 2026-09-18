# Test

## Step

Prepare a rosa MultiAZ cluster

## Expect

## Step

Check the help message of create machinepool
```bash
rosa create machinepool -h
```

## Expect

- There will be "--availability-zone" and introduction in the help message
[xueli@xueli-work rosa]$ rosa create machinepool -h
Add a machine pool to the cluster.


```
Usage:
rosa create machinepool [flags]
```


```
Aliases:
machinepool, machinepools, machine-pool, machine-pools
```


```
Examples:
\# Interactively add a machine pool to a cluster named "mycluster"
rosa create machinepool --cluster=mycluster --interactive
```


\# Add a machine pool mp-1 with 3 replicas of m5.xlarge to a cluster
```bash
rosa create machinepool --cluster=mycluster --name=mp-1 --replicas=3 --instance-type=m5.xlarge
```


\# Add a machine pool mp-1 with autoscaling enabled and 3 to 6 replicas of m5.xlarge to a cluster
```bash
rosa create machinepool --cluster=mycluster --name=mp-1 --enable-autoscaling \
```
--min-replicas=3 --max-replicas=6 --instance-type=m5.xlarge


\# Add a machine pool with labels to a cluster
```bash
rosa create machinepool -c mycluster --name=mp-1 --replicas=2 --instance-type=r5.2xlarge --labels=foo=bar,bar=baz,
```


\# Add a machine pool with spot instances to a cluster
```bash
rosa create machinepool -c mycluster --name=mp-1 --replicas=2 --instance-type=r5.2xlarge --use-spot-instances \
```
--spot-max-price=0.5


```
Flags:
--availability-zone string Select availability zone to create a single AZ machine pool for a multi-AZ cluster
-c, --cluster string Name or ID of the cluster.
--enable-autoscaling Enable autoscaling for the machine pool.
...
```

## Step

List the machinepool
```bash
rosa list machinepool -c <clustername>
```

## Expect

There will be default machinepool listed

## Step

Create a single AZ machinepool to the cluster
```bash
rosa create machinepool --availability-zone us-east-2a --name=xuelisz -c xuelimz --replicas 1
```

## Expect

The machinepool should be created successfully
[xueli@xueli-work rosa]$ rosa create machinepool --availability-zone us-east-2a --name=xuelisz -c xuelimz --replicas 1
```
I: Machine pool 'xuelisz' created successfully on cluster 'xuelimz'
I: To view all machine pools, run 'rosa list machinepools -c xuelimz'
```

## Step

List the machinepool

## Expect

- The created single zone machinepool should be listed
- The zone should be the one used for machinepool creation
- The replicas should be correct
[xueli@xueli-work rosa]$ rosa list machinepool -c xuelimz
ID AUTOSCALING REPLICAS INSTANCE TYPE LABELS TAINTS AVAILABILITY ZONES SPOT INSTANCES
Default No 3 m5.xlarge us-east-2a, us-east-2b, us-east-2c N/A
aaa No 1 m5.xlarge us-east-2b No
bbb Yes 2-2 m5.4xlarge aaa=bbb ccc=ddd:NoSchedule us-east-2b Yes (max $20)
mz No 3 m6a.12xlarge us-east-2a, us-east-2b, us-east-2c No
xuelisz No 1 m5.xlarge us-east-2a No

## Step

Scale up the machinepool replicas to 2

## Expect

The machinepool should be updated successfully

## Step

List the machinepool

## Expect

The machinepool should be updated successfully in the new output

## Step

Delete the machinepool

## Expect

The machinepool should be deleted successfully

## Step

Create another singlezone machine pool with autoscale enabled

## Expect

The machinepool should be created successfully on only the selected zone

## Step

Create a machinepool without --availability-zone specified

## Expect

A multi-zone machinepool will be created
