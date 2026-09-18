# Test

## Step
Prepare HCP cluster

## Expect

## Step
Check help message
```bash
rosa create,edit machinepool --help
```

## Expect
-node-drain-grace-period string You may set a grace period for how long Pod Disruption Budget-protected workloads will be respected when the NodePool is being replaced or upgraded.
After this grace period, all remaining workloads will be forcibly evicted.
Valid value is from 0 to 1 week (10080 minutes), and the supported units are 'minute|minutes' or 'hour|hours'. 0 or empty value means that the NodePool can be drained without any time limitations.

## Step
Create machinepool to the cluster with --node-drain-grace-period
```bash
rosa create machinepool --name test1 -c <cluster> --node-drain-grace-period 20 --replicas 2
rosa create machinepool --name test1 -c <cluster> --node-drain-grace-period="20 hours" --replicas 2
rosa create machinepool --name test1 -c <cluster> --node-drain-grace-period="20 minutes" --replicas 2
```

## Expect
-The machinepool will be created successfully
-With value 20, the Node drain grace period is 20 min
-With value 20 hours , the Node drain grace period is 1200 min
-With value 20 minues , the Node drain grace period is 20 min

## Step
Check the machinepool detail by
```bash
rosa describe machinepool test -c <cluster>
```

## Expect
There will be output of machinepool shows the node-drain-grace-period
```
./rosa describe machinepool --cluster ying-hcp-auth2 --machinepool test1
```


```
ID: test1
Cluster ID: 2a44ga6kd7rndnir0e94tari2t8u4a5p
Autoscaling: No
Desired replicas: 2
Current replicas: 0
Instance type: m5.xlarge
Labels:
Taints:
Availability zone: us-west-2a
Subnet: subnet-047e30d1ec518e69c
Version: 4.16.0-0.nightly-2024-03-20-061740
Autorepair: Yes
Tuning configs:
Additional security group IDs:
Node drain grace period: 20 minutes
Message: WaitingForAvailableMachines: InstanceNotFound,WaitingForNodeRef
```

## Step
Create another machinepool without node-drain-grace-period and describe it

## Expect
-The Node drain grace period will be the cluster-level Node drain grace period value

## Step
Edit machinepool with node-drain-grace-period
```bash
rosa edit machinepool mp-1 -c ying-hcp-auth2 --node-drain-grace-period 10
rosa edit machinepool mp-1 -c ying-hcp-auth2 --node-drain-grace-period "10 hours"
rosa edit machinepool mp-1 -c ying-hcp-auth2 --node-drain-grace-period "10 minutes"
```

## Expect
The machinepool will be updated successfully
