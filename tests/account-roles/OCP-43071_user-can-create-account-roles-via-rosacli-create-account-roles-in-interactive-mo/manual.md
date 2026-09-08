# Setup
$ rosa create cluster -c ${name}aa --region ${region} --version ${version}-${channel_group} --channel-group ${channel_group} --role-arn arn:aws:iam::${aws_account_id}:role/OSDCCSAdmin --tags cluster-name:${name},cluster-version:${version}-${channel_group} ${roles} --external-id "<external_id>"

# Test

## Step
Get the latest version of rosacli

## Expect
Support sts from version 1.0.6

## Step
Check help message

## Expect
Flags:  
--classic Create only classic Rosa account roles  
-f, --force-policy-creation Forces creation of policies skipping compatibility check  
-h, --help help for account-roles  
--hosted-cp Technology Preview: Enable the use of Hosted Control Planes  
-i, --interactive Enable interactive mode.  
-m, --mode string How to perform the operation. Valid options are:  
auto: Resource changes will be automatic applied using the current AWS account  
  
manual: Commands necessary to modify AWS resources will be output to be run manually  
--path string The arn path for the account/operator roles as well as their policies  
--permissions-boundary string The ARN of the policy that is used to set the permissions boundary for the account roles.  
--prefix string User-defined prefix for all generated AWS resources (default "ManagedOpenShift")  
--version string Version of OpenShift that will be used to setup policy tag, for example "4.11"

## Step
Run below command go into interactive mode  
$ rosa create account-roles -i

## Expect
- Check all prompted options as bellow:  
- "Create Classic account roles" default value should be Y and "Create Hosted CP account roles" default value should be N  
- All options should work well and take effect after the inputs  
- No message to guide the user to create a cluster with the account-roles,"I: To create a cluster with these roles, run the following command:" (OCM-1755)  
- If inout Y both for hosted-cp and classic account-roles option,there is hint message "I: By default, the create account-roles command creates two sets of account roles, one for classic ROSA clusters, and one for Hosted Control Plane clusters.  
In order to create a single set, please set one of the following flags: --classic or --hosted-cp"  
  
yuwan1-mac:rosa yuwan$ ./rosa create account-roles -i  
I: Logged in as 'sdqe-rosa' on 'https://api.stage.openshift.com'  
I: Validating AWS credentials...  
I: AWS credentials are valid!  
I: Validating AWS quota...  
I: AWS quota ok. If cluster installation fails, validate actual AWS resource usage against https://docs.openshift.com/rosa/rosa_getting_started/rosa-required-aws-service-quotas.html  
I: Verifying whether OpenShift command-line tool is available...  
I: Current OpenShift Client Version: 4.7.13  
I: Creating account roles  
? Role prefix: yuwan-test3  
? Permissions boundary ARN (optional):   
? Path (optional): /asd/sf/  
? Role creation mode: manual  
? Create Classic account roles: No  
? Create Hosted CP account roles (optional): No

## Step
Set different flags then to to the interactive mode

## Expect
- The default value should be the one set with the flag  
- If --hosted-cp is set,"Create Classic account roles" will not be asked; If --classic is set,"Create Hosted CP account roles" will not be asked

## Step
Create account-roles without login the rosacli

## Expect
The interactive mode should be prompted to guide users to input the token.  
[root@yuwan rosa]# ./rosa create account-roles  
To login to your Red Hat account, get an offline access token at https://console.redhat.com/openshift/token/rosa  
? Copy the token and paste it here: *********************************************************************************************************************************  
I: Logged in as 'sdqe-regular01' on 'https://api.openshift.com'  
I: Validating AWS credentials...  
I: AWS credentials are valid!  
I: Validating AWS quota...  
I: AWS quota ok. If cluster installation fails, validate actual AWS resource usage against https://docs.openshift.com/rosa/rosa_getting_started/rosa-required-aws-service-quotas.html  
I: Verifying whether OpenShift command-line tool is available...  
I: Current OpenShift Client Version: 4.8.0-fc.2  
I: Starting to create the account roles!  
? OpenShift version to create account roles: 4.8..........

## Step
Create account-roles with the account who has no enough aws quota

## Expect
There is a warning message shown.

## Step
Create account-roles with oc not installed

## Expect
There is a warning message shown.  
W: OpenShift command-line tool is not installed.

## Step
Create account-roles with the invalid aws credential

## Expect
There is error message,  
E: Failed to create AWS client: SignatureDoesNotMatch: The request signature we calculated does not match the signature you provided. Check your AWS Secret Access Key and signing method. Consult the service documentation for details.
