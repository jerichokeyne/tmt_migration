# Test

## Step
Prepare the byo oidc config via `rosa create oidc-config --mode auto` command

## Expect

## Step
Create operator-roles with '--prefix' and --oidc-config-idl and --installer-role-arn flags, using the oidc-config-id created in step1 in manaul mode

## Expect
- AWS Commands are prompted  
- The roles(6 for classic sts operator roles) are created after execute the commands  
- The operator-roles should use the same path/version/managed-policy(true or false) with the installer-roles ones

## Step
Repeat step2 with --hosted-cp flag

## Expect
- AWS Commands are prompted  
- The roles(8 for classic sts operator roles) are created after execute the commands  
- The operator-roles should use the same path/version/managed-policy(true or false) with the installer-roles ones

## Step
List the operator-role with prefix

## Expect
All bellow field should be shown with correct values.  
$ ./rosa list operator-roles --prefix yuwan-test-op  
I: Fetching operator roles  
OPERATOR NAME OPERATOR NAMESPACE ROLE NAME ROLE ARN CLUSTER ID VERSION POLICIES

## Step
Check the interactive mode, by just setting prefix,  
\# rosa create operator-roles --prefix test -i

## Expect
- All required options should be promoted.  
- It works well, roles should be created after the interactive is finished.  
-If hosted-cp set yes, only managed policies account role are listed

## Step
[before classic sts managed policy ready]   
Create non-hosted-cp opeterator-roles with HCP installer role

## Expect
E: There was an error creating the operator roles: NoSuchEntity: Policy arn:aws:iam::301721915996:policy/ROSAMachineAPIOperator does not exist or is not attachable.  
status code: 404, request id: 7d2b8f42-40ec-44cf-9393-e7e846ca57f1  
  
This is caused by the operator-roles using the same configure of managed-policy with the installer role, it will happen this error before the managed policy ready

## Step
Create classic sts and hosted-cp cluster with the operator-roles created above

## Expect
The cluster should be created successfully
