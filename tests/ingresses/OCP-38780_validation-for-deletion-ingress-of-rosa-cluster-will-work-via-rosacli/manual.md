# Test

## Step

1. Prepare one ROSA cluster.

## Expect

## Step

2. Delete an ingress without specifying its name or ID.

```bash
rosa delete ingress
rosa delete ingress -c <cluster name>
```

## Expect

```
Failed with error:
Expected exactly one command line argument or flag containing the name or identifier of the cluster
<usage>
```

## Step

3. Delete a non-existent ingress.

```bash
rosa delete ingress <non existed> -c <cluster name>
```

## Expect

```
Failed with error:
Failed to delete ingress 'xueli-rosa2': There is no ingress with identifier or name 'xueli-rosa2'
```

## Step

4. Delete an ingress with an invalid ID.

```bash
rosa delete ingress p3s7aaa -c xueli-rosa
```

## Expect

```
Failed with error:
Ingress identifier 'p3s7aaa' isn't valid: it must contain only four letters or digits
```

## Step

5. Check that the other help options work.

- `--profile`
- `-v`

## Expect

## Step

6. Delete with the unknown `--interactive` flag.

## Expect

```
Error: unknown flag: --interactive
<usage>
```
