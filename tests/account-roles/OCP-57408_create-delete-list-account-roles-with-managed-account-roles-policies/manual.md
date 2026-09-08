# Test

## Step
Create account-roles with the managed account role polices in auto mode  
\# rosa create account-roles --managed-policies --mode auto  
\# rosa create account-roles --mp --mode auto

## Expect
- The account-roles are created on AWS and attached the managed polices  
- The roles on AWS should be tagged with rosa_managed_policies=true  
~~- Install role will be attached with three policy files named, ROSAInstallerCorePolicy, ROSAInstallerVPCPolicy,ROSAInstallerPrivateLinkPolicy (SDA-7941)~~

## Step
Create account-roles with the managed account role polices in manual mode  
\# rosa create account-roles --managed-policies --mode manual  
\# rosa create account-roles --mp --mode manual

## Expect
- The prompted aws commands have no ones to create policies and with the ones creating roles and attaching the manged policies  
- The roles on AWS should be tagged with rosa_managed_policies=true  
- After run the commands, the account-roles are created on AWS and attached the managed polices  
~~- Three comnands to attach with three policy files named, ROSAInstallerCorePolicy, ROSAInstallerVPCPolicy,ROSAInstallerPrivateLinkPolicy to install roles will be prompted(SDA-7941)~~

## Step
~~Repeat step 1~2 with the old version managed polices(this is a temporary check before the managed-policies can be created by CS/product )~~

## Expect
~~The result should be same~~

## Step
Repeat step 1~2 with the path setting

## Expect
The result should be same

## Step
Repeat step 1~2 with the different account role version

## Expect
The result should be same

## Step
Repeat step 1~2 with the different manage account policies version

## Expect
The result should be same

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
Delete the managed account roles in auto mode

## Expect
- The account roles should be detached and deleted.  
- The managed policies should NOT be deleted.

## Step
Delete the managed account roles in manual mode

## Expect
- There are aws commands to detach the policies and delete the roles  
- No aws commands to delete the managed policies
