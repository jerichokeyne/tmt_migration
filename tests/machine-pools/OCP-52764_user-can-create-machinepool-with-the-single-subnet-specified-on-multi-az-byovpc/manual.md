# Test

## Step
Prepare a multi zone sts cluster with BYOVPC set via rosacli

## Expect

## Step
Create a single zone machinepool with the private subnet used to create the cluster  
\# rosa create machinepool -c yuwan-stswj4 --name d5d --replicas=3 --subnet <subnet-id>

## Expect
- The machinepool is created successfully  
- The subnet should be the one used for the machinepool creation  
- The availability zone should be detected correctly

## Step
Retrieve the machinepool.  
\# rosa list machinepool

## Expect
- The subnet used for the machinepool creation will be in the 'SUBNETS' colume.  
- The availability zone should be detected correctly

## Step
~~Launch cluster console to check the machine $ oc get machine -n openshift-machine-api~~

## Expect
- The machine should be started correctly and finally running

## Step
Prepare another subnet belongs to same vpc in other zones and has a label of [kubernetes.io/cluster/](<http://kubernetes.io/cluster/>)<cluster-name>: shared

## Expect

## Step
Create machinepool with the subnet  
\# rosa create machinepool -c yuwan-stswj4 --name d5d --replicas=3 --subnet <subnet-id>

## Expect
- The machinepool should be created successfully  
- The zone should be detected correctly

## Step
Retrieve the machinepool.  
\# rosa list machinepool

## Expect
- The subnet used for the machinepool creation will be in the 'SUBNETS' colume.  
- The availability zone should be detected correctly

## Step
~~Launch cluster console to check the machine $ oc get machine -n openshift-machine-api~~

## Expect
~~- The machine should be started correctly and finally running~~

## Step
Scale up and down the machinepool by `rosa edit machinepool`

## Expect

## Step
~~Launch console to check the machine~~

## Expect
~~- The machine should be started correctly and finally running~~

## Step
Retrieve the machinepool.  
\# rosa list machinepool

## Expect
- The machinepool should be created successfully  
- The zone should be detected correctly

## Step
Prepare a multi zone privatelink cluster and repeat above steps

## Expect
The result should be same with the above ones

## Step
Repeat on a single zone cluster

## Expect
It will work as expected
