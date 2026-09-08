# Setup
The role policies should have all permissions defined in <https://github.com/openshift/managed-cluster-config/tree/master/resources/sts>

# Test

## Step
Get the latest version of rosacli and log in

## Expect
Support sts from version 1.0.6

## Step
Run 'rosa create account-roles --prefix <p> --mode auto --path <path> -y'

## Expect
* The account-roles with the default openshift version(X.Y) should be created.
  * 7 roles will be created, 3 for hosted-cp cluster, 4 for classic STS clusters
  * For those 3 hosted-cp account-roles, they will be attached with managed policies; Those 4 sts account-roles will be attached with NON-managed policies created by rosacli automatically(check via aws)
  * The hosted-cp account-roles are naming with the format <prefix>-HCP-ROSA-<role type name> and the sts account-roles are naming withe format <prefix>-<role type name>
  * The output specifies what policy was attached to which role. Additionally, the roles should also have a link to their page in the AWS Console e.g.: Attached policy 'arn:aws:iam::xxx:policy/test-Installer-Role-Policy' to role 'test-Installer-Role(https://console.aws.amazon.com/iam/home?#/roles/test-Installer-Role)'
  * Trust policies should include the contents of their policy in the output e.g.: I: Attached trust policy to role 'oa-417-Worker-Role(https://console.aws.amazon.com/iam/home?#/roles/oa-417-Worker-Role)': {"Version": "2012-10-17", "Statement": [{"Action": ["sts:AssumeRole"], "Effect": "Allow", "Principal": {"Service": ["ec2.amazonaws.com"]}}]}
  * Managed permission policies should include a link to their public AWS docs page:   
I: Attached policy 'ROSAWorkerInstancePolicy(https://docs.aws.amazon.com/aws-managed-policy/latest/reference/ROSAWorkerInstancePolicy)' to role 'oa-417-HCP-ROSA-Worker-Role(https://console.aws.amazon.com/iam/home?#/roles/oa-417-HCP-ROSA-Worker-Role)'  

  * No message to guide the user to create a cluster with the account-roles,"I: To create a cluster with these roles, run the following command:" (OCM-1755)
  * There is hint message "I: By default, the create account-roles command creates two sets of account roles, one for classic ROSA clusters, and one for Hosted Control Plane clusters.  
In order to create a single set, please set one of the following flags: --classic or --hosted-cp"

Role type name for hosted-cp : Installer-Role,Support-Role,Worker-Role   
Role type name for classic sts cluster: Installer-Role,Support-Role,Worker-Role ,ControlPlane-Role  
hosted-cp managed policies for account-roles: /service-role/ROSAInstallerPolicy,service-role/ROSASRESupportPolicy,service-role/ROSAWorkerInstancePolicy

## Step
Run 'rosa create account-roles --prefix <p> --mode auto --path <path> -y --hosted-cp'

## Expect
* Only 3 hosted-cp account-roles are created
  * They will be attached with managed policies as default and mandatorily
  * The hosted-cp account-roles are naming with the format <prefix>-HCP-ROSA-<role type name>
  * The output specifies what policy was attached to which role, e.g.: Attached policy 'arn:aws:iam::xxx:policy/test-Installer-Role-Policy' to role 'test-Installer-Role(https://console.aws.amazon.com/iam/home?#/roles/test-Installer-Role)'
  * No message to guide the user to create a cluster with the account-roles,"I: To create a cluster with these roles, run the following command:" (OCM-1755)

Role type name for hosted-cp : Installer-Role,Support-Role,Worker-Role   
hosted-cp managed policies for account-roles: /service-role/ROSAInstallerPolicy,service-role/ROSASRESupportPolicy,service-role/ROSAWorkerInstancePolicy

## Step
Run 'rosa create account-roles --prefix <p> --mode auto --path <path> -y --classic'

## Expect
* 4 classic STS account-roles are created
  * Those 4 sts account-roles will be attached with NON-managed policies created by rosacli automatically(check via aws)
  * The output specifies what policy was attached to which role, e.g.: Attached policy 'arn:aws:iam::xxx:policy/test-Installer-Role-Policy' to role 'test-Installer-Role(https://console.aws.amazon.com/iam/home?#/roles/test-Installer-Role)'
  * No message to guide the user to create a cluster with the account-roles,"I: To create a cluster with these roles, run the following command:" (OCM-1755)

  
Role type name for classic sts cluster: Installer-Role,Support-Role,Worker-Role ,ControlPlane-Role

## Step
Repeat step2 and step4 to check --managed-policies flag woks 
  * for hosted-cp account-roles, it only supports the managed-polices , see expected result 1st point.
  * for classic account-roles with `--managed-policies'` should use the managed polices, keep the original result. NOTE: this flag is hidden, and managed polices for classic account-roles are not ready on AWS, if you want to test it, it needs prepare managed-policies for classic account roles manually. And also creating classic account roles with managed policies are not support on PROD env

## Expect
If using --managed-policies flag, the classic sts roles will also be attached with the managed policies  
  
1. `yuwan1-mac:1.2.36rc3 yuwan$ ./rosa create account-roles --hosted-cp --managed-policies=false --mode auto -y --prefix test`  
`I: Logged in as 'sdqe-rosa' on '``[https://api.stage.openshift.com](<https://api.stage.openshift.com/>)``'`  
`E: Setting `hosted-cp` as unmanaged policies is not supported  
`
  * `Error message be same for staging env and prod (OCM-6570)`

## Step
Repeat step2~4 to check --permissions-boundary flag woks

## Expect
- The account-roles should be created with the permissions-boundary set.  
- Others results should be same with the ones of step2~4

## Step
Repeat step2~4 to check --version flag woks

## Expect
- The account-roles should be created with the version  
- Others results should be same with the ones of step2~4

## Step
Repeat step2~7 with "--mode manual"

## Expect
- AWS commands for creating account-roles should be prompted  
- The commands should be executed successfully  
- Roles should be created successfully, the final result should be same with the ones of step2~7

## Step
Set the mode to manual and pipeline the output into a file  
$ rosa create account-roles --prefix aaaa --mode manual --permissions-boundary arn:aws:iam::301721915996:policy/xueli-openshift>file

## Expect
Only commands will be write to the file, and the file can be executed with command without error

## Step
Create the account-roles with --force-policy-creation flag (works only with auto mode)  
rosa create account-roles --mode auto -y -f

## Expect
Default roles created/recreated with skipping compatibility check
