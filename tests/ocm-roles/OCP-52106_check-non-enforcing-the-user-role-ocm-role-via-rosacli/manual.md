# Test

## Step
Log in rosacli and create(link) ocm-role and make sure there is no linked user-role

## Expect

## Step
Create STS cluster via rosacli

## Expect
It should succeed

## Step
Test all actions bellow  

  * Create/Edit/Delete cluster
  * Create/Edit/Delete machinepool
  * Create/Edit/Delete idp
  * others operation

## Expect
It should succeed

## Step
Repeat step1~3 with an account which has no ocm-role

## Expect
It should succeed
