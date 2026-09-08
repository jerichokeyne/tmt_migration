# Test

## Step
Create autoscaler via CLI options  
$ rosa create autoscaler --cluster zhsun-4131 --balance-similar-node-groups --skip-nodes-with-local-storage --log-verbosity 4 --max-pod-grace-period 0 --pod-priority-threshold 0 --ignore-daemonsets-utilization --max-node-provision-time 10m --balancing-ignored-labels "aaa" --max-nodes-total 1000 --min-cores 0 --max-cores 100 --min-memory 0 --max-memory 4096 --scale-down-enabled --scale-down-utilization-threshold 0.5 --scale-down-delay-after-add 10s --scale-down-delay-after-delete 10s --scale-down-delay-after-failure 10s --gpu-limit nvidia.com/gpu,0,10 --gpu-limit amd.com/gpu,1,5 --scale-down-unneeded-time 10s  
I: Successfully created autoscaler configuration for cluster '2661bolncla3m0moj20ejt9khgojc8g4'

## Expect
Check all filed are covered(20 fileds) and the info are correct, examples are about create autoscaler.  
After autoscaler is created, check autoscaler parameters are same with what we set.  
  
$ rosa create autoscaler -h  
$ ocm get /api/clusters_mgmt/v1/clusters/2661bolncla3m0moj20ejt9khgojc8g4/autoscaler   
{  
"kind": "ClusterAutoscaler",  
"href": "/api/clusters_mgmt/v1/clusters/2661bolncla3m0moj20ejt9khgojc8g4/autoscaler",  
"balance_similar_node_groups": true,  
"skip_nodes_with_local_storage": true,  
"log_verbosity": 4,  
"max_pod_grace_period": 0,  
"pod_priority_threshold": 0,  
"ignore_daemonsets_utilization": true,  
"max_node_provision_time": "10m",  
"balancing_ignored_labels": [  
"aaa"  
],  
"resource_limits": {  
"max_nodes_total": 1000,  
"cores": {  
"min": 0,  
"max": 100  
},  
"memory": {  
"min": 0,  
"max": 4096  
},  
"gpus": [  
{  
"type": "nvidia.com/gpu",  
"range": {  
"min": 0,  
"max": 10  
}  
},  
{  
"type": "amd.com/gpu",  
"range": {  
"min": 1,  
"max": 5  
}  
}  
]  
},  
"scale_down": {  
"enabled": true,  
"unneeded_time": "10s",  
"utilization_threshold": "0.500000",  
"delay_after_add": "10s",  
"delay_after_delete": "10s",  
"delay_after_failure": "10s"  
}  
}  
  
$ rosa delete autoscaler --cluster=zhsun-4131   
I: Successfully deleted autoscaler configuration for cluster '2661bolncla3m0moj20ejt9khgojc8g4'

## Step
Create autoscaler via interactively.

## Expect
If user used -i or --interactive or provided no argument of autoscaler configuration, then the different options will be requested one-by-one.  

  * Input ? to check help info are correct for each parameter
  * After autoscaler is created, check autoscaler parameters are same with what we set.
  * All parameters are covered

$ rosa create autoscaler -c zhsun-4133   
I: Enabling interactive mode  
? Balance similar node groups (optional): No  
? Skip nodes with local storage (optional): No  
? Log verbosity: 1  
? Labels that cluster autoscaler should ignore when considering node group similarity (optional):  
? Ignore daemonsets utilization (optional): No  
? Maximum node provision time (optional):  
? Maximum pod grace period: 0  
? Pod priority threshold: 0  
? Maximum amount of nodes in the cluster: 180  
? Minimum number of cores to deploy in cluster: 0  
? Maximum number of cores to deploy in cluster: 100  
? Minimum amount of memory, in GiB, in the cluster: 0  
? Maximum amount of memory, in GiB, in the cluster: 4096  
? Enter the number of GPU limitations you wish to set: 0  
? Should scale-down be enabled (optional): No  
? How long a node should be unneeded before it is eligible for scale down (optional):  
? Node utilization threshold: 0.500000  
? How long after scale up should scale down evaluation resume (optional):  
? How long after node deletion should scale down evaluation resume (optional):  
? How long after node deletion failure should scale down evaluation resume. (optional):  
I: Successfully created autoscaler configuration for cluster '2661bolncla3m0moj20ejt9khgojc8g4'

## Step
Describe autoscaler   
  
$ rosa describe autoscaler -c 2ac3b5npu88bmqa0m3fk5jij0a2ft4lk   
$ rosa describe autoscaler -h  
$ rosa describe autoscaler -c 2ac3b5npu88bmqa0m3fk5jij0a2ft4lk -o json  
$ rosa describe autoscaler -c 2ac3b5npu88bmqa0m3fk5jij0a2ft4lk -o yaml

