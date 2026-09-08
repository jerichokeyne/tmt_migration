# Test

## Step
Describe autoscaler when no autoscaler exists in cluster

## Expect
Return error if no autoscaler exists for cluster  
$ rosa describe autoscaler -c 2ac3b5npu88bmqa0m3fk5jij0a2ft4lk   
E: No autoscaler exists for cluster '2ac3b5npu88bmqa0m3fk5jij0a2ft4lk'

## Step
Edit/Delete autoscaler when no autoscaler exists in cluster

## Expect
$ rosa edit autoscaler --cluster=zhsun-4131 --scale-down-delay-after-add 0s --gpu-limit amd.com/gpu,1,5 --max-cores 10 --ignore-daemonsets-utilization  
E: No autoscaler for cluster 'zhsun-4131' has been found. You should first create it via 'rosa create autoscaler'  
$ rosa edit autoscaler --cluster=zhsun-4131   
E: No autoscaler for cluster 'zhsun-4131' has been found. You should first create it via 'rosa create autoscaler'  
$ rosa edit autoscaler --cluster=zhsun-4131 -i   
E: No autoscaler for cluster 'zhsun-4131' has been found. You should first create it via 'rosa create autoscaler'  
$ rosa edit autoscaler --cluster=zhsun-4131 --interactive   
E: No autoscaler for cluster 'zhsun-4131' has been found. You should first create it via 'rosa create autoscaler'  
  
$ rosa delete autoscaler --cluster=zhsun-4131   
E: Failed to delete autoscaler configuration for cluster '2661bolncla3m0moj20ejt9khgojc8g4': Autoscaler for cluster ID '2661bolncla3m0moj20ejt9khgojc8g4' is not found

## Step
Create/update autoscaler without setting "cluster"

## Expect
$ rosa create autoscaler  
Failed to execute root command: required flag(s) "cluster" not set

## Step
Create/update autoscaler with invalid filed   
$ rosa create autoscaler --cluster=zhsun-4131 --invalid invalid --autoscaler-log-verbosity 1

## Expect
$ rosa create autoscaler --cluster=zhsun-4131 --invalid invalid --autoscaler-log-verbosity 1  
Failed to execute root command: unknown flag: --invalid

## Step
Create/update autoscaler with invalid value, test one value every time

## Expect
$ rosa create autoscaler -c zhsun-4131   
I: Enabling interactive mode  
? Balance similar node groups (optional): Yes  
X Sorry, your reply was invalid: Number must be greater or equal to zero.  
? Log verbosity: 4  
? Labels that cluster autoscaler should ignore when considering node group similarity (optional): qqq  
? Ignore daemonsets utilization (optional): Yes  
X Sorry, your reply was invalid: time: unknown unit "-" in duration "9-"  
? Maximum node provision time (optional): 20m  
X Sorry, your reply was invalid: Number must be greater or equal to zero.  
? Maximum pod grace period: 10  
? Pod priority threshold: -4  
? Maximum amount of nodes in the cluster: 200  
X Sorry, your reply was invalid: Number must be greater or equal to zero.  
? Minimum number of cores to deploy in cluster: 10  
X Sorry, your reply was invalid: Number must be greater or equal to zero.  
? Maximum number of cores to deploy in cluster: 10  
X Sorry, your reply was invalid: Number must be greater or equal to zero.  
? Minimum amount of memory, in GiB, in the cluster: 20  
X Sorry, your reply was invalid: max value must be greater or equal than min value 20.  
? Maximum amount of memory, in GiB, in the cluster: 30  
? Enter the number of GPU limitations you wish to set: 1  
? 1. Enter the type of desired GPU limitation: ...  
? 1. Enter minimum number of GPUS of type '...' to deploy in the cluster.: 10  
X Sorry, your reply was invalid: Number must be greater or equal to zero.  
? 1. Enter maximum number of GPUS of type '...' to deploy in the cluster.: 20  
? Should scale-down be enabled (optional): Yes  
X Sorry, your reply was invalid: time: missing unit in duration "60"  
? How long a node should be unneeded before it is eligible for scale down (optional): 60m  
X Sorry, your reply was invalid: Expecting a floating-point number between 0 and 1.  
? Node utilization threshold: 0.3  
? How long after scale up should scale down evaluation resume (optional): 58s  
X Sorry, your reply was invalid: time: unknown unit "d" in duration "40d"  
? How long after node deletion should scale down evaluation resume (optional): 40m  
? How long after node deletion failure should scale down evaluation resume. (optional): 50m  
I: Successfully created autoscaler configuration for cluster '2661bolncla3m0moj20ejt9khgojc8g4'  
  
