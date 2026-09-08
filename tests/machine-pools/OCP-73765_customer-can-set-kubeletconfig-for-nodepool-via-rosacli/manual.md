# Test

## Step
Prepare a hosted cluster

## Expect

## Step
Check the help message  
$ rosa create machinepool -h

## Expect
There should be a flag as below, check the description should be totally correct  
--kubelet-configs string

## Step
Create a machinepool with --kubelet-configs set  
$ rosa create machinepool -c <cluster> --name kubetest --replicas 0 --kubelet-configs <name>

## Expect
The machinepool is created successfully

## Step
Describe the machinepool

## Expect
It show the kubeletconfig in the description  
lixue@Xue-Lis-MacBook-Pro ~ % rosa describe machinepool --cluster xueli-qigoto7fw --machinepool xueli  
  
ID: xueli  
Cluster ID: 2b9ktom268m3vu0annau2kbmamrt0sc9  
Autoscaling: No  
Desired replicas: 3  
Current replicas: 0  
Instance type: m5.xlarge  
Labels:   
Tags: api.openshift.com/legal-entity-id=1jlfDskrR39egznAq3T18Ul0Xxv, api.openshift.com/nodepool-hypershift=xueli-qigoto7fw-xueli, qe-managed=true, red-hat-managed=true, test-tag=tagvalue, api.openshift.com/environment=staging, api.openshift.com/id=2b9ktom268m3vu0annau2kbmamrt0sc9, api.openshift.com/name=xueli-qigoto7fw, api.openshift.com/nodepool-ocm=xueli, red-hat-clustertype=rosa  
Taints:   
Availability zone: us-west-2a  
Subnet: subnet-010c896c5017463af  
Version: 4.14.24  
Autorepair: Yes  
Tuning configs:   
Kubelet configs: kubelet-2b9ld4hgkg5hipjkm7u5grbnrt1hch73  
Additional security group IDs:   
Node drain grace period:   
Message: Minimum availability requires 3 replicas, current 0 available

## Step
Check the machinepool edit command

## Expect
There will be a flag as below  
lixue@Xue-Lis-MacBook-Pro ~ % rosa edit machinepool -h|grep kubelet   
--kubelet-configs string Name of the kubelet configs to be applied to the machine pool. Format should be a comma-separated list. Kubelet config must already exist. This list will overwrite any modifications made to node kubelet configs on an ongoing basis.

## Step
Edit above machinepool with another kubeletconfig  
$ rosa edit machinepool xueli -c xueli-qigoto7fw --kubelet-configs xueli

## Expect
The machinepool is updated successfully  
lixue@Xue-Lis-MacBook-Pro ~ % rosa edit machinepool xueli -c xueli-qigoto7fw --kubelet-configs xueli  
I: Updated machine pool 'xueli' on hosted cluster 'xueli-qigoto7fw'

## Step
Describe the machinepool and check the output

## Expect
It is changed to the new kubeletconfig  
lixue@Xue-Lis-MacBook-Pro Downloads % rosa describe machinepool --cluster xueli-qigoto7fw --machinepool xueli  
  
ID: xueli  
Cluster ID: 2b9ktom268m3vu0annau2kbmamrt0sc9  
Autoscaling: No  
Desired replicas: 3  
Current replicas: 3  
Instance type: m5.xlarge  
Labels:   
Tags: red-hat-managed=true, test-tag=tagvalue, api.openshift.com/legal-entity-id=1jlfDskrR39egznAq3T18Ul0Xxv, api.openshift.com/nodepool-hypershift=xueli-qigoto7fw-xueli, api.openshift.com/nodepool-ocm=xueli, qe-managed=true, api.openshift.com/environment=staging, api.openshift.com/id=2b9ktom268m3vu0annau2kbmamrt0sc9, api.openshift.com/name=xueli-qigoto7fw, red-hat-clustertype=rosa  
Taints:   
Availability zone: us-west-2a  
Subnet: subnet-010c896c5017463af  
Version: 4.14.24  
Autorepair: Yes  
Tuning configs:   
Kubelet configs: xueli  
Additional security group IDs:   
Node drain grace period:   
Message:

## Step
Update to no kubeletconfig  
$ rosa edit machinepool xueli -c xueli-qigoto7fw --kubelet-configs ""

## Expect
It will succeed  
lixue@Xue-Lis-MacBook-Pro Downloads % rosa edit machinepool xueli -c xueli-qigoto7fw --kubelet-configs ""  
I: Updated machine pool 'xueli' on hosted cluster 'xueli-qigoto7fw'

## Step
Check the machinepool description

## Expect
kubeletconfig is removed  
lixue@Xue-Lis-MacBook-Pro Downloads % rosa describe machinepool --cluster xueli-qigoto7fw --machinepool xueli  
  
ID: xueli  
Cluster ID: 2b9ktom268m3vu0annau2kbmamrt0sc9  
Autoscaling: No  
Desired replicas: 3  
Current replicas: 3  
Instance type: m5.xlarge  
Labels:   
Tags: api.openshift.com/id=2b9ktom268m3vu0annau2kbmamrt0sc9, api.openshift.com/name=xueli-qigoto7fw, api.openshift.com/nodepool-hypershift=xueli-qigoto7fw-xueli, api.openshift.com/nodepool-ocm=xueli, red-hat-clustertype=rosa, test-tag=tagvalue, api.openshift.com/environment=staging, api.openshift.com/legal-entity-id=1jlfDskrR39egznAq3T18Ul0Xxv, qe-managed=true, red-hat-managed=true  
Taints:   
Availability zone: us-west-2a  
Subnet: subnet-010c896c5017463af  
Version: 4.14.24  
Autorepair: Yes  
Tuning configs:   
Kubelet configs:   
Additional security group IDs:   
Node drain grace period:   
Message:

## Step
Attach the kubeletconfig again  
$ rosa edit machinepool xueli -c xueli-qigoto7fw --kubelet-configs xueli

## Expect
It is changed to the new kubeletconfig  
lixue@Xue-Lis-MacBook-Pro Downloads % rosa describe machinepool --cluster xueli-qigoto7fw --machinepool xueli  
  
ID: xueli  
Cluster ID: 2b9ktom268m3vu0annau2kbmamrt0sc9  
Autoscaling: No  
Desired replicas: 3  
Current replicas: 3  
Instance type: m5.xlarge  
Labels:   
Tags: red-hat-managed=true, test-tag=tagvalue, api.openshift.com/legal-entity-id=1jlfDskrR39egznAq3T18Ul0Xxv, api.openshift.com/nodepool-hypershift=xueli-qigoto7fw-xueli, api.openshift.com/nodepool-ocm=xueli, qe-managed=true, api.openshift.com/environment=staging, api.openshift.com/id=2b9ktom268m3vu0annau2kbmamrt0sc9, api.openshift.com/name=xueli-qigoto7fw, red-hat-clustertype=rosa  
Taints:   
Availability zone: us-west-2a  
Subnet: subnet-010c896c5017463af  
Version: 4.14.24  
Autorepair: Yes  
Tuning configs:   
Kubelet configs: xueli  
Additional security group IDs:   
Node drain grace period:   
Message:

## Step
Delete the additional machinepool

## Expect
