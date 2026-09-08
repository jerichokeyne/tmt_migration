# Test

## Step
Enable machine autoscaler, disable cluster-autoscaler, shouldn't have autoscaler link.  
As long as there is an autoscaler parameter configured, clusterautoscaler should be created.  
  
1) $ rosa create cluster --cluster-name zhsun-ca5 --enable-autoscaling  
2) $ rosa create cluster --cluster-name zhsun-ca2 --enable-autoscaling --autoscaler-balance-similar-node-groups  
  
3) interactive  
? Enable autoscaling (optional): Yes  
? Min replicas: 2  
? Max replicas: 2  
? Configure cluster-autoscaler (optional): No  
$ rosa describe cluster -c zhsun-ca1

## Expect
If autoscaler is not created, no autoscaler link.  
1) $ ocm get /api/clusters_mgmt/v1/clusters/25oi1ntrsltn4l9qsug0ee18ql9k0nq9/autoscaler [22:24:41]  
{  
"kind": "Error",  
"id": "404",  
"href": "/api/clusters_mgmt/v1/errors/404",  
"code": "CLUSTERS-MGMT-404",  
"reason": "Autoscaler for cluster ID '25oi1ntrsltn4l9qsug0ee18ql9k0nq9' is not found",  
"operation_id": "333dfcb1-6aba-450b-94cf-47272f82ec57"  
}  
2) $ ocm get /api/clusters_mgmt/v1/clusters/25oi9s4garuqjtml82i9pgj83484a6as/autoscaler [22:25:55]  
{  
"kind": "ClusterAutoscaler",  
"href": "/api/clusters_mgmt/v1/clusters/25oi9s4garuqjtml82i9pgj83484a6as/autoscaler",  
"balance_similar_node_groups": true,  
"skip_nodes_with_local_storage": true,  
"log_verbosity": 1,  
"max_pod_grace_period": 0,  
"pod_priority_threshold": 0,  
"ignore_daemonsets_utilization": false,  
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
"utilization_threshold": "0.500000"  
}  
}  
  
3) $ ocm get /api/clusters_mgmt/v1/clusters/25oi9counn8g908j1u3j3ljhjngpfd5t/autoscaler [22:26:09]  
{  
"kind": "Error",  
"id": "404",  
"href": "/api/clusters_mgmt/v1/errors/404",  
"code": "CLUSTERS-MGMT-404",  
"reason": "Autoscaler for cluster ID '25oi9counn8g908j1u3j3ljhjngpfd5t' is not found",  
"operation_id": "dd4890b6-92ab-4c61-b24a-7b0906b817ff"  
}

## Step
Create/update autoscaler with invalid value, test one value every time

## Expect
$ rosa create cluster --cluster-name zhsun-ca2 --autoscaler-log-verbosity "invalid"  
Failed to execute root command: invalid argument "invalid" for "--autoscaler-log-verbosity" flag: strconv.ParseInt: parsing "invalid": invalid syntax  
  
X Sorry, your reply was invalid: strconv.Atoi: parsing "invalid": invalid syntax  
? Log verbosity: [? for help] (1)  
  
$ rosa create cluster --cluster-name zhsun-ca2 --autoscaler-scale-down-unneeded-time "invalid"  
W: In a future release STS will be the default mode.  
W: --sts flag won't be necessary if you wish to use STS.  
W: --non-sts/--mint-mode flag will be necessary if you do not wish to use STS.  
I: Creating cluster 'zhsun-ca2'  
I: To view a list of clusters and their status, run 'rosa list clusters'  
E: Failed to create cluster: Cannot parse duration string for field 'unneeded_time': 'invalid' is not a valid duration string.  
  
X Sorry, your reply was invalid: Expecting an integer plus unit of time (without spaces). Options for time units include: ns, us, µs, ms, s, m, h. Examples: 2000000ns, 180s, 2m, etc.  
? How long a node should be unneeded before it is eligible for scale down (optional): [? for help]  
  
$ rosa create cluster --cluster-name zhsun-ca2 --autoscaler-scale-down-utilization-threshold "invalid"  
Failed to execute root command: invalid argument "invalid" for "--autoscaler-scale-down-utilization-threshold" flag: strconv.ParseFloat: parsing "invalid": invalid syntax  
  
