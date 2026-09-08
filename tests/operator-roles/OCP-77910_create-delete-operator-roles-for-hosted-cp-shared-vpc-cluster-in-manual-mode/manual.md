# Test

## Step
`Create hosted-cp operator-roles with setting '--vpc-endpoint-role-arn`' and '--route53-role-arn' in manual mode  
  
./rosa create operator-roles --prefix yuwan1121svs1 --role-arn arn:aws:iam::301721915996:role/aa/bb/yuwan1121accr1-HCP-ROSA-Installer-Role --oidc-config-id 2f5g2q5v1tggidltc70a01nr1a2cpfp1 --vpc-endpoint-role-arn arn:aws:iam::641733028092:role/yuwan-sharevpc-vpc-endpoint-role --hosted-cp --route53-role-arn arn:aws:iam::641733028092:role/yuwan-sharevpc-role -y --mode auto -y

## Expect
`- There are aws commands promoted. There are two additional commands to create assume-role policies, with the 'sts:AssumeRole`' permission on the route53-role and vpc-endpoint-role  
- There are commands to attach the two assume role policies on the 'kube-system-control-plane-operator' role and to attach the 'vpc-endpoint-role' assume role policy on the 'openshift-ingress-operator-cloud-credentials' role  
- The two assume role policies are with tags hcp-shared-vpc=true and red-hat-managed=true  
After execute the aws commands,  
- 8 operator-roles are created  
- openshift-ingress-operator-cloud-credentials roles has two attached policies, one is the managed policy, the other is the `assume role policy for route53-role  
- kube-system-control-plane-operator roles has THREE attached policies, one is its managed policy, the other two are the assume role policies for route53-role and vpc-endpoint-role-arn, the policies has the 'sts:AssumeRole' permission of the two share vpc roles.`  
- The two assume role policies are with tags hcp-shared-vpc=true and red-hat-managed=true

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
Create another set of operator-roles with same settings except prefix

## Expect
- There will not be the commands to creeate the assume role policies if they have already existed.  
- It should succeed as above

## Step
Delere the shared-vpc hcp operator-roles in manual mode

## Expect
`All roles are deleted successfully by the prompted commands  
There are commmads to delete two created assume role policies.`

## Step
Validations:  
- --vpc-endpoint-role-arn + NO --route53-role-arn + NO --hosted-cp  
-  NO --vpc-endpoint-role-arn + --route53-role-arn + --hosted-cp  
- The assume role policies already existed, or policies with duplicated name has existed

## Expect
`- E: Setting the `vpc-endpoint-role-arn` flag is only supported for hosted clusters  
- E: Invalid configuration: Must supply 'route53-role-arn' flag when using the 'vpc-endpoint-role-arn' flag  
- It will returns error when execte the commands. Actually the error is from the awscli.  
  
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
As a regression testing, reperat step1 then attach some arbitrary policies on operator roles then delete operator roles in manual mode

## Expect
It shouls succeed.
