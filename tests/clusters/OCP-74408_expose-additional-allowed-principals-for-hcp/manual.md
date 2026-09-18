# Test

## Step

1. Verify creation of HCP cluster using the --additional-allowed-principals flag
```bash
rosa create cluster --cluster-name $name --hosted-cp --additional-allowed-principals $account_role_arn
```

## Expect

Cluster is installed successfully

## Step

2. Describe the cluster and make sure the Addional Principals field is available
```bash
rosa describe cluster -c $name | grep Additional
```

## Expect

Additional Principals: arn:aws:iam::301721915996:role/$arn
