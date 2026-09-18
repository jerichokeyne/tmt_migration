# Setup
Prepare a HCP cluster with `--external-auth-providers-enabled`

# Test

## Step
Create break_glass_credential via interactive mode

```bash
rosa create break-glass-credential -c 2a83k03lilf22l1d4kqkkt96i0hfgpbr -i
```

## Expect
- Check the parameters are optional.
- Input `?` to check the help message.

```
rosa create break-glass-credential -c 2a83k03lilf22l1d4kqkkt96i0hfgpbr
I: Enabling interactive mode
? Username (optional):
? Expiration duration (optional): 2h
```
