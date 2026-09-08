# Test

## Step
Check the help message of `rosa create operator-roles`

## Expect
.....  
--route53-role-arn string AWS IAM Role Arn with policy attached, associated with shared VPC. Grants permission necessary to handle route53 operations associated with a cross-account VPC. This flag deprecates '--shared-vpc-role-arn'.  
--vpc-endpoint-role-arn string AWS IAM Role ARN with policy attached, associated with the shared VPC. Grants permissions necessary to communicate with and handle a cross-account VPC.  
  
.......

## Step
`Create hosted-cp operator-roles with setting '--vpc-endpoint-role-arn`' and '--route53-role-arn'  
  
./rosa create operator-roles --prefix yuwan1121svs1 --role-arn arn:aws:iam::301721915996:role/aa/bb/yuwan1121accr1-HCP-ROSA-Installer-Role --oidc-config-id 2f5g2q5v1tggidltc70a01nr1a2cpfp1 --vpc-endpoint-role-arn arn:aws:iam::641733028092:role/yuwan-sharevpc-vpc-endpoint-role --hosted-cp --route53-role-arn arn:aws:iam::641733028092:role/yuwan-sharevpc-role -y --mode auto -y

## Expect
`  
` - 8 operator-roles are created  
- openshift-ingress-operator-cloud-credentials roles has two attached policies, one is the managed policy, the other is the `assume role policy for route53-role  
- The two assume role policies has red-hat-managed=true tag  
- kube-system-control-plane-operator roles has THREE attached policies, one is its managed policy, the other two are the assume role policies for route53-role and vpc-endpoint-role-arn, the policies has the 'sts:AssumeRole' permission of the two share vpc roles.  
- The two assume role policies are with tags hcp-shared-vpc=true and red-hat-managed=true`  
- There are INFO message about creating roles and attaching policies as before.

## Step
Create another set of operator-roles with same settings except prefix

## Expect
It should succeed as above

## Step
Delere the shared-vpc hcp operator-roles in auto mode

## Expect
`All roles are deleted successfully.  
  
- If there is no resource attaching the shared vpc assume role policies, the two assume role policies will be deleted and bellow info message showns,  
/ time=2024-12-03T16:37:37+08:00 level=info msg=Deleting policy 'arn:aws:iam::301721915996:policy/yuwan-sharevpc-vpc-endpoint-role2-assume-role'  
...  
\ time=2024-12-03T16:38:00+08:00 level=info msg=Deleting policy 'arn:aws:iam::301721915996:policy/yuwan-sharevpc-role2-assume-role'  
  
- If there is someresource attaching the shared vpc assume role policies blocking the policies deletion, the two assume role policies will be NOT deleted and bellow WARN message showns, and the warning message should be shown once for same policies  
time=2024-12-03T16:01:58+08:00 level=warning msg=Unable to delete policy arn:aws:iam::301721915996:policy/yuwan-sharevpc-vpc-endpoint-role-assume-role: Policy still attached to other resources  
time=2024-12-03T16:01:58+08:00 level=warning msg=Unable to delete policy arn:aws:iam::301721915996:policy/yuwan-sharevpc-role-assume-role: Policy still attached to other resources`

## Step
Check the "--delete-hcp-shared-vpc-policies" works  
- without --delete-hcp-shared-vpc-policies in auto mode  
- with --delete-hcp-shared-vpc-policies in auto mode  
- with --delete-hcp-shared-vpc-policies=false in auto mode

## Expect
- Try to delete the assume role policies. If there is no additional resource attaching the policies, they will be deleted.  
  
- Try to delete the assume role policies. If there is no additional resource attaching the policies, they will be deleted.  
  
- Don't try to delete the assume role policies, the policies will remain

## Step
Validations:  
- --vpc-endpoint-role-arn + NO --route53-role-arn + NO --hosted-cp  
-  NO --vpc-endpoint-role-arn + --route53-role-arn + --hosted-cp

## Expect
`- E: Setting the `vpc-endpoint-role-arn` flag is only supported for hosted clusters  
- E: Invalid configuration: Must supply 'route53-role-arn' flag when using the 'vpc-endpoint-role-arn' flag  
  
  
`
