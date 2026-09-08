# Test

## Step
Create STS cluster with the account roles with managed account-role policies then-->Upgrade the account-roles in manual mode

## Expect
It should be forbidden and some message bellow:  
I: Account roles with the prefix 'yw0113mpaccr1' have attached managed policies. An upgrade isn't needed

## Step
Upgrade the account-roles in auto mode

## Expect
The result should be same

## Step
Upgrade that account-roles if any managed policies missing

## Expect
It should fail with message:  
E: Failed while validating managed policies: role <> is missing the attached managed policy <manage policiy arn>
