# Test

## Step

Prepare one ROSA cluster

## Expect

## Step

Delete the cluster without indicated cluster Name or ID
```bash
rosa delete cluster
```

## Expect

Failed with error:
Expected exactly one command line argument or flag containing the name or identifier of the cluster

## Step

Delete a non-existed cluster
```bash
rosa delete cluster <cluster name>
```

## Expect

Failed with error:
Failed to delete cluster 'xueli-rosa2': There is no cluster with identifier or name 'xueli-rosa2'

## Step

Prepare two clusters in same display name
```bash
rosa delete cluster <cluster name>
```

## Expect

It will failed with readable error message to ask user delete with cluster ID

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
