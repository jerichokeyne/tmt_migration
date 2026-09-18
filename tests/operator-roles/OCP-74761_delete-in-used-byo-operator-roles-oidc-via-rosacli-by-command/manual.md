# Test

## Step
Cluster two clusters with the same shared oidc-provider and operator-roles

## Expect

## Step
Delete the cluster, then delete the operator-roles with an operator-roles prefix:

```bash
rosa delete operator-roles --prefix <prefix>
```

Delete the OIDC provider with `oidc-endpoint-url`.

Note: Test both manual and auto modes.

## Expect
- Same with the step 2~3
- If the OIDC provider is used by other clusters, it will fail to delete it with an error:
```
E: There are clusters using OIDC config 'https://yw0308byocc1-oidc-t6s9.s3.us-east-2.amazonaws.com', can't delete the provider
```

## Step
Delete operator-roles and oidc-provider with not-exist entrance

## Expect
There will be some readable message
