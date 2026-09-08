# Test

## Step
Create account-roles in interactive mode,

## Expect
- Hosted-cp option should be asked.  
- Other options should be shown as classic sts account-roles

## Step
Repeat step 1 with the different channel-group

## Expect
The result should be same

## Step
Create multiple managed account roles

## Expect
The result should be same

## Step
List the account-roles and check the the 'AWS Managed' column

## Expect
The should be 'AWS Managed' in the output of 'rosa list account-roles'.  
The values should be correct, the account-roles attached the managed policies shows 'Yes' in that column, Or should be 'No'

## Step
Create hypershift cluster in manual mode

## Expect
- The aws commands should be prompted.  
- There are only commands for creating roles and attaching managed polices, no creating policies ones  
- There will be 3 account-roles with -HCP- midsuffix created with managed policies

## Step
Delete the hypershift account roles in manual mode  
\# rosa delete account-roles --prefix <prefix> --hosted-cp --mode manual

## Expect
- There are aws commands to detach the policies and delete the roles  
- No aws commands to delete the managed policies

## Step
Try to delete the account-roles with --hosted-cp but the prefix is not for hypershift account-roles

## Expect
E: There are no hosted CP account roles to be deleted
