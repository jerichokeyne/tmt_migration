# Test

## Step
1. Prepare a ROSA cluster.

## Expect

## Step
2. Check the `rosa edit` help message.

```bash
rosa edit -h
```

## Expect
The output includes `kubeletconfig Edit a kubeletconfig for a cluster`.

```
Edit a specific resource

Usage:
  rosa edit [command]

Aliases:
  edit, update

Available Commands:
  addon           Edit add-on installation parameters on cluster
  autoscaler      Edit the autoscaler of a cluster
  cluster         Edit cluster
  image-mirror    Edit image mirror for a cluster
  ingress         Edit a cluster ingress (load balancer)
  kubeletconfig   Edit a kubeletconfig for a cluster
  log-forwarder   Edit a log forwarder for a cluster
  machinepool     Edit machine pool
  tuning-configs  Edit tuning config

Flags:
  -h, --help             help for edit
  -i, --interactive      Enable interactive mode.
      --profile string   Use a specific AWS profile from your credential file.
      --region string    Use a specific AWS region, overriding the AWS_REGION environment variable.
  -y, --yes              Automatically answer yes to confirm operation.

Global Flags:
      --color string   Surround certain characters with escape sequences to display them in color on the terminal. Allowed options are [auto never always] (default "auto")
      --debug          Enable debug mode.

Use "rosa edit [command] --help" for more information about a command.
```

## Step
3. Check the `rosa edit kubeletconfig` help message.

```bash
rosa edit kubeletconfig -h
```

## Expect
There are no typos and all descriptions are clear.

```
Edit a kubeletconfig for a cluster

Usage:
  rosa edit kubeletconfig [flags]

Aliases:
  kubeletconfig, kubelet-config

Examples:
  # Edit a KubeletConfig to have a pod-pids-limit of 10000
  rosa edit kubeletconfig --cluster=mycluster --pod-pids-limit=10000
  # Edit a KubeletConfig named 'bar' to have a pod-pids-limit of 10000
  rosa edit kubeletconfig --cluster=mycluster --name=bar --pod-pids-limit=10000

Flags:
  -c, --cluster string       Name or ID of the cluster.
  -i, --interactive          Enable interactive mode.
      --pod-pids-limit int   Sets the requested pod_pids_limit for this KubeletConfig.
      --name string          Name of the KubeletConfig (required for Hosted Control Plane clusters)
  -h, --help                 help for kubeletconfig

Global Flags:
      --color string     Surround certain characters with escape sequences to display them in color on the terminal. Allowed options are [auto never always] (default "auto")
      --debug            Enable debug mode.
      --profile string   Use a specific AWS profile from your credential file.
      --region string    Use a specific AWS region, overriding the AWS_REGION environment variable. (DEPRECATED: Region flag will be removed from this command in future versions)
  -y, --yes              Automatically answer yes to confirm operation.
```

## Step
4. Edit the kubeletconfig before it is created.

```bash
rosa edit kubeletconfig -c yunjiang-lx
```

## Expect
An error is returned.

```
E: No KubeletConfig for cluster 'yunjiang-lx' has been found. You should first create it via 'rosa create kubeletconfig'
```

## Step
5. Create a kubeletconfig for the cluster.

## Expect

## Step
6. Edit the kubeletconfig.

```bash
rosa edit kubeletconfig -c trad-class --pod-pids-limit 12345
```

## Expect
A warning explains the impact to the customer.

```
? Updating the custom KubeletConfig for cluster '27d9uge7mvjd9dhmjb7l9ed6mvcdf0kn' will cause all non-Control Plane nodes to reboot. This may cause outages to your applications. Do you wish to continue? (y/N)
I: Creation of custom KubeletConfig for cluster '27d9uge7mvjd9dhmjb7l9ed6mvcdf0kn' aborted.
```

## Step
7. Edit the kubeletconfig without the warning prompt.

```bash
rosa edit kubeletconfig -c yunjiang-lx --pod-pids-limit 12346 -y
```

## Expect
The kubeletconfig is updated.

```
I: Successfully updated custom KubeletConfig for cluster '27dlmit7s04t5ovoesfcmajmn9ua7n4a'
```

## Step
8. Describe the kubeletconfig.

```bash
rosa describe kubeletconfig -c trad-class
```

## Expect
The updated configuration is displayed.

```
Pod Pids Limit: 12345
```

## Step
9. Update a machinepool with `--kubelet-configs` set.

## Expect
An error reports that the setting is not supported for a classic cluster.
