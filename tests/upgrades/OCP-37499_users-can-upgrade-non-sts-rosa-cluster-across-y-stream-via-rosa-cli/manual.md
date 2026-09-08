# Test

## Step
Log in with the rosa tool, and prepare bellow rosa clusters.  
cluster1: with some available upgrade versions and machinepool  
cluster2: without any available upgrade versions

## Expect

## Step
Check the help message for 'upgrade cluster'  
$ rosa upgrade cluster -h

## Expect
- Description is correct and clear  
- No typo error  
[xueli@xueli-work tmp]$ rosa upgrade cluster -h  
Upgrade cluster to a new available version  
  
  
Usage:  
rosa upgrade cluster [flags]  
  
  
Examples:  
\# Interactively schedule an upgrade on the cluster named "mycluster"  
rosa upgrade cluster --cluster=mycluster --interactive  
  
  
\# Schedule a cluster upgrade within the hour  
rosa upgade cluster -c mycluster --version 4.5.20  
  
  
Flags:  
-c, --cluster string Name or ID of the cluster to schedule the upgrade for (required)  
--version string Version of OpenShift that the cluster will be upgraded to  
--schedule-date string Next date the upgrade should run at the specified time. Format should be 'yyyy-mm-dd'  
--schedule-time string Next time the upgrade should run on the specified date. Format should be 'HH:mm'  
--node-drain-grace-period string You may set a grace period for how long Pod Disruption Budget-protected workloads will be respected during upgrades.  
After this grace period, any workloads protected by Pod Disruption Budgets that have not been successfully drained from a node will be forcibly evicted (default "1 hour")  
-h, --help help for cluster  
  
  
Global Flags:  
--debug Enable debug mode.  
-i, --interactive Enable interactive mode.  
--profile string Use a specific AWS profile from your credential file.  
-v, --v Level log level for V logs

## Step
Try to upgrade the cluster with latest version  
$ rosa upgrade cluster -c <cluster name>

## Expect
[xueli@xueli-work tmp]$ rosa upgrade cluster -c xueli-rosa2  
W: There are no available upgrades

## Step
Try to schedule an upgrade on cluster in low version  
[xueli@xueli-work tmp]$ rosa upgrade cluster -c <cluster name> --version 4.6.2 --schedule-date <date> --schedule-time <time> --node-drain-grace-period "<drain time> minutes"

## Expect
[xueli@xueli-work tmp]$ rosa upgrade cluster -c xueli-rosa --version 4.6.2 --schedule-date 2021-04-11 --schedule-time 11:59  
I: Upgrade successfully scheduled for cluster 'xueli-rosa'

## Step
List the upgrades of the cluster  
$ rosa list upgrades -c <cluster name>

## Expect
- The scheduled time should be correct  
- The version should be correct  
[xueli@xueli-work tmp]$ rosa list upgrade -c xueli-rosa  
VERSION NOTES  
4.6.2 scheduled for 2021-04-11 11:59 UTC  
4.6.1   
- The upgrade status should be shown correctly (pending->scheduled->started)

## Step
Verify whether cluster with machine pool can be upgrade successfully

## Expect
Cluster with machine pool can be upgrade successfully
