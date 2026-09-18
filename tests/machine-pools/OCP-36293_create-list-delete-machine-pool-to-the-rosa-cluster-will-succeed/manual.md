# Test

## Step
Log in the rosa tool and prepare one ready cluster

## Expect

## Step
Run command to check the help information
```bash
rosa create machine pool --help
```

## Expect
- The help message will show
- No typo issue in the message
```
Add a machine pool to the cluster.

Usage:
  rosa create machinepool [flags]

Aliases:
  machinepool, machinepools, machine-pool, machine-pools

Examples:
  # Interactively add a machine pool to a cluster named "mycluster"
  rosa create machinepool --cluster=mycluster --interactive
  # Add a machine pool mp-1 with 3 replicas of m7i.xlarge to a cluster
  rosa create machinepool --cluster=mycluster --name=mp-1 --replicas=3 --instance-type=m7i.xlarge
  # Add a machine pool mp-1 with autoscaling enabled and 3 to 6 replicas of m7i.xlarge to a cluster
  rosa create machinepool --cluster=mycluster --name=mp-1 --enable-autoscaling \
	--min-replicas=3 --max-replicas=6 --instance-type=m7i.xlarge
  # Add a machine pool with labels to a cluster
  rosa create machinepool -c mycluster --name=mp-1 --replicas=2 --instance-type=r5.2xlarge --labels=foo=bar,bar=baz,
  # Add a machine pool with spot instances to a cluster
  rosa create machinepool -c mycluster --name=mp-1 --replicas=2 --instance-type=r5.2xlarge --use-spot-instances \
    --spot-max-price=0.5
  # Add a machine pool to a cluster and set the node drain grace period
  rosa create machinepool -c mycluster --name=mp-1 --node-drain-grace-period="90 minutes"

Flags:
      --additional-security-group-ids strings    The additional Security Group IDs to be added to the machine pool. Format should be a comma-separated list.
      --autorepair                               Select auto-repair behaviour for a machinepool in a hosted cluster. (default true)
      --availability-zone string                 Select availability zone to create a single AZ machine pool for a multi-AZ cluster
      --capacity-reservation-id string           The ID of an AWS On-Demand Capacity Reservation. The 'capacity-reservation-id' must be pre-created in advance, before creating a NodePool.
      --capacity-reservation-preference string   A configurable preference for a capacity-reservation. Options are: 'none' | 'capacity-reservations-only' | 'open'
  -c, --cluster string                           Name or ID of the cluster.
      --disk-size string                         Root disk size with a suffix like GiB or TiB
      --ec2-metadata-http-tokens string          Should cluster nodes use both v1 and v2 endpoints or just v2 endpoint of EC2 Instance Metadata Service (IMDS)This flag is only supported for Hosted Control Planes.
      --enable-autoscaling                       Enable autoscaling for the machine pool.
  -h, --help                                     help for machinepool
      --instance-type string                     Instance type that should be used. (default "m7i.xlarge")
  -i, --interactive                              Enable interactive mode.
      --kubelet-configs string                   Name of the kubelet config to be applied to the machine pool. A single kubelet config is allowed. Kubelet config must already exist. This will overwrite any modifications made to node kubelet configs on an ongoing basis.
      --labels string                            Labels for machine pool. Format should be a comma-separated list of 'key=value'. This list will overwrite any modifications made to Node labels on an ongoing basis.
      --max-replicas int                         Maximum number of machines for the machine pool.
      --max-surge string                         The maximum number of nodes that can be provisioned above the desired number of nodes in the machinepool during the upgrade. It can be an absolute number i.e. 1, or a percentage i.e. '20%'. (default "1")
      --max-unavailable string                   The maximum number of nodes in the machinepool that can be unavailable during the upgrade. It can be an absolute number i.e. 1, or a percentage i.e. '20%'. (default "0")
      --min-replicas int                         Minimum number of machines for the machine pool.
      --multi-availability-zone                  Create a multi-AZ machine pool for a multi-AZ cluster (default true)
      --name string                              Name for the machine pool (required).
      --node-drain-grace-period string           You may set a grace period for how long Pod Disruption Budget-protected workloads will be respected when the NodePool is being replaced or upgraded.
                                                 After this grace period, all remaining workloads will be forcibly evicted.
                                                 Valid value is from 0 to 1 week (10080 minutes), and the supported units are 'minute|minutes' or 'hour|hours'. 0 or empty value means that the NodePool can be drained without any time limitations.
                                                 This flag is only supported for Hosted Control Planes.
  -o, --output string                            Output format. Allowed formats are [json yaml]
      --replicas int                             Count of machines for the machine pool (required when autoscaling is disabled).
      --spot-max-price string                    Max price for spot instance. If empty use the on-demand price. (default "on-demand")
      --subnet string                            Select subnet to create a single AZ machine pool for BYOVPC cluster
      --tags strings                             Apply user defined tags to all resources created by ROSA in AWS. Tags are comma separated, for example: 'key value, foo bar'
      --taints string                            Taints for machine pool. Format should be a comma-separated list of 'key=value:ScheduleType'. This list will overwrite any modifications made to Node taints on an ongoing basis.
      --tuning-configs string                    Name of the tuning configs to be applied to the machine pool. Format should be a comma-separated list. Tuning config must already exist. This list will overwrite any modifications made to node tuning configs on an ongoing basis.
      --type string                              Specifies the image type used by Hosted Control Plane machine pools. Use '--type Windows' to create a machine pool that uses a Windows image.
      --use-spot-instances                       Use spot instances for the machine pool.
      --version string                           Version of OpenShift that will be used to install a machine pool for a hosted cluster, for example "4.12.4"

Global Flags:
      --color string     Surround certain characters with escape sequences to display them in color on the terminal. Allowed options are [auto never always] (default "auto")
      --debug            Enable debug mode.
      --profile string   Use a specific AWS profile from your credential file.
      --region string    Use a specific AWS region, overriding the AWS_REGION environment variable.
  -y, --yes              Automatically answer yes to confirm operation.
```
## Step
Run command to record the machine pools
```bash
rosa list machinepool -c <cluster name>
```

