# Test

## Step
Prepare one ROSA Hypershift cluster

## Expect

## Step
Delete the machinepool of cluster without indicated ID
```bash
rosa delete machinepool -c <cluster name>
```

## Expect
Failed with error:
Expected exactly one command line argument or flag containing the name or identifier of the cluster
<usage>

## Step
Delete a non-existed machinepool
```bash
rosa delete machinepool <non existed> -c <cluster name>
```

## Expect
Failed with error:
```
E: Failed to get machine pools for hosted cluster 'am-hp': Node pool with id 'gfdtfd' not found.
```

## Step
Delete with invalid machinepool id
```bash
rosa delete machinepool %^& -c <cluster name>
```

## Expect
Failed with error:
Expected a valid identifier for the machine pool

## Step
Check other options in help message should work
--profile
-v

## Expect

## Step
Delete with unknown flag --interactive

## Expect
It will show
```
Error: unknown flag: --interactive
<usage>
```

## Step
Try to delete the latest node pool
~ > rosa delete machinepool workers -c <cluster name>
? Are you sure you want to delete machine pool 'workers' on hosted cluster '<cluster name>'? Yes

## Expect
The error message is shown
```
E: Failed to delete machine pool 'workers' on hosted cluster 'am-hp': The last NodePool can not be deleted from a cluster.
```
