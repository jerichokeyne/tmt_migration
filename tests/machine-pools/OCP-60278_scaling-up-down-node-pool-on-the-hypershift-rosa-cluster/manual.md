# Test

## Step
~~Create a hypershift rosa cluster whose instance type is m5.2xlarge .~~
~~[Hypershift Cluster Creation via ROSA CLI](<https://docs.google.com/document/d/1Jga9YCNSTlsowoRsUl5gCCTtM5B9XRIDCkEgG_lNQXk/edit%A0>) (**This seems an invalid link~~)**

Create a rosa HCP cluster whose instance type is m5.2xlarge
**Prepare:
pls make sure you have the below resources, because the resources may be cleaned automatically through crontab tasks.**
(1) create account-roles
```bash
rosa create account-roles --prefix <xxxx> --mode auto -y
```
(2) create oidc config
```bash
rosa create oidc-config --mode auto -y --managed
```
(3) create vpc
// create a vpc on the indicated region
ocmqe create vpc --region us-west-2 --name <your-alias>-vpc
// create subnets
ocmqe create subnets --region us-west-2 --zones a --vpc-id <vpc id, got from the above command's output>

**Create**
```bash
rosa create cluster -i
```

choose the above resource, other choice can use the default value.

## Expect
The cluster is created successfully.

## Step
~~Add a node pool 'np-1' with 2-m5.2xlarge nodes on the cluster and check the quota cost. ~~
Create a node pool 'mp-amd-60278' with 1 replica of "m5.xlarge" typed instance type(AMD)

## Expect
The node pool with 1 node is created successfully.

// Maybe using the below API **" /subscriptions"** not "**/organizations "**, because there're many user under the same organization

// get subscription id
```
ocm get /api/clusters_mgmt/v1/clusters/<cluster_id> | jq -r .subscription.id
```

// get reserved resources
```
ocm get /api/accounts_mgmt/v1/subscriptions/<subscription got from the above cmd>/reserved_resources
```

// It will add a `compute.node.aws` resource_type record with `Replicas` count.
It can refer to OCP-60818, which check in the ocm-backend-test repo

~~2 more m5.2xlarge compute.node resource quotas are taken. > ocm get /api/accounts_mgmt/v1/organizations/<org_id>/consumed_quota > ocm get /api/accounts_mgmt/v1/organizations/1jlfDskrR39egznAq3T18Ul0Xxv/consumed_quota | jq -r '.items[] | select(.resource_name=="m5.2xlarge") | select(.billing_model=="marketplace-aws") | select(.resource_type=="compute.node.aws")' ~~ **Check through rosa client** Wait a while to
- check if the node pool's desired replicas equal 1
- check if the node pool's desired replicas equal current replicas
- check if instance_type == "m5.xlarge"

## Step
Scaling up the node pool 'mp-amd-60278' from 1 to 2
// AMD
```bash
rosa edit machinepool --replicas=2 --cluster=<cluster name> mp-amd-60278
```

## Expect
It will add a new node.

**Check through rosa client**
Wait a while to
- check if the node pool's desired replicas equal 2
- check if the node pool's desired replicas equal current replicas

**Another manual check method through oc or ocm client**
// Get the method how to login oc through below command
```
rosa describe admin -c dawang-hcp-auto
```
// FInd your created admin password, or if you don't create, you can create the admin
// Then login oc
```
oc login ....
```
// View the real nodes
```
oc get nodes
```

// You can also through the below command to view the edit detail status
// You can ask your mentor for $SUPER_ADMIN_USER_TOKEN, you need to login with a super admin role
```
ocm login --url staging --token $SUPER_ADMIN_USER_TOKEN
```
// view the output of conditions
```
ocm get /api/clusters_mgmt/v1/clusters/<cluster id>/resources/live | jq '.resources."manifest_work-<cluster_id>-<node pool name>"' | jq -j | jq -j
```

From the above result, you can see if it happened an issue.

## Step
Scaling down the nodepool 'mp-amd-60278' to 1
// AMD
```bash
rosa edit machinepool --replicas=1 --cluster=<cluster name> mp-amd-60278
```

## Expect
It will delete a new node.

**Check through rosa client**
Wait a while to
- check if the node pool's desired replicas equal 1
- check if the node pool's desired replicas equal current replicas

## Step
Repeat nodepool creation/scaling up/scaling down with "m6g.xlarge" typed instance type(ARM)

## Expect

## Step
~~Add an autoscaling node pool ''np-2'' with 2~4 m5.2xlarge nodes on the cluster.~~

Create a node pool 'scale-60278' with enabling autoscale and '1~3' m5.2xlarge nodes on the cluster.

## Expect
The node pool with 1 node is created successfully.
~~6 more m5.2xlarge compute.node resource quotas are taken. > ocm get /api/accounts_mgmt/v1/organizations/<org_id>/consumed_quota > ocm get /api/accounts_mgmt/v1/organizations/1jlfDskrR39egznAq3T18Ul0Xxv/consumed_quota | jq -r '.items[] | select(.resource_name=="m5.2xlarge") | select(.billing_model=="marketplace-aws") | select(.resource_type=="compute.node.aws")'~~

**Check through rosa client** Wait a while to
- check if the node pool's desired replicas equal 1
- check if the node pool's desired replicas equal current replicas
- check if instance_type == "m5.2xlarge"

## Step
Scaling up the node pool 'scale-60278' from 1~3 to 2~3
```bash
rosa edit machinepool --min-replicas=1 --cluster=<cluster name> mp-arm-60278
```

## Expect
It will add a new node.

**Check through rosa client**
Wait a while to
- check if the node pool's desired replicas
- Min replicas equal 2
- Max replicas equal 3
- check if the node pool's current replicas equal Min replicas

## Step
Scaling down the node pool 'scale-60278' from 2~3 to 1~5
```bash
rosa edit machinepool --min-replicas=1 --max-replicas=5 --cluster=<cluster name> mp-arm-60278
```

## Expect
It won't delete the node, the nodes' change only depends on the autoscale strategy

**Check through rosa client**
- check if the node pool's desired replicas
- Min replicas equal 1
- Max replicas equal 5

## Step
~~Scaling up the node pool 'np-1' to 3, and checking the quota cost.~~

## Expect
~~7 more m5.2xlarge compute.node resource quotas are taken. > ocm get /api/accounts_mgmt/v1/organizations/<org_id>/consumed_quota > ocm get /api/accounts_mgmt/v1/organizations/1jlfDskrR39egznAq3T18Ul0Xxv/consumed_quota | jq -r '.items[] | select(.resource_name=="m5.2xlarge") | select(.billing_model=="marketplace-aws") | select(.resource_type=="compute.node.aws")'~~

## Step
~~Scaling down the nodepool 'np-1' to 0 ~~

## Expect
~~It will scale down successfully~~

## Step
Delete the node pool 'np-1', and check the quota cost.

## Expect
The occupied quotas are released.
// It can't get the quota through rosa client. So it needs to add the relevant check scenarios in the repo 'ocm-backend-tests'

## Step
~~Scaling down the node pool 'np-2' to 1-3, and checking the quota cost.~~

## Expect
~~3 m5.2xlarge compute.node resource quotas are taken.~~

## Step
Scaling the autoscaled node pool(new created) to invalid replicas.
0-3
0-1000
-1-3
5-3
a-b

## Expect
**It will fail with related error messages which contains messages like**
Min replicas must be a positive number when autoscaling is set
exceeds the maximum allowed
Min replicas must be a positive number when autoscaling is set
The number of machine pool min-replicas needs to be less than the number of machine pool max-replicas
invalid syntax

## Step
Scaling the non-autoscaled node pool(new created) to invalid replicas.
1000
-1
a

## Expect
**It will fail with related error messages which contains messages like**
exceeds the maximum allowed
Replicas must be a positive number
invalid syntax

## Step
Scaling the default created node pool(Only one node pool with 2 compute nodes), scale replica to 1.

## Expect
It will fail because the minimal replicas of a full ROSA hcp cluster is 2.

## Step
~~Repeat nodepool creation with another instance type, e.g. m5.xlarge~~

## Expect
