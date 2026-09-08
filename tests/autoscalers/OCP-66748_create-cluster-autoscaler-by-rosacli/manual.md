# Test

## Step
Create cluster with all autoscaler perameters  
$ rosa create cluster --cluster-name zhsun-ca2 --autoscaler-balance-similar-node-groups --autoscaler-skip-nodes-with-local-storage --autoscaler-log-verbosity 4 --autoscaler-max-pod-grace-period 0 --autoscaler-pod-priority-threshold 0 --autoscaler-ignore-daemonsets-utilization --autoscaler-max-node-provision-time 10m --autoscaler-balancing-ignored-labels "aaa" --autoscaler-max-nodes-total 1000 --autoscaler-min-cores 0 --autoscaler-max-cores 100 --autoscaler-min-memory 0 --autoscaler-max-memory 4096 --autoscaler-scale-down-enabled --autoscaler-scale-down-utilization-threshold 0.5 --autoscaler-scale-down-delay-after-add 10s --autoscaler-scale-down-delay-after-delete 10s --autoscaler-scale-down-delay-after-failure 10s --enable-autoscaling --min-replicas 2 --max-replicas 6  
I: Cluster 'zhsun-ca2' has been created.  
I: Once the cluster is installed you will need to add an Identity Provider before you can login into the cluster. See 'rosa create idp --help' for more information.  
  
Name: zhsun-ca2  
ID: 25odmobce13h95ru1o94js16t8chq33g  
External ID:  
Control Plane: Customer Hosted  
OpenShift Version:  
Channel Group: stable  
DNS: Not ready  
AWS Account: 301721915996  
API URL:  
Console URL:  
Region: us-east-2  
Multi-AZ: false  
Nodes:  
- Control plane: 3  
- Infra: 2  
- Compute: 4  
Network:  
- Type: OVNKubernetes  
- Service CIDR: 172.30.0.0/16  
- Machine CIDR: 10.0.0.0/16  
- Pod CIDR: 10.128.0.0/14  
- Host Prefix: /23  
Ec2 Metadata Http Tokens: optional  
State: pending (Preparing account)  
Private: No  
Created: Aug 21 2023 09:07:47 UTC  
Details Page: https://qaprodauth.console.redhat.com/openshift/details/s/2UHuXfLa4NzHMcahB44aRCAATTq  
  
I: To determine when your cluster is Ready, run 'rosa describe cluster -c zhsun-ca2'.

## Expect
Should success, check all values are same with what we set  
$ rosa describe cluster -c zhsun-ca2   
  
  
Name: zhsun-ca2  
ID: 25odmobce13h95ru1o94js16t8chq33g  
External ID: ce86b487-266c-4840-9ea9-7990377d2b8c  
Control Plane: Customer Hosted  
OpenShift Version:  
Channel Group: stable  
DNS: zhsun-ca2.hppa.s1.devshift.org  
AWS Account: 301721915996  
API URL:  
Console URL:  
Region: us-east-2  
Multi-AZ: false  
Nodes:  
- Control plane: 3  
- Infra: 2  
- Compute: 4  
Network:  
- Type: OVNKubernetes  
- Service CIDR: 172.30.0.0/16  
- Machine CIDR: 10.0.0.0/16  
- Pod CIDR: 10.128.0.0/14  
- Host Prefix: /23  
Infra ID: zhsun-ca2-dxdh4  
Ec2 Metadata Http Tokens: optional  
State: installing (Cluster is installing)  
Private: No  
Created: Aug 21 2023 09:07:47 UTC  
Details Page: https://qaprodauth.console.redhat.com/openshift/details/s/2UHuXfLa4NzHMcahB44aRCAATTq  
  
  
  
  
  
$ ocm get /api/clusters_mgmt/v1/clusters/25odmobce13h95ru1o94js16t8chq33g/autoscaler   
{  
"kind": "ClusterAutoscaler",  
"href": "/api/clusters_mgmt/v1/clusters/25odmobce13h95ru1o94js16t8chq33g/autoscaler",  
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
}  
},  
"scale_down": {  
"enabled": true,  
"utilization_threshold": "0.500000",  
"delay_after_add": "10s",  
"delay_after_delete": "10s",  
"delay_after_failure": "10s"  
}  
}

## Step
Create cluster without autoscaler boolean parameters  
  