## Expect
Check all commands results are good.  
$ rosa describe autoscaler -c 2ac3b5npu88bmqa0m3fk5jij0a2ft4lk   
  
Balance Similar Node Groups: Yes  
Skip Nodes With Local Storage Yes  
Log Verbosity: 4  
Labels Ignored For Node Balancing: aaa  
Ignore DaemonSets Utilization: Yes  
Maximum Node Provision Time: 10m  
Maximum Pod Grace Period: 0  
Pod Priority Threshold: 0  
Resource Limits:  
- Maximum Nodes: 1000  
- Minimum Number of Cores: 0  
- Maximum Number of Cores: 100  
- Minimum Memory (GiB): 0  
- Maximum Memory (GiB): 4096  
- GPU Limitations:  
- Type: nvidia.com/gpu  
- Min: 0  
- Max: 10  
- Type: amd.com/gpu  
- Min: 1  
- Max: 5  
Scale Down:  
- Enabled Yes  
- Node Unneeded Time: 10s  
- Node Utilization Threshold: 0.500000  
- Delay After Node Added: 10s  
- Delay After Node Deleted: 10s  
- Delay After Node Deletion Failure: 10s

## Step
Edit autoscaler via CLI options  
  
Before edit autoscaler:   
$ ocm get /api/clusters_mgmt/v1/clusters/2661bolncla3m0moj20ejt9khgojc8g4/autoscaler   
{  
"kind": "ClusterAutoscaler",  
"href": "/api/clusters_mgmt/v1/clusters/2661bolncla3m0moj20ejt9khgojc8g4/autoscaler",  
"balance_similar_node_groups": false,  
"skip_nodes_with_local_storage": false,  
"log_verbosity": 1,  
"max_pod_grace_period": 0,  
"pod_priority_threshold": 0,  
"ignore_daemonsets_utilization": false,  
"resource_limits": {  
"max_nodes_total": 180,  
"cores": {  
"min": 0,  
"max": 100  
},  
"memory": {  
"min": 0,  
"max": 4096  
}  
},  
"scale_down": {  
"enabled": false,  
"utilization_threshold": "0.500000"  
}  
}

## Expect
Check all filed are covered(20 fileds) and the info are correct, examples are about edit autoscaler.  
After autoscaler is installed, check autoscaler parameters are same with what we set.  
  
$ rosa edit autoscaler -h  
  
Edit autoscaler by adding new fileds, update existing fields  
$ rosa edit autoscaler --cluster=zhsun-4131 --scale-down-delay-after-add 0s --gpu-limit amd.com/gpu,1,5 --max-cores 10 --min-cores 0 --ignore-daemonsets-utilization  
I: Successfully updated autoscaler configuration for cluster '2661bolncla3m0moj20ejt9khgojc8g4'  
  
$ ocm get /api/clusters_mgmt/v1/clusters/2661bolncla3m0moj20ejt9khgojc8g4/autoscaler   
{  
"kind": "ClusterAutoscaler",  
"href": "/api/clusters_mgmt/v1/clusters/2661bolncla3m0moj20ejt9khgojc8g4/autoscaler",  
"balance_similar_node_groups": false,  
"skip_nodes_with_local_storage": false,  
"log_verbosity": 1,  
"max_pod_grace_period": 0,  
"pod_priority_threshold": 0,  
"ignore_daemonsets_utilization": true,  
"resource_limits": {  
"max_nodes_total": 180,  
"cores": {  
"min": 0,  
"max": 10  
},  
"memory": {  
"min": 0,  
"max": 4096  
},  
"gpus": [  
{  
"type": "amd.com/gpu",  
"range": {  
"min": 1,  
"max": 5  
}  
}  
]  
},  
"scale_down": {  
"enabled": false,  
"utilization_threshold": "0.500000",  
"delay_after_add": "0s"  
}  
}

## Step
Edit autoscaler only with some atrributes (OCM-10460)  
rosa edit autoscaler -c awesome-cluster --max-cores=10000 --min-cores=0

## Expect
-Only the two attributes are changed  
-Other attributes keep the origin value

## Step
Edit autoscaler via interactively.  
  
Before edit autoscaler:   
$ ocm get /api/clusters_mgmt/v1/clusters/2661bolncla3m0moj20ejt9khgojc8g4/autoscaler   
{  
"kind": "ClusterAutoscaler",  
"href": "/api/clusters_mgmt/v1/clusters/2661bolncla3m0moj20ejt9khgojc8g4/autoscaler",  
"balance_similar_node_groups": true,  
"skip_nodes_with_local_storage": false,  
"log_verbosity": 9,  
"max_pod_grace_period": 20,  
"pod_priority_threshold": 20,  
"ignore_daemonsets_utilization": false,  
"max_node_provision_time": "20m",  
"balancing_ignored_labels": [  
"bbb"  
],  
"resource_limits": {  
"max_nodes_total": 200,  
"cores": {  
"min": 20,  
"max": 200  
},  
"memory": {  
"min": 20,  
"max": 200  
},  
"gpus": [  
{  
"type": "m",  
"range": {  
"min": 20,  
"max": 200  
}  
}  
]  
},  
"scale_down": {  
"enabled": false,  
"unneeded_time": "20s",  
"utilization_threshold": "0.600000",  
"delay_after_add": "20s",  
"delay_after_delete": "20s",  
"delay_after_failure": "20s"  
}  
}

