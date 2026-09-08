# Test

## Step
check the help message of   
- rosa describe autoscaler -h  
- rosa edit autoscaler -h  
- rosa create autoscaler -h

## Expect
The help message of `rosa create autoscaler -h` contains "Configuring cluster-wide autoscaling behavior. At least one machine-pool should have autoscaling enabled for the configuration to be active. Supported only on ROSA clusters with self-hosted Control Plane (Classic)"  
  
The help message of `rosa describe autoscaler -h` contains "Describes the configuration for cluster's Cluster Auto-scaler. Supported on ROSA clusters service-hosted (HCP) with self-hosted (Classic) control planes."  
  
the help message of `rosa delete autoscaler -h` contains "Delete autoscaler configuration for a given cluster. Supported only on ROSA clusters with self-hosted Control Plane (Classic)"  
  
For the flags about the autoscaler configurations, all the flags expept 'max-nodes-total', 'max-pod-grace-period', 'max-node-provision-time', 'pod-priority-threshold', has "Only supported for self-hosted (Classic) control plane clusters." description.

## Step
Prepare a hosted-cp cluster then `rosa describe autoscaler -c <cluster_id>`

## Expect
Bellow output should be printed with bellow default value  
  
% ./rosa describe autoscaler -c 2h1g414ugutdsai3rd097kfaag2l91bv   
  
Maximum Node Provision Time: 15m  
Maximum Pod Grace Period: 600  
Pod Priority Threshold: -10  
Resource Limits:  
- Maximum Nodes: 0

## Step
Edit the autoscaler by command  
  
% ./rosa edit autoscaler -c 2h0q1fap8484giajtlp75lkue6thj8qk --max-nodes-total 311 --max-pod-grace-period 10000 --max-node-provision-time 1.1m --pod-priority-threshold 1

## Expect
- "I: Successfully updated autoscaler configuration for cluster '2h0q1fap8484giajtlp75lkue6thj8qk'"  
- `rosa describe autoscaler` the output should be updated as the interactive input

## Step
Edit the autoscaler agian with different values

## Expect
- It shoulld succeed  
- `rosa describe autoscaler` the output should be updated as the interactive input

## Step
Check the valiadtons for `rosa edit autoscaler` flags  
- max-node-provision-time with no unit  
- max-node-provision-time with negative value, '-10s'  
- max-node-provision-time with unknown unit ,'100o'  
- max-node-provision-time with a time not between 15m and 60m  
  
- pod-priority-threshold with a not integer value, '-11.1' '34.5'  
- pod-priority-threshold with a value not between -21474836485 and 1000000000  
  
- max-pod-grace-period with negative value, '-100'  
- max-pod-grace-period with a not integer value '10.1'  
- max-pod-grace-period with a value < 600 but not 0. 0 is allowed, means indefinite  
  
- max-nodes-total with the value X such that X+<all fixed replicas of all worker node> \+ <all minReplicas of all worker nodes> > 500  
- max-nodes-total with negative value, '-1'  
  
- Edit the autoscaler with other unsupported flags.  
  
- Edit autoscaler with interactive mode `rosa edit autoscaler -c <cluster_id> -i`

## Expect
- % ./rosa edit autoscaler -c 2h0q1fap8484giajtlp75lkue6thj8qk --max-nodes-total 311 --max-pod-grace-period 10000 --max-node-provision-time 1.1 --pod-priority-threshold 1  
E: Failed updating autoscaler configuration for cluster '2h0q1fap8484giajtlp75lkue6thj8qk': time: missing unit in duration "1.1"  
- E: Failed updating autoscaler configuration for cluster '2h0q1fap8484giajtlp75lkue6thj8qk': Only positive durations are allowed, got '-1s'  
- E: Failed updating autoscaler configuration for cluster '2h0q1fap8484giajtlp75lkue6thj8qk': time: unknown unit "o" in duration "100o"  
- E: Failed updating autoscaler configuration for cluster '2h1g414ugutdsai3rd097kfaag2l91bv': status is 400, identifier is '400', code is 'CLUSTERS-MGMT-400', at '2025-02-20T03:17:49Z' and operation identifier is '61c9c734-d572-4bb6-a2be-314f3b937203': Invalid max_node_provision_time '2h': value should be between 15m and 60m  
  
- "Failed to execute root command: invalid argument "-1.1" for "--pod-priority-threshold" flag: strconv.ParseInt: parsing "-1.1": invalid syntax" -- it is a error message from rosacli side  
- E: Failed updating autoscaler configuration for cluster '2h1g414ugutdsai3rd097kfaag2l91bv': status is 400, identifier is '400', code is 'CLUSTERS-MGMT-400', at '2025-02-20T03:19:35Z' and operation identifier is 'fbfb5f0e-855c-4e75-935a-1ea3a9355ac7': Invalid pod_priority_threshold 1000000003: value should be between -21474836485 and 1000000000  
  
- E: Failed updating autoscaler configuration for cluster '2h0q1fap8484giajtlp75lkue6thj8qk': Error validating max-pod-grace-period: Number must be greater or equal to zero.  
- "Failed to execute root command: invalid argument "10.1" for "--max-pod-grace-period" flag: strconv.ParseInt: parsing "10.1": invalid syntax" -- it is a error message from rosacli side  
- E: Failed updating autoscaler configuration for cluster '2h1g414ugutdsai3rd097kfaag2l91bv': status is 400, identifier is '400', code is 'CLUSTERS-MGMT-400', at '2025-02-20T03:15:38Z' and operation identifier is '5c116d45-e3cb-4bb8-918c-2126469d744b': Invalid max_pod_grace_period 599: value should be larger than 600  
  
- E: Failed updating autoscaler configuration for cluster '2h0q1fap8484giajtlp75lkue6thj8qk': status is 400, identifier is '400', code is 'CLUSTERS-MGMT-400', at '2025-02-19T08:55:50Z' and operation identifier is '1f03e5d3-a881-4fde-aedc-695f6a73ca8f': Replicas+Autoscaler.ResourceLimits.MaxNodesTotal: The total number of compute nodes for a single cluster '508' exceeds the maximum allowed '500'. Reduce the total compute nodes requested to be within the maximum allowed.  
- E: Failed updating autoscaler configuration for cluster '2h0q1fap8484giajtlp75lkue6thj8qk': Error validating max-nodes-total: Number must be greater or equal to zero.  
  
- E: Unable to use flag 'log-verbosity' when editing a Hosted Control Plane cluster autoscaler.  
Supported flags are: 'max-nodes-total', 'max-pod-grace-period', 'max-node-provision-time', 'pod-priority-threshold'  
  
E: Editing a Hosted Control Plane cluster autoscaler does not support interactive mode

## Step
Create autoscaler on hosted-cp cluster

## Expect
% ./rosa create autoscaler -c 2h0q1fap8484giajtlp75lkue6thj8qk  
E: Hosted Control Plane clusters do not support cluster-autoscaler configuration

## Step
Delete the autoscaler of hosted-cp cluster

## Expect
% ./rosa delete autoscaler -c 2h0q1fap8484giajtlp75lkue6thj8qk  
E: Hosted Control Plane clusters do not support cluster-autoscaler configuration
