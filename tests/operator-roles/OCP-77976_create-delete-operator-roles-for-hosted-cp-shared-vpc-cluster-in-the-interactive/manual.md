# Test

## Step
Create account-roles in the interactive mode:

```bash
```bash
rosa create operator-roles -i
```
```

## Expect
```
? Create Hosted CP account roles: Yes
? Use operator roles for Hosted CP shared VPC?: Yes
```
? Set VPC endpoint role ARN: arn:aws:iam::641733028092:role/yuwan-sharevpc-vpc-endpoint-role
? Set route53 role ARN: arn:aws:iam::641733028092:role/yuwan-sharevpc-role

- If 'Create Hosted CP account roles' choose Yes, above three questions will prompte or they will not prompt
- If 'Use operator roles for Hosted CP shared VPC' choose YES, 'Set VPC endpoint role ARN' and 'Set route53 role ARN' will prompt and as required values
- After input 'Set VPC endpoint role ARN' and 'Set route53 role ARN' and choose auto mode, operator-roles will be created, kube-system-control-plane-operator  role will attach one managed policy and two assume role policies as command mode does; openshift-ingress-operator-cloud-credentials will attach one managed policy and one route53 assume role policy
- If use manual mode, after input 'Set VPC endpoint role ARN' and 'Set route53 role ARN', the aws command to create operator-roles should be print out as the command mode does. The commands includes two to create assume-role policies and attach them on kube-system-control-plane-operator role, and to attach route53 assume role policy to openshift-ingress-operator-cloud-credentials role.
- The two assume role policies are with tags hcp-shared-vpc=true and red-hat-managed=true

## Step
Create shared vpc operator-roles by command which doesn't set all required flags, like , --mode

## Expect
- Interacitve mode will be prompted and following flow should be same as step1
- The value has set by flags should be prefilled as default value in the questions

## Step
Validations:
- vpc-endpoint-role-arn + NO route53-role-arn
-  Empty vpc-endpoint-role-arn and route53-role-arn. NOTE: empty value can be passed by double quotation marks or entering the 'return/enter' key on the keyborad
- Invalid arn format

## Expect
```
X Sorry, your reply was invalid: Value is required
- X Sorry, your reply was invalid: Value is required
X Sorry, your reply was invalid: Invalid ARN: arn: invalid prefix
```

## Step
Check the help message for the three question

## Expect
```
? Whether or not to set route53/VPC endpoint role ARNs to be used for Hosted CP shared VPC (cross-account VPC)
? AWS IAM Role ARN with policy attached, associated with the shared VPC. Grants permissions necessary to communicate with and handle a cross-account VPC.
? AWS IAM Role Arn with policy attached, associated with shared VPC. Grants permission necessary to handle route53 operations associated with a cross-account VPC. This flag deprecates '--shared-vpc-role-arn'.
```

## Step
Check the `--delete-hcp-shared-vpc-policies` flag and the `? Attempt to delete Hosted CP shared VPC policies?` question in interactive mode.

Delete the account-roles by invoking interactive mode without all required flags, such as `--mode`:

```bash
```bash
rosa delete account-roles --prefix <--delete-hcp-shared-vpc-policies>
```
```

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


- There is "? Attempt to delete Hosted CP shared VPC policies?" question. If choose Y, the following process will try to delete the assume role policies; If chosse N, it will not delete the assume role policies.

- There is no "? Attempt to delete Hosted CP shared VPC policies?" question during hosted-cp shared vpc account-roles deletion and it will not delete the assume polcies in following process.
