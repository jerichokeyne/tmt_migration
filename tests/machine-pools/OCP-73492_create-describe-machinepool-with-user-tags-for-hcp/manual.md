# Test

## Step
Prepare a hosted cp cluster

## Expect

## Step
Create a machinepool without tags to the cluster  
$ rosa create machinepool --name=mp-6729 --replicas 3 -c aaraj-hcp

## Expect
I: Checking available instance types for machine pool 'mp-6729'  
I: Machine pool 'mp-6729' created successfully on hosted cluster 'aaraj-hcp'  
I: To view the machine pool details, run 'rosa describe machinepool --cluster aaraj-hcp --machinepool mp-6729'  
I: To view all machine pools, run 'rosa list machinepools --cluster aaraj-hcp'

## Step
Describe the machinepool  
$ rosa describe machinepool mp-6729 -c aaraj-hcp

## Expect
It much show the system tags  
There must be 8 of them  
  
ID: mp-6729  
Cluster ID: 2aud6upeadfbjo8v69jov3g3cf23uk4i  
Autoscaling: No  
Desired replicas: 3  
Current replicas: 0  
Instance type: m5.xlarge  
Labels:   
Tags: red-hat-clustertype=rosa, red-hat-managed=true, api.openshift.com/environment=staging, api.openshift.com/id=2aud6upeadfbjo8v69jov3g3cf23uk4i, api.openshift.com/legal-entity-id=1jlfDskrR39egznAq3T18Ul0Xxv, api.openshift.com/name=aaraj-hcp, api.openshift.com/nodepool-hypershift=aaraj-hcp-mp-6729, api.openshift.com/nodepool-ocm=mp-6729  
Taints:   
Availability zone: us-west-2a  
Subnet: subnet-0551ad6eaa5f9169e  
Version: 4.15.9  
Autorepair: Yes  
Tuning configs:   
Additional security group IDs:   
Node drain grace period:   
Message: Minimum availability requires 3 replicas, current 0 available

## Step
Describe the machinepool in json format  
$ rosa describe machinepool mp-6729 -c aaraj-hcp -o json

## Expect
{  
"auto_repair": true,  
"availability_zone": "us-west-2a",  
"aws_node_pool": {  
"instance_profile": "rosa-service-managed-staging-2aud6upeadfbjo8v69jov3g3cf23uk4i-aaraj-hcp-worker",  
"instance_type": "m5.xlarge",  
"kind": "AWSNodePool",  
"tags": {  
"api.openshift.com/environment": "staging",  
"api.openshift.com/id": "2aud6upeadfbjo8v69jov3g3cf23uk4i",  
"api.openshift.com/legal-entity-id": "1jlfDskrR39egznAq3T18Ul0Xxv",  
"api.openshift.com/name": "aaraj-hcp",  
"api.openshift.com/nodepool-hypershift": "aaraj-hcp-mp-6729",  
"api.openshift.com/nodepool-ocm": "mp-6729",  
"red-hat-clustertype": "rosa",  
"red-hat-managed": "true"  
}  
},  
"href": "/api/clusters_mgmt/v1/clusters/2aud6upeadfbjo8v69jov3g3cf23uk4i/node_pools/mp-6729",  
"id": "mp-6729",  
"kind": "NodePool",  
"node_drain_grace_period": {  
"unit": "minutes",  
"value": 0  
},  
"replicas": 3,  
"status": {  
"current_replicas": 3,  
"kind": "NodePoolStatus"  
},  
"subnet": "subnet-0551ad6eaa5f9169e",  
"tuning_configs": [],  
"version": {  
"href": "/api/clusters_mgmt/v1/versions/openshift-v4.15.9",  
"id": "openshift-v4.15.9",  
"kind": "VersionLink"  
}  
}

## Step
Create a machinepool with tags to the cluster  
$ rosa create machinepool -c aaraj-hcp --name=mp-6729-1 --replicas 3 --tags="foo: bar, test: value"

