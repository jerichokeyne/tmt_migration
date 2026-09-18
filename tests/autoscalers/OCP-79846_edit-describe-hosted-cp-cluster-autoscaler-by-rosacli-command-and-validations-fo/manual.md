# Test

## Step
1. Check the help messages.

```bash
rosa describe autoscaler -h
rosa edit autoscaler -h
rosa create autoscaler -h
rosa delete autoscaler -h
```

## Expect
- `rosa create autoscaler -h` contains `Configuring cluster-wide autoscaling behavior. At least one machine-pool should have autoscaling enabled for the configuration to be active. Supported only on ROSA clusters with self-hosted Control Plane (Classic)`.
- `rosa describe autoscaler -h` contains `Describes the configuration for cluster's Cluster Auto-scaler. Supported on ROSA clusters service-hosted (HCP) with self-hosted (Classic) control planes.`
- `rosa delete autoscaler -h` contains `Delete autoscaler configuration for a given cluster. Supported only on ROSA clusters with self-hosted Control Plane (Classic)`.
- All autoscaler configuration flags except `max-nodes-total`, `max-pod-grace-period`, `max-node-provision-time`, and `pod-priority-threshold` state `Only supported for self-hosted (Classic) control plane clusters.`

## Step
2. Prepare a hosted control plane cluster and describe its autoscaler.

```bash
rosa describe autoscaler -c 2h1g414ugutdsai3rd097kfaag2l91bv
```

## Expect
The following default values are displayed.

```
Maximum Node Provision Time: 15m
Maximum Pod Grace Period: 600
Pod Priority Threshold: -10
Resource Limits:
- Maximum Nodes: 0
```

## Step
3. Edit the autoscaler by command.

```bash
rosa edit autoscaler -c 2h0q1fap8484giajtlp75lkue6thj8qk --max-nodes-total 311 --max-pod-grace-period 10000 --max-node-provision-time 1.1m --pod-priority-threshold 1
```

## Expect
- `I: Successfully updated autoscaler configuration for cluster '2h0q1fap8484giajtlp75lkue6thj8qk'` is displayed.
- `rosa describe autoscaler` reflects the interactive input.

## Step
4. Edit the autoscaler again with different values.

## Expect
- The command succeeds.
- `rosa describe autoscaler` reflects the interactive input.

## Step
5. Validate `rosa edit autoscaler` flags.

- Test `max-node-provision-time` with no unit, a negative value (`-10s`), an unknown unit (`100o`), and a value outside `15m` through `60m`.
- Test `pod-priority-threshold` with non-integers (`-11.1`, `34.5`) and a value outside `-21474836485` through `1000000000`.
- Test `max-pod-grace-period` with a negative value (`-100`), a non-integer (`10.1`), and a value below `600` other than `0`; `0` is allowed and means indefinite.
- Test `max-nodes-total` where `X + <all fixed replicas of all worker nodes> + <all minReplicas of all worker nodes> > 500`, and with `-1`.
- Edit with unsupported flags and in interactive mode: `rosa edit autoscaler -c <cluster_id> -i`.

## Expect
```
$ rosa edit autoscaler -c 2h0q1fap8484giajtlp75lkue6thj8qk --max-nodes-total 311 --max-pod-grace-period 10000 --max-node-provision-time 1.1 --pod-priority-threshold 1
E: Failed updating autoscaler configuration for cluster '2h0q1fap8484giajtlp75lkue6thj8qk': time: missing unit in duration "1.1"
E: Failed updating autoscaler configuration for cluster '2h0q1fap8484giajtlp75lkue6thj8qk': Only positive durations are allowed, got '-1s'
E: Failed updating autoscaler configuration for cluster '2h0q1fap8484giajtlp75lkue6thj8qk': time: unknown unit "o" in duration "100o"
E: Failed updating autoscaler configuration for cluster '2h1g414ugutdsai3rd097kfaag2l91bv': status is 400, identifier is '400', code is 'CLUSTERS-MGMT-400', at '2025-02-20T03:17:49Z' and operation identifier is '61c9c734-d572-4bb6-a2be-314f3b937203': Invalid max_node_provision_time '2h': value should be between 15m and 60m
Failed to execute root command: invalid argument "-1.1" for "--pod-priority-threshold" flag: strconv.ParseInt: parsing "-1.1": invalid syntax
E: Failed updating autoscaler configuration for cluster '2h1g414ugutdsai3rd097kfaag2l91bv': status is 400, identifier is '400', code is 'CLUSTERS-MGMT-400', at '2025-02-20T03:19:35Z' and operation identifier is 'fbfb5f0e-855c-4e75-935a-1ea3a9355ac7': Invalid pod_priority_threshold 1000000003: value should be between -21474836485 and 1000000000
E: Failed updating autoscaler configuration for cluster '2h0q1fap8484giajtlp75lkue6thj8qk': Error validating max-pod-grace-period: Number must be greater or equal to zero.
Failed to execute root command: invalid argument "10.1" for "--max-pod-grace-period" flag: strconv.ParseInt: parsing "10.1": invalid syntax
E: Failed updating autoscaler configuration for cluster '2h1g414ugutdsai3rd097kfaag2l91bv': status is 400, identifier is '400', code is 'CLUSTERS-MGMT-400', at '2025-02-20T03:15:38Z' and operation identifier is '5c116d45-e3cb-4bb8-918c-2126469d744b': Invalid max_pod_grace_period 599: value should be larger than 600
E: Failed updating autoscaler configuration for cluster '2h0q1fap8484giajtlp75lkue6thj8qk': status is 400, identifier is '400', code is 'CLUSTERS-MGMT-400', at '2025-02-19T08:55:50Z' and operation identifier is '1f03e5d3-a881-4fde-aedc-695f6a73ca8f': Replicas+Autoscaler.ResourceLimits.MaxNodesTotal: The total number of compute nodes for a single cluster '508' exceeds the maximum allowed '500'. Reduce the total compute nodes requested to be within the maximum allowed.
E: Failed updating autoscaler configuration for cluster '2h0q1fap8484giajtlp75lkue6thj8qk': Error validating max-nodes-total: Number must be greater or equal to zero.
E: Unable to use flag 'log-verbosity' when editing a Hosted Control Plane cluster autoscaler.
Supported flags are: 'max-nodes-total', 'max-pod-grace-period', 'max-node-provision-time', 'pod-priority-threshold'
E: Editing a Hosted Control Plane cluster autoscaler does not support interactive mode
```

## Step
6. Create an autoscaler on a hosted control plane cluster.

```bash
rosa create autoscaler -c 2h0q1fap8484giajtlp75lkue6thj8qk
```

## Expect
```
E: Hosted Control Plane clusters do not support cluster-autoscaler configuration
```

## Step
7. Delete the autoscaler of a hosted control plane cluster.

```bash
rosa delete autoscaler -c 2h0q1fap8484giajtlp75lkue6thj8qk
```

## Expect
```
E: Hosted Control Plane clusters do not support cluster-autoscaler configuration
```
