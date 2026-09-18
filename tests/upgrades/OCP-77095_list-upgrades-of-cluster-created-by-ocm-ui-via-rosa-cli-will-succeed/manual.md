# Test

## Step

Set automatic upgrade policy via OCM UI

## Expect

## Step

Run the command to list the upgrade:

```bash
rosa list upgrades -c <cluster_name>
```

## Expect

The scheduled upgrade should be showed

## Step

Other flags also work well:

- `-v`
- `--debug`
- `--profile`

## Expect