$ rosa create cluster --cluster-name zhsun-ca2 --autoscaler-scale-down-delay-after-add --autoscaler-scale-down-delay-after-delete [23:00:25]  
W: In a future release STS will be the default mode.  
W: --sts flag won't be necessary if you wish to use STS.  
W: --non-sts/--mint-mode flag will be necessary if you do not wish to use STS.  
I: Creating cluster 'zhsun-ca2'  
I: To view a list of clusters and their status, run 'rosa list clusters'  
E: Failed to create cluster: Cannot parse duration string for field 'delay_after_add': '--autoscaler-scale-down-delay-after-delete' is not a valid duration string.  
  
$ rosa create cluster --cluster-name zhsun-ca2 --autoscaler-scale-down-delay-after-add  
Failed to execute root command: flag needs an argument: --autoscaler-scale-down-delay-after-add  
  
$ rosa create cluster --cluster-name zhsun-ca2 --autoscaler-min-cores -5 --autoscaler-max-cores 100 [23:07:00]  
W: In a future release STS will be the default mode.  
W: --sts flag won't be necessary if you wish to use STS.  
W: --non-sts/--mint-mode flag will be necessary if you do not wish to use STS.  
I: Creating cluster 'zhsun-ca2'  
I: To view a list of clusters and their status, run 'rosa list clusters'  
E: Failed to create cluster: Bad request body: field 'min' must be non-negative  
  
X Sorry, your reply was invalid: Number must be greater or equal to zero.  
? Maximum number of cores to deploy in cluster: [? for help] (100)  
  
$ rosa create cluster --cluster-name zhsun-ca22 --autoscaler-max-nodes-total -100 [23:11:28]  
W: In a future release STS will be the default mode.  
W: --sts flag won't be necessary if you wish to use STS.  
W: --non-sts/--mint-mode flag will be necessary if you do not wish to use STS.  
I: Creating cluster 'zhsun-ca22'  
I: To view a list of clusters and their status, run 'rosa list clusters'  
E: Failed to create cluster: Bad request body: field 'max_nodes_total' must be non-negative  
  
X Sorry, your reply was invalid: Number must be greater or equal to zero.  
? Maximum amount of nodes in the cluster: [? for help] (1000)

## Step
Create/update autoscaler with max/min out of range

## Expect
$ rosa create cluster --cluster-name zhsun-ca2 --autoscaler-min-cores 5 --autoscaler-max-cores 100000000000000000000000  
Failed to execute root command: invalid argument "100000000000000000000000" for "--autoscaler-max-cores" flag: strconv.ParseInt: parsing "100000000000000000000000": value out of range  
  
X Sorry, your reply was invalid: Failed parsing '100000000000000000000000' to an integer number.  
? Maximum number of cores to deploy in cluster: [? for help] (100)

## Step
Create/update autoscaler with max<min

## Expect
$ rosa create cluster --cluster-name zhsun-ca2 --autoscaler-min-cores 100 --autoscaler-max-cores 5 [23:19:01]  
W: In a future release STS will be the default mode.  
W: --sts flag won't be necessary if you wish to use STS.  
W: --non-sts/--mint-mode flag will be necessary if you do not wish to use STS.  
I: Creating cluster 'zhsun-ca2'  
I: To view a list of clusters and their status, run 'rosa list clusters'  
E: Failed to create cluster: Invalid cores range: 100 - 5: 'min' must be less than or equal to 'max'.  
  
$ rosa create cluster --cluster-name zhsun-ca222 --autoscaler-min-memory 1000 --autoscaler-max-memory 100 [23:28:53]  
W: In a future release STS will be the default mode.  
W: --sts flag won't be necessary if you wish to use STS.  
W: --non-sts/--mint-mode flag will be necessary if you do not wish to use STS.  
I: Creating cluster 'zhsun-ca222'  
I: To view a list of clusters and their status, run 'rosa list clusters'  
E: Failed to create cluster: Invalid memory range: 1000 - 100: 'min' must be less than or equal to 'max'.  
  
$ rosa create cluster --autoscaler-gpu-limit nvidia.com/gpu,0,10 --autoscaler-gpu-limit amd.com/gpu,15,5 --cluster-name zhsun-gp  
u  
E: Failed to create cluster: Invalid gpus range: 15 - 5: 'min' must be less than or equal to 'max'.  
  
Interactive, core/memory/gpu max < min, report error.  
? Minimum number of cores to deploy in cluster (optional): 1000  
X Sorry, your reply was invalid: max value must be greater or equal than min value 1000.  
? Maximum limit for the amount of cores to deploy in the cluster.  
? Maximum number of cores to deploy in cluster: (100)   
  
