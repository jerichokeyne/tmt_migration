# Test

## Step
Create managed account-roles and make sure some ones are not attached the managed policies.

## Expect

## Step
Create the sts cluster in the manual mode with the account-roles in step1 on STAGE env

## Expect
It should fail with error message, like below:  
E: Failed while validating account roles: role 'yw0203acc1manp1-Worker-Role' is missing the attached managed policy 'arn:aws:iam::301721915996:policy/ROSAWorkerPolicy'

## Step
Attach managed policy on the role in the error message then repeat step2

## Expect
It should fail with error message for other account-role missing the policy.

## Step
Repeat step2 in auto mode

## Expect
The result should be same

## Step
Repeat step2,4 on hypershift cluster creation.

## Expect
The result should be same

## Step
repeat the step2 on product env

## Expect
There should be error message, the managed account-roles are not supported on prod env
