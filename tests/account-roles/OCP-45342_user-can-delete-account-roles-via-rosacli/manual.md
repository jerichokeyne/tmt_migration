# Test

## Step
Log in via rosacli and create account-roles

## Expect
Support sts from version 1.0.6

## Step
Check the help message of 'rosa delete'  
\# rosa delete -h  
\#rosa delete account-roles -h

## Expect
\# ./rosa delete -h  
.....  
account-roles Delete Account Roles  
......  
\# ./rosa delete account-roles -h  
Cleans up account roles from the current AWS account.  
  
  
Usage:  
rosa delete account-roles [flags]  
  
  
Aliases:  
account-roles, accountroles, accountrole, account-role  
  
  
Examples:  
\# Delete Account roles"  
rosa delete account-roles [-r role-name | -p prefix]  
  
  
Flags:  
-h, --help help for account-roles  
--mode string How to perform the operation. Valid options are:  
auto: Account roles will be deleted automatically using the current AWS account  
manual: Command to delete the account roles will be output which can be used to delete manually (default "auto")  
-p, --prefix string Prefix of the account roles to be deleted.  
-r, --role-name string Account role name to be deleted.  
  
  
Global Flags:  
--debug Enable debug mode.  
--profile string Use a specific AWS profile from your credential file.  
--region string Use a specific AWS region, overriding the AWS_REGION environment variable.  
-y, --yes Automatically answer yes to confirm operation.  
[root@yuwan rosa]#

## Step
Check the validation for deleting the account-roles.  

  * delete them without setting -p 
  * delete them with invalid mode
  * ~~delete them with invalid role name format~~

## Expect
\# ./rosa delete account-role  
E: Option account role prefix '-p' or role name '-r' is mandatory  
Defaulting into interactive mode here counts as a pass.  
  
\# rosa delete account-role --mode xxx  
E: Invalid mode. Allowed values are [auto manual]  
  
~~# ./rosa delete account-role -r arn:aws:iam::301721915996:role/yw1019-Installer-Role E: Error getting role: ValidationError: The specified value for roleName is invalid. It must contain only alphanumeric characters and/or the following: +=,.@_- status code: 400, request id: 4594c028-ecfc-4e72-aa0e-99b926937b7f~~

## Step
Delete the account-role with without the mode flag

## Expect
After choose confirmation messages 'yes', all the resources are deleted.  
They are deleted from AWS.

## Step
Delete the account-role which some cluster is using

## Expect
E: Role aaraj-HCP-ROSA-Installer-Role is associated with the cluster aaraj-hcp

## Step
Delete the account-rolewith '--mode manual'

## Expect
There are aws commands prompted, and all the resources can be deleted with them.  
They are deleted from AWS.

## Step
Delete the account-roles without setting '--mode'

## Expect
There is options of 'auto' and 'manual' prompted.Others are same as step5~6.

## Step
Try to delete account-roles which were used by some sts cluster

## Expect
They should be deleted successfully
