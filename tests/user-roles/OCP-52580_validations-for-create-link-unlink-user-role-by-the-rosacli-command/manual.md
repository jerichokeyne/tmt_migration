# Setup
$ rosa create cluster -c ${name}aa --region ${region} --version ${version}-${channel_group} --channel-group ${channel_group} --role-arn arn:aws:iam::${aws_account_id}:role/OSDCCSAdmin --tags cluster-name:${name},cluster-version:${version}-${channel_group} ${roles} --external-id "<external_id>"

# Test

## Step
Check help message  
\#rosa create -h  
\#rosa create user-role -h

## Expect
\#rosa create -h  
.......  
user-role Create user role to verify account association  
.......  
\# ./rosa create user-role -h  
Create user role that allows OCM to verify that users creating a cluster have access to the current AWS account.  
  
  
Usage:  
rosa create user-role [flags]  
  
  
Aliases:  
user-role, userrole  
  
  
Examples:  
\# Create user roles   
rosa create user-role --prefix   
  
  
Flags:  
-h, --help help for user-role  
-i, --interactive Enable interactive mode.  
-m, --mode string How to perform the operation. Valid options are:  
auto: Resource changes will be automatic applied using the current AWS account  
  
manual: Commands necessary to modify AWS resources will be output to be run manually  
--permissions-boundary string The ARN of the policy that is used to set the permissions boundary for the account roles.  
--prefix string User-defined prefix for ocm-user role (default "ManagedOpenShift")  
  
  
Global Flags:  
--debug Enable debug mode.  
--profile string Use a specific AWS profile from your credential file.  
--region string Use a specific AWS region, overriding the AWS_REGION environment variable.  
-y, --yes Automatically answer yes to confirm operation.

## Step
Check the validation for `rosa create user-role`  
- Create an user-role with invalid mode  
- Create an user-role with invalid permision boundady  
- Create an user-role with the permision boundady under another aws account  
- Create another user-role with the existed prefix

## Expect
Should fail with readable error message

## Step
Check the validation for `rosa unlink user-role`  
- Unlink user-role with not-exist role  
- Unlink user-role with the role arn in incorrect format  
\-

## Expect
Should fail with readable error message

## Step
Check the validation for `rosa link user-role`  
- Link user-role with the role arn in incorrect format

## Expect
Should fail with readable error message
