# Test

## Step
1. Verify login fails when using `--use-auth-code` with govcloud.

```bash
rosa login --env=integration --govcloud --use-auth-code
```

## Expect
```
E: This login method is currently not supported with FedRAMP
```

## Step
2. Verify login fails when using `--use-device-code` with govcloud.

```bash
rosa login --env=integration --govcloud --use-device-code
```

## Expect
```
E: This login method is currently not supported with FedRAMP
```
