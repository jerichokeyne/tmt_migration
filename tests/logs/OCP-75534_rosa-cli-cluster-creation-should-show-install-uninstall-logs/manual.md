# Test

## Step
1. Create one Hypershift cluster.

## Expect

## Step
2. Check the install logs of the Hypershift cluster.

```bash
rosa logs install -c <cluster name>
```

## Expect
- The logs are shown correctly.

## Step
3. Check the install logs of the Hypershift cluster with the `--watch` flag.

```bash
rosa logs install -c <cluster name> --watch
```

## Expect
- The process does not exit until cluster installation finishes or the cluster enters an error state.

## Step
4. Delete the Hypershift cluster by `rosa delete cluster`.

## Expect
- The cluster can be deleted.
- All resources on AWS should be deleted.

## Step
5. Check the uninstall log of the hosted cluster.

```bash
rosa log uninstall -c <cluster name>
```

## Expect
- The uninstall log is shown correctly.

## Step
6. Check the uninstall log of the hosted cluster with the `--watch` flag.

```bash
rosa log uninstall -c <cluster name> --watch
```

## Expect
- The process does not exit and the logs refresh until uninstallation finishes or the cluster enters an error state.
