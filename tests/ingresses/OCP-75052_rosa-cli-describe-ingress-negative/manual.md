# Setup

Prepare a cluster.

# Test

## Step

1. Verify the error when no cluster is provided.

```bash
rosa describe ingress $ingressID
```

## Expect

```
Failed to execute root command: required flag(s) "cluster" not set
```

## Step

2. Verify the error when an incorrect ingress ID is provided.

```bash
rosa describe ingress xxx -c $cluster
```

## Expect

```
E: Failed to get ingress 'xxx' for cluster '27fd1e14gi4pkct19qo1jgbsodv22n5i'
```
