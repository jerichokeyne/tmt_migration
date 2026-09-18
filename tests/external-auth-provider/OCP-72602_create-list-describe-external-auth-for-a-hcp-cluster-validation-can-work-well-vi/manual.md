# Test

## Step
Prepare HCP cluster with `--external-auth-providers-enabled`

## Expect

## Step
Create/list external provider for an HCP cluster where external authentication configuration is not enabled

## Expect
It should return a readable and actionable error message.

```bash
./rosa create external-auth-provider -c sdq-ci-bgzwy
```

```
E: external authentication configuration is not enabled for cluster 'sdq-ci-bgzwy'
```

Create a hosted control plane with the `--external-auth-providers-enabled` parameter to enable the configuration.

## Step
Create external provider for the cluster without attribute `id`, `issuer`, `issuer.audiences`, `issuer.url`, or `claim`, one by one, for the external authentication request. It will go to interactive mode.

## Expect
It should return a readable and actionable error message.

## Step
Create/list non-HCP cluster with external authentication configuration and external authentications

## Expect
It should return a readable and actionable error message.

```bash
rosa create external-auth-provider -c sdq-ci-izzxi
```

```
E: external authentication provider is only supported for Hosted Control Planes
```
