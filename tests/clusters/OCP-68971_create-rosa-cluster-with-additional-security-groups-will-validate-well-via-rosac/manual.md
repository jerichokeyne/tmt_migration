# Test

## Step

Create cluster with --additional-infra-security-group-ids ,--additional-control-plane-security-group-ids, --additional-compute-security-group-ids
but no subnet-ids

## Expect

There should be error
lixue@Xue-Lis-MacBook-Pro ~ % rosa create cluster -c test --additional-infra-security-group-ids djlajfd
```
W: In a future release STS will be the default mode.
W: --sts flag won't be necessary if you wish to use STS.
W: --non-sts/--mint-mode flag will be necessary if you do not wish to use STS.
E: Setting the `additional-infra-security-group-ids` flag is only allowed for BYO VPC clusters
```

## Step

Create cluster with version lower than 4.14 with --additional-infra-security-group-ids ,--additional-control-plane-security-group-ids, --additional-compute-security-group-ids set

## Expect

There will be error message that only supports from 4.14
```
E: Parameter 'additional-infra-security-group-ids' is not supported prior to version '4.14.0'
```

## Step

Create cluster with invalid --additional-infra-security-group-ids ,--additional-control-plane-security-group-ids, --additional-compute-security-group-ids like "invalid string"

## Expect

There should be error message
lixue@Xue-Lis-MacBook-Pro ~ % rosa create cluster -c xueli --subnet-ids subnet-0111c2cd0b0a702b5 --private-link --additional-infra-security-group-ids invalid
```
W: In a future release STS will be the default mode.
W: --sts flag won't be necessary if you wish to use STS.
W: --non-sts/--mint-mode flag will be necessary if you do not wish to use STS.
W: You are choosing to use AWS PrivateLink for your cluster. Once the cluster is created, this option cannot be changed.
? Are you sure you want to use AWS PrivateLink for cluster 'xueli'? Yes
I: Creating cluster 'xueli'
I: To view a list of clusters and their status, run 'rosa list clusters'
E: Failed to create cluster: Security Group ID 'invalid' doesn't have 'sg-' prefix
```

## Step

Create cluster with invalid --additional-infra-security-group-ids ,--additional-control-plane-security-group-ids, --additional-compute-security-group-ids with more than 10 SG ids

## Expect

There should be error message show that the limitation is 5

## Step

Create cluster --additional-infra-security-group-ids ,--additional-control-plane-security-group-ids, ~~--additional-compute-security-group-ids(OCM-6053)~~ with more than 5 SG ids and --hosted-cp

## Expect

There should be error message that the flags cannot work for hosted cluster
Parameter 'additional-infra-security-group-ids' is not supported for Hosted Control Plane clusters
