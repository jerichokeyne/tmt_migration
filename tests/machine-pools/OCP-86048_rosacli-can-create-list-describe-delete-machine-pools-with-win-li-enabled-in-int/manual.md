# Setup
- You will need an HCP cluster
  - Pick an instance type that will support Win-LI: `ocm get /api/clusters_mgmt/v1/machine_types -p search="features.win_li = 'true'" | jq -r '.items[].id'`

# Test

## Step
1. You can create a machine pool and skip the image type

`**?` Image Type (optional, choose 'Skip' to skip selection; ):** [Use arrows to move, type to filter]
**> Skip**
Default
Windows

**❯ rosa create machinepool -c $CLUSTER_ID -i**
? Machine pool name: mp0
? Image Type (optional, choose 'Skip' to skip selection; ): Skip
? OpenShift version (default = '4.19.0'): 4.19.0
? Select subnet for a hosted machine pool: No
? AWS availability zone (default = 'us-west-2a'): us-west-2a
? Enable autoscaling: No
? Replicas: 1
? Labels (optional):
? Taints (optional):
? Tags (optional):
```
I: Checking available instance types for machine pool 'mp0'
? Instance type (default = 'm5.xlarge'): m5.xlarge
? Autorepair: Yes
? Capacity Reservation ID (optional):
? Capacity Reservation Preference (optional, choose 'Skip' to skip selection; ): Skip
W: No kubelet configs available for cluster '2mltihjs36olg9nqigqgpj251ppjcnd6'. Any kubelet config in input will be ignored
? Configure the use of IMDSv2 for ec2 instances (default = 'optional'): optional
? Root disk size (GiB or TiB): 300 GiB
? Node drain grace period (optional):
? Max surge: 1
? Max unavailable: 0
I: Machine pool 'mp0' created successfully on hosted cluster 'jkeyne-1119-10'
I: To view the machine pool details, run 'rosa describe machinepool --cluster jkeyne-1119-10 --machinepool mp0'
I: To view all machine pools, run 'rosa list machinepools --cluster jkeyne-1119-10'
```

## Expect
The machine pool is created successfully, and you can describe the machine pool

`**❯` rosa describe machinepool --cluster $CLUSTER_ID mp0**
`ID: mp0`
```
Cluster ID: 2mltihjs36olg9nqigqgpj251ppjcnd6
Autoscaling: No
Desired replicas: 1
Current replicas: 0
Instance type: m5.xlarge
Image type: Default
Labels:
Tags: api.openshift.com/environment=staging, api.openshift.com/id=2mltihjs36olg9nqigqgpj251ppjcnd6, api.openshift.com/legal-entity-id=2wLZWMFZgGEBkd1MBfJPtHTFSJZ, api.openshift.
com/name=jkeyne-1119-10, api.openshift.com/nodepool-hypershift=jkeyne-1119-10-mp0, api.openshift.com/nodepool-ocm=mp0, red-hat-clustertype=rosa, red-hat-managed=true
Taints:
Availability zone: us-west-2a
Subnet: subnet-056cd6f207b3d4b96
Disk Size: 300 GiB
Version: 4.19.0
EC2 Metadata Http Tokens: optional
Autorepair: Yes
Tuning configs:
Kubelet configs:
Additional security group IDs:
Node drain grace period:
Capacity Reservation:
Management upgrade:
- Type: Replace
- Max surge: 1
- Max unavailable: 0
Message: Minimum availability requires 1 replicas, current 0 available
```

You can also query the API to confirm the image type: `
` `**❯` ocm get /api/clusters_mgmt/v1/clusters/2mltihjs36olg9nqigqgpj251ppjcnd6/node_pools/mp0 | jq -r .image_type**
Default

## Step
2. You can create a machine pool with the type "Default"

`**?` Image Type (optional, choose 'Skip' to skip selection; ):** [Use arrows to move, type to filter]
Skip
**> Default**
Windows

