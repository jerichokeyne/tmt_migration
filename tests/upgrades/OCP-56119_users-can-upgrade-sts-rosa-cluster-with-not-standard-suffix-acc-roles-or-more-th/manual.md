# Test

## Step

Create account-roles with not-standard suffix acc roles.
NOTE: It can be done by change the role and policies name with some custom suffix in the aws commands.

## Expect

## Step

Prepare 4.9.z rosa sts cluster which has an upgrade path to 4.10.z using the 4.9 version account-roles with the account-roles create in step1

## Expect

## Step

Run `rosa upgrade roles` command in auto mode then run `rosa upgrade cluster` to upgrade cluster to 4.10.z

## Expect

- All the wide AMI roles are upgraded to the compatible version
- The specific operator role for the upgrading version should be created.
- The cluster can be upgraded successfully

## Step

Repeat step1~2 with the cluster in 4.10.z version which has upgrade path to 4.11.z

## Expect

The results should be same with the ones in step 1~2

## Step

Repeat step1~2 with the cluster in 4.11.z version which has upgrade path to 4.12.z

## Expect

The results should be same with the ones in step 1~2

## Step

Prepare 4.9.z rosa sts cluster which has an upgrade path to 4.10.z using the 4.9 version account-roles with more than one policies attached to the account role.

## Expect

## Step

Run `rosa upgrade roles` command in auto mode then run `rosa upgrade cluster` to upgrade cluster to 4.10.z

## Expect

- There should be prompted message "More than one policy attached to account role " ....Would you like to dettach current policies and setup a new one ?
- If choose yes, new account-roles will be created with the latest version and existing ones will be detached. and it works both for manual mode and auto mode
- If choose no, interactive mode will ask users to choose one account-roles policie is to be upgraded, and update the choosen ones.
