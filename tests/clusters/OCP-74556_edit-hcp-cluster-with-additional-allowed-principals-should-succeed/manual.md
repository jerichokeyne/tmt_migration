# Test

## Step
3. Verify editing of HCP cluster using the --additional-allowed-principals flag  
rosa edit cluster --cluster-name $name --additional-allowed-principals $account_role_arn

## Expect
Cluster is edited successfully

## Step
4. Describe the cluster and make sure the Addional Principals field is available  
rosa describe cluster -c $name | grep Additional

## Expect
Additional Principals: arn:aws:iam::301721915996:role/$arn
