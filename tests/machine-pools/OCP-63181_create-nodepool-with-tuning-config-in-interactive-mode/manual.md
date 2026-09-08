# Test

## Step
Prepare a hosted cluster

## Expect

## Step
Create 3 tuning configs to the cluster  
See

## Expect
Tuned configs created successfully

## Step
Create a nodepool with the 3 tuning configs  
~ >rosa create machinepool --name aaraj-worker --replicas 3 -c aaraj-hcp -i  
? Machine pool name: aaraj-worker  
? OpenShift version (default = '4.15.2'): 4.15.2  
? Select subnet for a hosted machine pool: No  
? AWS availability zone (default = 'ap-northeast-1a'): ap-northeast-1a  
? Replicas: 3  
? Labels (optional):   
? Taints (optional):   
I: Checking available instance types for machine pool 'aaraj-worker'  
? Instance type (default = 'm5.xlarge'): m5.xlarge  
? Autorepair: Yes  
? Tuning configs (optional): [Use arrows to move, space to select, <right> to all, <left> to none, type to filter, ? for more help]  
[x] am2  
[x] am1  
> [x] am3

## Expect
I: Machine pool 'aaraj-worker' created successfully on hosted cluster 'aaraj-hcp'  
I: To view the machine pool details, run 'rosa describe machinepool --cluster aaraj-hcp --machinepool aaraj-worker'  
I: To view all machine pools, run 'rosa list machinepools --cluster aaraj-hcp'

## Step
Describe machinepools  
>rosa describe machinepool -c aaraj-hcp aaraj-worker

## Expect
ID: aaraj-worker  
Cluster ID: 2a7ar228hfni73sivslj16tq2fb2i590  
Autoscaling: No  
Desired replicas: 3  
Current replicas: 0  
Instance type: m5.xlarge  
Labels:   
Taints:   
Availability zone: ap-northeast-1a  
Subnet: subnet-003ce22ca4c6dee40  
Version: 4.15.2  
Autorepair: Yes  
Tuning configs: am2,am1,am3  
Additional security group IDs:   
Node drain grace period:   
Message: WaitingForAvailableMachines: NodeProvisioning

## Step
Update the nodepool's tuning to only 1  
~ > rosa edit machinepool aaraj-worker -c aaraj-hcp -i  
? Enable autoscaling: No  
? Replicas: 3  
? Labels (optional):   
? Taints (optional):   
? Autorepair: Yes  
? Tuning configs: [Use arrows to move, space to select, <right> to all, <left> to none, type to filter, ? for more help]  
[ ] am2  
[x] am1  
> [ ] am3

## Expect
I: Updated machine pool 'aaraj-worker' on hosted cluster 'aaraj-hcp'

## Step
Update the nodepool without tuning config  
~ > rosa edit machinepool aaraj-worker -c aaraj-hcp -i  
? Enable autoscaling: No  
? Replicas: 3  
? Labels (optional):   
? Taints (optional):   
? Autorepair: Yes  
? Tuning configs: [Use arrows to move, space to select, <right> to all, <left> to none, type to filter, ? for more help]  
[ ] am2  
> [ ] am1  
[ ] am3

## Expect
I: Updated machine pool 'aaraj-worker' on hosted cluster 'aaraj-hcp'

## Step
Describe machinepools  
> rosa describe machinepools -c aaraj-hcp aaraj-worker

## Expect
No tuning configs are shown  
  
ID: aaraj-worker  
Cluster ID: 2a7ar228hfni73sivslj16tq2fb2i590  
Autoscaling: No  
Desired replicas: 3  
Current replicas: 3  
Instance type: m5.xlarge  
Labels:   
Taints:   
Availability zone: ap-northeast-1a  
Subnet: subnet-003ce22ca4c6dee40  
Version: 4.15.2  
Autorepair: Yes  
Tuning configs:   
Additional security group IDs:   
Node drain grace period:   
Message:
