# Test

## Step

1. Prepare a ready ROSA cluster.

## Expect

## Step

1. Edit the VPC so that the subnet network cannot work correctly.

Create a VPC, then add deny rules in the VPC Network ACLs, for example to deny port 443, with a rule number less than 100.

## Expect

## Step

1. Verify the network with the cluster ID.

## Expect

- The result fails.
- The domain list differs by cluster type.
- Refer to [the network verifier configuration](https://gitlab.cee.redhat.com/service/osd-network-verifier-golden-ami/-/tree/master/build/config).

## Step

1. Check `--status-only`, `--watch`, and `--region`.

## Expect

## Step

1. Confirm that the network verification result synchronizes to the cluster inflight check.

```bash
rosa describe cluster <>
```

## Expect

- The failed result is displayed in the cluster description.
- The response contains the failed inflight check result:
  - Inflight check ID.
  - Inflight check last-run time.
  - Inflight check private-subnet failure reason.
  - A tip to rerun the network verification command.

```
Name: sdq-rosa-bpcjx
ID: 27ccfk1shne5obr7vvqm84vnejc2okiq
External ID:
Control Plane: Customer Hosted
OpenShift Version:
Channel Group: stable
DNS: Not ready
AWS Account: 301721915996
API URL:
Console URL:
Region: us-east-2
Multi-AZ: true
Nodes:
- Control plane: 3
- Infra: 3
- Compute: 3
Network:
- Type: OVNKubernetes
- Service CIDR: 172.30.0.0/16
- Machine CIDR: 10.0.0.0/16
- Pod CIDR: 10.128.0.0/14
- Host Prefix: /23
Workload Monitoring: Enabled
Ec2 Metadata Http Tokens: optional
State: error (Inflight checks failed. Check inflight checks API for details)
Private: No
Created: Nov 8 2023 05:00:02 UTC
Details Page: https://qaprodauth.console.redhat.com/openshift/details/s/2XsZA9Qdv2bRknvzpp3CgatCMI6
Provisioning Error Code: OCM4001
Provisioning Error Message: Inflight checks failed. Get 'inflight_checks' endpoint for details.
Failed Inflight Checks:
ID: bc8afa3e-b679-44d9-aba4-a5496a5c6d19
Last run: Nov 8 2023 05:03:22 UTC
Invalid configurations on subnet 'subnet-0093e0e8e8bc28f28' have been identified:
Details for 'Egress URL access issues':
- quay-registry.s3.amazonaws.com:443
Invalid configurations on subnet 'subnet-00f1df15c6d6bce33' have been identified:
Details for 'Egress URL access issues':
- events.us-east-2.amazonaws.com:443
Invalid configurations on subnet 'subnet-09db3e4745f1952a4' have been identified:
Details for 'Egress URL access issues':
- ec2.us-east-2.amazonaws.com:443

Please run `rosa verify network -c 27ccfk1shne5obr7vvqm84vnejc2okiq` after adjusting the cluster's network configuration to remove the warning.
```

## Step

1. Remove the AWS deny rule so the subnet network works correctly.

## Expect

- The result synchronizes to the cluster inflight check.
- The passed result is not listed in the cluster description.

## Step

1. ~~Verify the network with subnet IDs.~~ Test with and without `--hosted-cp`.

## Expect

- The result fails.
- The domain list differs by cluster type.
- Refer to [the network verifier configuration](https://gitlab.cee.redhat.com/service/osd-network-verifier-golden-ami/-/tree/master/build/config).

## Step

1. Check `--status-only`, `--watch`, and `--region`.

## Expect

## Step

1. Repeat the steps for BYO VPC STS, non-STS, and Hosted ROSA clusters.

## Expect
