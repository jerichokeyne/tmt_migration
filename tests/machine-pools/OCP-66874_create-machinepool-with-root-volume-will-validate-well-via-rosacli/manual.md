# Test

## Step
Create machinepool to a cluster whose version lower than 4.10 with volume size set

## Expect
There will be error message returns that volume size only supports on version higher than 4.10

## Step
Prepare a rosa cluster

## Expect

## Step
Create machinepool with a too small volume size set
```bash
rosa create machinepool -c <cluster> --name rootvolume --disk-size 2GiB
```

## Expect
**For classical cluster, minimum disk size is 128GiB**
It will return error message.
```
E: Invalid root disk size: 2 GiB. Must be between 128 GiB and 16384 GiB.
```

**For HCP cluster, minimum disk size is 75GiB
**It will return error message.
```
E: Invalid root disk size: 2 GiB. Must be between 128 GiB and 16384 GiB.
```

## Step
Create machinepool with a large volume size set
```bash
rosa create machinepool -c <cluster> --name rootvolume --disk-size 20000GiB
```

## Expect
As above

## Step
Create machinepool with volume size set which missing unit suffix
```bash
rosa create machinepool -c <cluster> --name rootvolume --disk-size 2
```
~~{ "kind": "MachinePool", "id": "xuelidsk2", "instance_type": "m5.xlarge", "labels": { }, "replicas": 3, "root_volume": { "aws": { "size": 2 } }, "taints": [ ] }~~

## Expect
It will return error message.
```
E: Expected a valid machine pool root disk size value '2': missing unit suffix: '2'. accepted units are Giga or Tera in the form of g, G, GB, GiB, Gi, t, T, TB, TiB, Ti
```

~~It will return error message { "kind": "Error", "id": "400", "href": "/api/clusters_mgmt/v1/errors/400", "code": "CLUSTERS-MGMT-400", "reason": "Invalid root disk size: 2 GiB. Must be between 128 GiB and 1024 GiB.", "details": [ { "Error_Key": "InvalidRootDiskSize" } ], "operation_id": "8d9c5879-8ce5-4fd1-8221-326204fe725d" } For version higher than 4.14, the error message will be : { "kind": "Error", "id": "400", "href": "/api/clusters_mgmt/v1/errors/400", "code": "CLUSTERS-MGMT-400", "reason": "Invalid root disk size: 2 GiB. Must be between 128 GiB and 16384 GiB.", "details": [ { "Error_Key": "InvalidRootDiskSize" } ], "operation_id": "8d9c5879-8ce5-4fd1-8221-326204fe725d" }~~

## Step
Create machinepool with an negative volume size set
```bash
rosa create machinepool -c <cluster> --name rootvolume --disk-size -1GiB
```

## Expect
It will return error message.
```
E: Expected a valid node pool root disk size value '-1GB': invalid disk size: '-1G'. positive size required
```

## Step
Create machinepool with unknown unit like "abcd"
```bash
rosa create machinepool -c <cluster> --name rootvolume --disk-size abcd
```

## Expect
It will return error message.
```
E: Expected a valid node pool root disk size value 'abcd': invalid disk size format: 'abcd'. accepted units are Giga or Tera in the form of g, G, GB, GiB, Gi, t, T, TB, TiB, Ti
```

## Step
Create machinepool with very large value "34567865467898765789GiB"
```bash
rosa create machinepool -c <cluster> --name rootvolume --disk-size 34567865467898765789GiB
```

## Expect
? Replicas: 1
```
I: Checking available instance types for machine pool 'rootvolume'
E: Expected a valid node pool root disk size value '34567865467898765789GiB': invalid disk size: '34567865467898765789Gi'. maximum size exceeded
```
