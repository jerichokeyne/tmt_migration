# Test

## Step
Prepare a hcp cluster

## Expect

## Step
Create a nodepool with max-surge and max-unavailable set in percentage value in interactive mode and a lower version to be upgradeable  
$ rosa create machinepool -c aaraj-hcp --interactive  
? Machine pool name: test3  
? OpenShift version (default = '4.15.16'): 4.15.15  
? Select subnet for a hosted machine pool: No  
? AWS availability zone (default = 'us-west-2a'): us-west-2a  
? Enable autoscaling: No  
? Replicas: 3  
? Labels (optional):   
? Taints (optional):   
? Tags (optional):   
I: Checking available instance types for machine pool 'test3'  
? Instance type (default = 'm5.xlarge'): m5.xlarge  
? Autorepair: Yes  
W: No kubelet configs available for cluster '2bsp4507t5kjaqqpsr2brdk18dq3east'. Any kubelet config in input will be ignored  
? Node drain grace period (optional):   
? The maximum number of nodes that can be provisioned above the desired number of nodes in the machinepool during the upgrade. It can be an absolute number i.e. 1, or a percentage i.e. '20%'.  
? Max surge: (5%) 5%  
? The maximum number of nodes in the machinepool that can be unavailable during the upgrade. It can be an absolute number i.e. 1, or a percentage i.e. '20%'.  
? Max unavailable: (10%) 10%

## Expect
I: Machine pool 'test3' created successfully on hosted cluster 'aaraj-hcp'  
I: To view the machine pool details, run 'rosa describe machinepool --cluster aaraj-hcp --machinepool test3'  
I: To view all machine pools, run 'rosa list machinepools --cluster aaraj-hcp'

## Step
Describe the machinepool to check the value is correctly set.  
$ rosa describe machinepool -c aaraj-hcp test3

## Expect
ID: test3  
Cluster ID: 2bsp4507t5kjaqqpsr2brdk18dq3east  
Autoscaling: No  
Desired replicas: 3  
Current replicas: 0  
Instance type: m5.xlarge  
Labels:   
Tags: api.openshift.com/legal-entity-id=1jlfDskrR39egznAq3T18Ul0Xxv, api.openshift.com/name=aaraj-hcp, api.openshift.com/nodepool-hypershift=aaraj-hcp-test3, api.openshift.com/nodepool-ocm=test3, red-hat-clustertype=rosa, red-hat-managed=true, api.openshift.com/environment=staging, api.openshift.com/id=2bsp4507t5kjaqqpsr2brdk18dq3east  
Taints:   
Availability zone: us-west-2a  
Subnet: subnet-00da7443f5b52e2e0  
Version: 4.15.15  
Autorepair: Yes  
Tuning configs:   
Kubelet configs:   
Additional security group IDs:   
Node drain grace period:   
Management upgrade:   
- Type: Replace  
- Max surge: 5%  
- Max unavailable: 10%  
Message: Minimum availability requires 3 replicas, current 0 available

## Step
Try to upgrade the nodepool

## Expect
It should be upgraded successfully

## Step
Create a nodepool with max-surge and max-unavailable set in absolute value in interactive mode and  
$ rosa create machinepool -c aaraj-hcp --interactive  
? Machine pool name: test3  
? OpenShift version (default = '4.15.16'): 4.15.16  
? Select subnet for a hosted machine pool: No  
? AWS availability zone (default = 'us-west-2a'): us-west-2a  
? Enable autoscaling: No  
? Replicas: 3  
? Labels (optional):   
? Taints (optional):   
? Tags (optional):   
I: Checking available instance types for machine pool 'test3'  
? Instance type (default = 'm5.xlarge'): m5.xlarge  
? Autorepair: Yes  
W: No kubelet configs available for cluster '2bsp4507t5kjaqqpsr2brdk18dq3east'. Any kubelet config in input will be ignored  
? Node drain grace period (optional):   
? The maximum number of nodes that can be provisioned above the desired number of nodes in the machinepool during the upgrade. It can be an absolute number i.e. 1, or a percentage i.e. '20%'.  
? Max surge: (2) 2  
? The maximum number of nodes in the machinepool that can be unavailable during the upgrade. It can be an absolute number i.e. 1, or a percentage i.e. '20%'.  
? Max unavailable: (1) 1

## Expect
I: Machine pool 'test3' created successfully on hosted cluster 'aaraj-hcp'  
I: To view the machine pool details, run 'rosa describe machinepool --cluster aaraj-hcp --machinepool test3'  
I: To view all machine pools, run 'rosa list machinepools --cluster aaraj-hcp'

## Step
Describe the machinepool to check the value is correctly set.  
$ rosa describe machinepool -c aaraj-hcp test3

