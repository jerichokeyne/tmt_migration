# Test

## Step
Check help message:  
\# rosa -h  
\# rosa attach -h  
\# rosa attach policy -h  
  
\# rosa detach -h  
\# rosa detach policy -h

## Expect
$ ./rosa -h  
....  
attach Attach AWS resource  
detach Detach AWS resource  
....  
$ ./rosa attach --help  
Attach AWS resource  
  
Usage:  
rosa attach [command]  
  
Available Commands:  
policy Attach AWS IAM Policies to an AWS IAM Role  
  
Flags:  
-h, --help help for attach  
  
Global Flags:  
--color string Surround certain characters with escape sequences to display them in color on the terminal. Allowed options are [auto never always] (default "auto")  
--debug Enable debug mode.  
  
$ ./rosa attach policy -h  
Attach existing AWS IAM Policies to an AWS IAM Role in the authenticated AWS Account  
  
Usage:  
rosa attach policy [flags]  
  
Examples:  
\# Attach policy <policy_arn_1> and <policy_arn_2> to role <role_name>  
rosa attach policy --role-name=<role_name> --policy-arns=<policy_arn_1>,<policy_arn_2>  
  
Flags:  
-h, --help help for policy  
-m, --mode string How to perform the operation. Valid options are:  
auto: Resource changes will be automatic applied using the current AWS account  
  
manual: Commands necessary to modify AWS resources will be output to be run manually  
-p, --policy-arns string Policy arn of the policies to be attached to the specified role. Format should be a comma-separated list. (required).  
-r, --role-name string Role name of the role to attach the specified policy (required).  
  
Global Flags:  
--color string Surround certain characters with escape sequences to display them in color on the terminal. Allowed options are [auto never always] (default "auto")  
--debug Enable debug mode.  
  
$ ./rosa detach -h  
Detach AWS resource  
  
Usage:  
rosa detach [command]  
  
Available Commands:  
policy Detach AWS IAM Policies from an AWS IAM Role  
  
Flags:  
-h, --help help for detach  
  
Global Flags:  
--color string Surround certain characters with escape sequences to display them in color on the terminal. Allowed options are [auto never always] (default "auto")  
--debug Enable debug mode.  
  
  
$ ./rosa detach policy -h  
Detach AWS IAM Policies from an AWS IAM Role in the authenticated AWS Account  
  
Usage:  
rosa detach policy [flags]  
  
Examples:  
\# Detach policy <policy_arn_1> and <policy_arn_2> from role <role_name>  
rosa detach policy --role-name=<role_name> --policy-arns=<policy_arn_1>,<policy_arn_2>  
  
Flags:  
-h, --help help for policy  
-m, --mode string How to perform the operation. Valid options are:  
auto: Resource changes will be automatic applied using the current AWS account  
  
manual: Commands necessary to modify AWS resources will be output to be run manually  
-p, --policy-arns string Policy arn of the policies to be detached from the specified role. Format should be a comma-separated list. (required).  
-r, --role-name string Role name of the role to detach the specified policy (required).  
  
Global Flags:  
--color string Surround certain characters with escape sequences to display them in color on the terminal. Allowed options are [auto never always] (default "auto")  
--debug Enable debug mode.

## Step
Prepare 12 custom policies on aws as prerequisite

## Expect

## Step
Attach policy to IAM role which is tagged with red-hat-managed=true  
- use '--mode manual'  
- dont setting --mode flag in the command  
- there are duplicated arns exists

## Expect
manual mode:  
- INFO message shows "I: Run the following command to attach the policy:"  
- the aws command used for attaching policies shows  
- The policies can be attached by the prompted command.  
  
dont setting --mode flag:  
- Will call out the interactive mode to ask to choose the mode  
? Attach policy mode: auto  
- After choose the mode, the result shoud be as above  
  
there are duplicated arns exists:  
Only one of duplicated policy is attached

## Step
Detach policy from   
IAM role which is tagged with red-hat-managed=true  
- use '--mode manual'  
- dont setting --mode flag in the command  
- there are duplicated arns exists  
- One existing policy but not attached to the role

## Expect
manual mode:  
- INFO message shows "I: Run the following command to detach the policy:"  
- the aws command used for detaching policies shows  
- The policies can be detached by the prompted command.  
  
dont setting --mode flag:  
- Will call out the interactive mode to ask to choose the mode  
? Detach policy mode: auto  
- After choose the mode, the result shoud be as above  
  
there are duplicated arns exists:  
Only one of duplicated policy is detached  
  
  
One existing policy but not attached to the role:  
I: The policy 'arn:aws:iam::301721915996:policy/aa/cc/yuwan-testp9' is currently not attached to role 'yw0428accr1-Installer-Role'

## Step
Attach multiple policies to IAM role which is tagged with red-hat-managed=true  
- use '--mode manual'  
- dont setting --mode flag in the command

## Expect
manual mode:  
- INFO message shows "I: Run the following command to attach the policy:"  
- the aws command used for attaching policies shows  
- The policies can be attached by the prompted command.  
  
dont setting --mode flag:  
- Will call out the interactive mode to ask to choose the mode  
? Attach policy mode: auto  
- After choose the mode, the result shoud be as above  
  
