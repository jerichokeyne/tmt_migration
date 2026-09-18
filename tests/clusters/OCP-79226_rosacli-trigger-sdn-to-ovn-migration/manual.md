# Test

## Step

Prepare 2 clusters for testing

  1. Install a cluster on 4.14 with the "--network-type OpenShiftSDN" set: "**rosa create cluster -i --version 4.14.22 --network-type OpenShiftSDN** "
  2. Upgrade that cluster to 4.15: "**rosa upgrade cluster -c jkeyne-0122-02 --version 4.15.43** "

  3. Upgrade the cluster again to at least 4.16.24: "**rosa upgrade cluster -c jkeyne-0122-02 --version 4.16.30** "

## Expect

You should have a cluster running at least 4.16.24 with the network type of OpenShiftSDN. You can check the network type by running:

**rosa describe cluster -c $CLUSTER_ID -o json | jq .network.type**
"OpenShiftSDN"

## Step

Start to trigger the migration by running: **rosa edit cluster -c $CLUSTER_ID --network-type OVNKubernetes**

## Expect

It should force interactive mode

## Step

Verify the help message, then say yes to:
? Migrate cluster network type from OpenShiftSDN -> OVN-Kubernetes: Yes

## Expect

```
? Clusters are required to migrate from network type 'OpenShiftSDN' to 'OVN-Kubernetes', this allows you to do this along with your cluster changes
```

## Step

Verify the help message, and then enter "OVNKubernetes"
? Network type for cluster: (OVNKubernetes)

## Expect

```
? Migrate a cluster's network type from OpenShiftSDN to OVN-Kubernetes
```

## Step

Verify the help message for:
? OVN-Kubernetes internal subnet configuration for cluster (key=value format) (optional):

## Expect

```
? OVN-Kubernetes internal subnet configuration for migrating 'network-type' from OpenShiftSDN -> OVN-Kubernetes. Must be supplied as a string=value pair with any of 'join', 'transit', 'masquerade' followed by a CIDR. Example: '--ovn-internal-subnets="join=192.168.255.0/24,transit=192.168.255.0/24,masquerade=192.168.255.0/24"'
```

## Step

Leave the internal subnet configuration blank

## Expect

## Step

Confirm the migration

? Changing the network plugin will reboot cluster nodes, can not be interrupted or rolled back, and can not be combined with other operations such as cluster upgrades.

Confirm that you want to proceed with migrating from 'OpenShiftSDN' to 'OVN-Kubernetes: Yes

## Expect

Migration should start

## Step

Check the progress for the migration by running **rosa describe cluster -c $CLUSTER_ID** or **ocm get /api/clusters_mgmt/v1/clusters/$CLUSTER_ID/migrations/$MIGRATION_ID** , monitor the status and make sure the migration completes successfully

## Expect

Should show the current status of the migration, and should eventually succeed

Migrations:
- 2gkltf2iav79v1k8a4p5egq7j0cdl6fd
- Type: sdnToOvn
- State: scheduled
- Description:

```json
{
"kind":"ClusterMigration",
"href":"/api/clusters_mgmt/v1/clusters/2gg6bsna8g1h744e9bm9do4ppfo66vh9/migrations/2ggqpun3v4a7tev6ufol3dkia50uroge",
"id":"2ggqpun3v4a7tev6ufol3dkia50uroge",
"cluster_id":"2gg6bsna8g1h744e9bm9do4ppfo66vh9",
"type":"sdnToOvn",
"state": {
"value":"in progress",
"description":"migration in progress"
},
"creation_timestamp":"2025-01-24T20:41:30.84316Z",
"updated_timestamp":"2025-01-24T20:49:50.843172Z"
}
```

## Step

Repeat the migration (on the second cluster) with a subnet configuration eg: join=192.168.253.0/24,transit=192.168.254.0/24,masquerade=192.168.255.0/24

Make sure to use the --debug flag to get the full output

## Expect

Migration should be scheduled and succeed as before

In the debug output you should see something like this:
time=2025-02-12T10:09:56-05:00 level=debug msg=Request body follows
time=2025-02-12T10:09:56-05:00 level=debug msg={
"kind": "ClusterMigration",
"sdn_to_ovn": {
"join_ipv4": "192.168.253.0/24",
"transit_ipv4": "192.168.254.0/24",
"masquerade_ipv4": "192.168.255.0/24"
},
"type": "sdnToOvn"
}

Make sure that the "join_ipv4", "transit_ipv4", and "masquerade_ipv4" fields are populated correctly
