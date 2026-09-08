# Test

## Step
Prepare a hosted cluster with machine pool version those can be upgraded

## Expect

## Step
Prepare a manual policy

## Expect

## Step
Check the help information  
./rosa list upgrade --help  
./rosa describe upgrade --help  
./rosa delete upgrade --help

## Expect
-There will be an option for machinepool  
--machinepool string Machine pool of the cluster to target

## Step
Describe machinepool to check the upgrade policies  
rosa describe machinepool -c CLUSTER1 --machinepool MPNAME

## Expect
-It should contail upgrade information  
./rosa describe machinepool workers-0 -c sdq-ci-xoccc  
  
ID: workers-0  
Cluster ID: 26dbcaqd8772osav95kgbtu71j6198m2  
Autoscaling: Yes  
Desired replicas: 1-2  
Current replicas: 1  
Instance type: m5.xlarge  
Labels:   
Taints:   
Availability zone: us-west-2a  
Subnet: subnet-020998166dcb99132  
Version: 4.13.11  
Autorepair: Yes  
Tuning configs:   
Message:   
Scheduled upgrade: pending 4.13.12 on 2023-09-22 09:46 UTC

## Step
Describe the upgrade policies  
./rosa describe upgrade --machinepool mp-3 --cluster ying-up1

## Expect
-If not upgrade policy,it will return an information  
I: No scheduled upgrades for machine pool 'mp-3' in cluster 'ying-up1'  
-If there is policies for the machine pool  
./rosa describe upgrade --machinepool mp-3 --cluster ying-up1  
ID: d9f3042b-3539-11ef-a1ef-0a580a8303c3  
Cluster ID: 2c620qiq7i5u5ovvrtop9rggf7isto2s  
Schedule Type: manual  
Next Run: 2024-06-28 10:43 UTC  
Upgrade State: pending  
State Message: Upgrade policy defined, pending scheduling.  
  
  
Version: 4.16.1

## Step
List the upgrade policies  
./rosa list upgrade --machinepool mp-3 --cluster ying-up1

## Expect
-The listed version should be same with the nodePool.version.available_upgrades  
-If there is no upgrade policy for it, it will not show "scheduled for 2023-09-13 09:00 UTC"   
./rosa list upgrade --machinepool mp-3 --cluster ying-up1  
VERSION NOTES  
4.13.10 recommended  
4.12.31   
4.12.30   
4.12.29   
4.12.28 scheduled for 2023-09-13 09:00 UTC

## Step
Delete the upgrade policies  
./rosa delete upgrade --machinepool mp-3 --cluster ying-up1

## Expect
-If not set "-y", it will promote with a confirmation infor  
[yingzhan@localhost rosa]$ ./rosa delete upgrade --machinepool mp-3 --cluster ying-up1  
? Are you sure you want to cancel scheduled upgrade on machine pool 'mp-3'? Yes  
I: Successfully canceled scheduled upgrade for machine pool 'mp-3' for cluster 'ying-up1'  
-If there is no upgrade policies  
I: There are no scheduled upgrades for machine pool 'mp-3' for cluster 'ying-up1'

## Step
Repeat above steps with automatic upgrade policy

## Expect
