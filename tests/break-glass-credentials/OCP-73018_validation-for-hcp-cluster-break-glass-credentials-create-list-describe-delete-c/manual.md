# Test

## Step
Create/list/revoke break-glass-credential to non-HCP cluster
```bash
rosa create break-glass-credential -c ${CLASSIC_CLUSTER_ID}
rosa list break-glass-credential -c ${CLASSIC_CLUSTER_ID}
rosa revoke break-glass-credential -c ${CLASSIC_CLUSTER_ID}
```

## Expect
It returns error message.

```
E: external authentication provider is only supported for Hosted Control Planes
```

## Step
Create/list/revoke break-glass-credential to external-auth-providers-enabled not enable

```bash
rosa create break-glass-credential -c aaraj-hcp
```

## Expect
It returns error message.

```
E: External authentication configuration is not enabled for cluster 'aaraj-hcp'
Create a hosted control plane with '--external-auth-providers-enabled' parameter to enabled the configuration
```

## Step
Create break-glass-credential with invalid `--username` and `--expiration`

### TODO: Update this section 

## Expect
It returns error message.

## Step
Create break-glass-credential with --expiration is less than 10min

```bash
rosa create break-glass-credential --expiration="1s" --username="" -c sdq-ci-bzoci
```

## Expect
It returns error message.

```
E: failed to create a break glass credential for cluster 'sdq-ci-bzoci': Expiration needs to be at least 10 minutes from now
```
