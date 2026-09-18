# Test

## Step
1. Create an autoscaler with CLI options.

```bash
rosa create autoscaler --cluster zhsun-4131 --balance-similar-node-groups --skip-nodes-with-local-storage --log-verbosity 4 --max-pod-grace-period 0 --pod-priority-threshold 0 --ignore-daemonsets-utilization --max-node-provision-time 10m --balancing-ignored-labels "aaa" --max-nodes-total 1000 --min-cores 0 --max-cores 100 --min-memory 0 --max-memory 4096 --scale-down-enabled --scale-down-utilization-threshold 0.5 --scale-down-delay-after-add 10s --scale-down-delay-after-delete 10s --scale-down-delay-after-failure 10s --gpu-limit nvidia.com/gpu,0,10 --gpu-limit amd.com/gpu,1,5 --scale-down-unneeded-time 10s
```

## Expect
- All 20 fields are covered and correct.
- The autoscaler configuration matches the supplied values: balanced and local-storage skipping enabled, log verbosity `4`, grace period and priority threshold `0`, daemonsets ignored, provision time `10m`, ignored label `aaa`, node limit `1000`, cores `0-100`, memory `0-4096`, NVIDIA GPU `0-10`, AMD GPU `1-5`, and enabled scale-down settings of `10s` and utilization `0.500000`.

```
I: Successfully created autoscaler configuration for cluster '2661bolncla3m0moj20ejt9khgojc8g4'
```

```bash
rosa delete autoscaler --cluster=zhsun-4131
```

```
I: Successfully deleted autoscaler configuration for cluster '2661bolncla3m0moj20ejt9khgojc8g4'
```

## Step
2. Create an autoscaler interactively.

```bash
rosa create autoscaler -c zhsun-4133
```

## Expect
- `-i`, `--interactive`, or no autoscaler configuration prompts for each option.
- Enter `?` to check help for each parameter.
- All parameters are covered and the created configuration matches the selections.

## Step
3. Describe an autoscaler in default, JSON, and YAML formats.

```bash
rosa describe autoscaler -c 2ac3b5npu88bmqa0m3fk5jij0a2ft4lk
rosa describe autoscaler -h
rosa describe autoscaler -c 2ac3b5npu88bmqa0m3fk5jij0a2ft4lk -o json
rosa describe autoscaler -c 2ac3b5npu88bmqa0m3fk5jij0a2ft4lk -o yaml
```

## Expect
All command results are valid. The output includes the values from step 1, including the two GPU limits and scale-down values.

## Step
4. Edit an autoscaler using CLI options.

```bash
rosa edit autoscaler --cluster=zhsun-4131 --scale-down-delay-after-add 0s --gpu-limit amd.com/gpu,1,5 --max-cores 10 --min-cores 0 --ignore-daemonsets-utilization
```

## Expect
All 20 fields are covered and correct. The existing configuration is retained except that daemonsets are ignored, maximum cores is `10`, AMD GPU range is `1-5`, and scale-down delay after add is `0s`.

```
I: Successfully updated autoscaler configuration for cluster '2661bolncla3m0moj20ejt9khgojc8g4'
```

## Step
5. Edit only some attributes (`OCM-10460`).

```bash
rosa edit autoscaler -c awesome-cluster --max-cores=10000 --min-cores=0
```

## Expect
- Only the two attributes change.
- Other attributes retain their original values.

## Step
6. Edit an autoscaler interactively.

```bash
rosa edit autoscaler --cluster=zhsun-4131 --interactive
```

## Expect
- Enter `?` to check help for each parameter.
- All parameters are covered and show their original values.
- The resulting configuration has log verbosity `90`, ignored label `ccc`, daemonsets ignored, provision time `30m`, grace period and priority threshold `30`, node limit `300`, cores and memory `30-300`, scale-down enabled with `30s` delays and utilization `0.700000`; the existing GPU type `m` remains `20-200`.

## Step
7. Delete an autoscaler using the CLI.

```bash
rosa delete cluster -h
rosa delete autoscaler --cluster=zhsun-4131
ocm get /api/clusters_mgmt/v1/clusters/2661bolncla3m0moj20ejt9khgojc8g4/autoscaler
```

## Expect
The delete help examples concern autoscalers, deletion succeeds, and the OCM request returns `CLUSTERS-MGMT-404` with reason `Autoscaler for cluster ID '2661bolncla3m0moj20ejt9khgojc8g4' is not found`.