? Minimum amount of memory, in GiB, in the cluster (optional): 1000  
X Sorry, your reply was invalid: max value must be greater or equal than min value 1000.  
? Maximum limit for the amount of memory, in GiB, in the cluster.  
? Maximum amount of memory, in GiB, in the cluster: (4096)  
  
? Enter the number of GPU limitations you wish to set (optional): 2  
? 1. Enter the type of desired GPU limitation: nvidia.com/gpu111  
? 1. Enter minimum number of GPUS of type 'nvidia.com/gpu111' to deploy in the cluster. (optional): 10  
X Sorry, your reply was invalid: max value must be greater or equal than min value 10.  
? 1. Enter maximum number of GPUS of type 'nvidia.com/gpu111' to deploy in the cluster. (optional): 100

## Step
Create autoscaler in hosted cluster is not allowed. Only support on rosa classic, osd aws, osd gcp.

## Expect
If enable autoscaler No, there are no autoscaler related fields in rosa create cluster command.  
If enable autoscaler Yes, shouldn't have "Configure cluster-autoscaler (optional)" to enable clusterautoscaler.  
Config clusterautoscaler is only supported on rosa classic, osd aws, osd gcp.  
  
$ rosa create cluster --hosted-cp   
E:Hosted Control Plane clusters do not support cluster-autoscaler configuration  
  
<https://issues.redhat.com/browse/OCM-3640>   
interactive mode  
$ rosa create cluster --hosted-cp   
I: Enabling interactive mode  
? Cluster name: zhsun-host  
? Deploy cluster with Hosted Control Plane: Yes  
? Enable autoscaling (optional): Yes  
? Min replicas: 2  
? Max replicas: 2  
Shouldn't have below fields.  
? Configure cluster-autoscaler (optional): Yes  
? Balance similar node groups (optional): No  
? Skip nodes with local storage (optional): No  
? Log verbosity: 1  
? Labels that cluster autoscaler should ignore when considering node group similarity (optional):  
? Ignore daemonsets utilization (optional): Yes  
? Maximum node provision time (optional):  
? Maximum pod grace period (optional):  
? Pod priority threshold (optional):  
? Maximum amount of nodes in the cluster: 1000  
? Minimum number of cores to deploy in cluster (optional):  
? Maximum number of cores to deploy in cluster: 100  
? Minimum amount of memory, in GiB, in the cluster (optional):  
? Maximum amount of memory, in GiB, in the cluster: 4096  
? Should scale-down be enabled (optional): No  
? How long a node should be unneeded before it is eligible for scale down (optional):  
? Node utilization threshold: 0.500000  
? How long after scale up should scale down evaluation resume (optional):  
? How long after node deletion should scale down evaluation resume (optional):  
? How long after node deletion failure should scale down evaluation resume. (optional):  
? Host prefix: 23  
? Machine pool root disk size (GiB or TiB): 300 GiB  
? Enable FIPS support (optional): No  
? Encrypt etcd data (optional): No  
? Disable Workload monitoring (optional): No  
? Use cluster-wide proxy (optional): No  
? Additional trust bundle file path (optional):  
? Enable audit log forwarding to AWS CloudWatch (optional): No  
I: Creating cluster 'zhsun-26'  
I: To create this cluster again in the future, you can run:  
rosa create cluster --cluster-name zhsun-26 --sts --role-arn arn:aws:iam::301721915996:role/zhsun-host-HCP-ROSA-Installer-Role --support-role-arn arn:aws:iam::301721915996:role/zhsun-host-HCP-ROSA-Support-Role --worker-iam-role arn:aws:iam::301721915996:role/zhsun-host-HCP-ROSA-Worker-Role --operator-roles-prefix zhsun-26-i7e5 --oidc-config-id 2668unhs4k5apn3n9oilc41q4e0p2be9 --region us-east-2 --version 4.12.31 --enable-autoscaling --min-replicas 2 --max-replicas 2 --compute-machine-type m5.xlarge --machine-cidr 10.0.0.0/16 --service-cidr 172.30.0.0/16 --pod-cidr 10.128.0.0/14 --host-prefix 23 --subnet-ids subnet-014976475941dfbaf,subnet-0612e89c121666569 --hosted-cp --autoscaler-log-verbosity 1 --autoscaler-max-pod-grace-period 0 --autoscaler-pod-priority-threshold 0 --autoscaler-max-node-provision-time --autoscaler-balancing-ignored-labels --autoscaler-max-nodes-total 1000 --autoscaler-min-cores 0 --autoscaler-max-cores 100 --autoscaler-min-memory 0 --autoscaler-max-memory 4096 --autoscaler-scale-down-utilization-threshold 0.500000
