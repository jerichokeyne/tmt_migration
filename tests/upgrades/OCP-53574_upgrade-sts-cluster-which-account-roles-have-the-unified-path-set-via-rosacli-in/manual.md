# Test

## Step

~~Prepare account-roles prefixed 'test1' with setting 'Role Path' and 'Policy Path'.~~
Prepare account-roles prefixed 'test1' with setting the unified path

## Expect

## Step

Create a 4.9.z STS cluster with the account-roles created in step1~~and setting the operator role/policies path,~~
then upgrade to 4.10.z in the interactive mode

## Expect

- The cluster is created successfully
- All the IAM roles are created with the path setting
- The upgrade should succeed
- The new operator role and policy for 4.10.z cluster should be created with the path

## Step

Repeat step1~2 with the upgrade path 4.10.z --> 4.11.z

## Expect

- The cluster is created successfully
- The upgrade should succeed

## Step

Repeat step1~2 with the upgrade path 4.8.z --> 4.9.z

## Expect

- The cluster is created successfully
- The upgrade should succeed
