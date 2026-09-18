# Test

## Step

Prepare one ROSA cluster

## Expect

## Step

Run command to check the delete cluster help message, it should match with the doc
```bash
rosa delete cluster --help
```

## Expect

```
Delete cluster.

Usage:
  rosa delete cluster [flags]

Examples:
  # Delete a cluster named "mycluster"
  rosa delete cluster --cluster=mycluster

Flags:
  -c, --cluster string   Name or ID of the cluster.
      --best-effort      Skips steps in the cluster destruction chain that are known to cause the cluster deletion process to fail. You should use this option with care and it is recommended that you manually check your AWS account for any resources that might be left over after using --best-effort.
  -w, --watch            Watch cluster uninstallation logs.
  -h, --help             help for cluster

Global Flags:
      --color string     Surround certain characters with escape sequences to display them in color on the terminal. Allowed options are [auto never always] (default "auto")
      --debug            Enable debug mode.
      --profile string   Use a specific AWS profile from your credential file.
      --region string    Use a specific AWS region, overriding the AWS_REGION environment variable. (DEPRECATED: Region flag will be removed from this command in future versions)
  -y, --yes              Automatically answer yes to confirm operation.
```

## Step

Try to delete the MOA cluster with the rosa with command
```bash
rosa delete cluster -c <cluster name>
```

## Expect

There should prompt a confirmation.

```
[root@yuwan moactl]# rosa delete cluster yuwan-test-0721-moa1
? Are you sure you want to delete cluster yuwan-test-0721-moa1? (y/N) N
```

## Step

Input "n" and enter

## Expect

- The process will exit
- No request send out

## Step

Get the cluster again
```bash
rosa list cluster
```

## Expect

- The cluster won't be in uninstalling status

## Step

Delete the ROSA again with command
```bash
rosa delete cluster -c <cluster name> --debug
```

## Expect

The output will ask again whether deleting the cluster

## Step

Get the cluster again
```bash
rosa list cluster
```

## Expect

The cluster will be in status of uninstalling

## Step

Prepare another ROSA cluster

## Expect

## Step

Run command to delete the cluster
```bash
rosa delete cluster -c <cluster name> -y --watch
```

## Expect

- No question for deletion confirmation
- The cluster will be in status of uninstalling
- Cluster unisnatllation log will show to user continously
- The process will exit after uninstallation finished

## Step

Check the uninstall logs.

## Expect

Check the uninstall log when cluster in pending/installing status before installation pod start in HIVE.
```bash
rosa logs uninstall --cluster <cluster id>
```
```
W: Cluster 'xueli-rosa3' is not currently uninstalling
```

Check the uninstall log during uninstall progress.
- uninstallation log will show
- last tail 2000 logs will show
- Logs will be wrapped by lines
Tail the uninstall log.Only the last 10 lines of logs will show

```bash
rosa logs uninstall --cluster <cluster id> --tail 10
```

Watch the tail of the uninstall log.

```bash
rosa logs uninstall --cluster <cluster id> --tail 15 --watch
```

- It will show the last 5 line logs and kept waiting for new logs to show
- New logs will kept outputting when received
- The process won't exit until the cluster uninstallation finished
