# Test

## Step
Create autoscaler when autoscaler already exists in cluster

## Expect
1) Cli options:  
$ rosa create autoscaler --cluster=zhsun-4131 --max-cores 10 --ignore-daemonsets-utilization   
E: Failed creating autoscaler configuration for cluster '2661bolncla3m0moj20ejt9khgojc8g4': Autoscaler associated with cluster ID '2661bolncla3m0moj20ejt9khgojc8g4' already exists. Only one autoscaler object is allowed per cluster.

## Step
update autoscaler without setting "cluster"

## Expect
$ rosa edit autoscaler  
Failed to execute root command: required flag(s) "cluster" not set

## Step
update autoscaler with invalid filed

## Expect
$ rosa create autoscaler --cluster=zhsun-4131 --invalid invalid --autoscaler-log-verbosity 1  
Failed to execute root command: unknown flag: --invalid

## Step
update autoscaler with invalid value, test one value every time

## Expect
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
update autoscaler with max<min

## Expect
core/memory/gpu max < min, report error.