$ rosa edit autoscaler --cluster=zhsun-4131 --interactive   
X Sorry, your reply was invalid: "kk" is not a valid answer, please try again.  
? Balance similar node groups (optional): Yes  
X Sorry, your reply was invalid: "yy" is not a valid answer, please try again.  
? Skip nodes with local storage (optional): Yes  
? Log verbosity: 00  
X Sorry, your reply was invalid: label 'aaa ' is not a valid Kubernetes label key. It must start with an alphanumeric character and may additionally contain only forward-slashes, dashes, underscores, and dots  
? Labels that cluster autoscaler should ignore when considering node group similarity: ddd  
X Sorry, your reply was invalid: "yy" is not a valid answer, please try again.  
? Ignore daemonsets utilization: Yes  
X Sorry, your reply was invalid: time: missing unit in duration "-80"  
? Maximum node provision time: -80m  
X Sorry, your reply was invalid: Failed parsing 'hh' to an integer number.  
? Maximum pod grace period: 70  
? Pod priority threshold: -70  
X Sorry, your reply was invalid: Number must be greater or equal to zero.  
? Maximum amount of nodes in the cluster: 60  
X Sorry, your reply was invalid: Number must be greater or equal to zero.  
? Minimum number of cores to deploy in cluster: 10  
X Sorry, your reply was invalid: max value must be greater or equal than min value 10.  
? Maximum number of cores to deploy in cluster: 10  
X Sorry, your reply was invalid: Number must be greater or equal to zero.  
? Minimum amount of memory, in GiB, in the cluster: 20  
X Sorry, your reply was invalid: max value must be greater or equal than min value 20.  
? Maximum amount of memory, in GiB, in the cluster: 80  
X Sorry, your reply was invalid: Number must be greater or equal to zero.  
? Enter the number of GPU limitations you wish to set: 1  
? 1. Enter the type of desired GPU limitation: tt  
? 1. Enter minimum number of GPUS of type 'tt' to deploy in the cluster.: 6  
X Sorry, your reply was invalid: max value must be greater or equal than min value 6.  
? 1. Enter maximum number of GPUS of type 'tt' to deploy in the cluster.: 7  
? Should scale-down be enabled: Yes  
? How long a node should be unneeded before it is eligible for scale down: -20s  
X Sorry, your reply was invalid: Expecting a floating-point number between 0 and 1.  
? Node utilization threshold: 0.700000  
X Sorry, your reply was invalid: time: missing unit in duration "-50"  
? How long after scale up should scale down evaluation resume: -50s  
? How long after node deletion should scale down evaluation resume: -40s  
? How long after node deletion failure should scale down evaluation resume.: -30s  
I: Successfully updated autoscaler configuration for cluster '2661bolncla3m0moj20ejt9khgojc8g4'

## Step
Create/update autoscaler with max<min

## Expect
core/memory/gpu max < min, report error.  
$ rosa create autoscaler --cluster zhsun-4131 --min-cores 10 --max-cores 8   
E: Failed creating autoscaler configuration for cluster '2661bolncla3m0moj20ejt9khgojc8g4': max value must be greater or equal than min value 10.  
$ rosa create autoscaler --cluster zhsun-4131 --min-memory 10 --max-memory 8   
E: Failed creating autoscaler configuration for cluster '2661bolncla3m0moj20ejt9khgojc8g4': max value must be greater or equal than min value 10.  
$ rosa create autoscaler --cluster zhsun-4131 --gpu-limit nvidia.com/gpu,0,10 --gpu-limit amd.com/gpu,5,1   
E: Failed creating autoscaler configuration for cluster '2661bolncla3m0moj20ejt9khgojc8g4': Invalid gpus range: 5 - 1: 'min' must be less than or equal to 'max'.  
  
  
? Minimum number of cores to deploy in cluster: 10  
X Sorry, your reply was invalid: max value must be greater or equal than min value 10.  
? Maximum number of cores to deploy in cluster: 10  
X Sorry, your reply was invalid: Number must be greater or equal to zero.  
? Minimum amount of memory, in GiB, in the cluster: 20  
X Sorry, your reply was invalid: max value must be greater or equal than min value 20.  
? Maximum amount of memory, in GiB, in the cluster: 80  
X Sorry, your reply was invalid: Number must be greater or equal to zero.  
? Enter the number of GPU limitations you wish to set: 1  
? 1. Enter the type of desired GPU limitation: tt  
? 1. Enter minimum number of GPUS of type 'tt' to deploy in the cluster.: 6  
X Sorry, your reply was invalid: max value must be greater or equal than min value 6.  
? 1. Enter maximum number of GPUS of type 'tt' to deploy in the cluster.: 7

## Step
Create/describe/edit/delete autoscaler in hosted cluster

## Expect
Should not allowed. Config autoscaler only support on rosa classic, osd aws, osd gcp.  
  
$ rosa describe autoscaler -c sdq-ci-bzoci   
E: Hosted Control Plane clusters do not support cluster-autoscaler configuration

## Step
Create/describe/edit/delete autoscaler in not ready cluster

## Expect
