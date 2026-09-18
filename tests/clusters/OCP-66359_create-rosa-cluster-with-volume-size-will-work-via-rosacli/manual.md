# Test

## Step

Login with rosacli and init
```bash
rosa login --token $<token>; rosa init
```

## Expect

It will init successfully

## Step

Create a cluster with volume size set
% rosa create cluster -c xueli --worker-disk-size 200GB

## Expect

The cluster will be created
- Check that the Root disk size is calculated correctly from GB -> GiB
(1GB=1000*1000*1000*1000byte, 1GiB = 1024*1024*1024*1024byte)
- It shows the correct worker disk size as below.
```
"nodes": {
...
"compute_root_volume": {
"aws": {
"size": 186
}
}
},

```

~~Name: xueli ID: 25g0a8uusnck46aiehd1e9171b7uv0bv External ID: Control Plane: Customer Hosted OpenShift Version: Channel Group: stable DNS: Not ready AWS Account: 301721915996 API URL: Console URL: Region: us-west-2 Multi-AZ: false Nodes: - Control plane: 3 - Infra: 2 - Compute: 2 - Root disk size: 186 GiB Network: - Type: OVNKubernetes - Service CIDR: 172.30.0.0/16 - Machine CIDR: 10.0.0.0/16 - Pod CIDR: 10.128.0.0/14 - Host Prefix: /23 Ec2 Metadata Http Tokens: optional State: validating Private: No Created: Aug 8 2023 14:37:27 UTC Details Page: https://qaprodauth.console.redhat.com/openshift/details/s/2Thq1r7hy4rJuH0TeuZXsByhsrK I: To determine when your cluster is Ready, run 'rosa describe cluster -c xueli'. I: To watch your cluster installation logs, run 'rosa logs install -c xueli --watch'.~~

## Step

Check the machinepool root volume size by launching the cluster

## Expect

The default worker should be 186 GiB

## Step

Below should be checking after the day2 machinepool enabled with volume size

## Expect

## Step

List the machinepool of the cluster
```bash
rosa list machinepool -c <cluster>
```

## Expect

There should be correct volume size setting in the default worker

## Step

Describe the machinepool of the cluster
```bash
rosa describe machinepool <machinepool> -c <cluster>
```

## Expect

As above.
