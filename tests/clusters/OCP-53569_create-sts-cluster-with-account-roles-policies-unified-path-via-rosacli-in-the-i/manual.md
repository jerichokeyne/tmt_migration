# Test

## Step
Check the help message of `rosa create account-roles -h`

## Expect
It should have the help message and example of the '--path' flag

## Step
~~Check the help message and the validation for 'Role Path' and 'Policy Path' ~~

## Expect
~~- ? - > "? The arn path for the account roles" - ? ? The arn path for the account policies - The arn should match the regexp of `^\/[a-zA-Z0-9\/]*\/$` and "X Sorry, your reply was invalid: invalid ARN Path. It must begin and end with / and contain only alphanumeric characters" message error for invalid values~~

## Step
~~Create account-roles prefixed 'test1' with setting 'Role Path' and 'Policy Path' both in auto mode and manual mode.~~  
Create account-roles prefixed 'test1' with setting the unified path both in the interactive mode and choose manual mode

## Expect
- in the manual mode the aws commands should be correct with the '--path'  
- The account-roles should be created successfully with the path

## Step
~~Check the help message of `rosa create cluster -h`~~

## Expect
~~- There should be info for '--operator-roles-path' and '--operator-policies-path'~~

## Step
~~Create cluster with the account-roles created in step3 and set 'Operator Role Path' and 'Policy Path' in auto mode.~~  
Create cluster with the account-roles created in step3 and set the unified path in auto mode

## Expect
- The cluster is created successfully  
- There will be specified message to clarify the detection of the path like below  
INFO: ARN path '/test/xue/' detected. This ARN path will be used for subsequent created operator roles and policies, for the account roles with prefix 'xueli'  
  
- The operator role and policy with path will be created successfully with the unified path

## Step
~~Create cluster with the account-roles created in step3 and set 'Operator Role Path' and 'Policy Path' in manual mode.~~  
Create cluster with the account-roles created in step3 and set the unified path in manual mode

## Expect
- Using the prompted `rosa create operator-roles.....` command in the auto mode, the cluster will be created successfully with the path  
- There will be specified message to clarify the detection of the path like below  
INFO: ARN path '/test/xue/' detected. This ARN path will be used for subsequent created operator roles and policies, for the account roles with prefix 'xueli'  
- Using the prompted `rosa create operator-roles.....` command in the manual mode, the aws commands should be correct with the '--path' flag AND the cluster will be created successfully finally
