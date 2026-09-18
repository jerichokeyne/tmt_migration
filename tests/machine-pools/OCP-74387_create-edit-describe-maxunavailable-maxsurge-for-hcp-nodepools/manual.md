# Test

## Step
Prepare a HCP cluster

## Expect

## Step
Create a nodepool to the cluster with MaxUnavailable/MaxSurge set with percentage value and a lower version to be able to upgrade
```bash
rosa create machinepool -c <cluster_name> --name <mp_name> --replicas 3 --max-surge 5% --max-unavailable 10% --version 4.15.2
```

## Expect
```
I: Checking available instance types for machine pool 'new-mp'
I: Machine pool 'new-mp' created successfully on hosted cluster 'aaraj-hcp'
I: To view the machine pool details, run 'rosa describe machinepool --cluster aaraj-hcp --machinepool new-mp'
I: To view all machine pools, run 'rosa list machinepools --cluster aaraj-hcp'
```

## Step
List the nodepool to see if it is created successfully and present
```bash
rosa list machinepools --cluster <cluster_name>
```

## Expect
```
ID AUTOSCALING REPLICAS INSTANCE TYPE LABELS TAINTS AVAILABILITY ZONE SUBNET VERSION AUTOREPAIR
new-mp No 0/3 m5.xlarge us-west-2a subnet-037c1b72c1f86ea04 4.15.16 Yes
test Yes 3/3-6 m5.xlarge us-west-2a subnet-037c1b72c1f86ea04 4.15.16 Yes
test1 No 0/3 m5.xlarge us-west-2a subnet-0906953a751821025 4.15.16 Yes
worlers No 0/0 m5.xlarge us-west-2a subnet-037c1b72c1f86ea04 4.15.16 Yes
```

## Step
Describe the machinepool to check the value of MaxUnavailable/MaxSurge is present and the value is set correctly

```bash
rosa describe machinepool <mp_name> -c <cluster_name>
```

## Expect
```
ID: new-mp
Cluster ID: 2bs61bvgivf5ehmftkm97190av91mg5s
Autoscaling: No
Desired replicas: 3
Current replicas: 0
Instance type: m5.xlarge
Labels:
Tags: api.openshift.com/nodepool-hypershift=aaraj-hcp-new-mp, api.openshift.com/nodepool-ocm=new-mp, red-hat-clustertype=rosa, red-hat-managed=true, api.openshift.com/environment=staging, api.openshift.com/id=2bs61bvgivf5ehmftkm97190av91mg5s, api.openshift.com/legal-entity-id=1jlfDskrR39egznAq3T18Ul0Xxv, api.openshift.com/name=aaraj-hcp
Taints:
Availability zone: us-west-2a
Subnet: subnet-037c1b72c1f86ea04
Version: 4.15.16
Autorepair: Yes
Tuning configs:
Kubelet configs:
Additional security group IDs:
Node drain grace period:
Management upgrade:
- Type: Replace
- Max surge: 5%
- Max unavailable: 10%
Message: Minimum availability requires 3 replicas, current 0 available
```

## Step
Try to upgrade the nodepool
```bash
rosa upgrade machinepool -c <cluster_name> <mp_name>
```
? Are you sure you want to upgrade machine pool 'test1' to version '4.15.14'? Yes
```
I: Upgrade successfully scheduled for the machine pool 'test1' on cluster 'aaraj-hcp'
```

## Expect
It should be successfully upgraded.

## Step
Create a nodepool to the cluster with MaxUnavailable/MaxSurge set with absolute value and repeat above steps to check the value of MaxUnavailable/MaxSurge is set correctly.
```bash
rosa create machinepool -c <cluster_name> --name <mp_name> --replicas 3 --max-surge 1 --max-unavailable 0
```

