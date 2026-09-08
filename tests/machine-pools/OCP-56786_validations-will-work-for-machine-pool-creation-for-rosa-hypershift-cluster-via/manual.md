# Test

## Step
Log in the rosa tool and prepare one ROSA Hypershift ready cluster

## Expect

## Step
Create machine pool with invalid value  
$ rosa create machinepool -c <cluster-name> --replicas -9

## Expect
Failed with error:  
~~E: Failed to add machine pool to hosted cluster 'am-hp': Attribute 'replicas' must be a non-negative integer. ~~ E: replicas must be a non-negative integer

## Step
Create nodepool to the cluster with replicas > 180  
$ rosa create machinepool -c <cluster name> --replicas 181 --instance-type m5.xlarge --name new-0-mp

## Expect
Failed with error:  
E: Failed to add machine pool to hosted cluster 'aaraj-hcp': Replicas+Autoscaling.Min: The total number of compute nodes for a single cluster 181 exceeds the maximum allowed: 180

## Step
Create machine pool with invalid name  
$ rosa create machinepool -c <cluster-name> --replicas 0 --name %^#@

## Expect
Failed with error:  
E: Expected a valid name for the machine pool

## Step
Set replicas and enable-autoscaling at the same time  
$ rosa create machinepool -c <cluster-name> --min-replicas 3 --max-replicas 3 --enable-autoscaling --replicas 0 --instance-type m5.2xlarge

## Expect
Failed with error:  
Replicas can't be set when autoscaling is enabled

## Step
Set min-replicas large than max-replicas  
$ rosa create machinepool -c <cluster-name> --min-replicas 9 --max-replicas 3 --enable-autoscaling --instance-type m5.2xlarge

## Expect
Failed with error:  
E: Failed to add machine pool to hosted cluster 'am-hp': Invalid autoscaling range: 9 - 3. 'min_replica' must be less than or equal to 'max_replica'.

## Step
set min-replicas and max-replicas without set --enable-autoscaling  
$ rosa create machinepool -c <cluster-name> --min-replicas 9 --max-replicas 3 --name aaa --instance-type m5.2xlarge

## Expect
Failed with error  
E: Autoscaling must be enabled in order to set min and max replicas

## Step
set max-replicas > 180  
$ rosa create machinepool -c <cluster-name> --enable-autoscaling --min-replicas 1 --max-replicas 92 --name aaa --instance-type m5.2xlarge

## Expect
Failed with error:  
E: Failed to add machine pool to hosted cluster 'aaraj-hcp': Replicas+Autoscaling.Max: The total number of compute nodes for a single cluster 203 exceeds the maximum allowed: 180

## Step
Validate for non-supported machinetypes  
  
$ rosa create machinepool -c <cluster-name> --min-replicas 9 --max-replicas 3 --name aaa --instance-type wrong_type

## Expect
E: Expected a valid machine type: A valid machine type number must be specified

## Step
Validate for not-existing subnet:   
--subnet <not-existing-subnet-id>

## Expect

## Step
Create nodepool with subnet NOT in same vpc with cluster

## Expect

## Step
Create nodepool with label no key

## Expect
> rosa create machinepool -c $CLUSTER_NAME --name nptest --replicas 2 --labels =v  
E: Invalid label key '': name part must be non-empty; name part must consist of alphanumeric characters, '-', '_' or '.', and must start and end with an alphanumeric character (e.g. 'MyName', or 'my.name', or '123-abc', regex used for validation is '([A-Za-z0-9][-A-Za-z0-9_.]*)?[A-Za-z0-9]')

## Step
Create nodepool with taint no key

## Expect
> rosa create machinepool -c $CLUSTER_NAME --name nptest2 --replicas 2 --taints =v:Noschedule  
E: Invalid taint key '': name part must be non-empty; name part must consist of alphanumeric characters, '-', '_' or '.', and must start and end with an alphanumeric character (e.g. 'MyName', or 'my.name', or '123-abc', regex used for validation is '([A-Za-z0-9][-A-Za-z0-9_.]*)?[A-Za-z0-9]')

## Step
Create nodepool with taint no schedule type

## Expect
> rosa create machinepool -c $CLUSTER_NAME --name nptest2 --replicas 2 --taints k=v  
E: Expected key=value:scheduleType format for taints. Got 'k=v'

## Step
Create nodepool with taint empty schedule type

## Expect
> rosa create machinepool -c $CLUSTER_NAME --name nptest2 --replicas 2 --taints k=v:  
E: Expected a not empty effect

## Step
Validate --autorepair parameter - should be boolean

## Expect

## Step
Create a machineppol with a below minimum version:  
rosa create machinepool -c=eld1 --version=4.12.1

## Expect
it will fail

## Step
create a nodepool with --multi-availability-zone flag  
$ rosa create machinepool --multi-availability-zone -c 2c97a883a1q5us0o8gi1arr5pvfitfl2 --name test --replicas 2

## Expect
E: Setting the `multi-availability-zone` flag is not allowed for Hosted Control Plane clusters (OCM-8453)