## Expect
ID: test3  
Cluster ID: 2bsp4507t5kjaqqpsr2brdk18dq3east  
Autoscaling: No  
Desired replicas: 3  
Current replicas: 0  
Instance type: m5.xlarge  
Labels:   
Tags: api.openshift.com/legal-entity-id=1jlfDskrR39egznAq3T18Ul0Xxv, api.openshift.com/name=aaraj-hcp, api.openshift.com/nodepool-hypershift=aaraj-hcp-test3, api.openshift.com/nodepool-ocm=test3, red-hat-clustertype=rosa, red-hat-managed=true, api.openshift.com/environment=staging, api.openshift.com/id=2bsp4507t5kjaqqpsr2brdk18dq3east  
Taints:   
Availability zone: us-west-2a  
Subnet: subnet-00da7443f5b52e2e0  
Version: 4.15.15  
Autorepair: Yes  
Tuning configs:   
Kubelet configs:   
Additional security group IDs:   
Node drain grace period:   
Management upgrade:   
- Type: Replace  
- Max surge: 2  
- Max unavailable: 1  
Message: Minimum availability requires 3 replicas, current 0 available

## Step
Edit the nodepool with max-surge and max-unavailable set in percentage value in interactive mode  
$ rosa edit machinepool -c aaraj-hcp test3 --interactive  
? Enable autoscaling: No  
? Replicas: 3  
? Labels (optional):   
? Taints (optional):   
? Autorepair: Yes  
? Node drain grace period (optional):   
? The maximum number of nodes that can be provisioned above the desired number of nodes in the machinepool during the upgrade. It can be an absolute number i.e. 1, or a percentage i.e. '20%'.  
? Max surge: (1%) 1%  
? The maximum number of nodes in the machinepool that can be unavailable during the upgrade. It can be an absolute number i.e. 1, or a percentage i.e. '20%'.  
? Max unavailable: (5%) 5%

## Expect
I: Updated machine pool 'test3' on hosted cluster 'aaraj-hcp'

## Step
Describe the machinepool to check the value is correctly set.  
$ rosa describe machinepool -c aaraj-hcp test3

## Expect
ID: test3  
Cluster ID: 2bsp4507t5kjaqqpsr2brdk18dq3east  
Autoscaling: No  
Desired replicas: 3  
Current replicas: 3  
Instance type: m5.xlarge  
Labels:   
Tags: api.openshift.com/environment=staging, api.openshift.com/id=2bsp4507t5kjaqqpsr2brdk18dq3east, api.openshift.com/legal-entity-id=1jlfDskrR39egznAq3T18Ul0Xxv, api.openshift.com/name=aaraj-hcp, api.openshift.com/nodepool-hypershift=aaraj-hcp-test3, api.openshift.com/nodepool-ocm=test3, red-hat-clustertype=rosa, red-hat-managed=true  
Taints:   
Availability zone: us-west-2a  
Subnet: subnet-00da7443f5b52e2e0  
Version: 4.15.15  
Autorepair: Yes  
Tuning configs:   
Kubelet configs:   
Additional security group IDs:   
Node drain grace period:   
Management upgrade:   
- Type: Replace  
- Max surge: 1%  
- Max unavailable: 5%  
Message:

## Step
Edit the nodepool with max-surge and max-unavailable set in absolute value in interactive mode  
$ rosa edit machinepool -c aaraj-hcp test3 --interactive  
? Enable autoscaling: No  
? Replicas: 3  
? Labels (optional):   
? Taints (optional):   
? Autorepair: Yes  
? Node drain grace period (optional):   
? The maximum number of nodes that can be provisioned above the desired number of nodes in the machinepool during the upgrade. It can be an absolute number i.e. 1, or a percentage i.e. '20%'.  
? Max surge: (1) 1  
? The maximum number of nodes in the machinepool that can be unavailable during the upgrade. It can be an absolute number i.e. 1, or a percentage i.e. '20%'.  
? Max unavailable: (0) 0

## Expect
I: Updated machine pool 'test3' on hosted cluster 'aaraj-hcp'

## Step
Describe the machinepool to check the value is correctly set.  
$ rosa describe machinepool -c aaraj-hcp test3

## Expect
$ rosa describe machinepool -c aaraj-hcp test3  
  
  
ID: test3  
Cluster ID: 2bsp4507t5kjaqqpsr2brdk18dq3east  
Autoscaling: No  
Desired replicas: 3  
Current replicas: 3  
Instance type: m5.xlarge  
Labels:   
Tags: api.openshift.com/nodepool-hypershift=aaraj-hcp-test3, api.openshift.com/nodepool-ocm=test3, red-hat-clustertype=rosa, red-hat-managed=true, api.openshift.com/environment=staging, api.openshift.com/id=2bsp4507t5kjaqqpsr2brdk18dq3east, api.openshift.com/legal-entity-id=1jlfDskrR39egznAq3T18Ul0Xxv, api.openshift.com/name=aaraj-hcp  
Taints:   
Availability zone: us-west-2a  
Subnet: subnet-00da7443f5b52e2e0  
Version: 4.15.15  
Autorepair: Yes  
Tuning configs:   
Kubelet configs:   
Additional security group IDs:   
Node drain grace period:   
Management upgrade:   
- Type: Replace  
- Max surge: 1  
- Max unavailable: 0  
Message:

