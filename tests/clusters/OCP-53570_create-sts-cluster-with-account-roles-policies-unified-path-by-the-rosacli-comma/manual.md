# Test

## Step
~~Create account-roles prefixed 'test1' with setting 'Role Path' and 'Policy Path' by the rosacli command both in auto mode and manual mode.~~  
Create account-roles prefixed 'test1' with setting the unified path by the rosacli command in auto mode  
\# rosa create account-roles --prefix <prefix> --path /accroles/test/path/ --mode auto -y

## Expect
- in the manual mode the aws commands should be correct with the '--path'  
- The account-roles and policies should be created successfully

## Step
Create cluster with the account-roles created in step1 in manual mode

## Expect
- The cluster will keep in waitting status  
- There will be specified message to clarify the detection of the path like below  
INFO: ARN path '/test/xue/' detected. This ARN path will be used for subsequent created operator roles and policies, for the account roles with prefix 'xueli'  
- The operator role and policy with the unified path will be created successfully

## Step
Create operator-roles of the cluster

## Expect
- Ther operator roles and policy with the unified path will be created successfully  
- There will be specified message to clarify the detection of the path like below  
INFO: ARN path '/test/xue/' detected. This ARN path will be used for subsequent created operator roles and policies, for the account roles with prefix 'xueli'

## Step
Create oidc provider of the cluster

## Expect

## Step
Check cluster status

## Expect
Cluster will be in the status of ready
