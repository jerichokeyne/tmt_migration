# Test

## Step
1. Create a cluster with all autoscaler parameters.

```bash
rosa create cluster --cluster-name zhsun-ca2 --autoscaler-balance-similar-node-groups --autoscaler-skip-nodes-with-local-storage --autoscaler-log-verbosity 4 --autoscaler-max-pod-grace-period 0 --autoscaler-pod-priority-threshold 0 --autoscaler-ignore-daemonsets-utilization --autoscaler-max-node-provision-time 10m --autoscaler-balancing-ignored-labels "aaa" --autoscaler-max-nodes-total 1000 --autoscaler-min-cores 0 --autoscaler-max-cores 100 --autoscaler-min-memory 0 --autoscaler-max-memory 4096 --autoscaler-scale-down-enabled --autoscaler-scale-down-utilization-threshold 0.5 --autoscaler-scale-down-delay-after-add 10s --autoscaler-scale-down-delay-after-delete 10s --autoscaler-scale-down-delay-after-failure 10s --enable-autoscaling --min-replicas 2 --max-replicas 6
```

## Expect
The cluster is created successfully and all supplied autoscaler values are retained: enabled balancing, local-storage skipping, and daemonset ignoring; log verbosity `4`; grace period and priority threshold `0`; provision time `10m`; label `aaa`; node limit `1000`; cores `0-100`; memory `0-4096`; scale-down enabled with `0.500000` utilization and `10s` delays; replicas `2-6`.

```bash
rosa describe cluster -c zhsun-ca2
ocm get /api/clusters_mgmt/v1/clusters/25odmobce13h95ru1o94js16t8chq33g/autoscaler
```

## Step
2. Create a cluster without autoscaler boolean parameters.

```bash
rosa create cluster --cluster-name zhsun-ca3 --autoscaler-log-verbosity 4 --autoscaler-max-pod-grace-period 0 --autoscaler-pod-priority-threshold -10 --autoscaler-max-node-provision-time 10m --autoscaler-balancing-ignored-labels "aaa" --autoscaler-max-nodes-total 1000 --autoscaler-min-cores 0 --autoscaler-max-cores 100 --autoscaler-min-memory 0 --autoscaler-max-memory 4096 --autoscaler-scale-down-utilization-threshold 0.5 --autoscaler-scale-down-delay-after-add 10s --autoscaler-scale-down-delay-after-delete 10s --autoscaler-scale-down-delay-after-failure 10s --enable-autoscaling --min-replicas 2 --max-replicas 6
```

## Expect
All boolean autoscaler parameters are `false`. The remaining values are log verbosity `4`, grace period `0`, priority threshold `-10`, provision time `10m`, label `aaa`, node limit `1000`, cores `0-100`, memory `0-4096`, utilization `0.500000`, and `10s` delays.

```bash
ocm get /api/clusters_mgmt/v1/clusters/25oeas6d7o04kq0kt191c7ujvmg9b86d/autoscaler
```

## Step
3. Create a cluster without autoscaler string and integer parameters.

```bash
rosa create cluster --cluster-name zhsun-ca4 --autoscaler-balance-similar-node-groups --autoscaler-skip-nodes-with-local-storage --autoscaler-ignore-daemonsets-utilization --autoscaler-scale-down-enabled --enable-autoscaling --min-replicas 2 --max-replicas 6
```

## Expect
All float and integer parameters use defaults and string parameters are empty. The resulting configuration has enabled balancing, local-storage skipping, daemonset ignoring, and scale-down; log verbosity `1`; grace period `600`; priority threshold `-10`; node limit `180`; cores `0-11520`; memory `0-230400`; and utilization `0.500000`.

```bash
ocm get /api/clusters_mgmt/v1/clusters/25oee36vmsgf6r44juuo8svr6pv7mklt/autoscaler
```

## Step
4. Create a cluster with GPU parameters.

```bash
rosa create cluster --cluster-name zhsun-gpu --autoscaler-gpu-limit nvidia.com/gpu,0,10 --autoscaler-gpu-limit amd.com/gpu,1,5 --enable-autoscaling --min-replicas 2 --max-replicas 6
```

## Expect
The configuration contains GPU limits for `nvidia.com/gpu` from `0` through `10` and `amd.com/gpu` from `1` through `5`.

```bash
ocm get /api/clusters_mgmt/v1/clusters/2625rt07gegu3b01hmu2akmtkvhtqhie/autoscaler
```

## Step
5. Create a cluster with an autoscaler in interactive mode. See [OCP-64494](</polarion/#/project/OSE/workitem?id=OCP-64494>).

```bash
rosa create cluster --cluster-name zhsun-ca5 -i
```

## Expect
- Enter `?` to check help for each parameter.
- Configure autoscaling with replicas `2-2`, balancing and local-storage skipping disabled, log verbosity `1`, ignored label `b`, daemonsets not ignored, grace period `600`, priority threshold `-10`, node limit `180`, cores `0-11520`, memory `0-230400`, GPU type `1` with range `3-12`, scale-down enabled, and utilization `0.500000`.
- The generated command retains those values and OCM reports the same configuration.

```bash
ocm get /api/clusters_mgmt/v1/clusters/293105vhpj1uv57v90tg2t0ivl8p2chc/autoscaler
```

## Step
6. Create a cluster interactively without autoscaling. See [OCP-64494](</polarion/#/project/OSE/workitem?id=OCP-64494>).

```bash
rosa create cluster
```

## Expect
Select `Enable autoscaling (optional): No`. No cluster autoscaler is configured by design; the OCM request for cluster `25ofgre3jfoi57skj5i6te0jarfms3bl` returns `CLUSTERS-MGMT-404` and reports that its autoscaler is not found.

```bash
ocm get /api/clusters_mgmt/v1/clusters/25ofgre3jfoi57skj5i6te0jarfms3bl/autoscaler
```
