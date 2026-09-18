# Test

## Step

Log in with t the rosa cli

## Expect

## Step

Check the help message of "rosa create cluster -h"

## Expect

```bash
rosa create cluster --help
```
Create cluster.


```
Usage:
rosa create cluster [flags]
```


```
Examples:
\# Create a cluster named "mycluster"
rosa create cluster --cluster-name=mycluster
```


\# Create a cluster in the us-east-2 region
```bash
rosa create cluster --cluster-name=mycluster --region=us-east-2
```


```
Flags:
-c, --cluster-name string Name of the cluster. This will be used when generating a sub-domain for your cluster on openshiftapps.com.
--role-arn string The Amazon Resource Name of the role that OpenShift Cluster Manager will assume to create the cluster.
--external-id string An optional unique identifier that might be required when you assume a role in another account.
--support-role-arn string The Amazon Resource Name of the role used by Red Hat SREs to enable access to the cluster account in order to provide support.
--operator-iam-roles stringArray List of OpenShift name and namespace, and role ARNs used to perform credential requests by operators needed in the OpenShift installer.
--master-iam-role string The IAM role ARN that will be attached to master instances.
--worker-iam-role string The IAM role ARN that will be attached to worker instances.
--multi-az Deploy to multiple data centers.
--region string Use a specific AWS region, overriding the AWS_REGION environment variable.
--version string Version of OpenShift that will be used to install the cluster, for example "4.3.10"
--channel-group string Channel group is the name of the group where this image belongs, for example "stable" or "fast". (default "stable")
--private-link Provides private connectivity between VPCs, AWS services, and your on-premises networks, without exposing your traffic to the public internet.
--subnet-ids strings The Subnet IDs to use when installing the cluster. Format should be a comma-separated list. Leave empty for installer provisioned subnet IDs.
--compute-machine-type string Instance type for the compute nodes. Determines the amount of memory and vCPU allocated to each compute node.
--compute-nodes int Number of worker nodes to provision per zone. Single zone clusters need at least 2 nodes, multizone clusters need at least 3 nodes. (default 2)
--enable-autoscaling Enable autoscaling of compute nodes.
--min-replicas int Minimum number of compute nodes. (default 2)
--max-replicas int Maximum number of compute nodes. (default 2)
--machine-cidr ipNet Block of IP addresses used by OpenShift while installing the cluster, for example "10.0.0.0/16".
--service-cidr ipNet Block of IP addresses for services, for example "172.30.0.0/16".
--pod-cidr ipNet Block of IP addresses from which Pod IP addresses are allocated, for example "10.128.0.0/14".
--host-prefix int Subnet prefix length to assign to each individual node. For example, if host prefix is set to "23", then each node is assigned a /23 subnet out of the given CIDR.
--private Restrict master API endpoint and application routes to direct, private connectivity.
--disable-scp-checks Indicates if cloud permission checks are disabled when attempting installation of the cluster.
--watch Watch cluster installation logs.
--dry-run Simulate creating the cluster.
-i, --interactive Enable interactive mode.
-h, --help help for cluster
```


```
Global Flags:
--debug Enable debug mode.
--profile string Use a specific AWS profile from your credential file.
-y, --yes Automatically answer yes to confirm operation.
```

## Step

Check the validation for the cluster-name in the command line.
test012345678912
1-test-1
-test-cluster
test-cluster-

## Expect

```
E:Cluster name must consist of no more than 15 lowercase alphanumeric characters or '-', start with a letter, and end with an alphanumeric character.
```

## Step

Check the validation for the cluster-name in the interactive mode

## Expect

Same with the last step.

## Step

Check the validation for '--compute-machine-type' in the command line
```bash
rosa create cluster -c test-cluster --compute-machine-type=invalidtype
```

## Expect

```
E: Expected a valid machine type: A valid machine type number must be specified
Valid machine types: m5.xlarge r5.xlarge m5.2xlarge c5.2xlarge r5.2xlarge m5.4xlarge c5.4xlarge r5.4xlarge m5.8xlarge
```

## Step

Check the validation for '--compute-nodes' in the interactive mode

## Expect

## Step

Check the validation for '--compute-nodes' in the command line
Single-az:
1. with the compute nodes <2 (-1,0,1)
2. with the compute nodes not a INT(1.1,-1.1,string)
multi-az:
1. with the compute nodes <3 (-3,0,2)
2. with a nodes >3 and not a multiple of 3
3. with the compute nodes not a INT(1.1,-1.1,string)

## Expect

Single-az clusters:
1. E: The number of compute nodes needs to be at least 2
2. TBD
Multi-az:
1. [root@yuwan moactl]# ./rosa create cluster -c yuwan-0125-sr2 --multi-az --compute-nodes=2
```
E: The number of compute nodes needs to be at least 3
2.[root@yuwan moactl]# ./rosa create cluster -c yuwan-0125-sr2 --multi-az --compute-nodes=4
E: Multi AZ clusters require that the number of compute nodes be a multiple of 3
3.TBD
```

## Step

Check the validation for '--region' in the command line.

## Expect

\# ./rosa create cluster -c yuwan-0125-sr2 --region=aiai
```
E: Region 'aiai' is not supported for this AWS account
[root@yuwan moactl]#
```

## Step

Repeat the steps on Windows/MacOS/Linux

## Expect

- The function should work well
- The output should displau well

## Step

add --billing-account string in the command line when create a classic rosa cluster

## Expect

response with clear error message
```
E: Billing accounts are only supported for Hosted Control Plane clusters
```

## Step

Create cluster with "--disable-workload-monitoring" flag

## Expect

Since OCM-17719, this flag is deprecated, there is warning message when using it,"Flag --disable-workload-monitoring has been deprecated, Disable user workload monitoring (--disable-workload-monitoring) is deprecated and will be discontinued in a future version of ROSA CLI.
"

- In M1 of deprecating UWM, the option of UWM still works functionally with rosacli<=1.2.56. In future M2, rosacli 1.2.57, will disable it. and warning message will display,"W: [DEPRECATED FOR ROSA HCP] User workload monitoring (--disable-workload-monitoring) has been deprecated for Hosted Control Plane clusters, and will be removed in a future version of ROSA CLI. Please remove from your workflows to avoid future issues"
