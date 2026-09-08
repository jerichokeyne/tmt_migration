# Test

## Step
Prepare version like below  
version A has lower version and hcp_enabled:true  
version B with upgrade version and also low versions but hcp_enabled:false  
Channel group: candidate

## Expect

## Step
Create two hosted cluster in  
H1 in version A  
H2 in version higher version than B

## Expect

## Step
DIsable both version A and version B to hcp_enabled:false  
How to prepare a disabled CIS version(Needs a kbase here)

## Expect

## Step
Below steps for H1

## Expect

## Step
Create a nodepool **npc** in interactive mode  
$ rosa create machinepool -c <cluster name> --version <version A> --name npc -i

## Expect
Version A is still listed in interactive mode. Even it is hcp:enabled=false  
And node pool can be created successfully for version A

## Step
Create another nodepool **npu** in lower version than A  
$ rosa create machinepool -c <cluster name> --version <lower version tahn A> --name npc --replicas 1

## Expect
The nodepool will be created successfully

## Step
Create manual upgrade policy to the nodepool  
$ rosa upgrade machinepool npu -c <cluster name> -i

## Expect
Check that version A is listed in the upgrade list and upgrade can be scheduled to the version successfully

## Step
Delete the scheduled manual upgrade policy

## Expect

## Step
Create another automatic upgrade policy to the node pool  
NOTE: automatic can only be created by ocmcli until rosa support it  
$ ocm post /api/clusters_mgmt/v1/clusters/<cluster id>/node_pools/npu/upgrade_policies<<EOF  
{ "kind": "NodePoolUpgradePolicy",  
"schedule": "1 2 * * *",  
"node_pool_id": "xueli-m",  
"schedule_type": "automatic",  
"upgrade_type": "NodePool"}   
EOF

## Expect
The policy should be created  
The version upgrade should be scheduled to A

## Step
Below steps for H2

## Expect

## Step
Create a nodepool to version B in interactive mode

## Expect
The version B can be listed in interactive mode  
And  
the node pool is created successfully

## Step
Upgrade the node pool to cluster version

## Expect
The nodepool will be upgraded successfully

## Step
Create a new nodepool in version lower than B

## Expect
The nodepool will be created successfully

## Step
Create an upgrade policy to the node pool with version B in interactive mode

## Expect
The version B can be listed in interactive mode  
And  
the node pool upgrade policy is created successfully

## Step
Wait for the upgrade finished

## Expect
node pool can be successfully upgraded to version B
