# Setup
**
**

# Test

## Step

1. Login to integration env

## Expect

## Step

2. Create 2subnets under the VPC in different regions,

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

5. Create an HCP cluster with property "skip_inflight_tests":"true"

```bash
rosa create cluster --cluster-name gc-multiaz-hcp --role-arn $installer_role --support-role-arn $support_role --worker-iam-role $worker_role--operator-roles-prefix $prefix--oidc-config-id 2lcbbdmirovgiv0qjjh1t49hse7mqqek --region us-west-2 --replicas 3 --subnet-ids <private-subnet1>,<public-subnet1>,<private-subnet2>,<public-subnet2> --hosted-cp -y --mode auto --billing-account $billing_account --properties "skip_inflight_tests":"true"
```

## Expect

Cluster is created

## Step

6. Check in the dynatrace logs that the cluster went into pending state, example:


    2025-10-24T18:51:07.155606464Z WARN pending_oidc_worker.go:547 [opid='e9ebcf03-cf35-4d1e-89d1-8eb7fb0a607f'] [cid='2m4nnm3sqnoonm219uhoj3jcdjkq94os'] Skipping inflight checks for cluster '2m4nnm3sqnoonm219uhoj3jcdjkq94os': capability enabled and property set

## Expect

Logs are shown

## Step

7. Delete the cluster

```bash
rosa delete cluster -c $cluster
```

## Expect

Cluster is deleted successfully

## Step

8. Repeat the process in stage env

## Expect

## Step

Repeat the steps on classic cluster

## Expect