## Expect
I: Checking available instance types for machine pool 'mp-6729-1'  
I: Machine pool 'mp-6729-1' created successfully on hosted cluster 'aaraj-hcp'  
I: To view the machine pool details, run 'rosa describe machinepool --cluster aaraj-hcp --machinepool mp-6729-1'  
I: To view all machine pools, run 'rosa list machinepools --cluster aaraj-hcp'

## Step
Describe the machinepool  
$ rosa describe machinepool mp-6729-1 -c aaraj-hcp

## Expect
It much show the system tags + user tags  
  
ID: mp-6729-1  
Cluster ID: 2aud6upeadfbjo8v69jov3g3cf23uk4i  
Autoscaling: No  
Desired replicas: 3  
Current replicas: 0  
Instance type: m5.xlarge  
Labels:   
Tags: foo:=bar, test:=value, api.openshift.com/id=2aud6upeadfbjo8v69jov3g3cf23uk4i, api.openshift.com/legal-entity-id=1jlfDskrR39egznAq3T18Ul0Xxv, api.openshift.com/nodepool-hypershift=aaraj-hcp-mp-6729-1, api.openshift.com/nodepool-ocm=mp-6729-1, red-hat-clustertype=rosa, red-hat-managed=true, api.openshift.com/environment=staging, api.openshift.com/name=aaraj-hcp  
Taints:   
Availability zone: us-west-2a  
Subnet: subnet-0551ad6eaa5f9169e  
Version: 4.15.9  
Autorepair: Yes  
Tuning configs:   
Additional security group IDs:   
Node drain grace period:   
Message: Minimum availability requires 3 replicas, current 0 available

## Step
Describe the machinepool in json format  
$ rosa describe machinepool mp-6729-1 -c aaraj-hcp -o json

## Expect
{  
"auto_repair": true,  
"availability_zone": "us-west-2a",  
"aws_node_pool": {  
"instance_profile": "rosa-service-managed-staging-2aud6upeadfbjo8v69jov3g3cf23uk4i-aaraj-hcp-worker",  
"instance_type": "m5.xlarge",  
"kind": "AWSNodePool",  
"tags": {  
"api.openshift.com/environment": "staging",  
"api.openshift.com/id": "2aud6upeadfbjo8v69jov3g3cf23uk4i",  
"api.openshift.com/legal-entity-id": "1jlfDskrR39egznAq3T18Ul0Xxv",  
"api.openshift.com/name": "aaraj-hcp",  
"api.openshift.com/nodepool-hypershift": "aaraj-hcp-mp-6729-1",  
"api.openshift.com/nodepool-ocm": "mp-6729-1",  
"foo:": "bar",  
"red-hat-clustertype": "rosa",  
"red-hat-managed": "true",  
"test:": "value"  
}  
},  
"href": "/api/clusters_mgmt/v1/clusters/2aud6upeadfbjo8v69jov3g3cf23uk4i/node_pools/mp-6729-1",  
"id": "mp-6729-1",  
"kind": "NodePool",  
"node_drain_grace_period": {  
"unit": "minutes",  
"value": 0  
},  
"replicas": 3,  
"status": {  
"current_replicas": 0,  
"kind": "NodePoolStatus",  
"message": "Minimum availability requires 3 replicas, current 0 available"  
},  
"subnet": "subnet-0551ad6eaa5f9169e",  
"tuning_configs": [],  
"version": {  
"href": "/api/clusters_mgmt/v1/versions/openshift-v4.15.9",  
"id": "openshift-v4.15.9",  
"kind": "VersionLink"  
}  
}

## Step
Create machinepool with invalid tags  
$ rosa create machinepool -c aaraj-hcp --name=mp-6729-1 --replicas 3 --tags="#:bar"

## Expect
E: expected a valid user tag key '#' matching ^[\pL\pZ\pN_.:/=+\-@]{1,128}$
