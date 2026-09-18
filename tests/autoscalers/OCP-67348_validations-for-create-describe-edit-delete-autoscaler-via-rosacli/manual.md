# Test

## Step
1. Describe an autoscaler when none exists on the cluster.

```bash
rosa describe autoscaler -c 2ac3b5npu88bmqa0m3fk5jij0a2ft4lk
```

## Expect
```
E: No autoscaler exists for cluster '2ac3b5npu88bmqa0m3fk5jij0a2ft4lk'
```

## Step
2. Edit or delete an autoscaler when none exists on the cluster.

```bash
rosa edit autoscaler --cluster=zhsun-4131 --scale-down-delay-after-add 0s --gpu-limit amd.com/gpu,1,5 --max-cores 10 --ignore-daemonsets-utilization
rosa edit autoscaler --cluster=zhsun-4131
rosa edit autoscaler --cluster=zhsun-4131 -i
rosa edit autoscaler --cluster=zhsun-4131 --interactive
rosa delete autoscaler --cluster=zhsun-4131
```

## Expect
```
E: No autoscaler for cluster 'zhsun-4131' has been found. You should first create it via 'rosa create autoscaler'
E: Failed to delete autoscaler configuration for cluster '2661bolncla3m0moj20ejt9khgojc8g4': Autoscaler for cluster ID '2661bolncla3m0moj20ejt9khgojc8g4' is not found
```

## Step
3. Create or update an autoscaler without `cluster`.

```bash
rosa create autoscaler
```

## Expect
```
Failed to execute root command: required flag(s) "cluster" not set
```

## Step
4. Create or update an autoscaler with an invalid field.

```bash
rosa create autoscaler --cluster=zhsun-4131 --invalid invalid --autoscaler-log-verbosity 1
```

## Expect
```
Failed to execute root command: unknown flag: --invalid
```

## Step
5. Create or update an autoscaler with invalid values, testing one value at a time in interactive mode.

```bash
rosa create autoscaler -c zhsun-4131
rosa edit autoscaler --cluster=zhsun-4131 --interactive
```

## Expect
The prompts reject invalid log verbosity, labels, durations, numeric values, maximums lower than minimums, and scale-down utilization values, then accept the recorded valid values and create or update the autoscaler.

## Step
6. Create or update an autoscaler with `max < min`.

```bash
rosa create autoscaler --cluster zhsun-4131 --min-cores 10 --max-cores 8
rosa create autoscaler --cluster zhsun-4131 --min-memory 10 --max-memory 8
rosa create autoscaler --cluster zhsun-4131 --gpu-limit nvidia.com/gpu,0,10 --gpu-limit amd.com/gpu,5,1
```

## Expect
```
E: Failed creating autoscaler configuration for cluster '2661bolncla3m0moj20ejt9khgojc8g4': max value must be greater or equal than min value 10.
E: Failed creating autoscaler configuration for cluster '2661bolncla3m0moj20ejt9khgojc8g4': Invalid gpus range: 5 - 1: 'min' must be less than or equal to 'max'.
```

Interactive core, memory, and GPU maximum values lower than their minimum values also report errors.

## Step
7. Create, describe, edit, or delete an autoscaler in a hosted control plane cluster.

```bash
rosa describe autoscaler -c sdq-ci-bzoci
```

## Expect
```
E: Hosted Control Plane clusters do not support cluster-autoscaler configuration
```

## Step
8. Create, describe, edit, or delete an autoscaler in a not-ready cluster.

## Expect
