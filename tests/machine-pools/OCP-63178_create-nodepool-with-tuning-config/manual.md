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
Create a nodepool with the 3 tuning configs
```bash
rosa create machinepool -c trad-ga --replicas 3 --tuning-configs tuned01,tuned02,tuned03 --name tc1
```

## Expect
```
I: Machine pool 'a' created successfully on hosted cluster 'am-hp0105'
```

## Step
Describe machinepools
```bash
rosa describe machinepool -c trad-ga tc1
```

## Expect
```
ID: tc1
Cluster ID: 27gileross02nn511ifjdmduk459520v
Autoscaling: No
Desired replicas: 3
Current replicas: 3
Instance type: m5.xlarge
Labels:
Taints:
Availability zone: us-east-1b
Subnet: subnet-04c7045b3a8b9d4f0
Version: 4.14.1
Autorepair: Yes
Tuning configs: tuned01,tuned02,tuned03
Message:
```

## Step
Update the nodepool's tuning to only 1
```bash
rosa edit machinepool -c trad-ga tc1 --tuning-configs tuned01
```

## Expect
```
I: Updated machine pool 'tc1' on hosted cluster 'trad-ga'
```

## Step
Update the nodepool without tuning config

## Expect
```
I: Updated machine pool 'tc1' on hosted cluster 'trad-ga'
```

## Step
Describe machinepools
```bash
rosa describe machinepool -c trad-ga tc1
```

## Expect
No tuning configs are shown

```
ID: tc1
Cluster ID: 27gileross02nn511ifjdmduk459520v
Autoscaling: No
Desired replicas: 3
Current replicas: 3
Instance type: m5.xlarge
Labels:
Taints:
Availability zone: us-east-1b
Subnet: subnet-04c7045b3a8b9d4f0
Version: 4.14.1
Autorepair: Yes
Tuning configs:
Message:
```