**❯ rosa create machinepool -c $CLUSTER_ID -i**
? Machine pool name: mp1
? Image Type (optional, choose 'Skip' to skip selection; ): Default
? OpenShift version (default = '4.19.0'): 4.19.0
? Select subnet for a hosted machine pool: No
? AWS availability zone (default = 'us-west-2a'): us-west-2a
? Enable autoscaling: No
? Replicas: 1
? Labels (optional):
? Taints (optional):
? Tags (optional):
```
I: Checking available instance types for machine pool 'mp1'
? Instance type (default = 'm5.xlarge'): m5.xlarge
? Autorepair: Yes
? Capacity Reservation ID (optional):
? Capacity Reservation Preference (optional, choose 'Skip' to skip selection; ): Skip
W: No kubelet configs available for cluster '2mltihjs36olg9nqigqgpj251ppjcnd6'. Any kubelet config in input will be ignored
? Configure the use of IMDSv2 for ec2 instances (default = 'optional'): optional
? Root disk size (GiB or TiB): 300 GiB
? Node drain grace period (optional):
? Max surge: 1
? Max unavailable: 0
I: Machine pool 'mp1' created successfully on hosted cluster 'jkeyne-1119-10'
I: To view the machine pool details, run 'rosa describe machinepool --cluster jkeyne-1119-10 --machinepool mp1'
I: To view all machine pools, run 'rosa list machinepools --cluster jkeyne-1119-10'
```

## Expect
The machine pool is created successfully, and you can describe the machine pool

`**❯` rosa describe machinepool --cluster $CLUSTER_ID mp0**
`ID: mp1`
```
Cluster ID: 2mltihjs36olg9nqigqgpj251ppjcnd6
Autoscaling: No
Desired replicas: 1
Current replicas: 0
Instance type: m5.xlarge
Image type: Default
Labels:
Tags: api.openshift.com/name=jkeyne-1119-10, api.openshift.com/nodepool-hypershift=jkeyne-1119-10-mp1, api.openshift.com/nodepool-ocm=mp1, red-hat-clustertype=rosa, red-hat-mana
ged=true, api.openshift.com/environment=staging, api.openshift.com/id=2mltihjs36olg9nqigqgpj251ppjcnd6, api.openshift.com/legal-entity-id=2wLZWMFZgGEBkd1MBfJPtHTFSJZ
Taints:
Availability zone: us-west-2a
Subnet: subnet-056cd6f207b3d4b96
Disk Size: 300 GiB
Version: 4.19.0
EC2 Metadata Http Tokens: optional
Autorepair: Yes
Tuning configs:
Kubelet configs:
Additional security group IDs:
Node drain grace period:
Capacity Reservation:
Management upgrade:
- Type: Replace
- Max surge: 1
- Max unavailable: 0
Message: Minimum availability requires 1 replicas, current 0 available
```

You can also query the API to confirm the image type: `
**❯` ocm get /api/clusters_mgmt/v1/clusters/2mltihjs36olg9nqigqgpj251ppjcnd6/node_pools/mp1 | jq -r .image_type**
Default

## Step
3. You can create a machine pool with the type "Windows"

```bash
rosa create machinepool -c $CLUSTER_ID -i
```

`**?` Image Type (optional, choose 'Skip' to skip selection; ):** [Use arrows to move, type to filter]
Skip
Default
**> Windows**

`**❯` rosa create machinepool -c $CLUSTER_ID -i**
**?** **Machine pool name:** mp2
**?** **Image Type (optional, choose 'Skip' to skip selection; ):** Windows
**?** **OpenShift version (default = '4.19.0'):** 4.19.0
**?** **Select subnet for a hosted machine pool:** No
**?** **AWS availability zone (default = 'us-west-2a'):** us-west-2a
**?** **Enable autoscaling:** No
**?** **Replicas:** 1
**?** **Labels (optional):**
**?** **Taints (optional):**
**?** **Tags (optional):**
```
I: Checking available instance types for machine pool 'mp2'
**?** **Instance type (default = 'm5.xlarge'):** c5.metal
**?** **Autorepair:** Yes
**?** **Capacity Reservation ID (optional):**
**?** **Capacity Reservation Preference (optional, choose 'Skip' to skip selection; ):** Skip
W: No kubelet configs available for cluster '2mltihjs36olg9nqigqgpj251ppjcnd6'. Any kubelet config in input will be ignored
**?** **Configure the use of IMDSv2 for ec2 instances (default = 'optional'):** optional
**?** **Root disk size (GiB or TiB):** 300 GiB
**?** **Node drain grace period (optional):**
**?** **Max surge:** 1
**?** **Max unavailable:** 0
I: Machine pool 'mp2' created successfully on hosted cluster 'jkeyne-1119-10'
I: To view the machine pool details, run 'rosa describe machinepool --cluster jkeyne-1119-10 --machinepool mp2'
I: To view all machine pools, run 'rosa list machinepools --cluster jkeyne-1119-10'
```

