# Test

## Step

Run command to check help message
```bash
rosa create cluster -h
```

## Expect

There should be flag
--additional-compute-security-group-ids strings The additional security groups for default worker machine pool.

## Step

Create a cluster with below options set
--additional-compute-security-group-ids
--additional-infra-security-group-ids
--additional-control-plane-security-group-ids
% rosa create cluster --cluster-name xuelisg --version 4.14.0-rc.4 --additional-compute-security-group-ids sg-08f1d3c305c402464 --channel-group candidate --subnet-ids subnet-0d61a41423986be56,subnet-062a2c4efad0a30ff --additional-infra-security-group-ids sg-08f1d3c305c402464 --additional-control-plane-security-group-ids sg-08f1d3c305c402464

For HCP cluster, set only below option:
--additional-compute-security-group-ids (OCM-6053)

## Expect

The cluster will be created

## Step

Wait for cluster ready

## Expect

## Step

Describe the cluster

## Expect

There should be security group of control plane and infra SGs show for cluster details
lixue@Xue-Lis-MacBook-Pro rosa % rosa describe cluster -c xuelisg

Name: xuelisg
ID: 26o1b8eooiqkmr2kikp99ucis32fqmuq
External ID: eab1003e-0dcb-499c-b80b-ad85a2aa11b6
Control Plane: Customer Hosted
OpenShift Version: 4.14.0-rc.4
Channel Group: candidate
DNS: xuelisg.b857.s1.devshift.org
AWS Account: 301721915996
API URL: https://api.xuelisg.b857.s1.devshift.org:6443
Console URL: https://console-openshift-console.apps.xuelisg.b857.s1.devshift.org
Region: us-west-2
Multi-AZ: false
Nodes:
- Control plane: 3
- Infra: 2
- Compute: 2
Network:
- Type: OVNKubernetes
- Service CIDR: 172.30.0.0/16
- Machine CIDR: 10.0.0.0/16
- Pod CIDR: 10.128.0.0/14
- Host Prefix: /23
Workload Monitoring: Enabled
Infra ID: xuelisg-pjvfr
Ec2 Metadata Http Tokens: optional
State: ready
Private: No
Created: Oct 8 2023 08:09:07 UTC
Details Page: https://qaprodauth.console.redhat.com/openshift/details/s/2WTNKhVjYBCqMTrarQDmj4xzeWt

## Step

List the machinepool of the cluster

## Expect

The default worker pool should have the security group listed
lixue@Xue-Lis-MacBook-Pro rosa % rosa list machinepool -c xuelisg
ID AUTOSCALING REPLICAS INSTANCE TYPE LABELS TAINTS AVAILABILITY ZONES SUBNETS SPOT INSTANCES DISK SIZE SG IDs
worker No 2 m5.xlarge us-west-2c subnet-0d61a41423986be56 No 300 GiB [sg-08f1d3c305c402464]

## Step

Launch cluster console to check the machineset of the workerpool (only classic)

## Expect

It has the security groups

## Step

Launch AWS to check the instances (HCP and Classic)

## Expect

They are in correct security groups value
