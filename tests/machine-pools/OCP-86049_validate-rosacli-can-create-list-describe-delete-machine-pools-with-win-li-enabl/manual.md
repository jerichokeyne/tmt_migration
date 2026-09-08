# Setup
You will need an HCP cluster

# Test

## Step
Creating a machine pool with an invalid instance type will fail`**  
  
` rosa create machinepool -c $CLUSTER_ID --name mp0 --replicas 1 --type Windows --instance-type m5.xlarge**  
  
It will also fail in interactive mode:  
`rosa create machinepool -c $CLUSTER_ID --name mp0 --replicas 1 -i`  
**?****Machine pool name:** mp0   
**?****Image Type (optional, choose 'Skip' to skip selection; ):** Windows   
**?****OpenShift version (default = '4.19.0'):** 4.19.0   
**?****Select subnet for a hosted machine pool:** No   
**?****AWS availability zone (default = 'us-west-2a'):** us-west-2a   
**?****Replicas:** 1   
**?****Labels (optional):**   
**?****Taints (optional):**   
**?****Tags (optional):**   
I: Checking available instance types for machine pool 'mp0'   
**?****Instance type (default = 'm5.xlarge'):** m5.xlarge   
**?****Autorepair:** Yes   
**?****Capacity Reservation ID (optional):**   
**?****Capacity Reservation Preference (optional, choose 'Skip' to skip selection; ):** Skip   
W: No kubelet configs available for cluster '2mltihjs36olg9nqigqgpj251ppjcnd6'. Any kubelet config in input will be ignored   
**?****Configure the use of IMDSv2 for ec2 instances (default = 'optional'):** optional   
**?****Root disk size (GiB or TiB):** 300 GiB   
**?****Node drain grace period (optional):**   
**?****Max surge:** 1   
**?****Max unavailable:** 0   
E: failed to add machine pool to hosted cluster 'jkeyne-1119-10': status is 400, identifier is '400', code is 'CLUSTERS-MGMT-400', at '2025-11-19T22:32:46Z' and operation identifier is 'b4f49aaf-b2fa-418d-8567-  
a4ed1cd84e73': Machine type 'm5.xlarge' does not support Windows License Included. Please select a machine type with Windows LI support

## Expect
`I:` Checking available instance types for machine pool 'mp0'  
E: failed to add machine pool to hosted cluster 'jkeyne-1119-10': status is 400, identifier is '400', code is 'CLUSTERS-MGMT-400', at '2025-11-19T21:19:03Z' and operation identifier is 'e6da684b-8d29-4365-84f6-  
45c642e7273e': Machine type 'm5.xlarge' does not support Windows License Included. Please select a machine type with Windows LI support  
  
To find the list of valid instance types (so you can pick an invalid one) run:  
`**❯` ocm get /api/clusters_mgmt/v1/machine_types -p search="features.win_li = 'true'" | jq -r '.items[].id'**  
c5d.metal  
c5.metal  
c5n.metal  
c6a.metal  
c6id.metal  
c6i.metal  
g4dn.metal  
i3en.metal  
i3.metal  
i4i.metal  
m5d.metal  
m5dn.metal  
m5.metal  
m5n.metal  
m5zn.metal  
m6a.metal  
m6id.metal  
m6i.metal  
r5b.metal  
r5d.metal  
r5dn.metal  
r5.metal  
r5n.metal  
r6a.metal  
r6id.metal  
r6i.metal  
u-12tb1.metal  
u-18tb1.metal  
u-24tb1.metal  
u-6tb1.metal  
u-9tb1.metal  
x2idn.metal  
x2iedn.metal  
x2iezn.metal  
z1d.metal  
(remove the "jq" part of the command to get the full output with specs and descriptions if needed)

## Step
Specifying an image type of anything other than "Windows" or "Default" will fail: 
  1. `rosa create machinepool -c $CLUSTER_ID --name mp0 --replicas 1 --instance-type c5d.metal --type 'invalid'`
     1. Can't specify an invalid type
  2. `rosa create machinepool -c $CLUSTER_ID --name mp0 --replicas 1 --instance-type c5d.metal --type 'Skip'`
     1. Can't use the "Skip" option that is allowed in interactive mode
  3. `rosa create machinepool -c $CLUSTER_ID --name mp0 --replicas 1 --instance-type c5d.metal --type 'windows'`
     1. Can't use a valid option that is all lower case
  4. `rosa create machinepool -c $CLUSTER_ID --name mp0 --replicas 1 --instance-type c5d.metal --type 'DEFAULT'`
     1. Can't use a valid option that is all upper case

## Expect
1. `E:` invalid image type: 'invalid' - please use one of: 'Default', 'Windows'
  2. `E:` invalid image type: 'Skip' - please use one of: 'Default', 'Windows'
  3. `E:` invalid image type: 'windows' - please use one of: 'Default', 'Windows'
  4. `E:` invalid image type: 'DEFAULT' - please use one of: 'Default', 'Windows'