## Expect
```
I: Checking available instance types for machine pool 'new-mp'
I: Machine pool 'new-mp' created successfully on hosted cluster 'aaraj-hcp'
I: To view the machine pool details, run 'rosa describe machinepool --cluster aaraj-hcp --machinepool new-mp'
I: To view all machine pools, run 'rosa list machinepools --cluster aaraj-hcp'
```

## Step
Edit the nodepool with MaxUnavailable/MaxSurge set with percentage value
```bash
rosa edit machinepool -c <cluster_name> --max-unavailable 4% --max-surge 3% <mp_name>
```
? Enable autoscaling: No
? Replicas: 3
? Labels (optional):
? Taints (optional):
? Autorepair: Yes
? Node drain grace period (optional):
? Max surge: 3%
? Max unavailable: 4%

## Expect
```
I: Updated machine pool 'new-m-1p' on hosted cluster 'aaraj-hcp'
```

## Step
Describe the nodepool to check if MaxUnavailable/MaxSurge value is set correctly
```bash
rosa describe machinepool -c <cluster_name> <mp_name>
```

## Expect
```
ID: new-m-1p
Cluster ID: 2bs61bvgivf5ehmftkm97190av91mg5s
Autoscaling: No
Desired replicas: 3
Current replicas: 0
Instance type: m5.xlarge
Labels:
Tags: api.openshift.com/id=2bs61bvgivf5ehmftkm97190av91mg5s, api.openshift.com/legal-entity-id=1jlfDskrR39egznAq3T18Ul0Xxv, api.openshift.com/name=aaraj-hcp, api.openshift.com/nodepool-hypershift=aaraj-hcp-new-m-1p, api.openshift.com/nodepool-ocm=new-m-1p, red-hat-clustertype=rosa, red-hat-managed=true, api.openshift.com/environment=staging
Taints:
Availability zone: us-west-2a
Subnet: subnet-037c1b72c1f86ea04
Version: 4.15.16
Autorepair: Yes
Tuning configs:
Kubelet configs:
Additional security group IDs:
Node drain grace period:
Management upgrade:
- Type: Replace
- Max surge: 3%
- Max unavailable: 4%
Message: Minimum availability requires 3 replicas, current 0 available
```

## Step
Edit the nodepool with MaxUnavailable/MaxSurge set with absolute value
```bash
rosa edit machinepool -c aaraj-hcp --max-unavailable 1 --max-surge 2 new-m-1p
```
? Enable autoscaling: No
? Replicas: 3
? Labels (optional):
? Taints (optional):
? Autorepair: Yes
? Node drain grace period (optional):
? Max surge: 2
? Max unavailable: 1

## Expect
```
I: Updated machine pool 'new-m-1p' on hosted cluster 'aaraj-hcp'
```

## Step
Describe the nodepool to check if MaxUnavailable/MaxSurge value is set correctly
```bash
rosa describe machinepool -c <cluster_name> <mp_name>
```

## Expect
```
ID: new-m-1p
Cluster ID: 2bs61bvgivf5ehmftkm97190av91mg5s
Autoscaling: No
Desired replicas: 3
Current replicas: 0
Instance type: m5.xlarge
Labels:
Tags: red-hat-managed=true, api.openshift.com/environment=staging, api.openshift.com/id=2bs61bvgivf5ehmftkm97190av91mg5s, api.openshift.com/legal-entity-id=1jlfDskrR39egznAq3T18Ul0Xxv, api.openshift.com/name=aaraj-hcp, api.openshift.com/nodepool-hypershift=aaraj-hcp-new-m-1p, api.openshift.com/nodepool-ocm=new-m-1p, red-hat-clustertype=rosa
Taints:
Availability zone: us-west-2a
Subnet: subnet-037c1b72c1f86ea04
Version: 4.15.16
Autorepair: Yes
Tuning configs:
Kubelet configs:
Additional security group IDs:
Node drain grace period:
Management upgrade:
- Type: Replace
- Max surge: 2
- Max unavailable: 1
Message: Minimum availability requires 2 replicas, current 0 available
```

