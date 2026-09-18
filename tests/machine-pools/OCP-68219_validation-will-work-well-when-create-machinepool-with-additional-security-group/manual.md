# Test

## Step
Prepare a rosa cluster provisioned not with BYOVPC

## Expect

## Step
Create a machine pool with additional SG

## Expect
There will be error show like below
lixue@Xue-Lis-MacBook-Pro rosa % rosa create machinepool -c xueli4 --additional-security-group-ids test-ssss --replicas 1 --name xueli
```
E: Setting the `additional-security-group-ids` flag is only allowed for BYOVPC clusters
```

## Step
Create machinepool with SG has tag red-hat-managed:true

## Expect
Error will return
lixue@Xue-Lis-MacBook-Pro rosa % rosa create machinepool -c xuelimzsg --additional-security-group-ids sg-0989058749b6b2b2f --name xuelizs --replicas 3
```
I: Fetching instance types
E: Failed to add machine pool to cluster 'xuelimzsg': Provided Additional Compute Security Group 'sg-0989058749b6b2b2f' is Red Hat managed
```

## Step
Create machinepool with SG not attached to the VPC

## Expect
error returns
lixue@Xue-Lis-MacBook-Pro rosa % rosa create machinepool -c xuelimzsg --additional-security-group-ids sg-0a46a784f38985fb8 --name xuelizs --replicas 3
```
I: Fetching instance types
E: Failed to add machine pool to cluster 'xuelimzsg': Provided Additional Compute Security Group 'sg-0a46a784f38985fb8' is not attached to VPC 'vpc-0bcb963b20b722c12'
```

## Step
Create machinepool with SG not attached to the VPC to cluster version lower than 4.11

## Expect
error returns that the version cannot lower than 4.11-0