$ rosa create cluster --cluster-name zhsun-ca3 --autoscaler-log-verbosity 4 --autoscaler-max-pod-grace-period 0 --autoscaler-pod-priority-threshold -10 --autoscaler-max-node-provision-time 10m --autoscaler-balancing-ignored-labels "aaa" --autoscaler-max-nodes-total 1000 --autoscaler-min-cores 0 --autoscaler-max-cores 100 --autoscaler-min-memory 0 --autoscaler-max-memory 4096 --autoscaler-scale-down-utilization-threshold 0.5 --autoscaler-scale-down-delay-after-add 10s --autoscaler-scale-down-delay-after-delete 10s --autoscaler-scale-down-delay-after-failure 10s --enable-autoscaling --min-replicas 2 --max-replicas 6

## Expect
All boolean parameters should be false  
$ ocm get /api/clusters_mgmt/v1/clusters/25oeas6d7o04kq0kt191c7ujvmg9b86d/autoscaler   
{  
"kind": "ClusterAutoscaler",  
"href": "/api/clusters_mgmt/v1/clusters/25oeas6d7o04kq0kt191c7ujvmg9b86d/autoscaler",  
"balance_similar_node_groups": false,  
"skip_nodes_with_local_storage": false,  
"log_verbosity": 4,  
"max_pod_grace_period": 0,  
"pod_priority_threshold": -10,  
"ignore_daemonsets_utilization": false,  
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
}  
},  
"scale_down": {  
"enabled": false,  
"utilization_threshold": "0.500000",  
"delay_after_add": "10s",  
"delay_after_delete": "10s",  
"delay_after_failure": "10s"  
}  
}

## Step
Create cluster without autoscaler string & int parameters  
  
$ rosa create cluster --cluster-name zhsun-ca4 --autoscaler-balance-similar-node-groups --autoscaler-skip-nodes-with-local-storage --autoscaler-ignore-daemonsets-utilization --autoscaler-scale-down-enabled --enable-autoscaling --min-replicas 2 --max-replicas 6

## Expect
All flloat & int parameters should be set default value. All string parameters should be set empty  
$ ocm get /api/clusters_mgmt/v1/clusters/25oee36vmsgf6r44juuo8svr6pv7mklt/autoscaler   
{  
"kind": "ClusterAutoscaler",  
"href": "/api/clusters_mgmt/v1/clusters/2930na1ickqjgr5vj69156lk7t16mgab/autoscaler",  
"balance_similar_node_groups": true,  
"skip_nodes_with_local_storage": true,  
"log_verbosity": 1,  
"max_pod_grace_period": 600,  
"pod_priority_threshold": -10,  
"ignore_daemonsets_utilization": true,  
"resource_limits": {  
"max_nodes_total": 180,  
"cores": {  
"min": 0,  
"max": 11520  
},  
"memory": {  
"min": 0,  
"max": 230400  
}  
},  
"scale_down": {  
"enabled": true,  
"utilization_threshold": "0.500000"  
}  
}

## Step
Create cluster with gpu paramters  
$ rosa create cluster --cluster-name zhsun-gpu --autoscaler-gpu-limit nvidia.com/gpu,0,10 --autoscaler-gpu-limit amd.com/gpu,1,5 --enable-autoscaling --min-replicas 2 --max-replicas 6

## Expect
The info is same with what we set  
$ ocm get /api/clusters_mgmt/v1/clusters/2625rt07gegu3b01hmu2akmtkvhtqhie/autoscaler  
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

