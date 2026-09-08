# Test

## Step
Prepare one ROSA cluster in low version with upgrade

## Expect

## Step
Run command to check the delete cluster help message  
$ rosa delete upgrade --help

## Expect
- The help message show correctly  
- No typo error  
[xueli@xueli-work tmp]$ rosa delete upgrade -c xueli-rosa -h  
Cancel scheduled cluster upgrade  
  
  
Usage:  
rosa delete upgrade [flags]  
  
  
Aliases:  
upgrade, upgrades  
  
  
Flags:  
-c, --cluster string Name or ID of the cluster to cancel the upgrade for (required)  
-h, --help help for upgrade  
  
  
Global Flags:  
--debug Enable debug mode.  
--profile string Use a specific AWS profile from your credential file.  
-v, --v Level log level for V logs  
-y, --yes Automatically answer yes to confirm operation.

## Step
Try to delete the ingress of cluster with the rosa with command  
$ rosa delete upgrade -c <cluster name>

## Expect
[xueli@xueli-work tmp]$ rosa delete upgrade -c xueli-rosa  
? Are you sure you want to cancel scheduled upgrade on cluster xueli-rosa?

## Step
Input "n" and enter

## Expect
- The process will exit  
- No request send out

## Step
Get the upgrade again  
$ rosa list upgrade -c <cluster name>

## Expect
- The scheduled upgrade still existed

## Step
Delete the upgrade again with command   
$ rosa delete upgrade -c <cluster name>

## Expect
The output will ask again whether deleting the upgrade

## Step
Input yes

## Expect
[xueli@xueli-work tmp]$ rosa delete upgrade -c xueli-rosa  
? Are you sure you want to cancel scheduled upgrade on cluster xueli-rosa? Yes  
I: Successfully canceled scheduled upgrade on cluster 'xueli-rosa'

## Step
Get the cluster again  
$ rosa list ingress -c <cluster name>

## Expect
The upgrade policy will be deleted

## Step
Create an automatic upgrade to the cluster via OCM UI

## Expect

## Step
Run command to delete the ingress  
$ rosa delete ingress -c <cluster name> -y --debug

## Expect
- No question for deletion confirmation  
- The upgrade will be deleted  
- debug parameter will show the request and response for the command
