# Test

## Step
Check cluster create cluster help information  
./rosa create cluster --help

## Expect
-There is 'compute-machine-type' flag  
...  
--compute-machine-type string Instance type for the compute nodes. Determines the amount of memory and vCPU allocated to each compute node.  
...

## Step
Create ROSA HCP cluster with --compute-machine-type

## Expect
-The cluster can be created successfully  
-The flag is in the created cluster command

## Step
Check the machinepool instance type  
rosa list machinepool -c <CLUSTER_NAME>

## Expect
-The instance type should be the one selected
