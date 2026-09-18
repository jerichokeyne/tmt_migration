# Test

## Step
1. Log in with the `rosa` tool and prepare a ready HyperShift ROSA cluster.

## Expect

## Step
2. Enable autoscaling in interactive mode.

```bash
rosa edit machinepool <mpname> -c <cluster_id> -i
```

## Expect
```
? Enable autoscaling (optional): [? for help] (y/N) y
? Enable autoscaling (optional): Yes
? Min replicas (optional): [? for help] 3
? Min replicas (optional): 3
? Max replicas (optional): [? for help] 5
? Max replicas (optional): 5
```

- The operation succeeds without error.
- ~~ClusterAutoscaler and MachineAutoscaler objects are created on the cluster console. `oc get ClusterAutoscaler`; `oc get MachineAutoscaler -n openshift-machine-api`~~
- ~~When describing the MachineAutoscaler~~, check the ManifestWork. It contains the following values:

```
Spec:
Max Replicas: 100
Min Replicas: 4
```

- Check whether autoscaling can be triggered (`OCP-28108`).
- The information can be listed by `rosa list machinepool`.

## Step
3. Repeat step 2 to update the autoscaling configuration.

## Expect
- The operation succeeds without error.
- ~~ClusterAutoscaler and MachineAutoscaler objects are created on the cluster console.~~
- ~~`oc get ClusterAutoscaler`; `oc get MachineAutoscaler -n openshift-machine-api`~~
- When describing the MachineAutoscaler, the following values are shown:

```
Spec:
Max Replicas: 50
Min Replicas: 10
```

- Check whether autoscaling can be triggered (`OCP-28108`).
- The information can be listed by `rosa list machinepool`.

## Step
4. Repeat step 2 from the command line and check `rosa edit machinepool` help.

```bash
rosa edit machinepool <mp-name> --enable-autoscaling --min-replicas=3 --max-replicas=6 -c 1i28ed2fq17dpmtc8ks59g2l22mr2rq2
```

If both `min-replicas` and `max-replicas` are not provided, the tool prompts for them in interactive mode.

## Expect
- The help output contains the following example:

```bash
rosa edit machinepool --enable-autoscaling --min-replicas=3 --max-replicas=5 --cluster=mycluster mp1
```

- The help output contains descriptions for `--enable-autoscaling`, `--max-replicas`, and `--min-replicas`.
- The result is the same as step 2.

## Step
5. Repeat step 4 to update the autoscaling configuration from the command line.

## Expect
The result is the same as step 4.

## Step
6. Disable cluster autoscaling in interactive mode.

```bash
rosa edit machinepool <mp-name> -c 1i264fjuslcbrulqmdhnlhq7p4m4nemo -i
```

## Expect
```
? Enable autoscaling: [? for help] (Y/n) n
? Enable autoscaling: No
? Replicas: [? for help] 3
? Replicas: 3
```

- The patch succeeds and there is no `nodes.autoscale_compute`.
- ~~The ClusterAutoscaler and MachineAutoscaler objects should be deleted on the cluster console. `oc get ClusterAutoscaler` (TBD: No resources found); `oc get MachineAutoscaler -n openshift-machine-api` (No resources found).~~

## Step
7. Disable cluster autoscaling from the command line.

```bash
rosa edit machinepool --replicas=6 -c 1i28ed2fq17dpmtc8ks59g2l22mr2rq2 default
```

## Expect
The result is the same as the preceding step.

## Step
8. Repeat steps 2 through 5 on an additional machine pool.

## Expect
The results are the same as above.

## Step
9. Enable autoscaling while creating a ROSA cluster interactively.

## Expect
The prompts include:

```
? Enable autoscaling (optional): [? for help] (y/N) y
? Enable autoscaling (optional): Yes
? Min replicas: [? for help] (2) 2
? Min replicas: 2
? Max replicas: [? for help] (2) 5
? Max replicas: 5
```

~~The operation succeeds without error. ClusterAutoscaler and MachineAutoscaler objects are created on the cluster console. When describing the MachineAutoscaler, the following values are shown:~~

```
Spec:
Max Replicas: 50
Min Replicas: 10
```

- Check whether autoscaling can be triggered (`OCP-28108`).
- The information can be listed by `rosa list machinepool`.

## Step
10. Repeat all steps on ROSA multi-AZ clusters (not supported in M4).

## Expect
The results are the same as above.

## Step
11. Enable autoscaling during cluster creation.

## Expect
The cluster is created successfully with autoscaling enabled.
