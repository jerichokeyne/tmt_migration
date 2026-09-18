# Test

## Step

Run below command to check the rosa cluster creation help
$--availability-zones strings The availability zones to use when installing a non-BYOVPC cluster. Format should be a comma-separated list. Leave empty for the installer to pick availability zones

## Expect

There will be flag
--availability-zones strings The availability zones to use when installing a non-BYOVPC cluster. Format should be a comma-separated list. Leave empty for the installer to pick availability zones

## Step

Run below command to create a sts rosa multi-az cluster on indicated zones
```bash
rosa create cluster --availability-zones us-east-1d,us-east-1c,us-east-1b
```
-c xuelirosa --region us-east-1 --role-arn <installer_role_arn> --support-role-arn <support_role_arn> --controlplane-iam-role <cp_role_arn> --worker-iam-role <worker_role_arn> --mode auto -y

## Expect

The cluster will be created successfully

## Step

Wait for cluster ready

## Expect

## Step

List the machinepool of the cluster and check the Default one
```bash
rosa list machinepool -c xuelirosa
```

## Expect

The default machine pool should use the indicated zone
[xueli@xueli-work rosa]$ rosa list machinepool -c xuelistssz3
ID AUTOSCALING REPLICAS INSTANCE TYPE LABELS TAINTS AVAILABILITY ZONES SPOT INSTANCES
Default No 2 m5.xlarge us-west-2b N/A
xuelimp No 2 m5.2xlarge us-west-2b No

## Step

Create a machinepool to the cluster
```bash
rosa create machinepool --mane mp1 -c xuelirosa
```

## Expect

The machinepool should be created successfully

## Step

List the machinepool again

## Expect

The machinepool should be created in the zone