## Expect
If user used -i or --interactive or provided no argument of autoscaler configuration, then the different options will be requested one-by-one.  

  * Input ? to check help info are correct for each parameter
  * After autoscaler is edit, check autoscaler parameters are same with what we set.
  * All parameters are covered and can get the original values

$ rosa edit autoscaler --cluster=zhsun-4131 --interactive   
? Balance similar node groups: Yes  
? Skip nodes with local storage (optional): [? for help] (y/N) n  
? Log verbosity: [? for help] (9) 90  
? Labels that cluster autoscaler should ignore when considering node group similarity: [? for help] (bbb) ccc  
? Ignore daemonsets utilization (optional): [? for help] (y/N) y  
? Maximum node provision time: [? for help] (20m) 30m  
? Maximum pod grace period: [? for help] (20) 30  
? Pod priority threshold: [? for help] (20) 30  
? Maximum amount of nodes in the cluster: [? for help] (200) 300  
? Minimum number of cores to deploy in cluster: [? for help] (20) 30  
? Maximum number of cores to deploy in cluster: [? for help] (200) 300  
? Minimum amount of memory, in GiB, in the cluster: [? for help] (20) 30  
? Maximum amount of memory, in GiB, in the cluster: [? for help] (200) 300  
? Enter the number of GPU limitations you wish to set: [? for help] (0)  
? Should scale-down be enabled (optional): [? for help] (y/N) y  
? How long a node should be unneeded before it is eligible for scale down: [? for help] (20s) 30s  
? Node utilization threshold: [? for help] (0.600000) 0.7  
? How long after scale up should scale down evaluation resume: [? for help] (20s) 30s  
? How long after node deletion should scale down evaluation resume: [? for help] (20s) 30s  
? How long after node deletion failure should scale down evaluation resume.: [? for help] (20s) 30s  
I: Successfully updated autoscaler configuration for cluster '2661bolncla3m0moj20ejt9khgojc8g4'  
  
$ ocm get /api/clusters_mgmt/v1/clusters/2661bolncla3m0moj20ejt9khgojc8g4/autoscaler   
{  
"kind": "ClusterAutoscaler",  
"href": "/api/clusters_mgmt/v1/clusters/2661bolncla3m0moj20ejt9khgojc8g4/autoscaler",  
"balance_similar_node_groups": false,  
"skip_nodes_with_local_storage": false,  
"log_verbosity": 90,  
"max_pod_grace_period": 30,  
"pod_priority_threshold": 30,  
"ignore_daemonsets_utilization": true,  
"max_node_provision_time": "30m",  
"balancing_ignored_labels": [  
"ccc"  
],  
"resource_limits": {  
"max_nodes_total": 300,  
"cores": {  
"min": 30,  
"max": 300  
},  
"memory": {  
"min": 30,  
"max": 300  
},  
"gpus": [  
{  
"type": "m",  
"range": {  
"min": 20,  
"max": 200  
}  
}  
]  
},  
"scale_down": {  
"enabled": true,  
"unneeded_time": "30s",  
"utilization_threshold": "0.700000",  
"delay_after_add": "30s",  
"delay_after_delete": "30s",  
"delay_after_failure": "30s"  
}  
}

## Step
Delete autoscaler via cli   
  
$ rosa delete cluster -h  
$ rosa delete autoscaler --cluster=zhsun-4131

## Expect
Check examples are about delete autoscaler.  
$ rosa delete cluster -h  
  
Check autoscaler can be deleted successfully.  
$ rosa delete autoscaler --cluster=zhsun-4131   
I: Successfully deleted autoscaler configuration for cluster '2661bolncla3m0moj20ejt9khgojc8g4'  
$ ocm get /api/clusters_mgmt/v1/clusters/2661bolncla3m0moj20ejt9khgojc8g4/autoscaler   
{  
"kind": "Error",  
"id": "404",  
"href": "/api/clusters_mgmt/v1/errors/404",  
"code": "CLUSTERS-MGMT-404",  
"reason": "Autoscaler for cluster ID '2661bolncla3m0moj20ejt9khgojc8g4' is not found",  
"operation_id": "8bdedc5a-fbf0-4e35-855e-e37838f7058e"  
}
