# Test

## Step

Prepare one ROSA cluster in low version with upgrade

## Expect

## Step

Run command to check the delete cluster help message:

```bash
rosa delete upgrade --help
```

## Expect

- The help message show correctly
- No typo error

```
Cancel scheduled cluster upgrade

Usage:
rosa delete upgrade [flags]

Aliases:
upgrade, upgrades

Flags:
  -c, --cluster string       Name or ID of the cluster.
      --machinepool string   Machine pool of the cluster to target
  -y, --yes                  Automatically answer yes to confirm operation.
  -h, --help                 help for upgrade

Global Flags:
      --color string     Surround certain characters with escape sequences to display them in color on the terminal. Allowed options are [auto never always] (default "auto")
      --debug            Enable debug mode.
      --profile string   Use a specific AWS profile from your credential file.
      --region string    Use a specific AWS region, overriding the AWS_REGION environment variable. (DEPRECATED: Region flag will be removed from this command in future versions)
```

## Step

Try to delete the ingress of cluster with the rosa with command:

```bash
rosa delete upgrade -c <cluster_name>
```

## Expect

```bash
rosa delete upgrade -c xueli-rosa
```

```
? Are you sure you want to cancel scheduled upgrade on cluster xueli-rosa?
```

## Step

Input "n" and enter

## Expect

- The process will exit
- No request send out

## Step

Get the upgrade again:

```bash
rosa list upgrade -c <cluster_name>
```

## Expect

- The scheduled upgrade still existed

## Step

Delete the upgrade again with command:

```bash
rosa delete upgrade -c <cluster_name>
```

## Expect

The output will ask again whether deleting the upgrade

## Step

Input yes

## Expect

```bash
rosa delete upgrade -c xueli-rosa
```

```
? Are you sure you want to cancel scheduled upgrade on cluster xueli-rosa? Yes
I: Successfully canceled scheduled upgrade on cluster 'xueli-rosa'
```

## Step

Get the cluster again:

```bash
rosa list ingress -c <cluster_name>
```

## Expect

The upgrade policy will be deleted

## Step

Create an automatic upgrade to the cluster via OCM UI

## Expect

## Step

Run command to delete the ingress:

```bash
rosa delete ingress -c <cluster_name> -y --debug
```

## Expect

- No question for deletion confirmation
- The upgrade will be deleted
- debug parameter will show the request and response for the command
