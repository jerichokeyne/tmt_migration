# Setup
[SDA-8472] Upgrade hypershift cluster via rosacli

# Test

## Step
Log in with the rosa tool, and prepare bellow hypershift clusters.  
cluster1: with some available upgrade versions  
cluster2: without any available upgrade versions

## Expect

## Step
Check the help message for 'upgrade cluster'  
$ rosa upgrade cluster -h

## Expect
- Description is correct and clear  
- There is "--control-plane For Hosted Control Plane, whether the upgrade should cover only the control plane"

## Step
Try to upgrade the cluster with latest version  
$ rosa upgrade cluster -c <cluster name> --control-plane

## Expect
- The interactive mode should work well(Will move to a separated TC in future)  
- The date and time can work  
- If there is version gate, it should work well as classic clusters  
- If there is any new add roles, it should ask for upgrade operator-roles(no new add role from 4.12.z to 4.13.z now)

## Step
List the upgrades of the cluster  
$ rosa list upgrades -c <cluster name>

## Expect
- The scheduled time should be correct  
- The version should be correct  
-The default version will be the recommended if it is available for upgrade   
example:  
[xueli@xueli-work tmp]$ rosa list upgrade -c xueli-rosa  
VERSION NOTES  
4.6.2 scheduled for 2021-04-11 11:59 UTC  
4.6.1   
- The upgrade status should be shown correctly (pending->scheduled->started)

## Step
Check the node drain by describe cluster  
$ rosa describe cluster -c <cluster name>

## Expect
- The node drain should be changed to the value set in the command  
- The upgrade status should be shown correctly (pending->scheduled->started)

## Step
~~Check validation for the command: OCP-73814~~  
- without --control-plane   
- invalida cluster id  
- incorrect format of the date and time

## Expect
There should be error message shown.

## Step
Delete the upgrade policies  
\# rosa delete upgrade -c <cluster_id>

## Expect
I: Successfully canceled scheduled upgrade on cluster '23ai3hv6bpt06bfpf3ss5df2r0ncht31'  
- The upgrade policies will be deleted.  
- Check the `rosa list upgrade` and `rosa describe upgrade`, there is no schedule one shown  
- If there is no upgrade policy existed, "I: There are no scheduled upgrades on cluster '23ai3hv6bpt06bfpf3ss5df2r0ncht31'"
