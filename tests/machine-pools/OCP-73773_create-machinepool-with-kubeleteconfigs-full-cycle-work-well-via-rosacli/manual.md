# Test

## Step
Prepare a hosted cluster

## Expect

## Step
Create machinepool with interactive mode

## Expect
There will be no question when there is no kubeletconfigs created to the cluster  
? Kubelet configs:

## Step
Prepare some kubeletconfigs to the cluster

## Expect
There will be a question when there are kubeletconfigs created to the cluster  
? Kubelet configs:

## Step
Type ? to check the help message

## Expect
There will be hint message  
? Name of the kubelet config to be applied to the machine pool. A single kubelet config is allowed. Kubelet config must already exist. This will overwrite any modifications made to node kubelet configs on an ongoing basis.

## Step
Check the list

## Expect
The created kubeconfigs will be listed  
? Kubelet configs (optional): [Use arrows to move, space to select, <right> to all, <left> to none, type to filter]  
> [ ] xueli

## Step
Select one of them

## Expect
The machinepool will be created with the selected kubeconfigs

## Step
Edit the nodepool in interactive mode

## Expect
There will be a question when there are kubeletconfigs created to the cluster  
? Kubelet configs:

## Step
unselect the kubeletconfigs

## Expect
The kubeletconfigs will be unselected

## Step
Update by removing kubeletconfig

## Expect
will succeed

## Step
Describe the machinepool

## Expect
The kubeletconfig is removed from the description

## Step
Prepare a classic cluster

## Expect
Retry interactive mode for machinepool creation/editing  
There will be no question about kubeletconfigs
