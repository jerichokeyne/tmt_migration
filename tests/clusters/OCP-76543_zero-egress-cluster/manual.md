# Setup
Ensure that AWS account organization has the capabilities:

capability.organization.hcp_enable_zero_egress

Clone terraform file from: https://github.com/dustman9000/rosa-hcp-zero-egress-terraform.git**
**

# Test

## Step

1. Use terraform file to setup vpc
terraform init
terraform apply

## Expect

Output will include private subnet IDs and vpc_id
private_subnet_ids = "[\"subnet-04601c71dd4bcd966\",\"subnet-0ca2b2373af87c24d\",\"subnet-01ac219ffc5660c64\"]"
vpc_id = "vpc-0e3e1fede9a5e2e9c"

## Step

2. Create an HCP cluster with zero-egress properties enabled (version 4.14.35 only, zero_egress set to true and the specific provision shard)

```bash
rosa create cluster --cluster-name my-hcp-cluster --mode auto --role-arn arn:aws:iam::301721915996:role/$installer-role --support-role-arn arn:aws:iam::301721915996:role/$support-role --worker-iam-role arn:aws:iam::301721915996:role/$worker-role --operator-roles-prefix $prefix --oidc-config-id $oidc --region us-west-2 --replicas 3 --compute-machine-type m5.xlarge --machine-cidr 10.0.0.0/16 --service-cidr 172.30.0.0/16 --pod-cidr 10.128.0.0/14 --host-prefix 23 --subnet-ids $subnet_ids --hosted-cp --billing-account 301721915996 --properties zero_egress:true --private --default-ingress-private
```

## Expect

Cluster is created

--default--ingress-private is needed for rosa cli >= v1.24.55

## Step

3. Once cluster is created, verify that the cluster is set to zero_egress true

```bash
ocm get /api/clusters_mgmt/v1/clusters/$cluster_id
```

## Expect

"properties": {
"provision_shard_id":"88d699d7-7821-11ee-8b13-0a580a82022a",
"rosa_cli_version":"1.2.45",
"rosa_creator_arn":"arn:aws:iam::301721915996:user/$user",
"zero_egress":"true"
}

## Step

4. Create a new machinepool on the cluster

```bash
rosa create machinepool --name=$name -c $cluster
```

## Expect

```
I: Checking available instance types for machine pool 'mp-1'
I: Machine pool 'mp-1' created successfully on hosted cluster 'my-hcp-cluster'
```

## Step

5. List machinepools associated with the cluster

```bash
rosa list machinepools -c $cluster
```

## Expect

ID AUTOSCALING REPLICAS INSTANCE TYPE LABELS TAINTS AVAILABILITY ZONE SUBNET DISK SIZE VERSION AUTOREPAIR
mp-1 Yes 0/5-20 m5.xlarge us-west-2a subnet-04601c71dd4bcd966 300 GiB 4.14.35 Yes
workers-0 No 1/1 m5.xlarge us-west-2c subnet-01ac219ffc5660c64 300 GiB 4.14.35 Yes
workers-1 No 1/1 m5.xlarge us-west-2a subnet-04601c71dd4bcd966 300 GiB 4.14.35 Yes
workers-2 No 1/1 m5.xlarge us-west-2b subnet-0ca2b2373af87c24d 300 GiB 4.14.35 Yes

## Step

6. Update the machinepool to enable autorepair, and 5/20 replicas

```bash
rosa edit machinepool $mp -c $cluster --min-replicas=5 --max-replicas=20 --autorepair
```

## Expect

```
I: Updated machine pool 'mp-1' on hosted cluster 'my-hcp-cluster'
```

## Step

7. Describe the machinepool

```bash
rosa describe machinepool $mp -c $cluster
```

## Expect

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

## Step

8. Delete the machinepool

```bash
rosa delete machinepool $mp -c $cluster
```

## Expect

```
I: Successfully deleted machine pool 'mp-1' from hosted cluster 'my-hcp-cluster'
```

## Step

9. Delete the cluster

```bash
rosa delete cluster -c $cluster
```

## Expect

Cluster is deleted successfully

## Step

10. Create a ZE cluster with a proxy
Refer to <https://legiondev.hashnode.dev/squid-proxy-on-linux-ec2-server> to create a proxy

## Expect

Cluster is created successfully

## Step

11. Delete the cluster

## Expect
