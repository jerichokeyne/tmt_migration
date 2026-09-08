# Test

## Step
Prepare a rosa non- sts byovpc multi-az cluster on the region which has local zone

## Expect

## Step
Create single-az local zone machinepool by the rosacli command with some invalid flag value:  
- the subnet without the required label  
- not-existed subnet id in the cluster region  
- the subnet id which is not under the same vpc of the cluster  
- the instance type which is not supported on the local zone   
- Setting --use-spot-instances flag

## Expect
It should failed with the readable error message.  
examples of some error message:  
E: Failed to add machine pool to cluster '1vtph47k2daro4vi19l7829j59o8slqk': Subnet with ID 'subnet-040c9f201c25fbb88' must have the following tag 'kubernetes.io/cluster/yuwan-dsrm1-g97bk:shared' in order to be assigned a single AZ machine pool  
  
E: Failed to add machine pool to cluster '1vtph47k2daro4vi19l7829j59o8slqk': Subnet with ID 'subnet-040c9f201c25fbb88' must belong to cluster's VPC 'vpc-0a57094837feb791c' in order to be assigned a single AZ machine pool  
  
E: Failed to add machine pool to cluster '1vtph47k2daro4vi19l7829j59o8slqk': Subnet with ID 'subnet-024262c9dc371a908' is a public subnet (has an Internet Gateway attached), please provide a private subnet to create a single AZ machine pool  
  
E: Expected a valid machine type: A valid machine type number must be specified  
Valid machine types: t3.xlarge c5d.2xlarge  
  
E: Spot instances are not supported for local zones

## Step
Prepare a rosa non- sts byovpc single-az cluster on the region which has local zone

## Expect

## Step
Create single-az local zone machinepool by the rosacli command with some invalid flag value:  
- the subnet without the required label  
- not-existed subnet id in the cluster region  
- the subnet id which is not under the same vpc of the cluster  
- the instance type which is not supported on the local zone   
- Setting --use-spot-instances flag

## Expect
It should failed with the readable error message
