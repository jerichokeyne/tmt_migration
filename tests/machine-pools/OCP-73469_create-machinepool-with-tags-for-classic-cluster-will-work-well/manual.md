# Test

## Step
Prepare a rosa classic cluster

## Expect

## Step
Check the help message of machinepool creation

## Expect
Here is help message of --tags
No type error
Message is readable
--tags strings Apply user defined tags to all resources created by ROSA in AWS. Tags are comma separated, for example: 'key value, foo bar'

## Step
Create a machinepool with tags set
```bash
rosa create machinepool -c <cluster> --name mp-tags --replicas 3 --tags "test:testvalue,test2:testValue/openshift"
```

## Expect
The machinepool is created successfully without any error

## Step
Describe the machinepool
```bash
rosa describe machinepool mp-tags -c <cluster>
```

## Expect
The tags including cluster tags will show
lixue@Xue-Lis-MacBook-Pro rosa % rosa describe machinepool --cluster 2atmfocid44m1621kdbsle5lpqimv1bh --machinepool tagsd

```
ID: tagsd
Cluster ID: 2atmfocid44m1621kdbsle5lpqimv1bh
Autoscaling: No
Replicas: 3
Instance type: m5.xlarge
Labels:
Taints:
Availability zones: us-east-1a, us-east-1b, us-east-1c
Subnets: subnet-03afc22b5ffc72ab4, subnet-02b7b9fb0c4b6ec20, subnet-011bd23ac6b95c0ed
Spot instances: No
Disk size: 300 GiB
Additional Security Group IDs:
Tags: jdfjald=aaa, red-hat-clustertype=rosa, red-hat-managed=true
```

## Step
Create with invalid tags like
no tag value
```bash
rosa create machinepool -c <cluster> --name mp-tags --replicas 0 --tags "notagvalue:"
```
No tag key
```bash
rosa create machinepool -c <cluster> --name mp-tags --replicas 0 --tags ":notagkey"
```
Invalid tag
```bash
rosa create machinepool -c <cluster> --name mp-tags --replicas 0 --tags "non-ascii:值"
```

## Expect
Correct error message will show
