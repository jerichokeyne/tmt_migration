# Test

## Step

Log in with the rosa tool, and prepare bellow rosa clusters.
cluster1: with some available upgrade versions

## Expect

## Step

Try to upgrade the cluster with not supported version
$ rosa upgrade cluster -c <cluster name> --version 4.6.9

## Expect

It will show
[xueli@xueli-work tmp]$ rosa upgrade cluster -c xueli-rosa --version 4.6.9
E: Expected a valid version to upgrade to

## Step

Try to upgrade the cluster with invalid schedule-date
$ rosa upgrade cluster -c xueli-rosa --schedule-date 73293028 --version 4.6.2

## Expect

It will show
[xueli@xueli-work tmp]$ rosa upgrade cluster -c xueli-rosa --schedule-date 73293028 --version 4.6.2
E: Time format invalid: parsing time "73293028 13:16" as "2006-01-02 15:04": cannot parse "3028 13:16" as "-"

## Step

Try to upgrade the cluster with passed schedule-date
$ rosa upgrade cluster -c xueli-rosa --schedule-date 2016-01-01 --version 4.6.2

## Expect

It will show
[xueli@xueli-work tmp]$ rosa upgrade cluster -c xueli-rosa --schedule-date 2016-01-01 --version 4.6.2
E: Failed to schedule upgrade for cluster 'xueli-rosa': identifier is '400', code is 'CLUSTERS-MGMT-400' and operation identifier is '1iescal33tebfl6rsjiakk2orrmqptk9': Cannot set upgrade to start earlier than 5 minutes from now

## Step

Try to upgrade the cluster with invalid schedule-time
$ rosa upgrade cluster -c xueli-rosa --schedule-date 2021-04-01 --version 4.6.2 --schedule-time 123:876

## Expect

[xueli@xueli-work tmp]$ rosa upgrade cluster -c xueli-rosa --schedule-date 2021-04-01 --version 4.6.2 --schedule-time 123:876
E: Time format invalid: parsing time "2021-04-01 123:876" as "2006-01-02 15:04": cannot parse "3:876" as ":"

## Step

Try to upgrade the cluster with invalid node-drain-grace-period
$ rosa upgrade cluster -c xueli-rosa --version 4.6.2 --node-drain-grace-period 10

## Expect

It should show node-drain-time is invalid

## Step

Try other flags
--debug
-v
--profile

## Expect

They should work well

## Step

Run command to list the upgrades without cluster set
$ rosa upgrade cluster

## Expect

Error: required flag(s) "cluster" not set
<usage> show

## Step

Run command to list the upgrades invalid flag
$ rosa upgrade cluster -c <cluster name> -y

## Expect

[xueli@xueli-work tmp]$ rosa upgrade cluster -c xueli-rosa -y
Error: unknown shorthand flag: 'y' in -y
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

Failed to execute root command: unknown shorthand flag: 'y' in -y

## Step

Create an upgrade policy to the cluster

## Expect

## Step

Schedule upgrade again to the cluster

## Expect

There will be error message reported that there is already an upgrade policy scheduled

    lixue@Xue-Lis-MacBook-Pro ~ % rosa upgrade cluster -c xueliup --version 4.14.10 -y
    I: Upgrade successfully scheduled for cluster 'xueliup'
    lixue@Xue-Lis-MacBook-Pro ~ % rosa upgrade cluster -c xueliup --version 4.14.10 -y
    W: There is already a pending upgrade to version 4.14.10 on 2024-02-05 12:28 UTC
