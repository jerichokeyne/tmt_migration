# Test

## Step
All `rosa list` commands should support the `-o` flag:

- `account-roles`: List account roles and policies --pass
- `addons`: List add-on installations --pass
- `clusters`: List clusters --pass
- `dns-domain`: List DNS Domains --pass
- `gates`: List available OCP Gates --pass
- `idps`: List cluster IDPs --pass
- `ingresses`: List cluster Ingresses --pass
- `instance-types`: List Instance types --pass
- `machinepools`: List cluster machine pools --pass
- `ocm-roles`: List ocm roles --pass
- `oidc-config`: List OIDC Configuration resources --pass
- `oidc-providers`: List OIDC providers --pass
- `operator-roles`: List operator roles and policies --pass
- `regions`: List available regions --pass
- `tuning-configs`: List tuning configs --pass
- `upgrades`: List available cluster upgrades --pass
- `user-roles`: List user roles --pass
- `users`: List cluster users --pass
- `versions`: List available versions

## Expect
- Check all list commands with JSON/YAML output, `-o json`, and `-o yaml`. All the results should be printed with the specific format.
- If there is no resource, `[]` will returned.
- These two formats should work well on all type of clusters, classic and hosted-cp clusters.

## Step
List cluster with the `--all` flag.

## Expect
- If the `--all` flag is set, all clusters (classic ROSA, ROSA STS, and hosted control plane) belonging to the Red Hat organization should be listed, including those not created via ROSA CLI and OCM UI, filtered by `product.id=rosa`.
- If `--all` is not set, only clusters created via ROSA CLI and OCM UI are listed. The filters should be `(properties.rosa_creator_arn LIKE '%<aws account-id>%' or aws.sts.role_arn LIKE '%<aws account-id>%')` and `product.id-rosa`.

## Step
Check all different OS, RHEL, MacOS, Windows.

## Expect
The result should be as above ones
