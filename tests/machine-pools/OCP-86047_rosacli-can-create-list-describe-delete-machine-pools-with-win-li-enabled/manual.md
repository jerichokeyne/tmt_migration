# Setup
- You will need an HCP cluster
  - Pick an instance type that will support Win-LI: `ocm get /api/clusters_mgmt/v1/machine_types -p search="features.win_li = 'true'" | jq -r '.items[].id'`

# Test

## Step
1. The help message shows the "--type" option

```bash
rosa create machinepool --help
```

## Expect
```
❯ rosa create machinepool -h
Add a machine pool to the cluster.

...
      --type string   Specifies the image type used by Hosted Control Plane machine pools. Use '--type Windows' to create a machine pool that uses a Windows image.
...

Global Flags:
      --color string     Surround certain characters with escape sequences to display them in color on the terminal. Allowed options are [auto never always] (default "auto")
      --debug            Enable debug mode.
      --profile string   Use a specific AWS profile from your credential file.
      --region string    Use a specific AWS region, overriding the AWS_REGION environment variable.
  -y, --yes              Automatically answer yes to confirm operation.
```

## Step
1. You can create a machine pool with type "Windows"

`rosa create machinepool -c $CLUSTER_ID --name mp0 --replicas 1 --type Windows --instance-type c6i.met`al`
`

## Expect
`I: Checking available instance types for machine pool 'mp0'`
```
I: Machine pool 'mp0' created successfully on hosted cluster 'jkeyne-1119-10'
I: To view the machine pool details, run 'rosa describe machinepool --cluster jkeyne-1119-10 --machinepool mp0'
I: To view all machine pools, run 'rosa list machinepools --cluster jkeyne-1119-10'
```

You can view the details of the machine pool:
$ `rosa describe machinepool -c $CLUSTER_ID mp0`
`ID: mp0
```
Cluster ID: 2mltihjs36olg9nqigqgpj251ppjcnd6
Autoscaling: No
Desired replicas: 1
Current replicas: 0
Instance type: c6i.metal
Image type: Windows`
Labels:
Tags: red-hat-managed=true, api.openshift.com/environment=staging, api.openshift.com/id=2mltihjs36olg9nqigqgpj251ppjcnd6, api.openshift.com/legal-entity-id=2wLZWMFZgGEBkd1MBfJPt
HTFSJZ, api.openshift.com/name=jkeyne-1119-10, api.openshift.com/nodepool-hypershift=jkeyne-1119-10-mp0, api.openshift.com/nodepool-ocm=mp0, red-hat-clustertype=rosa
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
Message: WaitingForAvailableMachines`
```

` You can also verify it via the API with this command:
`**❯` ocm get /api/clusters_mgmt/v1/clusters/2mltihjs36olg9nqigqgpj251ppjcnd6/node_pools/mp0 | jq -r .image_type
Windows**`
`

## Step
2. You can create a machine pool with type "Default"

```bash
rosa create machinepool -c $CLUSTER_ID --name mp1 --replicas 1 --type Default
```

## Expect
`I:` Checking available instance types for machine pool 'mp1'
```
I: Machine pool 'mp1' created successfully on hosted cluster 'jkeyne-1119-10'
I: To view the machine pool details, run 'rosa describe machinepool --cluster jkeyne-1119-10 --machinepool mp1'
I: To view all machine pools, run 'rosa list machinepools --cluster jkeyne-1119-10'
```

You can view the details of the machine pool:
$ `rosa describe machinepool -c $CLUSTER_ID mp1
```
ID: mp1
Cluster ID: 2mltihjs36olg9nqigqgpj251ppjcnd6
Autoscaling: No
Desired replicas: 1
Current replicas: 0
Instance type: m5.xlarge
Image type: Default`
Labels:
Tags: api.openshift.com/id=2mltihjs36olg9nqigqgpj251ppjcnd6, api.openshift.com/legal-entity-id=2wLZWMFZgGEBkd1MBfJPtHTFSJZ, api.openshift.com/name=jkeyne-1119-10, api.openshift.
com/nodepool-hypershift=jkeyne-1119-10-mp1, api.openshift.com/nodepool-ocm=mp1, red-hat-clustertype=rosa, red-hat-managed=true, api.openshift.com/environment=staging
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

## Step
3. You can create a machine pool without specifying a type

```bash
rosa create machinepool -c $CLUSTER_ID --name mp2 --replicas 1
```

## Expect
`I: Checking available instance types for machine pool 'mp2'`
```
I: Machine pool 'mp2' created successfully on hosted cluster 'jkeyne-1119-10'
I: To view the machine pool details, run 'rosa describe machinepool --cluster jkeyne-1119-10 --machinepool mp2'
I: To view all machine pools, run 'rosa list machinepools --cluster jkeyne-1119-10'
```

You can view the details of the machine pool:
$ `rosa describe machinepool -c $CLUSTER_ID mp2
```
ID: mp2`
Cluster ID: 2mltihjs36olg9nqigqgpj251ppjcnd6
Autoscaling: No
Desired replicas: 1
Current replicas: 0
Instance type: m5.xlarge
Image type: Default
Labels:
Tags: api.openshift.com/id=2mltihjs36olg9nqigqgpj251ppjcnd6, api.openshift.com/legal-entity-id=2wLZWMFZgGEBkd1MBfJPtHTFSJZ, api.openshift.com/name=jkeyne-1119-10, api.openshift.
com/nodepool-hypershift=jkeyne-1119-10-mp2, api.openshift.com/nodepool-ocm=mp2, red-hat-clustertype=rosa, red-hat-managed=true, api.openshift.com/environment=staging
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

