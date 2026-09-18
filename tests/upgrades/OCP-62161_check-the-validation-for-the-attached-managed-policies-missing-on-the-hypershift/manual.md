# Test

## Step

Create hypershift account-roles then create hypeshift with the account-roles in the version which has an upgrade path from 4.12. to 4.13.z

## Expect

## Step

Detach one managed policy from one operator-role Then run bellow upgrade command via rosacli:

1. ~~`rosa upgrade operator-roles --version`~~
2. `rosa upgrade cluster -c`
3. `rosa upgrade roles --version`

## Expect

- Error message will return to tell the related role missing attached managed policy:

```
E: Failed while validating managed policies: role 'yuwan-iihp3-a2f7-kube-system-control-plane-operator' is missing the attached managed policy 'arn:aws:iam::301721915996:policy/ROSAHCPControlPlane'
```

## Step

Attach the operator policy of the one in step2

## Expect

## Step

Detach one managed policy from one account-role then run bellow upgrade command via rosacli:

1. ~~`rosa upgrade account-roles-roles --prefix`~~
2. `rosa upgrade cluster -c`
3. `rosa upgrade roles --version`

## Expect

- Error message will return to tell the related role missing attached managed policy:

```
E: Failed while validating managed policies: role 'yw0403accr4hp2-HCP-Support-Role' is missing the attached managed policy 'arn:aws:iam::301721915996:policy/ROSAHCPSRESupportPolicy'
```
