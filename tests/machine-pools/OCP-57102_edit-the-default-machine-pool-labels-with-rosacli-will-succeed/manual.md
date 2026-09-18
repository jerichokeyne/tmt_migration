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
- The labels and taints should shown in the output
```

## Step
Run command to edit default machine pool and add label
```bash
rosa edit machinepool Default -c <cluster name> --labels test_1=test-2 --labels <labels> --taits <taits>
```
NOTE: SDA-8272, empty taints value is support ,--taints key=:NoSchedule

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
Default No 2 m5.xlarge test_1=test-2 us-west-2a N/A
- The labels and taints should shown in the output
```

## Step
Run command to edit default machine pool and add label with empty value
```bash
rosa edit machinepool Default -c <cluster name> --labels test=
```

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
```

## Step
Run command to edit default machine pool and delete label
```bash
rosa edit machinepool Default -c <cluster name> --labels "" --taints ""
```

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
Default No 2 m5.xlarge us-west-2a N/A
- - The labels and taints should shown in the output
```
