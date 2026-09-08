# Test

## Step
Check the help message,  
\# rosa create -h  
\# rosa create user-role -h

## Expect
\# rosa create -h  
......  
user-role Create user role to verify account association  
......  
\# rosa create user-role -h  
[root@yuwan rosa]# ./rosa create user-role -h  
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
--color string Surround certain characters with escape sequences to display them in color on the terminal. Allowed options are [auto never always] (default "auto")  
--debug Enable debug mode.  
--profile string Use a specific AWS profile from your credential file.  
--region string Use a specific AWS region, overriding the AWS_REGION environment variable.  
-y, --yes Automatically answer yes to confirm operation.

## Step
Create the user-role in the auto mode in the interactive mode  
NOTE: It needs the user which has 'AccountLabel' permission

## Expect
-----manual mode------  
[root@yuwan rosa]# ./rosa create user-role -i  
I: Creating User role  
? Role prefix: aa  
? Permissions boundary ARN (optional):   
? Role creation mode: auto  
I: Creating ocm user role using 'arn:aws:iam::301721915996:user/yuwan'  
? Create the 'aa-User-xueli_1-Role' role? Yes  
I: Created role 'aa-User-xueli_1-Role' with ARN 'arn:aws:iam::301721915996:role/aa-User-xueli_1-Role'  
I: Linking User role  
? User Role ARN: arn:aws:iam::301721915996:role/aa-User-xueli_1-Role  
? Link the 'arn:aws:iam::301721915996:role/aa-User-xueli_1-Role' role with account '1G9OXMM1oNIdUuatCH1FZJm2Nls'? Yes  
I: Successfully linked role-arn 'arn:aws:iam::301721915996:role/aa-User-xueli_1-Role' with account '1G9OXMM1oNIdUuatCH1FZJm2Nls'  
[root@yuwan rosa]#   
  
-----auto mode------  
[root@yuwan rosa]# ./rosa create user-role -i  
I: Creating User role  
? Role prefix: bb  
? Permissions boundary ARN (optional):   
? Role creation mode: manual  
I: All policy files saved to the current directory  
I: Run the following commands to create the account roles and policies:  
  
  
aws iam create-role \  
--role-name bb-User-xueli_1-Role \  
--assume-role-policy-document file://sts_ocm_user_trust_policy.json \  
--tags Key=rosa_role_prefix,Value=bb Key=rosa_role_type,Value=User Key=rosa_environment,Value=staging  
  
  
rosa link user-role --role-arn arn:aws:iam::301721915996:role/bb-User-xueli_1-Role  
[root@yuwan rosa]#

## Step
Repeat step2 with an acocunt which has no 'AccountLabel' permission

## Expect
E: Unable to link role arn 'arn:aws:iam::301721915996:role/ManagedOpenShift-User-sdqe-regular01-Role' with the account id : '1Pg91NjVkaKuxDvnp9iXQa8MlC3' : identifier is '11', code is 'ACCT-MGMT-11' and operation identifier is 'b96a902a-53c4-4b0c-a34b-d60d6beceead': Account with ID 1Pg91NjVkaKuxDvnp9iXQa8MlC3 denied access to perform get on Account with HTTP call GET /api/accounts_mgmt/v1/accounts/1Pg91NjVkaKuxDvnp9iXQa8MlC3/labels

## Step
Check the validation for the validation for the -permissions-boundary.

## Expect
There should be validation for it.  
X Sorry, your reply was invalid: Invalid ARN: arn: invalid prefix
