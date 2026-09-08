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
Create the user-role with the command

## Expect
$ rosa create user-role --prefix yw0620userrpb1 --permissions-boundary arn:aws:iam::301721915996:policy/yuwan_policy_pb --mode auto -y  
I: Creating User role  
I: Creating ocm user role using 'arn:aws:iam::301721915996:user/yuwan'  
I: Created role 'yw0620userrpb1-User-sdqe-regular01-Role' with ARN 'arn:aws:iam::301721915996:role/yw0620userrpb1-User-sdqe-regular01-Role'  
I: Linking User role  
I: Successfully linked role ARN 'arn:aws:iam::301721915996:role/yw0620userrpb1-User-sdqe-regular01-Role' with account '1Pg91NjVkaKuxDvnp9iXQa8MlC3'  
  
- The permission boundary is added.

## Step
List user-roles

## Expect
$ rosa list user-role  
I: Fetching user roles  
ROLE NAME ROLE ARN LINKED  
yw0620userr1-User-sdqe-regular01-Role arn:aws:iam::301721915996:role/yw0620userr1-User-sdqe-regular01-Role Yes  
yw0620userrpb1-User-sdqe-regular01-Role arn:aws:iam::301721915996:role/yw0620userrpb1-User-sdqe-regular01-Role Yes  
  
- The user-role created in step2 will be shown in the list output, and the 'Linked' field should be 'Yes'

## Step
Unlink user-role

## Expect
$ rosa unlink user-role arn:aws:iam::301721915996:role/QEAuto-user-2022062062000-User-sdqe-regular01-Role -y  
I: Unlinking user role  
I: Successfully unlinked role ARN 'arn:aws:iam::301721915996:role/QEAuto-user-2022062062000-User-sdqe-regular01-Role' from account '1Pg91NjVkaKuxDvnp9iXQa8MlC3'

## Step
List user-roles

## Expect
- The user-role created in step2 will be shown in the list output, and the 'Linked' field should be 'No'

## Step
Link user-role

## Expect
$ rosa link user-role arn:aws:iam::301721915996:role/QEAuto-user-2022062062000-User-sdqe-regular01-Role -y  
I: Linking User role  
I: Successfully linked role ARN 'arn:aws:iam::301721915996:role/QEAuto-user-2022062062000-User-sdqe-regular01-Role' with account '1Pg91NjVkaKuxDvnp9iXQa8MlC3'

## Step
List user-roles

## Expect
- The user-role created in step2 will be shown in the list output, and the 'Linked' field should be 'Yes'

## Step
Delete the user-role with the auto mode command

## Expect
$ rosa delete user-role --role-arn arn:aws:iam::301721915996:role/QEAuto-user-2022062062000-User-sdqe-regular01-Role --mode auto -y  
I: Deleting user role  
W: Role ARN 'arn:aws:iam::301721915996:role/QEAuto-user-2022062062000-User-sdqe-regular01-Role' is linked to account '1Pg91NjVkaKuxDvnp9iXQa8MlC3'  
I: Unlinking user role  
I: Successfully unlinked role ARN 'arn:aws:iam::301721915996:role/QEAuto-user-2022062062000-User-sdqe-regular01-Role' from account '1Pg91NjVkaKuxDvnp9iXQa8MlC3'  
I: Successfully deleted the user role  
  
- It should contain the step of unlink user-role and the message should be clear.  
- The role should be removed from the user-role list output of `rosa list user-role`
