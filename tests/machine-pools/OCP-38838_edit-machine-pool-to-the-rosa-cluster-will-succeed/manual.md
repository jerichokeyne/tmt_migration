# Test

## Step
Log in the rosa tool and prepare one ready cluster

## Expect

## Step
Run command to check the help information
```bash
rosa edit machine pool --help
```

## Expect
- The help message will show
- No typo issue in the message
```
Edit machine pools on a cluster.

Usage:
  rosa edit machinepool ID [flags]

Aliases:
  machinepool, machinepools, machine-pool, machine-pools

Examples:
  # Set 4 replicas on machine pool 'mp1' on cluster 'mycluster'
	rosa edit machinepool --replicas=4 --cluster=mycluster mp1
	# Enable autoscaling and Set 3-5 replicas on machine pool 'mp1' on cluster 'mycluster'
	rosa edit machinepool --enable-autoscaling --min-replicas=3 --max-replicas=5 --cluster=mycluster mp1
	# Set the node drain grace period to 1 hour on machine pool 'mp1' on cluster 'mycluster'
	rosa edit machinepool --node-drain-grace-period="1 hour" --cluster=mycluster mp1

Flags:
      --autorepair                       Select auto-repair behaviour for a machinepool in a hosted cluster. (default true)
  -c, --cluster string                   Name or ID of the cluster.
      --enable-autoscaling               Enable autoscaling for the machine pool.
  -h, --help                             help for machinepool
      --kubelet-configs string           Name of the kubelet config to be applied to the machine pool.  A single kubelet config is allowed. Kubelet config must already exist. This will overwrite any modifications made to node kubelet configs on an ongoing basis.
      --labels string                    Labels for machine pool. Format should be a comma-separated list of 'key=value'. This list will overwrite any modifications made to node labels on an ongoing basis.
      --machinepool string               Machine pool of the cluster to target
      --max-replicas int                 Maximum number of machines for the machine pool.
      --max-surge string                 The maximum number of nodes that can be provisioned above the desired number of nodes in the machinepool during the upgrade. It can be an absolute number i.e. 1, or a percentage i.e. '20%'.
      --max-unavailable string           The maximum number of nodes in the machinepool that can be unavailable during the upgrade. It can be an absolute number i.e. 1, or a percentage i.e. '20%'.
      --min-replicas int                 Minimum number of machines for the machine pool.
      --node-drain-grace-period string   You may set a grace period for how long Pod Disruption Budget-protected workloads will be respected when the NodePool is being replaced or upgraded.
                                         After this grace period, all remaining workloads will be forcibly evicted.
                                         Valid value is from 0 to 1 week (10080 minutes), and the supported units are 'minute|minutes' or 'hour|hours'. 0 or empty value means that the NodePool can be drained without any time limitations.
                                         This flag is only supported for Hosted Control Planes.
  -o, --output string                    Output format. Allowed formats are [json yaml]
      --replicas int                     Count of machines for this machine pool.
      --spot-max-price string            Max price for spot instances. Defaults to 'on-demand', which uses the on-demand price. (default "on-demand")
      --taints string                    Taints for machine pool. Format should be a comma-separated list of 'key=value:ScheduleType'. This list will overwrite any modifications made to node taints on an ongoing basis.
      --tuning-configs string            Name of the tuning configs to be applied to the machine pool. Format should be a comma-separated list. Tuning config must already exist. This list will overwrite any modifications made to node tuning configs on an ongoing basis.
      --use-spot-instances               Use spot instances for the hosted machine pool.
  -y, --yes                              Automatically answer yes to confirm operation.

Global Flags:
      --color string     Surround certain characters with escape sequences to display them in color on the terminal. Allowed options are [auto never always] (default "auto")
      --debug            Enable debug mode.
  -i, --interactive      Enable interactive mode.
      --profile string   Use a specific AWS profile from your credential file.
      --region string    Use a specific AWS region, overriding the AWS_REGION environment variable. (DEPRECATED: Region flag will be removed from this command in future versions)
```
## Step
Run command to record the machine pools
```bash
rosa list machinepool -c <cluster name>
```

## Expect
- The machine pools returned

## Step
Run command to edit default machine pools
```bash
rosa edit machinepool default -c <cluster name> --replicas 3 --enable-autoscaling=false
```

## Expect
- There will be succeeded message output
```
$ rosa edit machinepool default -c xueli-rosa --replicas 3 --enable-autoscaling=false
```

## Step
Run command to check the machine pools
```bash
rosa list machinepool -c <cluster name>
```

## Expect
- The updated machine pool should be listed
- The ID/replica should be default/0 and instance type should be m5.xlarge by default, the availability zones should be same with the default one
```
ID AUTOSCALING REPLICAS INSTANCE TYPE LABELS TAINTS AVAILABILITY ZONES
default No 3 m5.8xlarge us-east-1a, us-east-1b, us-east-1c
default No 0 m5.xlarge us-east-1a, us-east-1b, us-east-1c
```

## Step
Run command to edit an advanced machine pools
```bash
rosa edit machinepool --enable-autoscaling --min-replicas=3 max-replicas=6--cluster=mycluster default
```
NOTE: SDA-8272, empty taints value is support ,--taints key=:NoSchedule

## Expect
- There will be succeeded message output

## Step
Run command to check the machine pools
```bash
rosa list machinepool -c <cluster name>
```

## Expect
- The updated machine pool should be listed
- The ID/replica should be default/0 and instance type should be m5.xlarge by default, the availability zones should be same with the default one
```
[xueli@xueli-work tmp]$ rosa list machinepool -c xueli-rosa
ID AUTOSCALING REPLICAS INSTANCE TYPE LABELS TAINTS AVAILABILITY ZONES
default Yes 3-6 m5.8xlarge us-east-1a, us-east-1b, us-east-1c
default No 0 m5.xlarge us-east-1a, us-east-1b, us-east-1c
autoscale2 Yes 3-3 m5.xlarge aaa=bbb us-east-1a, us-east-1b, us-east-1c
```

## Step
Prepare another additional machine pool

## Expect

## Step
Run command to enable autoscaling and set the min-replicas to 0
```bash
rosa edit machinepool --enable-autoscaling --min-replicas=0 max-replicas=6--cluster=mycluster <mp-name>
```

## Expect
- There will be succeeded message output

## Step
Run command to check the machine pools
```bash
rosa list machinepool -c <cluster name>
```

## Expect

## Step
Edit machinepool by setting only min-replicas or max-replicas
```bash
rosa edit machinepool --min-replicas=3 --cluster=mycluster <mp-name>
```

## Expect

## Step
Run command to check the machine pools
```bash
rosa list machinepool -c <cluster name>
```

## Expect

## Step
Repeat above steps

## Expect
It should work as expected

## Step
Launch AWS console to check the instances created by the machine pools

## Expect
All of the instances should be AMI instances
