# Test

## Step
Create account-roles in the interactive mode  
\# rosa create account-roles -i

## Expect
`? Create Hosted CP account roles: Yes  
? Use account roles for Hosted CP shared VPC?: Yes  
? Set VPC endpoint role ARN (optional): arn:aws:iam::641733028092:role/yuwan-sharevpc-vpc-endpoint-role  
? Set route53 role ARN (optional): arn:aws:iam::641733028092:role/yuwan-sharevpc-role`  
  
- If 'Create Hosted CP account roles' choose Yes, above three questions will prompte or they will not prompt  
- If 'Use account roles for Hosted CP shared VPC' choose YES, 'Set VPC endpoint role ARN' and 'Set route53 role ARN' will prompt and as required values  
- After input 'Set VPC endpoint role ARN' and 'Set route53 role ARN' and choose auto mode, account-roles will be created, the hostecp installer role will attach one managed policy and two assume role policies as command mode does  
- If use manual mode, after input 'Set VPC endpoint role ARN' and 'Set route53 role ARN', the aws command to create account-roles should be print out as the command mode does. The commands includes two to create assume-role policies and attach them on the hostec-cp install role.  
- The two assume role policies are with tags hcp-shared-vpc=true and red-hat-managed=true

## Step
Create shared vpc account-roles by command which doesn't set all required flags, like --prefix, --mode

## Expect
- Interacitve mode will be prompted and following flow should be same as step1  
- The value has set by flags should be prefilled as default value in the questions

## Step
Validations:  
- vpc-endpoint-role-arn + NO route53-role-arn  
-  Empty vpc-endpoint-role-arn and route53-role-arn. NOTE: empty value can be passed by double quotation marks or entering the 'return/enter' key on the keyborad  
- Invalid arn format

## Expect
`  
- X Sorry, your reply was invalid: Value is required  
- X Sorry, your reply was invalid: Value is required  
- X Sorry, your reply was invalid: Invalid ARN: arn: invalid prefix  
  
`

## Step
Check the help message for the three question

## Expect
? Whether or not to set route53/VPC endpoint role ARNs to be used for Hosted CP shared VPC (cross-account VPC)  
? Role ARN associated with the shared VPC used for Hosted Control Plane clusters, this role contains policies to be used with the VPC endpoint  
? Role ARN associated with the private hosted zone used for Hosted Control Plane cluster shared VPC, this role contains policies to be used with Route 53

## Step
Delete the account-roles without mode flag to test the interactive mode

## Expect
- Interactive mode will prompt, and ask for the mode  
- There is a question "Attempt to delete Hosted CP shared VPC policies" if choose manual mode in the interactive mode.  
-- If choose auto mode and N at "Attempt to delete Hosted CP shared VPC policies", rosacli will delete the account-roles without trying to delete the two shared vpc assume role policies  
-- If choose auto mode and Y at "Attempt to delete Hosted CP shared VPC policies", rosacli will delete the account-roles roles and also try to delete the two shared vpc assume role policies  
--- If there is no resource attaching the shared vpc assume role policies, the two assume role policies will be deleted and bellow info message showns,  
/ time=2024-12-03T16:37:37+08:00 level=info msg=Deleting policy 'arn:aws:iam::301721915996:policy/yuwan-sharevpc-vpc-endpoint-role2-assume-role'  
...  
\ time=2024-12-03T16:38:00+08:00 level=info msg=Deleting policy 'arn:aws:iam::301721915996:policy/yuwan-sharevpc-role2-assume-role'  
  
--- If there is someresource attaching the shared vpc assume role policies blocking the policies deletion, the two assume role policies will be NOT deleted and bellow WARN message showns, and the warning message should be shown once for same policies  
I: Deleting account role 'yw1203svpc1-HCP-ROSA-Installer-Role'  
time=2024-12-03T17:14:01+08:00 level=warning msg=Unable to delete policy yuwan-sharevpc-role-assume-role: Policy still attached to 1 other resource(s)  
time=2024-12-03T17:14:01+08:00 level=warning msg=Unable to delete policy yuwan-sharevpc-vpc-endpoint-role-assume-role: Policy still attached to 1 other resource(s)  
  
  
---- If choose manual mode, and Y at "Create commands to delete Hosted CP shared VPC policies? question in the interactive mode, the aws commands will contains the ones to delete the shared vpc account-roles and also the ones to delete the shared vpc assume role policies. Using all the prompted commands can delete all account-roles and also the created role policies(classic) and also the shared-vpc assume roles policies.  
  
---- If choose manual mode, and Y at "Create commands to delete Hosted CP shared VPC policies?' question in the interactive mode, the aws commands will contains the ones to delete the shared vpc account-roles but NO ones to delete the shared vpc assume role policies. Using all the prompted commands can delete all account-roles and also the created role policies(classic) .

## Step
Check the '--delete-hcp-shared-vpc-policies' and the "? Attempt to delete Hosted CP shared VPC policies?" question in the interactive mode.  
  
Delete the account-roles calling out the interactive mode via the way which not apply all required flag, like '--mode', `rosa delete account-roles --prefix <--delete-hcp-shared-vpc-policies>`  
  
choose manual mode in the interactive mode:  
- with --delete-hcp-shared-vpc-policies in the command  
- without --delete-hcp-shared-vpc-policies in the command  
- with --delete-hcp-shared-vpc-policies=false in the command  
  
choose auto mode in the interactive mode:  
- with --delete-hcp-shared-vpc-policies in the command  
- without --delete-hcp-shared-vpc-policies in the command  
- with --delete-hcp-shared-vpc-policies=false in the command

## Expect
choose manual mode in the interactive mode:  
- There is commands to delete the assume roles policies prompted  
- There is no commands to delete the assume roles policies prompted  
- There is no commands to delete the assume roles policies prompted  
  
  
choose auto mode in the interactive mode:  
- There is no "? Attempt to delete Hosted CP shared VPC policies?" question during hosted-cp shared vpc account-roles deletion and try to delete the assume polcies in following process.  
  
% ./rosa delete account-roles --prefix yw1211svpc1 --delete-hcp-shared-vpc-policies   
? Account role deletion mode: auto  
W: There are no classic account roles to be deleted  
I: Deleting hosted CP account roles  
? Delete the account role 'yw1211svpc1-HCP-ROSA-Worker-Role'? Yes  
I: Deleting account role 'yw1211svpc1-HCP-ROSA-Worker-Role'  
? Delete the account role 'yw1211svpc1-HCP-ROSA-Installer-Role'? Yes  
I: Deleting account role 'yw1211svpc1-HCP-ROSA-Installer-Role'  
time=2024-12-12T11:27:38+08:00 level=info msg=Deleting policy 'arn:aws:iam::301721915996:policy/a/b/yuwan-sharevpc-role2-assume-role'  
time=2024-12-12T11:27:38+08:00 level=info msg=Deleting policy 'arn:aws:iam::301721915996:policy/a/b/yuwan-sharevpc-vpc-endpoint-role2-assume-role'  
? Delete the account role 'yw1211svpc1-HCP-ROSA-Support-Role'? Yes  
I: Deleting account role 'yw1211svpc1-HCP-ROSA-Support-Role'  
I: Successfully deleted the hosted CP account roles  
  
- There is "? Attempt to delete Hosted CP shared VPC policies?" question. If choose Y, the following process will try to delete the assume role policies; If chosse N, it will not delete the assume role policies.  
  
- There is no "? Attempt to delete Hosted CP shared VPC policies?" question during hosted-cp shared vpc account-roles deletion and it will not delete the assume polcies in following process.
