# Test

## Step
Prepare a hosted cluster with latest version

## Expect

## Step
List upgrades for current node pool  
  
[OCM-4512](<https://issues.redhat.com/browse/OCM-4512>)

## Expect
No upgrade should be available for the machine pools  
  
$ rosa list upgrades -c <cluster_name> --machinepool workers  
I: There are no available upgrades for machine pool 'workers'

## Step
Prepare a machinepool with available upgrade

## Expect

## Step
Try to upgrade the machine pool with manual mode with no date  
$ ./rosa upgrade machinepool mp-3 --cluster ying-up1 --version 4.12.28 -y

## Expect
The upgrade should be scheduled in the next 10 minutes  
./rosa describe upgrade --machinepool mp-3 --cluster ying-up1  
ID: d9f3042b-3539-11ef-a1ef-0a580a8303c3  
Cluster ID: 2c620qiq7i5u5ovvrtop9rggf7isto2s  
Schedule Type: manual  
Next Run: 2024-06-28 10:43 UTC  
Upgrade State: pending  
State Message: Upgrade policy defined, pending scheduling.  
  
  
Version: 4.16.1

## Step
Check the upgrade policy "Upgrade State"

## Expect
- Upgrade State will be pending--scheduled--started  
- The machine pool can be upgraded to the target version  
- If it is an automatic upgrade, the policy will be update to the next run and the version will be empty if there is no latest version(z-stream)/Upgrade State will be set to pending  
- If it is a manual upgrade, the policy will be delete

## Step
Repeat all above step on different OS

## Expect
result should be same
