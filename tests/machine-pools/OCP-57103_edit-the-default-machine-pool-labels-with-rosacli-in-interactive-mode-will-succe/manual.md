# Test

## Step
Log in with the rosa tool and create ROSA cluster

## Expect

## Step
Run command to record the machine pools
```bash
rosa list machinepool -c <cluster name>
```

## Expect
- The machine pools returned
- The ID/replica should be default/0 and instance type should be m5.xlarge by default, the availability zones should be same with the default one
```
ID AUTOSCALING REPLICAS INSTANCE TYPE LABELS TAINTS AVAILABILITY ZONES SUBNETS SPOT INSTANCES
Default No 2 m5.xlarge us-west-2a N/A
- The labels and taits should show in the output
```

## Step
Run command to edit default machine pool in interactive mode and add label test_1=test-2
```bash
rosa edit machinepool Default -c <cluster name>
```
? Enable autoscaling (optional): No
? Labels: test_1=test-2
? Taints (optional): key=value:NoSchedule

## Expect
- There will be succeeded message output
? Enable autoscaling (optional): No
? Labels: a=b
```
I: Updated machine pool 'Default' on cluster 'am-label-13'
```

## Step
Run command to check the machine pools
```bash
rosa list machinepool -c <cluster name>
```

## Expect
- The updated machine pool should be listed
```
ID AUTOSCALING REPLICAS INSTANCE TYPE LABELS TAINTS AVAILABILITY ZONES SUBNETS SPOT INSTANCES
Default No 2 m5.xlarge test_1=test-2 us-west-2a N/A
- The labels and taits should show in the output
```

## Step
Run command to edit default machine pool in interactive mode and add multiple labels
```bash
rosa edit machinepool Default -c <cluster name>
```
? Labels aaa=b,t=test
? Taints (optional): key=value:PreferNoSchedule

## Expect
- There will be succeeded message output

## Step
Run command to check the machine pools
```bash
rosa list machinepool -c <cluster name>
```

## Expect
- The updated machine pool should be listed
```
ID AUTOSCALING REPLICAS INSTANCE TYPE LABELS TAINTS AVAILABILITY ZONES SUBNETS SPOT INSTANCES
Default No 2 m5.xlarge aaa=b,t=test us-west-2a N/A
- The labels and taits should show in the output
```

## Step
Run command to edit default machine pool in interactive mode and add label with empty value
```bash
rosa edit machinepool Default -c <cluster name>
```
? Labels: test=
? Taints (optional): ""

## Expect
- There will be succeeded message output

## Step
Run command to check the machine pools
```bash
rosa list machinepool -c <cluster name>
```

## Expect
- The updated machine pool should be listed
```
ID AUTOSCALING REPLICAS INSTANCE TYPE LABELS TAINTS AVAILABILITY ZONES SUBNETS SPOT INSTANCES
Default No 2 m5.xlarge test= us-west-2a N/A
- The labels and taits should show in the output
```

## Step
Run command to edit default machine pool in interactive mode and delete label
```bash
rosa edit machinepool Default -c <cluster name>
```
? Labels: <Enter Space>

## Expect
- There will be succeeded message output
- <https://issues.redhat.com/browse/OCM-2385>

## Step
Run command to check the machine pools
```bash
rosa list machinepool -c <cluster name>
```

## Expect
- The updated machine pool should be listed
```
ID AUTOSCALING REPLICAS INSTANCE TYPE LABELS TAINTS AVAILABILITY ZONES SUBNETS SPOT INSTANCES
Default No 2 m5.xlarge us-west-2a N/A
```
