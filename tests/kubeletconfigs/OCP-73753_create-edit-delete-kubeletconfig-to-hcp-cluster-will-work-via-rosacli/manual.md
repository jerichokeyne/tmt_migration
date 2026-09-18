# Test

## Step
1. Prepare a HCP cluster.

## Expect

## Step
2. List kubeletconfigs when the cluster has none.

## Expect

## Step
3. Create a kubeletconfig without a name and with `--pod-pids-limit` set.

## Expect
~~The kubeletconfig should be created. There will be a message showing successful creation.~~ Interactive mode prompts for a name.

## Step
4. List kubeletconfigs.

## Expect
The created kubeletconfig is listed with correct information. Its name is automatically generated.

## Step
5. Create a kubeletconfig with a name specified by `--name`.

## Expect
The creation succeeds.

## Step
6. List kubeletconfigs.

## Expect
The kubeletconfig is listed with the correct setting.

## Step
7. Edit the kubeletconfig pod PIDs limit.

```bash
rosa edit kubeletconfig --name <name> -c <cluster> --pod-pids-limit 12345
```

## Expect
The edit succeeds.

## Step
8. Describe the kubeletconfig.

```bash
rosa describe kubeletconfig --name <name> -c <cluster>
```

## Expect

## Step
9. Delete the created kubeletconfigs.

```bash
rosa delete kubeletconfig --name <kubeletconfig-name> -c <cluster>
```

## Expect
The deletion succeeds.

## Step
10. Describe the kubeletconfig again.

## Expect
The kubeletconfig is reported as not found.
