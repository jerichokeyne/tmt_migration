# Test

## Step

Create STS cluster with the account roles with managed account-role policies then-->Create sts cluster with the account-roles with the version has upgrade path.
NOTE: 4.9.z -4.10.z is especial as the 4.10.z cluster needs the additional operator role

## Expect

## Step

Upgrade the cluster in the manual mode

## Expect

- The aws to create the role and to attach the manage policies will be shown if there needs additional role.
- The following message should be shown if no additional roles are needed:

```
I: Account roles with the prefix 'yw0113mpaccr2' have attached managed policies.
I: Cluster 'yuwan-ists2' operator roles have attached managed policies
```

For HCP cluster, the following message should be shown if no additional roles are needed:

```bash
rosa upgrade roles -c zwant9 --cluster-version 4.16.0-ec.5 -m manual -y
```

```
I: Account roles with the prefix 'zwant-up4' have attached managed policies.
I: Cluster 'zwant9' operator roles have attached managed policies. An upgrade isn't needed
```