## Step
Create cluster with autoscaler [by the interactive mode, Enable autoscaling (optional): Yes  
  
$ rosa create cluster --cluster-name zhsun-ca5 -i  
](</polarion/#/project/OSE/workitem?id=OCP-64494>)

## Expect
Input ? to check help info for each parameter, after cluster is installed, check autoscaler parameters are same with what we set. No parameters are missing.  
  
? Enable autoscaling: Yes  
? Min replicas: 2  
? Max replicas: 2  
? Configure cluster-autoscaler: Yes  
? Balance similar node groups: No  
? Skip nodes with local storage: No  
? Log verbosity: 1  
? Labels that cluster autoscaler should ignore when considering node group similarity (optional): b  
? Ignore daemonsets utilization: No  
? Maximum node provision time (optional):  
? Maximum pod grace period: 600  
? Pod priority threshold: -10  
? Maximum amount of nodes in the cluster: 180  
? Minimum number of cores to deploy in cluster: 0  
? Maximum number of cores to deploy in cluster: 11520  
? Minimum amount of memory, in GiB, in the cluster: 0  
? Maximum amount of memory, in GiB, in the cluster: 230400  
? Enter the number of GPU limitations you wish to set: 1  
? 1. Enter the type of desired GPU limitation: 1  
? 1. Enter minimum number of GPUS of type '1' to deploy in the cluster.: 3  
? 1. Enter maximum number of GPUS of type '1' to deploy in the cluster.: 12  
? Should scale-down be enabled: Yes  
? How long a node should be unneeded before it is eligible for scale down (optional):  
? Node utilization threshold: 0.500000  
? How long after scale up should scale down evaluation resume (optional):  
? How long after node deletion should scale down evaluation resume (optional):  
? How long after node deletion failure should scale down evaluation resume. (optional):  
? Worker machine pool labels (optional):  
  
I: Creating cluster 'zhsun-ca5'  
I: To create this cluster again in the future, you can run:  
rosa create cluster --cluster-name zhsun-ca5 --region us-east-2 --version 4.14.9 --ec2-metadata-http-tokens required --enable-autoscaling --min-replicas 2 --max-replicas 2 --compute-machine-type m5.xlarge --machine-cidr 10.0.0.0/16 --service-cidr 172.30.0.0/16 --pod-cidr 10.128.0.0/14 --host-prefix 23 --autoscaler-log-verbosity 1 --autoscaler-max-pod-grace-period 600 --autoscaler-pod-priority-threshold -10 --autoscaler-balancing-ignored-labels b --autoscaler-max-nodes-total 180 --autoscaler-min-cores 0 --autoscaler-max-cores 11520 --autoscaler-min-memory 0 --autoscaler-max-memory 230400 --autoscaler-gpu-limit 1,3,12 --autoscaler-scale-down-enabled --autoscaler-scale-down-utilization-threshold 0.500000  
  
$ ocm get /api/clusters_mgmt/v1/clusters/293105vhpj1uv57v90tg2t0ivl8p2chc/autoscaler   
{  
"kind": "ClusterAutoscaler",  
"href": "/api/clusters_mgmt/v1/clusters/293105vhpj1uv57v90tg2t0ivl8p2chc/autoscaler",  
"balance_similar_node_groups": false,  
"skip_nodes_with_local_storage": false,  
"log_verbosity": 1,  
"max_pod_grace_period": 600,  
"pod_priority_threshold": -10,  
"ignore_daemonsets_utilization": false,  
"balancing_ignored_labels": [  
"b"  
],  
"resource_limits": {  
"max_nodes_total": 180,  
"cores": {  
"min": 0,  
"max": 11520  
},  
"memory": {  
"min": 0,  
"max": 230400  
},  
"gpus": [  
{  
"type": "1",  
"range": {  
"min": 3,  
"max": 12  
}  
}  
]  
},  
"scale_down": {  
"enabled": true,  
"utilization_threshold": "0.500000"  
}  
}

## Step
Create cluster with autoscaler [by the interactive mode](</polarion/#/project/OSE/workitem?id=OCP-64494>), Enable autoscaling (optional): No

## Expect
No cluster-autoscaler need to be configured , this is by design.  
$ rosa create cluster   
I: Enabling interactive mode  
? Cluster name: zhsun-ca6  
? Deploy cluster with Hosted Control Plane (optional): No  
? Create cluster admin user: No  
? Deploy cluster using AWS STS: No  
W: In a future release STS will be the default mode.  
W: --sts flag won't be necessary if you wish to use STS.  
W: --non-sts/--mint-mode flag will be necessary if you do not wish to use STS.  
? OpenShift version: 4.12.28  
? Configure the use of IMDSv2 for ec2 instances optional/required: optional  
? Tags (optional):  
? Multiple availability zones (optional): No  
? AWS region: us-east-2  
? PrivateLink cluster (optional): No  
? Private cluster (optional): No  
? Machine CIDR: 10.0.0.0/16  
? Service CIDR: 172.30.0.0/16  
? Pod CIDR: 10.128.0.0/14  
? Install into an existing VPC (optional): No  
? Select availability zones (optional): No  
? Enable Customer Managed key (optional): No  
? Compute nodes instance type: m5.xlarge  
? Enable autoscaling (optional): No  
? Compute nodes: [? for help] (2)  
  
$ ocm get /api/clusters_mgmt/v1/clusters/25ofgre3jfoi57skj5i6te0jarfms3bl/autoscaler   
{  
"kind": "Error",  
"id": "404",  
"href": "/api/clusters_mgmt/v1/errors/404",  
"code": "CLUSTERS-MGMT-404",  
"reason": "Autoscaler for cluster ID '25ofgre3jfoi57skj5i6te0jarfms3bl' is not found",  
"operation_id": "2c030c57-ce7b-4379-b71a-aeec0cbe653d"  
}
