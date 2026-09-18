# Test

## Step
1. Create an autoscaler when one already exists on the cluster.

```bash
rosa create autoscaler --cluster=zhsun-4131 --max-cores 10 --ignore-daemonsets-utilization
```

## Expect
```
E: Failed creating autoscaler configuration for cluster '2661bolncla3m0moj20ejt9khgojc8g4': Autoscaler associated with cluster ID '2661bolncla3m0moj20ejt9khgojc8g4' already exists. Only one autoscaler object is allowed per cluster.
```

## Step
2. Update an autoscaler without `cluster`.

```bash
rosa edit autoscaler
```

## Expect
```
Failed to execute root command: required flag(s) "cluster" not set
```

## Step
3. Update an autoscaler with an invalid field.

```bash
rosa create autoscaler --cluster=zhsun-4131 --invalid invalid --autoscaler-log-verbosity 1
```

## Expect
```
Failed to execute root command: unknown flag: --invalid
```

## Step
4. Update an autoscaler with invalid values, testing one value at a time.

```bash
rosa edit autoscaler --cluster=zhsun-4131 --interactive
```

## Expect
The interactive prompts reject invalid answers, labels, durations, numeric values, maximums lower than minimums, and scale-down utilization values before accepting the recorded values.

## Step
5. Update an autoscaler with `max < min`.

## Expect
Core, memory, and GPU maximum values less than their minimum values report an error.
