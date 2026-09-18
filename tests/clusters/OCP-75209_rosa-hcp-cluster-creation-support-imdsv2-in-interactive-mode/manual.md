# Test

## Step

Try to create a hcp cluster in interactive mode by setting the "Configure the use of IMDSv2 for ec2 instances" value as "optional"
```bash
rosa create cluster -i
```
I: Interactive mode enabled.
Any optional fields can be left empty and a default will be selected.
? Cluster name: aaraj-hcp
? Domain prefix (optional):
? Deploy cluster with Hosted Control Plane: Yes
? Create cluster admin user: No
? Billing Account: 301721915996
I: Using '301721915996' as billing account.
? OpenShift version (default = '4.16.2'): 4.16.2
? Should cluster nodes use both v1 and v2 endpoints or just v2 endpoint of EC2 Instance Metadata Service (IMDS)
? Configure the use of IMDSv2 for ec2 instances (default = 'optional'): [Use arrows to move, type to filter]
```bash
optional
```
required
? Configure the use of IMDSv2 for ec2 instances (default = 'optional'): optional

## Expect

The default value must be showing optional.
The cluster should be created successfully.

## Step

Describe the cluster to see the value of ec2_metadata_http_tokens value at the cluster level spec
```bash
rosa describe cluster -c aaraj-hcp -o json | jq -r .aws.ec2_metadata_http_tokens
```

## Expect

The value should be optional

## Step

Describe the default workers machinepool for the cluster
```bash
rosa describe machinepool -c aaraj-hcp workers
```

## Expect

The value of ec2_metadata_http_tokens must be taken from cluster level spec attribute for the default workers nodepool
ID: workers
Cluster ID: 2cmeo59llnu4er51uoa36pfn33bcfh4q
Autoscaling: No
Desired replicas: 2
Current replicas: 2
Instance type: m5.xlarge
Labels:
Tags: api.openshift.com/nodepool-hypershift=aaraj-hcp-workers, api.openshift.com/nodepool-ocm=workers, red-hat-clustertype=rosa, red-hat-managed=true, api.openshift.com/environment=staging, api.openshift.com/id=2cmeo59llnu4er51uoa36pfn33bcfh4q, api.openshift.com/legal-entity-id=1jlfDskrR39egznAq3T18Ul0Xxv, api.openshift.com/name=aaraj-hcp
Taints:
Availability zone: us-west-2a
Subnet: subnet-026da85fa352a29ec
Version: 4.16.2
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
Message:

## Step

Try to create a hcp cluster in interactive mode by setting the "Configure the use of IMDSv2 for ec2 instances" value as "required"
```bash
rosa create cluster -i
```
I: Interactive mode enabled.
Any optional fields can be left empty and a default will be selected.
? Cluster name: aaraj-hcp-1
? Domain prefix (optional):
? Deploy cluster with Hosted Control Plane: Yes
? Create cluster admin user: No
? Billing Account: 301721915996
I: Using '301721915996' as billing account.
? OpenShift version (default = '4.16.2'): 4.16.2
? Configure the use of IMDSv2 for ec2 instances (default = 'optional'): required

## Expect

The cluster should be created successfully.

## Step

Describe the cluster to see the value of ec2_metadata_http_tokens value at the cluster level spec
```bash
rosa describe cluster -c aaraj-hcp-1 -o json | jq -r .aws.ec2_metadata_http_tokens
```

## Expect

the value should be required.

## Step

Describe the default workers machinepool for the cluster
```bash
rosa describe machinepool -c aaraj-hcp-1 workers
```

## Expect

The value of ec2_metadata_http_tokens must be taken from cluster level spec attribute for the default workers nodepool
ID: workers
Cluster ID: 2cmern4gl1qlbqr7msf0hhnvqgn66rpf
Autoscaling: No
Desired replicas: 2
Current replicas: 2
Instance type: m5.xlarge
Labels:
Tags: red-hat-managed=true, api.openshift.com/environment=staging, api.openshift.com/id=2cmern4gl1qlbqr7msf0hhnvqgn66rpf, api.openshift.com/legal-entity-id=1jlfDskrR39egznAq3T18Ul0Xxv, api.openshift.com/name=aaraj-hcp-1, api.openshift.com/nodepool-hypershift=aaraj-hcp-1-workers, api.openshift.com/nodepool-ocm=workers, red-hat-clustertype=rosa
Taints:
Availability zone: us-west-2a
Subnet: subnet-026da85fa352a29ec
Version: 4.16.2
EC2 Metadata Http Tokens: required
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
