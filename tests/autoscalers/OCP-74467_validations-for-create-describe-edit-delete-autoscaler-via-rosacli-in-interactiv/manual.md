# Test

## Step
1. Create an autoscaler interactively when one already exists. See <https://issues.redhat.com/browse/OCM-3643>.

```bash
rosa create autoscaler --cluster=zhsun-4131
```

## Expect
The interactive transcript ends with:

```
E: Failed creating autoscaler configuration for cluster '2661bolncla3m0moj20ejt9khgojc8g4': Autoscaler associated with cluster ID '2661bolncla3m0moj20ejt9khgojc8g4' already exists. Only one autoscaler object is allowed per cluster.
```

## Step
2. Create an autoscaler with invalid values, testing one value at a time in interactive mode.

```bash
rosa create autoscaler -c zhsun-4131
```

## Expect
Interactive validation rejects invalid values for log verbosity, durations, pod grace period, cores, memory, GPU limits, and scale-down utilization; then it accepts the recorded valid values and creates the autoscaler.

## Step
3. Update an autoscaler with invalid values, testing one value at a time in interactive mode.

```bash
rosa edit autoscaler --cluster=zhsun-4131 --interactive
```

## Expect
Interactive validation rejects invalid answers, labels, durations, pod grace period, cores, memory, GPU limits, and utilization; then it accepts the recorded valid values and updates the autoscaler.

## Step
4. Update an autoscaler with `max < min` in interactive mode.

## Expect
Core, memory, and GPU maximum values less than their minimum values report an error.

## Step
5. Create an autoscaler with `max < min` in interactive mode.

## Expect
Core, memory, and GPU maximum values less than their minimum values report an error.
