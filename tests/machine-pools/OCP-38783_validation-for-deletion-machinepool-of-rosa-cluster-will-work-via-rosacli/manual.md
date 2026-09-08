# Test

## Step
Prepare one ROSA cluster

## Expect

## Step
Delete the machinepool of cluster without indicated cluster Name or ID  
1. $ rosa delete machinepool  
2. $ rosa delete machinepool -c <cluster name>

## Expect
Failed with error:  
1. Error: required flag(s) "cluster" not set  
~~Expected exactly one command line argument or flag containing the name or identifier of the cluster <usage> ~~2. E: You need to specify a machine pool name

## Step
Delete a non-existed machinepool  
$ rosa delete machinepool <non existed> -c <cluster name>

## Expect
Failed with error:  
E: Error deleting machinepool: Failed to get machine pool 'test' for cluster '2brdsd8l5fhm5goiib9auiov555bin9b'  
~~Failed to delete machinepool 'xueli-rosa2': There is no machinepool with identifier or name 'xueli-rosa2'~~

## Step
Delete with invalid machinepool id  
$ rosa delete machinepool %^& -c xueli-rosa

## Expect
Failed with error:  
Expected a valid identifier for the machine pool

## Step
Check other options in help message should work  
--profile  
-v

## Expect

## Step
Delete with unknown flag --interactive

## Expect
It will show  
Error: unknown flag: --interactive  
<usage>