## Step
4. You can create a machine pool with both a type set and autoscaling enabled

$ `rosa create machinepool -c $CLUSTER_ID --name mp3 --enable-autoscaling --min-replicas 1 --max-replicas 6 --type Windows --instance-type c6i.metal
`
```bash
rosa create machinepool -c $CLUSTER_ID --name mp4 --enable-autoscaling --min-replicas 1 --max-replicas 6 --type Default
```

## Expect
`I: Checking available instance types for machine pool 'mp3'`
```
I: Machine pool 'mp3' created successfully on hosted cluster 'jkeyne-1119-10'
I: To view the machine pool details, run 'rosa describe machinepool --cluster jkeyne-1119-10 --machinepool mp3'
I: To view all machine pools, run 'rosa list machinepools --cluster jkeyne-1119-10'
```

You can view the details of the machine pool:
$ `rosa describe machinepool -c $CLUSTER_ID mp3
```
ID: mp3
Cluster ID: 2mltihjs36olg9nqigqgpj251ppjcnd6
Autoscaling: Yes
Desired replicas:
- Min replicas: 1`
- Max replicas: 6
Current replicas: 0
Instance type: c6i.metal
Image type: Windows
Labels:
Tags: api.openshift.com/id=2mltihjs36olg9nqigqgpj251ppjcnd6, api.openshift.com/legal-entity-id=2wLZWMFZgGEBkd1MBfJPtHTFSJZ, api.openshift.com/name=jkeyne-1119-10, api.openshift.
com/nodepool-hypershift=jkeyne-1119-10-mp3, api.openshift.com/nodepool-ocm=mp3, red-hat-clustertype=rosa, red-hat-managed=true, api.openshift.com/environment=staging
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


```
I: Checking available instance types for machine pool 'mp4'
I: Machine pool 'mp4' created successfully on hosted cluster 'jkeyne-1119-10'
I: To view the machine pool details, run 'rosa describe machinepool --cluster jkeyne-1119-10 --machinepool mp4'
I: To view all machine pools, run 'rosa list machinepools --cluster jkeyne-1119-10'
```

You can view the details of the machine pool:
$ `rosa describe machinepool -c $CLUSTER_ID mp4
```
ID: mp4`
Cluster ID: 2mltihjs36olg9nqigqgpj251ppjcnd6
Autoscaling: Yes
Desired replicas:
- Min replicas: 1
- Max replicas: 6
Current replicas: 0
Instance type: m5.xlarge
Image type: Default
Labels:
Tags: red-hat-managed=true, api.openshift.com/environment=staging, api.openshift.com/id=2mltihjs36olg9nqigqgpj251ppjcnd6, api.openshift.com/legal-entity-id=2wLZWMFZgGEBkd1MBfJPt
HTFSJZ, api.openshift.com/name=jkeyne-1119-10, api.openshift.com/nodepool-hypershift=jkeyne-1119-10-mp4, api.openshift.com/nodepool-ocm=mp4, red-hat-clustertype=rosa
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

## Step
5. You can list the machine pools created

```bash
rosa list machinepools -c $CLUSTER_ID
```

## Expect
`ID AUTOSCALING REPLICAS INSTANCE TYPE LABELS TAINTS AVAILABILITY ZONE SUBNET DISK SIZE VERSION AUTOREPAIR `
mp0 No 0/1 c6i.metal us-west-2a subnet-056cd6f207b3d4b96 300 GiB 4.19.0 Yes
mp1 No 0/1 m5.xlarge us-west-2a subnet-056cd6f207b3d4b96 300 GiB 4.19.0 Yes
mp2 No 0/1 m5.xlarge us-west-2a subnet-056cd6f207b3d4b96 300 GiB 4.19.0 Yes
mp3 Yes 0/1-6 c6i.metal us-west-2a subnet-056cd6f207b3d4b96 300 GiB 4.19.0 Yes
mp4 Yes 0/1-6 m5.xlarge us-west-2a subnet-056cd6f207b3d4b96 300 GiB 4.19.0 Yes
workers No 2/2 m5.xlarge us-west-2a subnet-056cd6f207b3d4b96 300 GiB 4.19.0 Yes

## Step
6. You can delete all the machine pools you created

  1. `rosa delete machinepool -c $CLUSTER_ID mp0`
  2. `rosa delete machinepool -c $CLUSTER_ID mp1`
  3. `rosa delete machinepool -c $CLUSTER_ID mp2`
  4. `rosa delete machinepool -c $CLUSTER_ID mp3`
  5. `rosa delete machinepool -c $CLUSTER_ID mp4`

## Expect
`**?` Are you sure you want to delete machine pool 'mp0' on hosted cluster 'jkeyne-1119-10'?** Yes
```
I: Successfully deleted machine pool 'mp0' from hosted cluster 'jkeyne-1119-10'
```
