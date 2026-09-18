# Test

## Step
Prepare a hosted-cp cluster

## Expect

## Step
Edit the autoscaler with setting a max-nodes-total, for example, x

## Expect

## Step
Check the validation of `rosa create machinepool` and `rosa edit machinepool` for multiple nodepools.
- Create additional machinepool
- Edit additional machinepool
- Edit default machinepool
- To cover autoscaling max and min replicas setting and replicas setting

## Expect
If sumOfReplicas + sumOfMinReplicas > HCPNodeLimitition(500), it will return error from backend.
```
E: Failed to update machine pool 'workers-2' on hosted cluster '2h0q1fap8484giajtlp75lkue6thj8qk': status is 400, identifier is '400', code is 'CLUSTERS-MGMT-400', at '2025-02-19T09:21:14Z' and operation identifier is '6d14e2f2-6b9f-47bd-a43d-dff10fb6ffb1': Replicas+Autoscaling.Min: The total number of compute nodes for a single cluster '503' exceeds the maximum allowed '500'. Reduce the total compute nodes requested to be within the maximum allowed.
```

## Step
After create some additional machinepool and edit the default worker pools.
Try to Edit/Create machinepool to meet bellow conditions:
- sumOfReplicas+sumOfMaxReplicas > max-nodes-total(x)
-  sumOfReplicas+sumOfMinReplicas > max-nodes-total(x)

## Expect
- If autoscaling is enable during eidt/create machinepool, there will be info message "Scaling max replicas to the maximum allowed value is subject to cluster autoscaler configuration"
- If sumOfReplicas+sumOfMaxReplicas > max-nodes-total(x), there will be info message "Actual maximum replicas can be lowered, since the replicas defined exceeds Cluster Autoscaler limit (MaxNodes)"
- If sumOfReplicas+sumOfMinReplicas > max-nodes-total(x), there will be info message "Actual total nodes in the cluster will be more than the maximum nodes configured in the cluster autoscaler"
