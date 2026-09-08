# Test

## Step
Craete autoscaler Interactively should return error immediately if autoscaler already exist exists <https://issues.redhat.com/browse/OCM-3643> :  
$ rosa create autoscaler --cluster=zhsun-4131   
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
E: Failed creating autoscaler configuration for cluster '2661bolncla3m0moj20ejt9khgojc8g4': Autoscaler associated with cluster ID '2661bolncla3m0moj20ejt9khgojc8g4' already exists. Only one autoscaler object is allowed per cluster.

## Expect

## Step
create autoscaler with invalid value, test one value every time in interactive mode

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

## Step
update autoscaler with invalid value, test one value every time in interactive mode

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
update autoscaler with max<min in interactive mode

## Expect
core/memory/gpu max < min, report error.

## Step
create autoscaler with max<min in interactive mode

## Expect
core/memory/gpu max < min, report error.
