# Test

## Step
`Create hosted-cp account-roles with setting '--vpc-endpoint-role-arn`' and '--route53-role-arn' in manual mode  
  
% ./rosa create account-roles --prefix yw1126svpc1 --path /aa/bb/ --route53-role-arn arn:aws:iam::641733028092:role/yuwan-sharevpc-role --vpc-endpoint-role-arn arn:aws:iam::641733028092:role/yuwan-sharevpc-vpc-endpoint-role --mode manual -y

## Expect
`- There are aws commands promoted. There are two additional commands to create assume-role policies, with the 'sts:AssumeRole`' permission on the route53-role and vpc-endpoint-role  
- There are commands to attach the two assume role policies on the 'HCP-ROSA-Installer-Role' role  
- The commands to create the two assume-role policies have red-hat-managed=true in the commands  
After execute the aws commands,  
- 8 operator-roles are created  
- HCP-ROSA-Installer-Role has one managed policy attached, and two assume-role policies atatched`  
` - The two assume role policies are with tags hcp-shared-vpc=true and red-hat-managed=true

## Step
If the two assume role policies have already existed, repeat step1

## Expect
- There will not be the commands to creeate the assume role policies  
- Others are same as the results in step1

## Step
Check the path setting:  
- The role-arn has path  
- `vpc-endpoint-role-arn and route53-role-arn have path setting`

## Expect
- The assume role policies path should be same with the `vpc-endpoint-role-arn and route53-role-arn path setting  
- The path of 'role-arn' will not affect the assume role policies path`

## Step
Create another set of account-roles with same settings except prefix

## Expect
- There will not be the commands to create the assume role policies if they have already existed.  
- It should succeed as above

## Step
Delere the shared-vpc hcp account-roles in manual mode

## Expect
`All created roles are deleted successfully by the prompted commands  
All the policies attached on the classic account roles are deleted.  
There are two commands to delete delete the assume role policies.  
  
After execute the aws commands:  
- All classic account roles and policies are deleted successfully  
- All the hcp account roles are deleted successfully  
`

## Step
Check '--delete-hcp-shared-vpc-policies' works  
- without --delete-hcp-shared-vpc-policies in manual mode  
- with --delete-hcp-shared-vpc-policies in manual mode  
- with --delete-hcp-shared-vpc-policies=false in manual mode

## Expect
"--delete-hcp-shared-vpc-policies Deletes the Hosted Control Plane shared vpc policies" in help message of `rosa delete account -h`  
- There will be no commands to delete the assume role policies prompted  
- There will be commands to delete the assume role policies prompted.  
- There will be no commands to delete the assume role policies prompted

## Step
Validations:  
- --vpc-endpoint-role-arn + NO --route53-role-arn + NO --hosted-cp  
-  NO --vpc-endpoint-role-arn + --route53-role-arn + --hosted-cp

## Expect
`- E: Setting the `vpc-endpoint-role-arn` flag is only supported for hosted clusters  
- E: Invalid configuration: Must supply 'route53-role-arn' flag when using the 'vpc-endpoint-role-arn' flag  
  
  
`

## Step
As a regression testing, reperat step1 then attach some arbitrary policies on account roles then delete operator roles in manual mode

## Expect
It shouls succeed.
