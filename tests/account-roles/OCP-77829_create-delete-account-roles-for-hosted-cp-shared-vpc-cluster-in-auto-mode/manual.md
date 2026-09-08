# Test

## Step
Check the help message of `rosa create account-roles`

## Expect
.....  
--route53-role-arn string Role ARN associated with the private hosted zone used for Hosted Control Plane cluster shared VPC, this role contains policies to be used with Route 53  
  
--vpc-endpoint-role-arn string Role ARN associated with the shared VPC used for Hosted Control Plane clusters, this role contains policies to be used with the VPC endpoint  
.......

## Step
`Create hosted-cp account-roles with setting '--vpc-endpoint-role-arn`' and '--route53-role-arn'  
  
rosa create account-roles --prefix yw1120svpc1 --path /aa/bb/ --permissions-boundary arn:aws:iam::301721915996:policy/aa/bb/yw1120accr2-Installer-Role-Policy --route53-role-arn arn:aws:iam::641733028092:role/yuwan-sharevpc-role --vpc-endpoint-role-arn arn:aws:iam::641733028092:role/yuwan-sharevpc-vpc-endpoint-role -y --hosted-cp --mode auto -y

## Expect
`  
` - Three account-roles are created  
- Install role has three policies attached, one is managed hcp installer policies, another two are assume role policies created by rosacli.   
The two assume role policies is named by <share_vpc_role_names>-assume-role  
`- The two assume role policies are with tags hcp-shared-vpc=true and red-hat-managed=true`  
- There are INFO message about creating roles and attaching policies as before.

## Step
Create second set of hcp shared vpc roles with the same setting but a new prefix

## Expect
The result should be same.

## Step
- Delere the shared-vpc hcp first account-roles created in step2 in auto mode:  
- Delere the shared-vpc hcp second account-roles created in step3 in auto mode:

## Expect
`1.  
All roles are deleted successfully.  
All two created assume role policies are Not deleted and report warning message :  
I: Deleting account role 'yw1128svpc2-HCP-ROSA-Installer-Role'  
time=2024-11-28T10:15:59+08:00 level=warning msg=Unable to delete policy yuwan-sharevpc-role-assume-role: Policy still attached to 1 other resource(s)  
time=2024-11-28T10:15:59+08:00 level=warning msg=Unable to delete policy yuwan-sharevpc-vpc-endpoint-role-assume-role: Policy still attached to 1 other resource(s)  
  
2.  
All roles are deleted successfully.  
All policies including the two assume role policies are deleted from AWS  
`

## Step
TBD: create with the two flags without setting '--hosted-cp' or 'classic'

## Expect
All roles are created , the hosted-cp roles are as above

## Step
Validations:  
- Invalid arns of the two flags  
- create classic roles with setting the two flag  
- Create with only one of the two flag

## Expect
`- failed with validation error  
- It should fail with error,  
E: Setting the `route53-role-arn` flag is only supported for hosted clusters  
E: Setting the `vpc-endpoint-role-arn` flag is only supported for hosted clusters  
- It should fail with error,  
E: Must supply 'vpc-endpoint-role-arn' flag when using the 'route53-role-arn' flag  
E: Must supply 'route53-role-arn' flag when using the 'vpc-endpoint-role-arn' flag  
  
  
`

## Step
Create multiple times with the same share vpc arns.

## Expect
It should succeed

## Step
Check the "--delete-hcp-shared-vpc-policies" works  
- without --delete-hcp-shared-vpc-policies in auto mode  
- with --delete-hcp-shared-vpc-policies in auto mode  
- with --delete-hcp-shared-vpc-policies=false in auto mode

## Expect
- Try to delete the assume role policies. If there is no additional resource attaching the policies, they will be deleted.  
time=2024-12-11T16:08:52-05:00 level=info msg=Deleting policy 'arn:aws:iam::301721915996:policy/jkeyne-1211-01-shared-route53-role-assume-role'  
time=2024-12-11T16:08:52-05:00 level=info msg=Deleting policy 'arn:aws:iam::301721915996:policy/jkeyne-1211-01-shared-vpce-role-assume-role'  
  
- Try to delete the assume role policies. If there is no additional resource attaching the policies, they will be deleted.  
  
- Don't try to delete the assume role policies, the policies will remain
