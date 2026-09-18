# Test

## Step

List the <INSTANCE_TYPE> using 'rosa list instace-types'

```bash
rosa list instance-types | grep <INSTANCE_TYPE>
```

## Expect

The <INSTANCE_TYPE> should be displayed on cli.

```bash
rosa list instance-types | grep r7i.48xlarge
```
r7i.48xlarge memory_optimized 192 1.5 TiB

## Step

Create a Rosa classic cluster by setting any one <INSTANCE_TYPE> from [OCM-5583](<https://issues.redhat.com/browse/OCM-5583>)

```bash
rosa create cluster -c <CLUSTER_NAME> --compute-machine-type <INSTANCE_TYPE> --availability-zones us-east-2b --region us-east-2
```

## Expect

The cluster should be provisioned successfully

```bash
rosa create cluster -c akanni-r7i-48xl --compute-machine-type r7i.48xlarge --availability-zones us-east-1b
```
```
W: In a future release STS will be the default mode.
```

```bash
rosa list cluster
```
ID NAME STATE TOPOLOGY
........
2a44968308fcivch37gvo4j60h5gq55j akanni-r7i ready Classic

## Step

Create a machinepool on the cluster created in STEP 2 with <INSTANCE_TYPE>

```bash
rosa create machinepool --cluster=<CLUSTER_NAME> --name=<MACHINEPOOL_NAME> --replicas=3 --instance-type=<INSTANCE_TYPE>
```

## Expect

The machinepool should be created, and after creation list the machinepool and check the instace type
it should match with what you used while creating

```bash
rosa list machinepools --cluster=<CLUSTER_NAME>
```

## Step

Repeat step 2~3 with lowest supported OCP version and the current OCP version

## Expect

It should work as expected, if in case of instance type is not supported for OCP version then file a bug.

## Step

UI checkpoints,

Check the <INSTANCE_TYPE> on the OCM UI web page under the “Compute nodes instance type” option
check for OSD cluster creation page and Rosa cluster creation page

## Expect

The <INSTANCE_TYPE> should be seen from the OCM UI under the “Compute nodes instance type” option

## Step

Repeat steps 2~4 across various kinds of clusters ROSA CLASSIC, ROSA HCP, OSD, OSD Trial.
To cover the testing across different product use this <https://docs.google.com/document/d/1Kc7T6lO7XwZq24ctzUeuiXZ5HHRcnE7LNScOyenxtWs/edit#heading=h.ss3gxh9t0b7q> test stratergy

## Expect

The result should be same
