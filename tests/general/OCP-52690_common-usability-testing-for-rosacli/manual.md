# Test

## Step
All deletion commands need a confirmation:

- `rosa delete account-roles`
- `rosa delete admin`
- `rosa delete cluster`
- `rosa delete idp`
- `rosa delete ingress`
- `rosa delete machinepool`
- `rosa delete ocm-role`
- `rosa delete oidc-provider`
- `rosa delete operator-roles`
- `rosa delete upgrade`
- `rosa delete user-role`

## Expect

## Step
For commands requiring many parameters in interactive mode, for example `rosa cluster cluster`, prompt the related command last if the request fails.

## Expect

## Step
It should prompt for parameter input again if an invalid parameter is entered in interactive mode:

- `rosa create account-roles`
- `rosa create admin`
- `rosa create cluster`
- `rosa create idp`
- `rosa create ingress`
- `rosa create machinepool`
- `rosa create ocm-role`
- `rosa create oidc-provider`
- `rosa create operator-roles`
- `rosa create user-role`
- `rosa edit addon`
- `rosa edit cluster`
- `rosa edit ingress`
- `rosa edit machinepool`
- `rosa install addon`
- `rosa revode user`
- `rosa grant user`
- `rosa upgrade cluster`

## Expect

## Step
For any operation, ROSA CLI should contain all commands for a whole workflow, including create, delete, list, describe, and edit, if no design is indicated specifically.
- machinepool
- idp
- upgrade
- addon
- ocm-role user-role account-role operator-roles oidc-provider
- ingress
- admin

## Expect

## Step
There should be a message returning the result for all operations.

## Expect

## Step
It should retry if it encounters a network issue during the request.

## Expect

## Step
For operations including more than one step, there should be a rollback step if they encounter an error in later steps:

- `rosa create admin`

## Expect

## Step
There should be a wait time and retry steps when it encounters a race condition, for example, multiple users sending requests at the same time.

## Expect
