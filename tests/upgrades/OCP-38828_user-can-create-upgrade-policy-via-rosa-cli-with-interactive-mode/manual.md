# Test

## Step
Log in with the rosa tool, and prepare bellow rosa clusters.  
cluster1: with some available upgrade versions

## Expect

## Step
Try to upgrade the cluster with latest version  
$ rosa upgrade cluster -c <cluster name>

## Expect
[xueli@xueli-work tmp]$ rosa upgrade cluster -c xueli-rosa2  
W: There are no available upgrades

## Step
Try to schedule an upgrade on cluster in low version with interactive mode  
[xueli@xueli-work tmp]$ rosa upgrade cluster -c <cluster name> --interactive

## Expect
- It will go into interactive mode  
- The version should can be selected by arrow up/down  
- The default value for desired date should be the current day  
- The default time should be 10 mins later from current time  
- Node drain also can be selected by arrow up/down  
[xueli@xueli-work tmp]$ rosa upgrade cluster -c xueli-rosa --interactive  
? Version: 4.6.2  
? Please input desired date in format yyyy-mm-dd: 2021-01-26  
? Please input desired UTC time in format HH:mm: 13:03  
? Node draining: 45 minutes  
I: Upgrade successfully scheduled for cluster 'xueli-rosa'

## Step
List the upgrades of the cluster  
$ rosa list upgrade -c <cluster name>

## Expect
- The scheduled time should be correct  
- The version should be correct  
[xueli@xueli-work tmp]$ rosa list upgrade -c xueli-rosa  
VERSION NOTES  
4.6.2 scheduled for 2021-04-11 11:59 UTC  
4.6.1

## Step
Delete the upgrade with command  
$ rosa delete upgrade -c xueli-rosa -y

## Expect

## Step
Run rosa create upgrade   
$ rosa upgrade cluster -c <cluster name>

## Expect
- It will be in interactive mode automatically  
- Only version as selected option  
- The upgrade will be created use the time 10 mins later than current time automaticallly