there are duplicated arns exists:  
Only one of duplicated policy is attached

## Step
Detach multiple policies to IAM role which is tagged with red-hat-managed=true  
- use '--mode manual'  
- dont setting --mode flag in the command  
- there are duplicated arns exists

## Expect
manual mode:  
- INFO message shows "I: Run the following command to detach the policy:"  
- the aws command used for detaching policies shows  
- The policies can be detached by the prompted command.  
  
dont setting --mode flag:  
- Will call out the interactive mode to ask to choose the mode  
? Detach policy mode: auto  
- After choose the mode, the result shoud be as above  
  
there are duplicated arns exists:  
Only one of duplicated policy is detached

## Step
Validations for the attch command:  
1. policy arn with invalid format  
2. not-existed policy arn  
3. not-existed role-name  
4. multiple policies arns and some of them are with invalid format or not existed  
5. The number of the attaching policies exceed the quote (L-0DA4ABF3)  
6. The role has no red-hat-managed=true tag  
7. There is empry string in the policy-arn

## Expect
1. E: Failed to find the policy 'aaaaa': operation error IAM: GetPolicy, https response error StatusCode: 400, RequestID: 83f82595-e3fa-465a-9d50-c7a6c444defe, api error ValidationError: 1 validation error detected: Value 'aaaaa' at 'policyArn' failed to satisfy constraint: Member must have length greater than or equal to 20  
  
2. E: Failed to find the policy 'arn:aws:iam::301721915996:policy/yuwan-testp999': operation error IAM: GetPolicy, https response error StatusCode: 404, RequestID: cccd5e7c-ff3e-4999-88ee-549f3681ed71, NoSuchEntity: Policy arn:aws:iam::301721915996:policy/yuwan-testp999 was not found.  
  
3. E: Failed to find the role 'yw0426accr999-Installer-Role': operation error IAM: GetRole, https response error StatusCode: 404, RequestID: 5bb239ba-cfdd-4d6b-b524-f3070f26ed46, NoSuchEntity: The role with name yw0426accr999-Installer-Role cannot be found.  
  
4. If should fail with the above message, and other policies should NOT be attached.  
  
5. E: Failed to attach policies due to quota limitations (total limit: 10, expected: 11)  
The total limit and expected number should be correct.  
  
6. E: Cannot attach/detach policies to non-ROSA roles  
  
7. E: Invalid policy arn '', expected a valid policy arn matching ^arn:aws[\w-]*:iam::(\d{12}|aws):policy(?:\/+[\w+=,.@-]+)+$

## Step
Validations for the detach command:  
1. policy arn with invalid format  
2. not-existed policy arn  
3. not-existed role-name  
4. multiple policies arns and some of them are with invalid format or not existed  
5. The role has no red-hat-managed=true tag  
6. There is empry string in the policy-arn

## Expect
1.E: Invalid policy arn 'arnaa', expected a valid policy arn matching ^arn:aws[\w-]*:iam::(\d{12}|aws):policy(?:\/+[\w+=,.@-]+)+$  
  
2. E: Failed to find the policy 'arn:aws:iam::301721915996:policy/aa/cc/yuwan-testp15': operation error IAM: GetPolicy, https response error StatusCode: 404, RequestID: 631b4655-4284-46dc-a835-aaf6b3f05982, NoSuchEntity: Policy arn:aws:iam::301721915996:policy/aa/cc/yuwan-testp15 was not found.  
  
3.E: Failed to find the role 'yw0428accr22-Installer-Role': operation error IAM: GetRole, https response error StatusCode: 404, RequestID: 1016545e-dd51-41e8-b24d-92a4fce0b182, NoSuchEntity: The role with name yw0428accr22-Installer-Role cannot be found.  
  
4. If should fail with the above message, and other policies should NOT be attached.  
  
5. E: Cannot attach/detach policies to non-ROSA roles  
  
6. E: Invalid policy arn '', expected a valid policy arn matching ^arn:aws[\w-]*:iam::(\d{12}|aws):policy(?:\/+[\w+=,.@-]+)+$

## Step
Attach multiple policies on account-roles and operator-roles then delete the roles

## Expect
- The roles deletion should work well  
- The arbitrary polcies should NOT be deleted by the command in auto mode. In manual mode, there should NOT be the commands to delete the arbitrary policies

## Step
Check '--debug' flag of `rosa attach/detach policy ....`

## Expect
--debug flag works well

## Step
Delete the installer role from AWS then repeat describe cluster with '--get-role-policy-bindings'

## Expect
E: Failed to get rolePolicyBinding: Failed to assume role with ARN 'arn:aws:iam::301721915996:role/aa/bb/yw0529accrv142-HCP-ROSA-Installer-Role': operation error STS: AssumeRole, https response error StatusCode: 403, RequestID: 9749829f-32af-413a-8024-ca43cf6f10b8, api error AccessDenied: User: arn:aws:sts::644306948063:assumed-role/RH-Managed-OpenShift-Installer/OCM is not authorized to perform: sts:AssumeRole on resource: arn:aws:iam::301721915996:role/aa/bb/yw0529accrv142-HCP-ROSA-Installer-Role
