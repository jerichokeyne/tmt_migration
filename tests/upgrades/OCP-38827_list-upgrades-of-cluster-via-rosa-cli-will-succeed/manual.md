# Test

## Step
Launch staging env via rosa cli and prepare a low version cluster

## Expect

## Step
Run command to check the list machine pool help  
$ rosa list upgrades --help

## Expect
[xueli@xueli-work tmp]$ rosa list upgrades -h  
List available and scheduled cluster version upgrades  
  
  
Usage:  
rosa list upgrades [flags]  
  
  
Aliases:  
upgrades, upgrade  
  
  
Flags:  
-c, --cluster string Name or ID of the cluster to list the upgrades of (required).  
-h, --help help for upgrades  
  
  
Global Flags:  
--debug Enable debug mode.  
--profile string Use a specific AWS profile from your credential file.  
-v, --v Level log level for V logs

## Step
Prepare no upgrades and list the upgrades  
$ rosa list upgrades -c <cluster name>

## Expect
- The scheduled upgrades will show with scheduled time  
[xueli@xueli-work tmp]$ rosa list upgrades -c xueli-rosa  
VERSION NOTES  
4.6.2 recommended  
4.6.1

## Step
Create a upgrades policy

## Expect

## Step
Run command to list the upgrade  
$ rosa list upgrades -c <cluster name>

## Expect
- The scheduled upgrades will show with scheduled time  
[xueli@xueli-work tmp]$ rosa list upgrades -c xueli-rosa  
VERSION NOTES  
4.6.2 recommended  
4.6.1 scheduled for 2021-01-26 11:56 UTC

## Step
Wait until the scheduled policy started/delayed  
Run command to list the upgrade  
$ rosa list upgrades -c <cluster name>

## Expect
- The scheduled upgrades will show current status of the policy  
[xueli@xueli-work tmp]$ rosa list upgrades -c xueli-rosa  
VERSION NOTES  
4.6.2 recommended  
4.6.1 started

## Step
Wait until policy upgrade finished/failed  
Wait until the scheduled policy started/delayed  
Run command to list the upgrade  
$ rosa list upgrades -c <cluster name>

## Expect
- The scheduled upgrades policy is deleted  
[xueli@xueli-work tmp]$ rosa list upgrades -c xueli-rosa  
VERSION NOTES  
4.6.2 recommended

## Step
Run command to list the upgrades without cluster set  
$ rosa list upgrades

## Expect
Error: required flag(s) "cluster" not set  
<usage> show

## Step
Run command to list the upgrades invalid flag  
$ rosa list upgrades --interactive

## Expect
[xueli@xueli-work tmp]$ rosa list upgrades --interactive  
Error: unknown flag: --interactive  
Usage:  
rosa list upgrades [flags]  
  
  
Aliases:  
upgrades, upgrade  
  
  
Flags:  
-c, --cluster string Name or ID of the cluster to list the upgrades of (required).  
-h, --help help for upgrades  
  
  
Global Flags:  
--debug Enable debug mode.  
--profile string Use a specific AWS profile from your credential file.  
-v, --v Level log level for V logs  
  
  
Failed to execute root command: unknown flag: --interactive