When you pick the instance type, it should be limited to just valid instance types
`**?` Instance type (default = 'm5.xlarge'):** [Use arrows to move, type to filter, ? for more help]
**> g4dn.metal**
c5d.metal
c5.metal
c5n.metal
c6a.metal
c6id.metal
c6i.metal`
`

## Expect
The machine pool is created successfully, and you can describe the machine pool

`**❯` rosa describe machinepool --cluster $CLUSTER_ID mp2**
```
ID: mp2
Cluster ID: 2mltihjs36olg9nqigqgpj251ppjcnd6
Autoscaling: No
Desired replicas: 1
Current replicas: 0
Instance type: c5.metal
Image type: Windows
Labels:
Tags: api.openshift.com/name=jkeyne-1119-10, api.openshift.com/nodepool-hypershift=jkeyne-1119-10-mp2, api.openshift.com/nodepool-ocm=mp2, red-hat-clustertype=rosa, red-hat-mana
ged=true, api.openshift.com/environment=staging, api.openshift.com/id=2mltihjs36olg9nqigqgpj251ppjcnd6, api.openshift.com/legal-entity-id=2wLZWMFZgGEBkd1MBfJPtHTFSJZ
Taints:
Availability zone: us-west-2a
Subnet: subnet-056cd6f207b3d4b96
Disk Size: 300 GiB
Version: 4.19.0
EC2 Metadata Http Tokens: optional
Autorepair: Yes
Tuning configs:
Kubelet configs:
Additional security group IDs:
Node drain grace period:
Capacity Reservation:
Management upgrade:
- Type: Replace
- Max surge: 1
- Max unavailable: 0
Message: WaitingForAvailableMachines
```

You can also query the API to confirm the image type: `
**❯` ocm get /api/clusters_mgmt/v1/clusters/2mltihjs36olg9nqigqgpj251ppjcnd6/node_pools/mp2 | jq -r .image_type **
Windows

While Win-LI is in technology preview, you should also see this warning show up after selecting the image type:
`**?` Image Type (optional, choose 'Skip' to skip selection; ): Windows
```
W:** Technology Preview Message for Windows LI: Windows License Included (LI) AMI support for ROSA HCP node pools
```

## Step
4. You can create a machine pool with the Windows image type, and autoscaling enabled

`**❯` rosa create machinepool -c $CLUSTER_ID -i**
`? Machine pool name:` mp3
? Image Type (optional, choose 'Skip' to skip selection; ): Windows
? OpenShift version (default = '4.19.0'): 4.19.0
? Select subnet for a hosted machine pool: No
? AWS availability zone (default = 'us-west-2a'): us-west-2a
? Enable autoscaling: Yes
? Min replicas: 1
? Max replicas: 6
? Labels (optional):
? Taints (optional):
? Tags (optional):
```
I: Checking available instance types for machine pool 'mp3'
? Instance type (default = 'm5.xlarge'): c5.metal
? Autorepair: Yes
W: No kubelet configs available for cluster '2mltihjs36olg9nqigqgpj251ppjcnd6'. Any kubelet config in input will be ignored
? Configure the use of IMDSv2 for ec2 instances (default = 'optional'): optional
? Root disk size (GiB or TiB): 300 GiB
? Node drain grace period (optional):
? Max surge: 1
? Max unavailable: 0
I: Machine pool 'mp3' created successfully on hosted cluster 'jkeyne-1119-10'
I: To view the machine pool details, run 'rosa describe machinepool --cluster jkeyne-1119-10 --machinepool mp3'
I: To view all machine pools, run 'rosa list machinepools --cluster jkeyne-1119-10'
```

