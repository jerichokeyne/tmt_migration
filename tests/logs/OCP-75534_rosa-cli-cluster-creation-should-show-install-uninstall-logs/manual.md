# Test

## Step
Create one Hypershift cluster

## Expect

## Step
Check the install logs of the hypershift cluster  
$ rosa logs install -c <cluster name>

## Expect
The logs can be show correctly

## Step
Check the install logs of the hypershift cluster with flag "--watch"  
$ rosa logs install -c <cluster name> --watch

## Expect
The process won't exit until cluster installation finished or cluster getting into error state

## Step
Delete the Hypershift cluster by `rosa delete cluster`

## Expect
- The cluster can be deleted  
- All resource on AWS should be deleted.

## Step
Check the uninstall log of the hosted cluster  
$ rosa log uninstall -c <cluster name>

## Expect
The uninstall log can show correctly

## Step
Check the uninstall log of the hosted cluster with flag --watch  
$ rosa log uninstall -c <cluster name> --watch

## Expect
The process won't exit and the logs will refresh all the time until uninstallation finished or cluster gets into error
