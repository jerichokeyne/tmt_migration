# Setup
Create a rosa HCP cluster with upgrade ability

create_node_pool.json
```json
{
"id": "mp-1",
"cluster": "$clusterId",
"auto_repair": true,
"replicas": 2,
"management_upgrade": {
"max_surge": 2,
"max_unavailable": 1,

},

"version": {
"kind": "VersionLink",
"id": "openshift-v4.15.6"
}
}
```

# Test

## Step
1. Create machinepool using maxSurge and maxUnavailable
```bash
ocm post /api/clusters_mgmt/v1/clusters/$cluster_id/node_pools --body $create_node_pool.json
```

## Expect
```json
{
"kind":"NodePool",
"href":"/api/clusters_mgmt/v1/clusters/2c49atvpa48l7b38ia8hjs62uib75oi5/node_pools/mp-1",
"id":"mp-1",
"replicas":2,
"auto_repair":true,
"aws_node_pool": {
"instance_type":"m5.xlarge",
"instance_profile":"rosa-service-managed-staging-2c49atvpa48l7b38ia8hjs62uib75oi5-jf-hcp-worker",
"tags": {
"api.openshift.com/environment":"staging",
"api.openshift.com/id":"2c49atvpa48l7b38ia8hjs62uib75oi5",
"api.openshift.com/legal-entity-id":"1jlfDskrR39egznAq3T18Ul0Xxv",
"api.openshift.com/name":"jf-hcp",
"api.openshift.com/nodepool-hypershift":"jf-hcp-mp-1",
"api.openshift.com/nodepool-ocm":"mp-1",
"cluster-tag":"cluster-value",
"red-hat-clustertype":"rosa",
"red-hat-managed":"true"
}
},
"availability_zone":"us-west-2a",
"subnet":"subnet-065d0a7d54a9fe48d",
"status": {
"current_replicas":0,
"message":"WaitingForAvailableMachines"
},
"version": {
"kind":"VersionLink",
"id":"openshift-v4.15.6",
"href":"/api/clusters_mgmt/v1/versions/openshift-v4.15.6"
},
"node_drain_grace_period": {
"value":0,
"unit":"minutes"
},
"management_upgrade": {
"type":"Replace",
"max_unavailable":"1",
"max_surge":"2"
}
}
```

## Step
2. Verify the machinepool was created with the correct values
```bash
ocm get /api/clusters_mgmt/v1/clusters/$cluster_id/node_pools/$nodepool_id
```

## Expect
```json
{
"kind":"NodePool",
"href":"/api/clusters_mgmt/v1/clusters/2c49atvpa48l7b38ia8hjs62uib75oi5/node_pools/mp-1",
"id":"mp-1",
"replicas":2,
"auto_repair":true,
"aws_node_pool": {
"instance_type":"m5.xlarge",
"instance_profile":"rosa-service-managed-staging-2c49atvpa48l7b38ia8hjs62uib75oi5-jf-hcp-worker",
"tags": {
"api.openshift.com/environment":"staging",
"api.openshift.com/id":"2c49atvpa48l7b38ia8hjs62uib75oi5",
"api.openshift.com/legal-entity-id":"1jlfDskrR39egznAq3T18Ul0Xxv",
"api.openshift.com/name":"jf-hcp",
"api.openshift.com/nodepool-hypershift":"jf-hcp-mp-1",
"api.openshift.com/nodepool-ocm":"mp-1",
"cluster-tag":"cluster-value",
"red-hat-clustertype":"rosa",
"red-hat-managed":"true"
}
},
"availability_zone":"us-west-2a",
"subnet":"subnet-065d0a7d54a9fe48d",
"status": {
"current_replicas":2
},
"version": {
"kind":"VersionLink",
"id":"openshift-v4.15.6",
"href":"/api/clusters_mgmt/v1/versions/openshift-v4.15.6",
"available_upgrades": [
"4.15.8",
"4.15.9",
"4.15.10",
"4.15.11",
"4.15.12",
"4.15.13",
"4.15.14",
"4.15.15",
"4.15.16",
"4.15.17"
]
},
"tuning_configs": [],
"kubelet_configs": [],
"node_drain_grace_period": {
"value":0,
"unit":"minutes"
},
"management_upgrade": {
"type":"Replace",
"max_unavailable":"1",
"max_surge":"2"
}
}
```

