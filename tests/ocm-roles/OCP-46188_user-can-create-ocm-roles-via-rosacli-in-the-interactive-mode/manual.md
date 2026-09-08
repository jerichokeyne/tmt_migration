# Test

## Step
Check the help message,  
\# rosa create -h  
\# rosa create ocm-role -h

## Expect
[root@yuwan rosa]# ./rosa create -h  
......  
ocm-role Create role used by OCM  
......  
\# ./rosa create ocm-role -h  
........  
Create role used by OCM to verify necessary roles and OIDC providers are in place.  
  
Usage:  
rosa create ocm-role [flags]  
  
Aliases:  
ocm-role, ocmrole  
  
Examples:  
\# Create default ocm role for ROSA clusters using STS  
rosa create ocm-role  
  
\# Create ocm role with a specific permissions boundary  
rosa create ocm-role --permissions-boundary arn:aws:iam::123456789012:policy/perm-boundary  
  
Flags:  
--admin Enable admin capabilities for the role  
-h, --help help for ocm-role  
-i, --interactive Enable interactive mode.  
-m, --mode string How to perform the operation. Valid options are:  
auto: Resource changes will be automatic applied using the current AWS account  
  
manual: Commands necessary to modify AWS resources will be output to be run manually  
--permissions-boundary string The ARN of the policy that is used to set the permissions boundary for the OCM role.  
--prefix string User-defined prefix for all generated AWS resources (default "ManagedOpenShift")  
  
Global Flags:  
--color string Surround certain characters with escape sequences to display them in color on the terminal. Allowed options are [auto never always] (default "auto")  
--debug Enable debug mode.  
--profile string Use a specific AWS profile from your credential file.  
--region string Use a specific AWS region, overriding the AWS_REGION environment variable.  
-y, --yes Automatically answer yes to confirm operation.

## Step
Create the ocm-role in the auto mode in the interactive mode  
NOTE: It needs the user who has '`OrganizationLabel`' permission

## Expect
-----manual mode------  
\# ./rosa create ocm-role -i  
I: Creating ocm role  
? Role prefix: ManagedOpenShift  
? Enable admin capabilities for the OCM role (optional): Yes  
? Permissions boundary ARN (optional):   
? Role creation mode: manual  
I: All policy files saved to the current directory  
I: Run the following commands to create the ocm role and policies:  
  
aws iam create-role \  
--role-name ManagedOpenShift-OCM-Role-12553207 \  
--assume-role-policy-document file://sts_ocm_trust_policy.json \  
--tags Key=rosa_role_prefix,Value=ManagedOpenShift Key=rosa_role_type,Value=OCM Key=rosa_environment,Value=staging Key=rosa_admin_role,Value=true  
  
aws iam create-policy \  
--policy-name ManagedOpenShift-OCM-Role-12553207-Policy \  
--policy-document file://sts_ocm_permission_policy.json \  
--tags Key=rosa_role_prefix,Value=ManagedOpenShift Key=rosa_role_type,Value=OCM Key=rosa_environment,Value=staging  
  
aws iam attach-role-policy \  
--role-name ManagedOpenShift-OCM-Role-12553207 \  
--policy-arn arn:aws:iam::301721915996:policy/ManagedOpenShift-OCM-Role-12553207-Policy  
  
aws iam create-policy \  
--policy-name ManagedOpenShift-OCM-Role-12553207-Admin-Policy \  
--policy-document file://sts_ocm_admin_permission_policy.json \  
--tags Key=rosa_admin_role,Value=true  
  
aws iam attach-role-policy \  
--role-name ManagedOpenShift-OCM-Role-12553207 \  
--policy-arn arn:aws:iam::301721915996:policy/ManagedOpenShift-OCM-Role-12553207-Admin-Policy  
  
rosa link ocm-role --role-arn arn:aws:iam::301721915996:role/ManagedOpenShift-OCM-Role-12553207  
  
-----auto mode------  
[root@yuwan rosa]# ./rosa create ocm-role -i  
I: Creating ocm role  
? Role prefix: yw4988i2  
? Enable admin capabilities for the OCM role (optional): Yes  
? Permissions boundary ARN (optional):   
? Role creation mode: auto  
I: Creating role using 'arn:aws:iam::301721915996:user/yuwan'  
? Create the 'yw4988i2-OCM-Role' role? Yes  
I: Created role 'yw4988i2-OCM-Role' with ARN 'arn:aws:iam::301721915996:role/yw4988i2-OCM-Role'  
? Link the 'arn:aws:iam::301721915996:role/yw4988i2-OCM-Role' role with organization '1H9SY60bJWyoynWMsZzZEvtLFdI'? Yes  
I: Successfully linked role-arn 'arn:aws:iam::301721915996:role/yw4988i2-OCM-Role' with organization account '1H9SY60bJWyoynWMsZzZEvtLFdI'  
[root@yuwan rosa]#   
  
When the interactive mode is called with not all flags set, the parameters which are set with flag will be prompted as the default one.

## Step
Repeat step2 with an acocunt which has no '`OrganizationLabel`' permission

## Expect
E: Unable to link role arn 'arn:aws:iam::301721915996:role/ywocmrole01-OCM-Role' with the organization id : '1OAqHo0k19kyq7Xt7I1Zqb8Ok4K' : identifier is '11', code is 'ACCT-MGMT-11' and operation identifier is 'bf96d87b-cb68-435e-9f23-12f6b0452cf5': Account with ID 1Pg91NjVkaKuxDvnp9iXQa8MlC3 denied access to perform create on OrganizationLabel with HTTP call POST /api/accounts_mgmt/v1/organizations/1OAqHo0k19kyq7Xt7I1Zqb8Ok4K/labels

## Step
Check the validation for the validation for the -permissions-boundary.

## Expect
There should be validation for it.  
X Sorry, your reply was invalid: Invalid ARN: arn: invalid prefix
