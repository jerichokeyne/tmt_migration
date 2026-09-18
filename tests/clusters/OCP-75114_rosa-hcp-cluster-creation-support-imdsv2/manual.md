# Test

## Step

Check the help message of rosa create cluster command

## Expect

It should contains the flag
--ec2-metadata-http-tokens string Should cluster nodes use both v1 and v2 endpoints or just v2 endpoint of EC2 Instance Metadata Service (IMDS)

## Step

Try to create a hcp cluster with --ec2-metadata-http-tokens set as required
```bash
rosa create cluster -c aaraj-hcp --hosted-cp --sts ............ --ec2-metadata-http-tokens required
```

## Expect

The cluster should be created successfully

## Step

Describe the cluster in json format
```bash
rosa describe cluster -c aaraj-hcp -o json | jq -r .aws.ec2_metadata_http_tokens
```

## Expect

The value must be required

## Step

Describe the default workers machinepool of the cluster
```bash
rosa describe machinepool -c aaraj-hcp workers
```

## Expect

ID: workers
Cluster ID: 2clllptf8ee7l2mn5s9kl4mbql31popf
Autoscaling: No
Desired replicas: 2
Current replicas: 0
Instance type: m5.xlarge
Labels:
Tags: api.openshift.com/environment=staging, api.openshift.com/id=2clllptf8ee7l2mn5s9kl4mbql31popf, api.openshift.com/legal-entity-id=1jlfDskrR39egznAq3T18Ul0Xxv, api.openshift.com/name=aaraj-hcp, api.openshift.com/nodepool-hypershift=aaraj-hcp-workers, api.openshift.com/nodepool-ocm=workers, red-hat-clustertype=rosa, red-hat-managed=true
Taints:
Availability zone: us-west-2a
Subnet: subnet-05a6a6f4b591fa783
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
Message: Minimum availability requires 2 replicas, current 0 available

## Step

Try to create a hcp cluster with --ec2-metadata-http-tokens set as optional
```bash
rosa create cluster -c aaraj-hcp --hosted-cp --sts ............ --ec2-metadata-http-tokens optional
```

## Expect

The cluster should be created successfully

## Step

Describe the cluster in json format
```bash
rosa describe cluster -c aaraj-hcp -o json | jq -r .aws.ec2_metadata_http_tokens
```

## Expect

The value must be optional

## Step

Describe the default workers machinepool of the cluster
```bash
rosa describe machinepool -c aaraj-hcp workers
```

**Note: The value of ec2_metadata_http_tokens must be taken from cluster level spec attribute for the default workers nodepool**

## Expect

ID: workers
Cluster ID: 2cllqijvcltjvbh1s2g4raoicamlfp4c
Autoscaling: No
Desired replicas: 2
Current replicas: 0
Instance type: m5.xlarge
Labels:
Tags: api.openshift.com/environment=staging, api.openshift.com/id=2cllqijvcltjvbh1s2g4raoicamlfp4c, api.openshift.com/legal-entity-id=1jlfDskrR39egznAq3T18Ul0Xxv, api.openshift.com/name=aaraj-hcp, api.openshift.com/nodepool-hypershift=aaraj-hcp-workers, api.openshift.com/nodepool-ocm=workers, red-hat-clustertype=rosa, red-hat-managed=true
Taints:
Availability zone: us-west-2a
Subnet: subnet-05a6a6f4b591fa783
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
Message: Minimum availability requires 2 replicas, current 0 available

## Step

Try to create a hcp cluster with --ec2-metadata-http-tokens set as empty value
```bash
rosa create cluster -c aaraj-hcp --hosted-cp --sts ............ --ec2-metadata-http-tokens ""
```

## Expect

The cluster should be created successfully

## Step

Describe the cluster in json format
```bash
rosa describe cluster -c aaraj-hcp -o json | jq -r .aws.ec2_metadata_http_tokens
```

## Expect

The value must be optional

## Step

Describe the default workers machinepool of the cluster
```bash
rosa describe machinepool -c aaraj-hcp workers
```

**Note: The value of ec2_metadata_http_tokens must be taken from cluster level spec attribute for the default workers nodepool**

## Expect

ID: workers
Cluster ID: 2cllqijvcltjvbh1s2g4raoicamlfp4c
Autoscaling: No
Desired replicas: 2
Current replicas: 0
Instance type: m5.xlarge
Labels:
Tags: api.openshift.com/environment=staging, api.openshift.com/id=2cllqijvcltjvbh1s2g4raoicamlfp4c, api.openshift.com/legal-entity-id=1jlfDskrR39egznAq3T18Ul0Xxv, api.openshift.com/name=aaraj-hcp, api.openshift.com/nodepool-hypershift=aaraj-hcp-workers, api.openshift.com/nodepool-ocm=workers, red-hat-clustertype=rosa, red-hat-managed=true
Taints:
Availability zone: us-west-2a
Subnet: subnet-05a6a6f4b591fa783
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
Message: Minimum availability requires 2 replicas, current 0 available
