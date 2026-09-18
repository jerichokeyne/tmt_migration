# Test

## Step
Prepare one ready ROSA cluster

## Expect

## Step
Verify the help message for `--best-effort` deletion.

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
Attempt deleting a cluster using the `--best-effort` flag.

```bash
rosa delete cluster -c cluster_name --best-effort
```

## Expect
You should get the following response:

```
[valeriiashapoval@fedora ~]$ rosa delete cluster -c cluster_name --best-effort
W: Deleting cluster 'cluster_name' with 'best effort' means that certain resources may be left behind in AWS account 'account_id'. These resources will need to be deleted manually.
? Are you sure you want to delete cluster cluster_name? (y/N)
```

## Step
Answer N to the prompt

## Expect
The process should exit and the cluster should stay in ready status.

## Step
Check with `rosa list clusters`.

## Expect
```
cluster_id cluster_name ready Classic
```

## Step
Repeat the deletion step and answer `Y`.

## Expect
You should get the warning message and the cluster status should be uninstalling.

Check with `rosa list clusters`.

```
cluster_id cluster_name uninstalling Classic
```

## Step
You should receive a notification about cluster deletion.

## Expect
This notification is for your cluster_name.

```
Cluster 'cluster_id' is starting forceful uninstall process. This skips steps in the cluster destruction chain that are known to cause the cluster deletion process to fail. You should use this option with care and it is recommended that you manually check your cloud account for any resources that might be left over and require manual cleanup.
```

## Step
Prepare a new ready ROSA cluster

## Expect

## Step
Attempt deleting a cluster using the `--best-effort` and `-y` flags.

## Expect
Cluster should be successfully uninstalling.

Check with `rosa list clusters`.

```
cluster_id cluster_name uninstalling Classic
```

## Step
You should receive a notification about cluster deletion.

## Expect
This notification is for your cluster_name.

```
Cluster 'cluster_id' is starting forceful uninstall process. This skips steps in the cluster destruction chain that are known to cause the cluster deletion process to fail. You should use this option with care and it is recommended that you manually check your cloud account for any resources that might be left over and require manual cleanup.
```

## Step
Ensure a successful deletion.

## Expect
