# Setup
**
**

# Test

## Step
1. Create a VPC

## Expect
VPC is created

## Step
2. Create 3 subnets under the VPC in different regions,

## Expect
subnets are created

## Step
3. Create account-roles

## Expect
account roles are created

## Step
4. Create oidc-config

## Expect
oidc-config is created

## Step
5. Create an HCP multiaz cluster

```bash
rosa create cluster --cluster-name gc-multiaz-hcp --role-arn $installer_role --support-role-arn $support_role --worker-iam-role $worker_role--operator-roles-prefix $prefix--oidc-config-id 2lcbbdmirovgiv0qjjh1t49hse7mqqek --region us-west-2 --replicas 3 --subnet-ids <private-subnet1>,<public-subnet1>,<private-subnet2>,<public-subnet2>,<private-subnet3>,<public-subnet3> --hosted-cp -y --mode auto --multi-az --billing-account $billing_account
```

## Expect
Cluster is created

## Step
6. Create machinepools on the cluster in each different region

```bash
rosa create machinepool --name=gc-worker-a --subnet=$private_subnet_id_region_1 -c gc-multiaz-hcp --replicas=3 --instance-type=m5.xlarge
rosa create machinepool --name=gc-worker-b --subnet=$private_subnet_id_region_2 -c gc-multiaz-hcp --replicas=3 --instance-type=m5.xlarge
rosa create machinepool --name=gc-worker-c --subnet=$private_subnet_id_region_3 -c gc-multiaz-hcp --replicas=3 --instance-type=m5.xlarge
```

## Expect
all machinepools are created normally

## Step
7. List machinepools associated with the cluster

```bash
rosa list machinepools -c $cluster
```

## Expect
```
ID AUTOSCALING REPLICAS INSTANCE TYPE LABELS TAINTS AVAILABILITY ZONE SUBNET DISK SIZE VERSION AUTOREPAIR
mp-1 Yes 0/5-20 m5.xlarge us-west-2a subnet-04601c71dd4bcd966 300 GiB 4.14.35 Yes
workers-0 No 1/1 m5.xlarge us-west-2c subnet-01ac219ffc5660c64 300 GiB 4.14.35 Yes
workers-1 No 1/1 m5.xlarge us-west-2a subnet-04601c71dd4bcd966 300 GiB 4.14.35 Yes
workers-2 No 1/1 m5.xlarge us-west-2b subnet-0ca2b2373af87c24d 300 GiB 4.14.35 Yes
```

## Step
8. Describe the machinepools

```bash
rosa describe machinepool $mp -c $cluster
```

## Expect
```
ID: mp-1
Cluster ID: 2e47d3sshogboast3dau345qabrbrvg5
Autoscaling: Yes
Desired replicas:
- Min replicas: 5
- Max replicas: 20
Current replicas: 0
Instance type: m5.xlarge
Labels:
Tags: red-hat-managed=true, api.openshift.com/environment=staging, api.openshift.com/id=2e47d3sshogboast3dau345qabrbrvg5, api.openshift.com/legal-entity-id=1jlfDskrR39egznAq3T18Ul0Xxv, api.openshift.com/name=my-hcp-cluster, api.openshift.com/nodepool-hypershift=my-hcp-cluster-mp-1, api.openshift.com/nodepool-ocm=mp-1, red-hat-clustertype=rosa
Taints:
Availability zone: us-west-2a
Subnet: subnet-04601c71dd4bcd966
Disk Size: 300 GiB
Version: 4.14.35
EC2 Metadata Http Tokens: optional
Autorepair: Yes
Tuning configs:
Kubelet configs:
Additional security group IDs:
Node drain grace period:
Management upgrade:
- Type: Replace
- Max surge: 1
- Max unavailable: 0
Message: Minimum availability requires 5 replicas, current 0 available
```

## Step
9. Delete the machinepool

```bash
rosa delete machinepool $mp -c $cluster
```

## Expect
```
I: Successfully deleted machine pool 'mp-1' from hosted cluster 'my-hcp-cluster'
```

## Step
10. Delete the cluster

```bash
rosa delete cluster -c $cluster
```

## Expect
Cluster is deleted successfully
