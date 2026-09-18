# Test

## Step
Prepare a multi zone ccs cluster with BYOVPC set via rosacli

## Expect

## Step
Create a single zone machinepool with the private subnet used to create the cluster

## Expect
- the 'Subnet ID' list will show after choose "Create multi-AZ machine pool:No" and "Select subnet for a single AZ machine pool (optional): Yes"
- Only the private subnet under the same VPC are shown in the 'Subnet ID' list

- The machinepool is created successfully
- The subnet should be the one used for the machinepool creation
- The availability zone should be detected correctly
- The subnets list should contain the subnet_name and vpc_id and az info,If the subnet name is empty , it will show as ''

## Step
Retrieve the machinepool.
\# rosa list machinepool

## Expect
- The subnet used for the machinepool creation will be in the 'SUBNETS' colume.
- The availability zone should be detected correctly

## Step
Launch cluster console to check the machine
```bash
oc get machine -n openshift-machine-api
```

## Expect
- The machine should be started correctly and finally running

## Step
Prepare another subnet belongs to same vpc in other zones and has a label of [kubernetes.io/cluster/](<http://kubernetes.io/cluster/>)<cluster-name>: shared

## Expect

## Step
Create machinepool with the subnet

## Expect
- The new created subnet will be shown in the 'Subnet ID' list.

- The machinepool should be created successfully
- The zone should be detected correctly

## Step
Launch cluster console to check the machine
```bash
oc get machine -n openshift-machine-api
```

## Expect
- The machine should be started correctly and finally running

## Step
Scale up and down the machinepool by `rosa edit machinepool`

## Expect

## Step
Launch console to check the machine

## Expect
- The machine should be started correctly and finally running

## Step
Prepare a multi zone sts cluster with BYOVPC set and repeat above steps

## Expect
The result should be same with the above ones

## Step
Prepare a multi zone privatelink cluster and repeat above steps

## Expect
The result should be same with the above ones

## Step
Repeat above steps on single zone cluster.

## Expect
