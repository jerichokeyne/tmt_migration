# Test

## Step
Login via rosacli and check the help message of `rosa create oidc-config -h` and `rosa create -h`

## Expect
- There is "oidc-config Create OIDC config for an STS cluster."  
- The help message for creating oidc-config  
- There is help message for 'prefix'  
yuwan1-mac:rosa yuwan$ ./rosa create oidc-config -h  
Create OIDC config in a S3 bucket for the client AWS account and populates it to be compliant with OIDC protocol. It also creates a Secret in Secrets Manager containing the private key.  
  
Usage:  
rosa create oidc-config [flags]  
  
Aliases:  
oidc-config, oidcconfig, oidcconfig  
  
Examples:  
\# Create OIDC config  
rosa create oidc-config  
  
Flags:  
-h, --help help for oidc-config  
-i, --interactive Enable interactive mode.  
-m, --mode string How to perform the operation. Valid options are:  
auto: Resource changes will be automatic applied using the current AWS account  
  
manual: Commands necessary to modify AWS resources will be output to be run manually  
--prefix string Prefix for the OIDC configuration, secret and provider.  
--raw-files Creates OIDC config documents (Private RSA key, Discovery document, JSON Web Key Set) and saves locally for the client to create the configuration.  
  
Global Flags:  
--color string Surround certain characters with escape sequences to display them in color on the terminal. Allowed options are [auto never always] (default "auto")  
--debug Enable debug mode.  
--profile string Use a specific AWS profile from your credential file.  
--region string Use a specific AWS region, overriding the AWS_REGION environment variable.  
-y, --yes Automatically answer yes to confirm operation.

## Step
Create oidc config in manual mode  
\# rosa create oidc-config --mode manual -y  
\# rosa create oidc-config --mode manual -y --prefix <preifx>

## Expect
- There are three files using for creating oidc config generated under the current folder  
rosa-private-key-oidc-b4k8.key and discovery-document-oidc-w5p2.json and jwks-oidc-w5p2.json  
- There are aws commands using for creating oidc config prompted. The aws commands should contain the flag to create tag 'red-hat-managed=true' for the resources.  
I: This command will create a S3 bucket populating it with documents to be compliant with OIDC protocol. It will also create a Secret in Secrets Manager containing the private key.  
aws s3api create-bucket \  
--bucket yw0301byocc1-oidc-n4h0 \  
--create-bucket-configuration LocationConstraint=us-east-2 \  
--region us-east-2  
  
aws s3api put-bucket-tagging \  
--bucket yw0301byocc1-oidc-n4h0 \  
--tagging 'TagSet=[{Key=red-hat-managed,Value=true}]'  
  
aws s3api put-object \  
--acl public-read \  
--body ./discovery-document-yw0301byocc1-oidc-n4h0.json \  
--bucket yw0301byocc1-oidc-n4h0 \  
--key .well-known/openid-configuration \  
--tagging 'red-hat-managed=true'  
  
rm discovery-document-yw0301byocc1-oidc-n4h0.json  
  
aws s3api put-object \  
--acl public-read \  
--body ./jwks-yw0301byocc1-oidc-n4h0.json \  
--bucket yw0301byocc1-oidc-n4h0 \  
--key keys.json \  
--tagging 'red-hat-managed=true'  
  
rm jwks-yw0301byocc1-oidc-n4h0.json  
  
aws secretsmanager create-secret \  
--description "Secret for yw0301byocc1-oidc-n4h0" \  
--name rosa-private-key-yw0301byocc1-oidc-n4h0 \  
--region us-east-2 \  
--secret-string file://rosa-private-key-yw0301byocc1-oidc-n4h0.key \  
--tags Key=red-hat-managed,Value=true  
  
rm rosa-private-key-yw0301byocc1-oidc-n4h0.key

## Step
Create oidc config with the '--raw-files' flag   
\# rosa create oidc-config --raw-files -y  
\# rosa create oidc-config --raw-files -y --prefix <prefix>

## Expect
- I: Please use generated files to create an OIDC compliant configuration.  
- There are three files using for creating oidc config generated under the current folder  
rosa-private-key-oidc-b4k8.key and discovery-document-oidc-w5p2.json and jwks-oidc-w5p2.json  
- The key and two json file can be used and works well  
- If the 'prefix' is specified, the generated files will be with the prefix in the names:  
-rw-r--r-- 1 yuwan staff 3243 Feb 8 16:46 rosa-private-key-yw0208bccr1-oidc-h6a6.key  
-rw-r--r-- 1 yuwan staff 387 Feb 8 16:46 discovery-document-yw0208bccr1-oidc-h6a6.json  
-rw-r--r-- 1 yuwan staff 917 Feb 8 16:46 jwks-yw0208bccr1-oidc-h6a6.json

## Step
Repeat step 2~3 to create oidc config with some region specified with '--region'

## Expect
The S3 should be created with the the LocationConstraint of the specified one

## Step
Try to create oidc config with the auto and manual mode in the interactive mode

## Expect
- There is "OIDC config creation mode" option to ask for choosing the mode  
- other results should be same with the non-interactive mode

## Step
Test other flags of this command:  
--output  
--color  
--debug  
--profile  
-y

## Expect
They should work well  
For the '-o' flag  
- The output should be shown in yaml or json format as the flag value  
- it only supports auto mode, otherwise prompts warning message "W: --output param is not supported outside auto mode."

## Step
Delete the byo config in manual mode

## Expect
- The secret manager will be deleted on AWS  
- The S3 bucket will be deleted from AWS  
- The interactive mode should work well
