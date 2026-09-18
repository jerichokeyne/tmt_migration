# Test

## Step

Log in with the rosa tool, and prepare bellow rosa clusters.
cluster1: with some available upgrade versions and machinepool
cluster2: without any available upgrade versions

## Expect

## Step

Check the help message for `upgrade cluster`:

```bash
rosa upgrade cluster -h
```

## Expect

- Description is correct and clear
- No typo error

```
Upgrade cluster to a new available version

Usage:
rosa upgrade cluster [flags]

Examples:
  # Interactively schedule an upgrade on the cluster named "mycluster"
rosa upgrade cluster --cluster=mycluster --interactive

  # Schedule a cluster upgrade within the hour
  rosa upgrade cluster -c mycluster --version 4.12.20

  # Check if any gates need to be acknowledged prior to attempting an upgrading
  rosa upgrade cluster -c mycluster --version 4.12.20 --dry-run

Flags:
  -c, --cluster string                   Name or ID of the cluster.
  -m, --mode string                      How to perform the operation. Valid options are:
                                         auto: Resource changes will be automatic applied using the current AWS account
                                         manual: Commands necessary to modify AWS resources will be output to be run manually
      --version string                   Version of OpenShift that the cluster will be upgraded to
      --schedule-date string             Next date the upgrade should run at the specified UTC time. Format should be 'yyyy-mm-dd'
      --schedule-time string             Next UTC time that the upgrade should run on the specified date. Format should be 'HH:mm'
      --schedule string                  cron expression in UTC which will be the time when an upgrade to the latest release will be automatically scheduled and repeated at each occurrence. Mutually exclusive with --schedule-date and --schedule-time. This is currently supported only for Hosted Control Planes.
      --node-drain-grace-period string   You may set a grace period for how long Pod Disruption Budget-protected workloads will be respected during upgrades.
                                         After this grace period, any workloads protected by Pod Disruption Budgets that have not been successfully drained from a node will be forcibly evicted.
                                         Valid options are ['15 minutes','30 minutes','45 minutes','1 hour','2 hours','4 hours','8 hours']
                                         This flag is not supported for Hosted Control Planes. (default "1 hour")
      --dry-run                          Simulate upgrading the cluster, or run through acknowledgements required to upgrade prior to upgrading a cluster.
  -y, --yes                              Automatically answer yes to confirm operation.
  -h, --help                             help for cluster

Global Flags:
      --color string     Surround certain characters with escape sequences to display them in color on the terminal. Allowed options are [auto never always] (default "auto")
      --debug            Enable debug mode.
  -i, --interactive      Enable interactive mode.
      --profile string   Use a specific AWS profile from your credential file.
      --region string    Use a specific AWS region, overriding the AWS_REGION environment variable. (DEPRECATED: Region flag will be removed from this command in future versions)
```

## Step

Try to upgrade the cluster with latest version:

```bash
rosa upgrade cluster -c <cluster_name>
```

## Expect

```bash
rosa upgrade cluster -c xueli-rosa2
```

```
W: There are no available upgrades
```

## Step

Try to schedule an upgrade on cluster in low version:

```bash
rosa upgrade cluster -c <cluster_name> --version 4.6.2 --schedule-date <date> --schedule-time <time> --node-drain-grace-period "<drain time> minutes"
```

## Expect

```bash
rosa upgrade cluster -c xueli-rosa --version 4.6.2 --schedule-date 2021-04-11 --schedule-time 11:59
```

```
I: Upgrade successfully scheduled for cluster 'xueli-rosa'
```

## Step

List the upgrades of the cluster:

```bash
rosa list upgrades -c <cluster_name>
```

## Expect

- The scheduled time should be correct
- The version should be correct

```bash
rosa list upgrade -c xueli-rosa
```

```
VERSION NOTES
4.6.2 scheduled for 2021-04-11 11:59 UTC
4.6.1
```
- The upgrade status should be shown correctly (pending->scheduled->started)

## Step

Verify whether cluster with machine pool can be upgrade successfully

## Expect

Cluster with machine pool can be upgrade successfully
