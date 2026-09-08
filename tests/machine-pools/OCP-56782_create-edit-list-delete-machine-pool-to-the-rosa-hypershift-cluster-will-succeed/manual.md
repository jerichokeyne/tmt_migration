# Test

## Step
Log in the rosa tool and prepare one ROSA Hypershift ready cluster

## Expect

## Step
Run command to record the machine pools  
$ rosa list machinepool -c <cluster name>

## Expect
- The machine pools returned  
ID AUTOSCALING REPLICAS INSTANCE TYPE AVAILABILITY ZONE SUBNET NODEPOOL   
workers No 2 m5.xlarge us-west-2a subnet-093ef2e9cd69cb74d am-hp-workers

## Step
Run command to create default machine pools  
$ rosa create machine -c <cluster name> --replicas 0 --instance-type m5.2xlarge --name new-mp -labels <labels> --taints <taints>

## Expect
- There will be succeeded message output  
  
I: Machine pool 'new-mp' created successfully on cluster 'xueli-rosa'

## Step
Run command to check the machine pools  
$ rosa list machinepool -c <cluster name>

## Expect
- The created machine pool should be listed  
> rosa list machinepool -c am-hp  
ID AUTOSCALING REPLICAS INSTANCE TYPE AVAILABILITY ZONE SUBNET NODEPOOL   
workers No 2 m5.xlarge us-west-2a subnet-093ef2e9cd69cb74d am-hp-workers   
new-mp No 0 m5.xlarge us-west-2a subnet-093ef2e9cd69cb74d am-hp-workers1   
NOTE: from SDA-8219, the labels and taints will show in the output

## Step
Run command to edit an advanced machine pools  
$ rosa edit machinepool new-mp -c <cluster name> --replicas 3 --labels <labels> --taints <taits>  
NOTE: SDA-8272, empty taints value is support ,--taints key=:NoSchedule

## Expect
- There will be succeeded message output

## Step
Run command to check the machine pools  
$ rosa list machinepool -c <cluster name>  
$ rosa describe machinepool new-mp -c <cluster name>

## Expect
list command:  
- The created machine pool should be listed  
- The ID should be set  
- The Autoscaling should be no  
- The replica should be 3  
- The instance type should be m5.2xlarge  
- The available zones should be correct  
- NOTE: from SDA-8219, the labels and taints will show in the output  
  
describe command:  
- The message is the same WaitingForAvailableMachines: NodeProvisioning  
- The MESSAGE is empty for the machinepools MAX after 20 minutes

## Step
Run below command to create an auto scaling machine pools  
$ rosa delete machinepool <machinepool_id> -c <cluster name>

## Expect
? Are you sure you want to delete machine pool 'new-mp' on hosted cluster 'am-hp'? No  
- The machinepool not deleted  
I: Successfully deleted machine pool 'new-mp' from hosted cluster 'am-hp'  
- There will be succeeded message output

## Step
Run command to check the machine pools  
$ rosa list machinepool -c <cluster name>

## Expect
- The deleted machine pool not listed
