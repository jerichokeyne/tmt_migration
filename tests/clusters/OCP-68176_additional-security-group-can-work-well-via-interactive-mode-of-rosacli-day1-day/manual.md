# Test

## Step
Create rosa cluster via interactive mode  
$ rosa create cluster -i

## Expect

## Step
There will be question show when conditionals meet:  
- byovpc  
- higher or equal 4.14  
- there is sg attached to the vpc without tag red-hat-managed:true  
~~- non-hypershift~~(OCM-6053)  
? Additional 'Compute' Security Group IDs (optional):  
? Additional 'Infra' Security Group IDs (optional): sg-0579a37419dd80b37 ('xueli-2')  
? Additional 'Control Plane' Security Group IDs (optional):

## Expect

## Step
Press "? " to check the help message

## Expect
There will be accurate help message  
The additional security groups for default worker machine pool.

## Step
Check the listed security groups

## Expect
- Only security groups attached to the vpc used by the cluster is listed  
- Only security groups not tagged with red-hat-managed:true listed  
- the "default" security group of the vpc is not listed

## Step
Select some security groups

## Expect

## Step
Create the cluster

## Expect
The cluster will be created successfully

## Step
Check in below conditions the question won't show:  
~~Create cluster via interactive mode that?~~ Deploy cluster with Hosted Control Plane: Yes (OCM-6053)  
Create cluster via interactive mode that ? Install into an existing VPC: No  
Create cluster via interactive mode that ? Version chosen lower than 4.14  
Create cluster via interactive mode that ? There is no security groups attached to the vpc

## Expect
In the conditions the question won't show

## Step
Wait for above cluster ready

## Expect

## Step
Create machinepool to the cluster with interactive mode  
$ rosa create machinepool -i

## Expect

## Step
Check that There is a question  
Additional Security Group IDs (optional):

## Expect
lixue@Xue-Lis-MacBook-Pro tmp % rosa create machinepool -c xuelisg -i  
? Machine pool name: xueli  
? Select subnet for a single AZ machine pool: No  
? Enable autoscaling: No  
? Replicas: 1  
? Additional Security Group IDs (optional): sg-07ba1c8b0d4960a53 ('xueli'), sg-0765ae95046f453e7 ('xuelisg3'), sg-05cdb6f3394a76d9a ('xueli2'), sg-0f0bafffcb9b0260b ('k8s-elb-a8d723be5ac5e4fc991b88a45aa92c5f')  
I: Fetching instance types  
? Instance type: m5.metal  
? Labels (optional): mm=ddd  
? Taints (optional): aaa=ddd:NoSchedule  
? Use spot instances: No  
? Root disk size (GiB or TiB): 150GiB

## Step
Type "?" to check the help message

## Expect
There will be help message  
Security Group IDs to be added to the machine pool

## Step
Check the listed security groups

## Expect
- Only security groups attached to the vpc used by the cluster is listed  
- Only security groups not tagged with red-hat-managed:true listed  
- the "default" security group of the vpc is not listed  
- the sgs with blow tags are not listed  

kubernetes.io/cluster/<cluster_id>:owned is not listed -- HCP only  
or  
kubernetes.io/cluster/<infra id>:owned is not listed -- classic only

## Step
Select some security groups

## Expect

## Step
NOTE: Retry below steps on HCP cluster  
Create the machinepool

## Expect
The machinepool will be created successfully with the selected sgs

## Step
Check in below conditions the question won't show:  
~~Cluster is a hosted cluster~~  
Cluster is non-byo vpc cluster  
Cluster version lower than 4.11/4.15 for hosted cluster  
No security groups attached to the vpc

## Expect
In the conditions the question won't show
