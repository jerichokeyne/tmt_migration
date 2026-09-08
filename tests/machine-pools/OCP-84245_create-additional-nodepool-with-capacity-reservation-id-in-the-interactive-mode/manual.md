# Test

## Step
Prepare on-demand Capacity Reservation on specific az and with specifc instance type

## Expect

## Step
Prepare a ready hosted-cp cluster

## Expect

## Step
Create machinepool in the interactive mode

## Expect
- There is questionaire of "? Capacity Reservation ID (optional):" and its help message is "? The ID of an AWS On-Demand Capacity Reservation. The 'capacity-reservation-id' must be pre-created in advance, before creating a NodePool."

## Step
Choose No at "autoscaling option" and the az/subnet and instance type matched with the on-demand Capacity Reservation and at the "? Capacity Reservation ID (optional):" input the reservation id created in step1

## Expect
- The nodepool should be created successfully.  
- 'rosa describe machinepool ' will show the "Capacity Reservation" field with type and id:  
% ./rosa describe machinepool --cluster 2ktf5ln6lmllejp5p8orf40o84u5mop8 --machinepool y2  
  
ID: y2  
Cluster ID: 2ktf5ln6lmllejp5p8orf40o84u5mop8  
Autoscaling: No  
Desired replicas: 1  
Current replicas: 0  
Instance type: m5.xlarge  
Labels:   
Tags: api.openshift.com/environment=staging, api.openshift.com/id=2ktf5ln6lmllejp5p8orf40o84u5mop8, api.openshift.com/legal-entity-id=2wLZWMFZgGEBkd1MBfJPtHTFSJZ, api.openshift.com/name=yuwan0826t1-cpi, api.openshift.com/nodepool-hypershift=yuwan0826t1-cpi-y2, api.openshift.com/nodepool-ocm=y2, red-hat-clustertype=rosa, red-hat-managed=true  
Taints:   
Availability zone: us-west-2b  
Subnet: subnet-095148bf01ee6b871  
Disk Size: 300 GiB  
Version: 4.18.20  
EC2 Metadata Http Tokens: optional  
Autorepair: Yes  
Tuning configs:   
Kubelet configs:   
Additional security group IDs:   
Node drain grace period:   
Capacity Reservation:   
- ID: cr-00b32b6e1312afe3b  
- Type: OnDemand  
Management upgrade:   
- Type: Replace  
- Max surge: 1  
- Max unavailable: 0  
Message: WaitingForAvailableMachines

## Step
Check error of validation failure from backend.  
- The az is not mataching with the reservation  
- The subnet is not mataching with the reservation  
- The instance type is not mataching with the reservation  
- Choose autoscaling  
- Input invalid reservation id

## Expect
- Will fail at last and return error from backend  
E: Failed to add machine pool to hosted cluster '2ktf5ln6lmllejp5p8orf40o84u5mop8': status is 400, identifier is '400', code is 'CLUSTERS-MGMT-400', at '2025-08-26T08:45:01Z' and operation identifier is 'c13228e8-de3e-4fc6-bbcc-780689af1b50': Capacity reservation 'cr-00b32b6e1312afe3b' availability zone 'us-west-2b' does not match machine pool availability zone 'us-west-2a'  
  
E: Failed to add machine pool to hosted cluster '2ktf5ln6lmllejp5p8orf40o84u5mop8': status is 400, identifier is '400', code is 'CLUSTERS-MGMT-400', at '2025-08-26T08:39:30Z' and operation identifier is '2bae0478-9692-4a31-9a65-a0c482c3ed3a': Capacity reservation 'cr-00b32b6e1312afe3b' instance type 'm5.xlarge' does not match machine pool instance type 'm5a.xlarge'  
  
E: Failed to add machine pool to hosted cluster '2ktf5ln6lmllejp5p8orf40o84u5mop8': status is 400, identifier is '400', code is 'CLUSTERS-MGMT-400', at '2025-08-26T08:33:20Z' and operation identifier is 'd001cc2f-78e2-423f-b750-96c56284db20': Replicas must be specified when using AWS Capacity Reservations  
  
E: Failed to add machine pool to hosted cluster '2ktf5ln6lmllejp5p8orf40o84u5mop8': status is 400, identifier is '400', code is 'CLUSTERS-MGMT-400', at '2025-08-26T09:44:30Z' and operation identifier is '17a2da88-2506-48f2-8a05-713709546942': Capacity reservation 'cr-asdkasklfla' not found or access denied

## Step
Repeat above step with Capacity Block for ML ID.  
NOTE: this kind of reservation will have a huge cost, be cautious about it!

## Expect
The result should be same with above.