## Step
3. Perform upgrade on machinepool
```bash
ocm patch /api/clusters_mgmt/v1/clusters/$cluster_id/node_pools/$nodepool_id/upgrade_policies --body $upgrade_node_pool.json
```

## Expect
Set an upgrade for node pool successfully

## Step
4. Wait for upgrade

## Expect

## Step
5. Verify that the machinepool is upgraded to selected version
```bash
ocm get /api/clusters_mgmt/v1/clusters/$cluster_id/node_pools/$nodepool_id
```

## Expect
```json
{
"kind":"NodePool",
"href":"/api/clusters_mgmt/v1/clusters/2c49atvpa48l7b38ia8hjs62uib75oi5/node_pools/mp-1",
"id":"mp-1",
"replicas":2,
"auto_repair":true,
"aws_node_pool": {
"instance_type":"m5.xlarge",
"instance_profile":"rosa-service-managed-staging-2c49atvpa48l7b38ia8hjs62uib75oi5-jf-hcp-worker",
"tags": {
"api.openshift.com/environment":"staging",
"api.openshift.com/id":"2c49atvpa48l7b38ia8hjs62uib75oi5",
"api.openshift.com/legal-entity-id":"1jlfDskrR39egznAq3T18Ul0Xxv",
"api.openshift.com/name":"jf-hcp",
"api.openshift.com/nodepool-hypershift":"jf-hcp-mp-1",
"api.openshift.com/nodepool-ocm":"mp-1",
"cluster-tag":"cluster-value",
"red-hat-clustertype":"rosa",
"red-hat-managed":"true"
}
},
"availability_zone":"us-west-2a",
"subnet":"subnet-065d0a7d54a9fe48d",
"status": {
"current_replicas":2
},
"version": {
"kind":"VersionLink",
"id":"openshift-v4.15.17",
"href":"/api/clusters_mgmt/v1/versions/openshift-v4.15.17",
"available_upgrades": [
]
},
"tuning_configs": [],
"kubelet_configs": [],
"node_drain_grace_period": {
"value":0,
"unit":"minutes"
},
"management_upgrade": {
"type":"Replace",
"max_unavailable":"1",
"max_surge":"2"
}
}
```

## Step
6. Verify that actions are visible in the manifest
```bash
ocm get /api/clusters_mgmt/v1/clusters/<id>/resources/live|jq -r .resources
```

## Expect
\":{}}}},\"subresource\":\"status\"}]},\"spec\":{\"workload\":{\"manifests\":[{\"apiVersion\":\"hypershift.openshift.io/v1beta1\",\"kind\":\"NodePool\",\"metadata\":{\"labels\":{\"api.openshift.com/environment\":\"staging\",\"api.openshift.com/id\":\"2c49atvpa48l7b38ia8hjs62uib75oi5\",\"api.openshift.com/legal-entity-id\":\"1jlfDskrR39egznAq3T18Ul0Xxv\",\"api.openshift.com/name\":\"jf-hcp\"},\"name\":\"jf-hcp-workers\",\"namespace\":\"ocm-staging-2c49atvpa48l7b38ia8hjs62uib75oi5\"},\"spec\":{\"clusterName\":\"jf-hcp\",\"management\":{\"autoRepair\":true,\"replace\":{\"rollingUpdate\":{\"maxSurge\":1,\"maxUnavailable\":0},\"strategy\":\"RollingUpdate\"},\"upgradeType\":\"Replace\"},\"platform\":{\"aws\":{\"instanceProfile\":\"rosa-service-managed-staging-2c49atvpa48l7b38ia8hjs62uib75oi5-jf-hcp-worker\",\"instanceType\":\"m5.xlarge\",\"resourceTags\":[{\"key\":\"api.openshift.com/environment\",\"value\":\"staging\"},{\"key\":\"api.openshift.com/id\",\"value\":\"2c49atvpa48l7b38ia8hjs62uib75oi5\"},{\"key\":\"api.openshift.com/legal-entity-id\",\"value\":\"1jlfDskrR39egznAq3T18Ul0Xxv\"},{\"key\":\"api.openshift.com/name\",\"value\":\"jf-hcp\"},{\"key\":\"api.openshift.com/nodepool-hypershift\",\"value\":