## Expect
- The machine pools returned

## Step
List machinepool with flags '--dedicated-host','--all','--win-li','az-type'

## Expect
- If '--all' flag is set, the output will have 'AZ TYPE','WIN-LI ENABLED','DEDICATED HOST' column and values should be correct. and if set '--all' all columns should be shown even the value is empty
- If any of '--dedicated-host','--win-li','az-type' or combination of them are set, the corresponding colume will be shown and other columns with empty information will not be shown

## Step
Run command to create default machine pools
```bash
rosa create machine -c <cluster name> --replicas 0 --name default
```

## Expect
- There will be succeeded message output
```
[xueli@xueli-work tmp]$ rosa create machinepool -c xueli-rosa --name default --replicas 0
I: Machine pool 'default' created successfully on cluster 'xueli-rosa'
```

## Step
Run command to check the machine pools
```bash
rosa list machinepool -c <cluster name>
```

## Expect
- The created machine pool should be listed
- The ID/replica should be default/0 and instance type should be m5.xlarge by default, the availability zones should be same with the default one
```
ID AUTOSCALING REPLICAS INSTANCE TYPE LABELS TAINTS AVAILABILITY ZONES
default No 3 m5.8xlarge us-east-1a, us-east-1b, us-east-1c
default No 0 m5.xlarge us-east-1a, us-east-1b, us-east-1c
```

## Step
Run command to create an advanced machine pools
```bash
rosa create machinepool -c <cluster name> --name default2 --replicas 3 --labels "m5.xlarge/test=aaa,bbb=ccc,ddd=fff,test.label.openshift/label=mmm" --taints "#$%^&*Key1=value1:NoExecute, openshift.taints.com/test=value2:NoSchedule" --instance-type m5.2xlarge
```
NOTE: SDA-8272, empty taints value is support ,--taints key=:NoSchedule need to update the automated TC

## Expect
- There will be succeeded message output
```
[xueli@xueli-work tmp]$ rosa create machinepool -c xueli-rosa --name default --replicas 0
I: Machine pool '<machine pool name>' created successfully on cluster 'xueli-rosa'
```

## Step
Run command to check the machine pools
```bash
rosa list machinepool -c <cluster name>
```

## Expect
- The created machine pool should be listed
- The ID should be default3
- The Autoscaling should be no
- The replica should be 3
- The instance type should be m5.2xlarge
- the labels should be correct
- The taints should be correct
- The available zones should be correct

## Step
Run below command to create an auto scaling machine pools
```bash
rosa create machinepool -c xueli-rosa --name autoscale --enable-autoscaling --max-replicas 6 --min-replicas 3 --labels "aaa=bbb"
```

## Expect
- There will be succeeded message output
```
[xueli@xueli-work tmp]$ rosa create machinepool -c xueli-rosa --name default --replicas 0
I: Machine pool '<machine pool name>' created successfully on cluster 'xueli-rosa'
```

## Step
Run command to check the machine pools
```bash
rosa list machinepool -c <cluster name>
```

## Expect
- The created machine pool should be listed
- The ID should be autoscale
- The Autoscaling should be yes
- The replica should be <min>-<max> like 3-6
- The instance type should be m5.xlarge
- the labels should be correct
- The taints should be correct
- The available zones should be correct

## Step
Launch AWS console to check the instances created by the machine pools

## Expect
All of the instances should be AMI instances
