# Test

## Step

Create account-role with the version 4.8

## Expect

## Step

Create the sts clusters with version 4.9.*

## Expect

It should be failed with error message,
```
E: Account role 'arn:aws:iam::301721915996:role/yw7-Installer-Role' is not compatible with version openshift-v4.8.12. Run 'rosa create account-roles' to create compatible roles and try again.
```

## Step

Create account-role with the version 4.7

## Expect

## Step

Create the sts clusters with version 4.8.* and 4.9.*

## Expect

It should be failed with error message,
```
E: Account role 'arn:aws:iam::301721915996:role/yw7-Installer-Role' is not compatible with version openshift-v4.8.12. Run 'rosa create account-roles' to create compatible roles and try again.
```

## Step

Create account-role with the version 4.9

## Expect

## Step

Create the sts clusters with version 4.10.z

## Expect

It should be failed with error message,
```
E: Account role 'arn:aws:iam::301721915996:role/yw7-Installer-Role' is not compatible with version openshift-v4.8.12. Run 'rosa create account-roles' to create compatible roles and try again.
```