## Expect
The machine pool is created successfully, and you can describe the machine pool

`**❯` rosa describe machinepool --cluster $CLUSTER_ID mp3**
```
ID: mp3
Cluster ID: 2mltihjs36olg9nqigqgpj251ppjcnd6
Autoscaling: Yes
Desired replicas:
- Min replicas: 1
- Max replicas: 6
Current replicas: 0
Instance type: c5.metal
Image type: Windows
Labels:
Tags: api.openshift.com/name=jkeyne-1119-10, api.openshift.com/nodepool-hypershift=jkeyne-1119-10-mp3, api.openshift.com/nodepool-ocm=mp3, red-hat-clustertype=rosa, red-hat-mana
ged=true, api.openshift.com/environment=staging, api.openshift.com/id=2mltihjs36olg9nqigqgpj251ppjcnd6, api.openshift.com/legal-entity-id=2wLZWMFZgGEBkd1MBfJPtHTFSJZ
Taints:
Availability zone: us-west-2a
Subnet: subnet-056cd6f207b3d4b96
Disk Size: 300 GiB
Version: 4.19.0
EC2 Metadata Http Tokens: optional
Autorepair: Yes
Tuning configs:
Kubelet configs:
Additional security group IDs:
Node drain grace period:
Capacity Reservation:
Management upgrade:
- Type: Replace
- Max surge: 1
- Max unavailable: 0
Message: WaitingForAvailableMachines
```

You can also query the API to confirm the image type: `
**❯` ocm get /api/clusters_mgmt/v1/clusters/2mltihjs36olg9nqigqgpj251ppjcnd6/node_pools/mp3 | jq -r .image_type **
Windows

## Step
5. The machine pools show up when you list them

```bash
rosa list machinepools --cluster $CLUSTER_ID
```

## Expect
You can view all the machine pools you created

`**❯` rosa list machinepools --cluster $CLUSTER_ID**
```
ID AUTOSCALING REPLICAS INSTANCE TYPE LABELS TAINTS AVAILABILITY ZONE SUBNET DISK SIZE VERSION AUTOREPAIR
mp0 No 1/1 m5.xlarge us-west-2a subnet-056cd6f207b3d4b96 300 GiB 4.19.0 Yes
mp1 No 0/1 m5.xlarge us-west-2a subnet-056cd6f207b3d4b96 300 GiB 4.19.0 Yes
mp2 No 0/1 c5.metal us-west-2a subnet-056cd6f207b3d4b96 300 GiB 4.19.0 Yes
mp3 Yes 0/1-6 c5.metal us-west-2a subnet-056cd6f207b3d4b96 300 GiB 4.19.0 Yes
workers No 2/2 m5.xlarge us-west-2a subnet-056cd6f207b3d4b96 300 GiB 4.19.0 Yes
```

## Step
6. You can delete all the machine pools

  1. `rosa delete machinepool -c $CLUSTER_ID mp0`
  2. `rosa delete machinepool -c $CLUSTER_ID mp1`
  3. `rosa delete machinepool -c $CLUSTER_ID mp2`
  4. `rosa delete machinepool -c $CLUSTER_ID mp3`

## Expect
All machine pools are deleted successfully

  1. `**?` Are you sure you want to delete machine pool 'mp0' on hosted cluster 'jkeyne-1119-10'?** Yes
```
I: Successfully deleted machine pool 'mp0' from hosted cluster 'jkeyne-1119-10'
  2. `**?` Are you sure you want to delete machine pool 'mp1' on hosted cluster 'jkeyne-1119-10'?** Yes
I: Successfully deleted machine pool 'mp1' from hosted cluster 'jkeyne-1119-10'
  3. `**?` Are you sure you want to delete machine pool 'mp2' on hosted cluster 'jkeyne-1119-10'?** Yes
I: Successfully deleted machine pool 'mp2' from hosted cluster 'jkeyne-1119-10'
  4. `**?` Are you sure you want to delete machine pool 'mp3' on hosted cluster 'jkeyne-1119-10'?** Yes
I: Successfully deleted machine pool 'mp3' from hosted cluster 'jkeyne-1119-10'
```
