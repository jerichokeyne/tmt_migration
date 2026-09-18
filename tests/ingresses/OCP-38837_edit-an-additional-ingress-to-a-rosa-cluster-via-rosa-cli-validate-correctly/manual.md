# Test

## Step

1. Note that additional ingresses cannot be created in staging/INT because `managed-ingress-support` is enabled for all users (from 09/18). Edit and delete additional ingress if present. Editing the default ingress is unchanged. Launch the ROSA CLI in the staging environment.

## Expect

## Step

2. Prepare a ready ROSA cluster.

## Expect

## Step

3. Record the ingress.

```bash
rosa list ingress -c <cluster name>
```

## Expect

## Step

4. Edit an ingress with an invalid label.

```bash
rosa edit ingress <ingress id> -c <cluster name> --label-match "aaa,"
```

## Expect

- `E: Expected key=value format for label-match` is returned.
- The ingress is not updated.

## Step

5. Run the command with a non-allowed flag.

```bash
rosa edit ingress <ingress id> --nonallowed
```

## Expect

- The help message is shown.
- `Error: unknown flag: --nonallowed` is returned.

## Step

6. Run the command without a cluster.

```bash
rosa edit ingress <ingress id>
```

## Expect

- `Error: required flag(s) "cluster" not set` is returned.
- The help usage is shown.

## Step

7. Run the command with all flags in the help message.

## Expect

- All flags are meaningful and work correctly.
