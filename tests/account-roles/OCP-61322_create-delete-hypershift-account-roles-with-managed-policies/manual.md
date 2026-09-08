# Test

## Step
Create account-roles with '--hosted-cp' flag in auto mode  
NOTE:  
1. just specify '--hosted-cp' and 'prefix' flag  
2. Also includes --path --permissions-boundary --force-policy-creation --version flags

## Expect
- Three roles will be created,<prefix>-HCP-Installer-Role,<prefix>-HCP-Support-Role,<prefix>-HCP-Worker-Role ,  
- The three roles are attached with the managed policies  
- All the --path --permissions-boundary --force-policy-creation --version flags should work well  
- The role name should be with the format <prefix>-HCP-ROSA-<role type>  
role type: Installer-Role/Support-Role/Worker-Role

## Step
Create account-roles with '--hosted-cp' flag in auto mode  
NOTE:  
1. just specify '--hosted-cp' and 'prefix' flag  
2. Also includes --path --permissions-boundary --version flags

## Expect
- The prompted aws commands includes the ones to create three roles in step1 and attach the related managed polices  
- The roles on AWS should be tagged with rosa_managed_policies=true  
- After run the commands, the account-roles are created on AWS and attached the managed polices  
- All the --path --permissions-boundary --force-policy-creation --version flags should work well, the commands should contain related parameters  
- There is warning message "W: Setting `version` flag for hosted CP managed policies has no effect, any supported ROSA version can be installed with managed policies"

## Step
Repeat step 1~2 with the different channel-group

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
Delete the hypershift account roles in auto mode   
\# rosa delete account-roles --prefix <prefix> --hosted-cp --mode auto

## Expect
- The account roles should be detached and deleted.  
- The managed policies should NOT be deleted.  
- There is warning message "W: Setting `version` flag for hosted CP managed policies has no effect, any supported ROSA version can be installed with managed policies"

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