## Step
Create a nodepool to the cluster with MaxUnavailable/MaxSurge set with empty value
```bash
rosa create machinepool -c <cluster_name> --max-unavailable "" --max-surge "" --name <mp_name> --replicas 3
```

## Expect
```
I: Checking available instance types for machine pool 'qw'
I: Machine pool 'qw' created successfully on hosted cluster 'aaraj-hcp'
I: To view the machine pool details, run 'rosa describe machinepool --cluster aaraj-hcp --machinepool qw'
I: To view all machine pools, run 'rosa list machinepools --cluster aaraj-hcp'
```

## Step
Check the description of the nodepool, MaxUnavailable/MaxSurge must be set with default value.
```bash
rosa describe machinepool -c <cluster_name> <mp_name>
```

## Expect
```
ID: qw
Cluster ID: 2bs61bvgivf5ehmftkm97190av91mg5s
Autoscaling: No
Desired replicas: 3
Current replicas: 0
Instance type: m5.xlarge
Labels:
Tags: red-hat-clustertype=rosa, red-hat-managed=true, api.openshift.com/environment=staging, api.openshift.com/id=2bs61bvgivf5ehmftkm97190av91mg5s, api.openshift.com/legal-entity-id=1jlfDskrR39egznAq3T18Ul0Xxv, api.openshift.com/name=aaraj-hcp, api.openshift.com/nodepool-hypershift=aaraj-hcp-qw, api.openshift.com/nodepool-ocm=qw
Taints:
Availability zone: us-west-2a
Subnet: subnet-037c1b72c1f86ea04
Version: 4.15.16
Autorepair: Yes
Tuning configs:
Kubelet configs:
Additional security group IDs:
Node drain grace period:
Management upgrade:
- Type: Replace
- Max surge: 1
- Max unavailable: 0
Message: Minimum availability requires 3 replicas, current 0 available
```

## Step
Create/edit nodepool with max-surge or max-unavailable set as 0%
```bash
rosa create machinepool -c aaraj-hcp-1 --name test --version 4.15.2 --replicas 3 --max-surge 0% --max-unavailable 1%
```

## Expect
```
I: Checking available instance types for machine pool 'test'
I: Machine pool 'test' created successfully on hosted cluster 'aaraj-hcp-1'
I: To view the machine pool details, run 'rosa describe machinepool --cluster aaraj-hcp-1 --machinepool test'
I: To view all machine pools, run 'rosa list machinepools --cluster aaraj-hcp-1'
```

## Step
Create/edit nodepool with max-surge or max-unavailable set as 100%
```bash
rosa create machinepool -c aaraj-hcp-1 --name test1 --version 4.15.2 --replicas 3 --max-surge 0% --max-unavailable 100%
```

## Expect
```
I: Checking available instance types for machine pool 'test1'
I: Machine pool 'test1' created successfully on hosted cluster 'aaraj-hcp-1'
I: To view the machine pool details, run 'rosa describe machinepool --cluster aaraj-hcp-1 --machinepool test1'
I: To view all machine pools, run 'rosa list machinepools --cluster aaraj-hcp-1'
```

## Step
Create/edit nodepool with max-surge or max-unavailable set as 0
```bash
rosa create machinepool -c aaraj-hcp-1 --name test2 --version 4.15.2 --replicas 3 --max-surge 0 --max-unavailable 1
```

## Expect
```
I: Checking available instance types for machine pool 'test2'
I: Machine pool 'test2' created successfully on hosted cluster 'aaraj-hcp-1'
I: To view the machine pool details, run 'rosa describe machinepool --cluster aaraj-hcp-1 --machinepool test2'
I: To view all machine pools, run 'rosa list machinepools --cluster aaraj-hcp-1'
```

## Step
Create/edit nodepool with just max surge set or just max unavailable set

## Expect
It should be created/edited successfully
