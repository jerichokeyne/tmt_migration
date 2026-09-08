# Test

## Step
Prepare one 4.8.x rosa cluster.  
NOTE: There is a version gate for upgrading to the 4.9.x version

## Expect

## Step
Try to upgrade the cluster without adding the gate agreement.

## Expect
If choose 'Y' at the option 'I acknowlegde' , the upgrade should be scheduled successfully.  
[root@yuwan rosa]# ./rosa upgrade cluster -c 1ptvlv52jurnsuibhqfg355tn045ih1c  
? Version: 4.9.11  
W: Missing required acknowledgements to schedule upgrade.   
  
? Read the below description and acknowledge to proceed with upgrade  
- Description: OpenShift removes several Kubernetes APIs in OpenShift 4.9. To help prevent issues with workloads and tools after upgrading, an administrator is required to provide manual acknowledgement before the cluster can be upgraded from OpenShift 4.8 to 4.9.  
URL: https://access.redhat.com/articles/6329921  
  
? I acknowledge Yes  
? Please input desired date in format yyyy-mm-dd: 2022-01-24  
? Please input desired UTC time in format HH:mm: 19:10  
? Node draining: 15 minutes  
W: To check and acknowledge gates prior to scheduling an upgrade, run this command with '--dry-run'  
I: Upgrade successfully scheduled for cluster '1ptvlv52jurnsuibhqfg355tn045ih1c'  
If choose 'N', the rosacli should quit without upgrade scheduled.

## Step
Try to upgrade the cluster with "--dry-run"

## Expect
There is info "I: Upgrading cluster '2koueoefaseah289bb7csu59fuu0pjmu' should succeed. Please wait 1 to 2 minutes, then rerun this command without the '--dry-run' flag, to allow time for the acknowledged agreements to be reflected."

## Step
Repeat step2 with adding the gate agreement manually.

## Expect
There is no 'W: Missing required acknowledgements to schedule upgrade. ' message, and the upgrade should be scheduled.

## Step
Repeat step2~3 on STS cluster.

## Expect
1. rosacli will check the policies compatibility first then check the gate agreement.  
2. others should be same with the results in step2~3

## Step
Prepare 4.9.z cluster then upgrade to 4.10.z

## Expect
- It should succeed.  
- New operator role is created - <prefix>openshift-cloud-network-config-controller-cloud.  
- There is no version gate agreement prompted, that will be done in background.(SDA-5771)