## Step
Create nodepool with max surge and max unavailable set empty should show default value  
$ rosa create machinepool -c aaraj-hcp-1 -i --max-surge "" --max-unavailable ""  
? Machine pool name: aaraj-hcp  
? OpenShift version (default = '4.16.3'): 4.16.3  
? Select subnet for a hosted machine pool: No  
? AWS availability zone (default = 'us-west-2a'): us-west-2a  
? Enable autoscaling: No  
? Replicas: 1  
? Labels (optional):   
? Taints (optional):   
? Tags (optional):   
I: Checking available instance types for machine pool 'aaraj-hcp'  
? Instance type (default = 'm5.xlarge'): m5.xlarge  
? Autorepair: Yes  
? Tuning configs (optional):   
W: No kubelet configs available for cluster '2crmr0cvactnkc83ef1o828p7mhrnnlo'. Any kubelet config in input will be ignored  
? Configure the use of IMDSv2 for ec2 instances (default = 'optional'): optional  
? Node drain grace period (optional):   
? Max surge (optional):   
? Max unavailable (optional):   
I: Machine pool 'aaraj-hcp' created successfully on hosted cluster 'aaraj-hcp-1'  
I: To view the machine pool details, run 'rosa describe machinepool --cluster aaraj-hcp-1 --machinepool aaraj-hcp'  
I: To view all machine pools, run 'rosa list machinepools --cluster aaraj-hcp-1'

## Expect

## Step
Describe the machinepool to check it has default value  
$ rosa describe machinepool -c aaraj-hcp-1 aaraj-hcp

## Expect
ID: aaraj-hcp  
Cluster ID: 2crmr0cvactnkc83ef1o828p7mhrnnlo  
Autoscaling: No  
Desired replicas: 1  
Current replicas: 0  
Instance type: m5.xlarge  
Labels:   
Tags: red-hat-managed=true, api.openshift.com/environment=staging, api.openshift.com/id=2crmr0cvactnkc83ef1o828p7mhrnnlo, api.openshift.com/legal-entity-id=1jlfDskrR39egznAq3T18Ul0Xxv, api.openshift.com/name=aaraj-hcp-1, api.openshift.com/nodepool-hypershift=aaraj-hcp-1-aaraj-hcp, api.openshift.com/nodepool-ocm=aaraj-hcp, red-hat-clustertype=rosa  
Taints:   
Availability zone: us-west-2a  
Subnet: subnet-00bcf802682ffeefd  
Version: 4.16.3  
EC2 Metadata Http Tokens: optional  
Autorepair: Yes  
Tuning configs:   
Kubelet configs:   
Additional security group IDs:   
Node drain grace period:   
Management upgrade:   
- Type: Replace  
- Max surge: 1  
- Max unavailable: 0  
Message: Minimum availability requires 1 replicas, current 0 available

## Step
Create/edit nodepool with max-surge or max-unavailable set as 0%   
$ rosa create machinepool -c aaraj-hcp-1 --name test --version 4.15.2 --replicas 3 --max-surge 0% --max-unavailable 1% --interactive

## Expect
It should succeed.

## Step
Create/edit nodepool with max-surge or max-unavailable set as 100%   
$ rosa create machinepool -c aaraj-hcp-1 --name test1 --version 4.15.2 --replicas 3 --max-surge 0% --max-unavailable 100% --interactive

## Expect
It should succeed.

## Step
Create/edit nodepool with max-surge or max-unavailable set as 0  
$ rosa create machinepool -c aaraj-hcp-1 --name test2 --version 4.15.2 --replicas 3 --max-surge 0 --max-unavailable 1 --interactive

## Expect
It should succeed.

## Step
edit machinepool with max surge and max unavailable set empty should show previous values that are set  
rosa edit machinepool -c aaraj-hcp np-77 -i --max-surge "" --max-unavailable ""  
? Enable autoscaling: No  
? Replicas: 3  
? Labels (optional):   
? Taints (optional):   
? Autorepair: Yes  
? Node drain grace period (optional):   
? Max surge: 2  
? Max unavailable: 3  
I: Updated machine pool 'np-77' on hosted cluster 'aaraj-hcp'

## Expect
