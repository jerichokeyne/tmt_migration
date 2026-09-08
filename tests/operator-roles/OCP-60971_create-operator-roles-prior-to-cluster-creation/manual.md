# Test

## Step
Prepare the byo oidc config via `rosa create oidc-config --mode auto` command

## Expect

## Step
Create operator-roles with '--prefix' and --oidc-config-idl and --installer-role-arn flags, using the oidc-config-id created in step1.

## Expect
- The operator roles are created with the prefix.  
- The policies are created with the installer role prefix.  
- The role document should be contain the oidc provider url.  
- If the installer role is with path, the operator roles and policies should be with the same path.  
- If the installer role is the hypershift account roles, which should be managed policies, the operator roles will be created with attaching the hypershift managed policies.  
- There should be bellow message to guide users to create cluster:  
I: To create a cluster with these roles, run the following command:  
rosa create cluster --sts --oidc-config-id 23gi45fq24fjsivamt6bmhc096bogi4i --operator-roles-prefix yw0504sharedop1

## Step
Repeat step2 with --hosted-cp flag

## Expect
All results should be same with the ones in step2. and hypershift cluster specific roles are also created.  
- If the installer role is the hypershift account roles, which should be managed policies, the operator roles will be created with attaching the hypershift managed policies.

## Step
Repeat step2~3 in manual mode

## Expect
- AWS commands are prompted to create roles and polcies including attach the polycies.  
- All results should be same with the ones in step2~3 after run the aws commands

## Step
Check the interactive mode, by just setting prefix,  
\# rosa create operator-roles --prefix test

## Expect
- 'OIDC Endpoint URL','Create hosted control plane operator roles (optional)','Installer Role ARN','Mode' options should be prompted.  
- All the results should be same with the ones in step2~3 after input the correct value in all options.

## Step
Create operator roles not setting prefix or cluster id.

## Expect
yuwan1-mac:rosa yuwan$ ./rosa create operator-roles --installer-role-arn arn:aws:iam::301721915996:role/yw0308accr2-Installer-Role   
E: Either a cluster key for STS cluster or an operator roles prefix must be specified.

## Step
~~Check the validation for oidc-endpoint-url: - invalid url - not start with https:// schem~~

## Expect
~~yuwan1-mac:rosa yuwan$ ./rosa create operator-roles --prefix yw0309oper1 --installer-role-arn arn:aws:iam::301721915996:role/yw0308accr1-Installer-Role --oidc-endpoint-url yw0309byocc1-oidc-u2n4.s3.us-east-2.amazonaws.com --mode manual -y E: parse "yw0309byocc1-oidc-u2n4.s3.us-east-2.amazonaws.com": invalid URI for request yuwan1-mac:rosa yuwan$ ./rosa create operator-roles --prefix yw0309oper1 --installer-role-arn arn:aws:iam::301721915996:role/yw0308accr1-Installer-Role --oidc-endpoint-url http://yw0309byocc1-oidc-u2n4.s3.us-east-2.amazonaws.com --mode manual -y E: Expected OIDC endpoint URL 'http://yw0309byocc1-oidc-u2n4.s3.us-east-2.amazonaws.com' to use an https:// scheme~~

## Step
Check the validation for installer-role-arn  
- Not existed role  
- Not match the format of arn  
- Not the naming rule for install role

## Expect
yuwan1-mac:rosa yuwan$ ./rosa create operator-roles --prefix yw0309oper1 --installer-role-arn arn:aws:iam::301721915996aaaa:role/yw0308accr1222-Installer-Role --oidc-endpoint-url https://yw0309byocc1-oidc-u2n4.s3.us-east-2.amazonaws.com --mode manual -y  
E: Failed to determine if cluster has managed policies: NoSuchEntity: The role with name yw0308accr1222-Installer-Role cannot be found.  
  
yuwan1-mac:rosa yuwan$ ./rosa create operator-roles --prefix yw0309oper1 --installer-role-arn 301721915996aaaa:role/yw0308accr1222-Installer-Role --oidc-endpoint-url https://yw0309byocc1-oidc-u2n4.s3.us-east-2.amazonaws.com --mode manual -y  
E: Invalid ARN: arn: invalid prefix  
  
yuwan1-mac:rosa yuwan$ ./rosa create operator-roles --prefix ywoper1 --installer-role-arn arn:aws:iam::301721915996:role/yw0308accr1-Support-Role --oidc-endpoint-url https://yw0308byocc1-oidc-t6s9.s3.us-east-2.amazonaws.com --mode manual -y  
I: Can only use installer roles created through ROSA CLI for this flow.
