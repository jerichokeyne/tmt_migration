# Test

## Step
Create STS cluster with the account roles with managed polices,  
NOTE: There is no validation for the compatibility of account-role version and cluster version, in other word, all managed roles will be shown in the account-roles list in the interactive mode, and the cluster creation should be successfully even the account roles version is less than the cluster version(SDA-8328).

## Expect

## Step
Create operator-roles with the managed operator role polices in auto mode  
\# rosa create operator-roles --mode auto

## Expect
- as the account-roles uses the managed policies, the operator roles will create with the managed operator policies by default  
- The operator roles will be created with the managed operator policies attached.  
- The roles on AWS should be tagged with rosa_managed_policies=true  
- For the STS cluster which version >4.9, the additional operator role will be created with the managed operator policies attached  
- For the Hypershift cluster, the hypershift cluster specific operator roles will be created with the managed operator policies attached

## Step
Create STS cluster with the account roles with managed policies then-->  
Create STS cluster in the auto mode

## Expect
- (Need to confirm with DEV) as the account-roles uses the managed policies, the operator roles will create with the managed operator policies by default  
- The operator roles will be created with the managed operator policies attached.  
- The roles on AWS should be tagged with rosa_managed_policies=true  
- For the STS cluster which version >4.9, the additional operator role will be created with the managed operator policies attached  
- For the Hypershift cluster, the hypershift cluster specific operator roles will be created with the managed operator policies attached

## Step
Repeat the step2 ~3 with manual mode

## Expect
- The prompted aws commands have no ones to create policies and with the ones creating roles and attaching the manged policies  
- For the STS cluster which version >4.9, there should be the aws command for the additional operator role with the managed operator policies attached  
- For the Hypershift cluster, there should be the aws command for the hypershift cluster specific operator roles with the managed operator policies attached  
- After run the commands, the account-roles are created on AWS and attached the managed polices

## Step
Repeat step2~4 with the hypershift account-roles and the cluster created with them

## Expect
- The operator roles should be created with the hypershift role polices which are named openshift_hcp_<roleType>_policy  
- Others should be same with the one of step2~4

## Step
Repeat step 1~3 with the old version managed polices(this is a temporary check before the managed-policies can be created by CS/product )

## Expect
- The operator roles will be created if the cluster version is compatible with the cluster version, or there should be some error message shown

## Step
Repeat step 1~2 with the different channel-group

## Expect
The result should be same

## Step
Create multiple managed operator roles

## Expect
The result should be same

## Step
Check the `rosa describe cluster`

## Expect
The 'Managed Policies' in the output should show 'Yes'

## Step
Delete the managed operator roles in auto mode

## Expect
- The operator roles should be detached and deleted.  
- The managed policies should NOT be deleted.  
- For the hypershift cluster, the hypershift cluster specific opertor roles should be deleted.

## Step
Delete the managed operator roles in manual mode

## Expect
- There are aws commands to detach the policies and delete the roles  
- No aws commands to delete the managed policies
