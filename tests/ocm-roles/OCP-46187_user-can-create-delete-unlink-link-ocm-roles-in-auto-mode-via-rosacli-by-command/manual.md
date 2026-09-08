# Setup
$ rosa create cluster -c ${name}aa --region ${region} --version ${version}-${channel_group} --channel-group ${channel_group} --role-arn arn:aws:iam::${aws_account_id}:role/OSDCCSAdmin --tags cluster-name:${name},cluster-version:${version}-${channel_group} ${roles} --external-id "<external_id>"  
  
NOTE:   
20240716: merge OCP-59406 to this case. Till now, the mananged policiy for ocm role is not ready/exists on AWS(ROSAOCMPolicy). The automation for that will be implemented after the managed policy is ready on AWS

# Test

## Step
Create the admin ocm role with the command  
\# rosa create ocm-role --admin --permision-boundary <pb>--mode auto -y

## Expect
Pay attention in the output to ensure that the trust policies output the contents of their policy and that the roles output a link to the AWS Console.   
INFO: Creating role using 'arn:aws:iam::301721915996:user/yuwan'  
I: Attached trust policy to role 'ManagedOpenShift-OCM-Role-13849960(https://console.aws.amazon.com/iam/home?#/roles/ManagedOpenShift-OCM-Role-13849960)': {"Version": "2012-10-17", "Statement": [{"Action": ["sts:AssumeRole"], "Effect": "Allow", "Condition": {"StringEquals": {"sts:ExternalId": "1kDmx7itdCqfKPXlaIihdT3CIZL"}}, "Principal": {"AWS": ["arn:aws:iam::896164604406:role/RH-Managed-OpenShift-Installer"]}}]}  
  
  
INFO: Created role 'QEAuto-user-20220624-401-OCM-Role-12553207' with ARN 'arn:aws:iam::301721915996:role/QEAuto-user-20220624-401-OCM-Role-12553207'  
I: Attached policy 'arn:aws:iam::301721915996:policy/ManagedOpenShift-OCM-Role-13849960-Policy' to role 'ManagedOpenShift-OCM-Role-13849960(https://console.aws.amazon.com/iam/home?#/roles/ManagedOpenShift-OCM-Role-13849960)'  
  
  
INFO: Successfully linked role-arn 'arn:aws:iam::301721915996:role/QEAuto-user-20220624-401-OCM-Role-12553207' with organization account '1OAqHo0k19kyq7Xt7I1Zqb8Ok4K'   
  
  
- The permission boundary is added

## Step
List ocm-roles  
\# rosa list ocm-role

## Expect
- The ocm role is displayed  
- All parameters of the role are shown

## Step
Unlink ocm-role  
\# rosa unlink ocm-role --role-arn <rosa arn>

## Expect
INFO: Successfully unlinked role-arn 'arn:aws:iam::301721915996:role/QEAuto-user-20220624-401-OCM-Role-12553207' from organization account '1OAqHo0k19kyq7Xt7I1Zqb8Ok4K'

## Step
List ocm-role

## Expect
The related item shows 'Linked' with 'No'

## Step
Link ocm-role  
\# rosa link ocm-role --role-arn <rosa arn>

## Expect
INFO: Successfully linked role ARN 'arn:aws:iam::301721915996:role/QEAuto-user-20220624-401-OCM-Role-12553207' with account '1Pg8PstQKeyanR20qpwlvkEF9NC'

## Step
List ocm-role

## Expect
The related item shows 'Linked' with 'Yes'

## Step
Delete the ocm role with auto mode by command

## Expect
The role is unlinked and deleted.

## Step
Create ocm-role with the default prefix then delete the role and keep the policy then create again

## Expect
The ocm-role should be created successfuly (new checkpoint OCM-7881)

## Step
Create ocm-roles with the managed ocm role polices in auto mode  
\# rosa create ocm-role --managed-policies --mode auto  
\# rosa create ocm-role --managed-policies --mode auto --admin

## Expect
- The ocm-role is created on AWS and attached the managed policy  
- If '--admin' flag is set, the ocm role should be created with two managed policies attatching, one ocm managed role policy, the other is the admin ocm managed policy  
- The roles on AWS should be tagged with rosa_managed_policies=true

## Step
Create ocm-role with the managed ocm role policy in manual mode  
\# rosa create ocm-role --managed-policies --mode manual  
\# rosa create ocm-role --managed-policies --mode manual --admin

## Expect
- The prompted aws commands have no ones to create policies and just includes the ones creating roles and attaching the manged policies. If the '--admin' is set, two attaching commands including  
- The roles on AWS should be tagged with rosa_managed_policies=true  
- After run the commands, the ocm-role is created on AWS and attached the managed polices

## Step
Repeat step 1~2 with the path setting

## Expect

## Step
Delete the managed ocm roles in auto mode

## Expect
- The ocm roles should be detached and deleted.  
- The managed policies should NOT be deleted.

## Step
elete the managed ocm roles in manual mode

## Expect
- There are aws commands to detach the policies and delete the roles  
- No aws commands to delete the managed policies
