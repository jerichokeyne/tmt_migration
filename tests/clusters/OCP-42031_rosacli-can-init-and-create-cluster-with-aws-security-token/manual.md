# Setup
How to generate security token and how to setup the env:  
1. Setup valid aws credentials on your local  
2. Run command below to get the security token and store it to a file  
$ aws sts assume-role --role-arn arn:aws:iam::301721915996:role/OSDCCSAdmin --role-session-name s3-access-example --profile default > assume-role-output.txt  
3. Run below commands to set the tokens to env variables  
`$ ``export AWS_ACCESS_KEY_ID=ASIAIOSFODNN7EXAMPLE`   
`$ ``export AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY`   
`$ ``export AWS_SESSION_TOKEN=AQoDYXdzEJr...<remainder of security token>  
`4. After setup, run below command to check whether it work`  
`$ ``aws ec2 describe-instances --region us-west-1`  
`You can move your credentials to credentials.bk to make sure below testing is using the security token`  
`Reference doc: [reference doc](<https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_use-resources.html>) ``

# Test

## Step
Launch rosa and Run command to init with invalid/non-setup token  
$ rosa init

## Expect
Error will output  
[xueli@xueli-work ~]$ rosa init  
I: Logged in as 'sdqe-regular01' on 'https://api.stage.openshift.com'  
E: Error creating AWS client: InvalidClientTokenId: The security token included in the request is invalid.  
status code: 403, request id: ba181ea8-9b05-4a3e-964c-d441d316c79c

## Step
Launch rosa and Run command to init with AWS_CA_BUNDLE env  
$ export AWS_CA_BUNDLE=~/rosa/ca.pem  
$ rosa init

## Expect
Error will output  
./rosa init  
I: Logged in as 'sdqe-regular01' on 'https://api.stage.openshift.com'  
E: Error creating AWS client: operation error STS: GetCallerIdentity, exceeded maximum number of attempts, 12, https response error StatusCode: 0, RequestID: , request send failed, Post "https://sts.us-east-2.amazonaws.com/": tls: failed to verify certificate: x509: certificate signed by unknown authority

## Step
Prepare sts security token according to the steps in setup

## Expect

## Step
Launch rosacli

## Expect

## Step
Check the init help message.

## Expect
\# rosa init -h  
Applies templates to support Red Hat OpenShift Service on AWS. If you are not  
yet logged in to OCM, it will prompt you for credentials.  
  
  
Usage:  
rosa init [flags]  
  
  
Examples:  
\# Configure your AWS account to allow IAM (non-STS) ROSA clusters  
rosa init  
  
  
\# Configure a new AWS account using pre-existing OCM credentials  
rosa init --token=$OFFLINE_ACCESS_TOKEN  
  
  
Flags:  
--delete   
--disable-scp-checks Indicates if cloud permission checks are disabled when attempting installation of the cluster.  
--client-id string OpenID client identifier. The default value is 'cloud-services'.  
--client-secret string OpenID client secret.  
--insecure Enables insecure communication with the server. This disables verification of TLS certificates and host names.  
--scope strings OpenID scope. If this option is used it will replace completely the default scopes. Can be repeated multiple times to specify multiple scopes. (default [openid])  
-t, --token string Access or refresh token generated from https://console.redhat.com/openshift/token/rosa.  
--token-url string OpenID token URL. The default value is 'https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token'.  
--profile string Use a specific AWS profile from your credential file.  
--region string Use a specific AWS region, overriding the AWS_REGION environment variable.  
-y, --yes Automatically answer yes to confirm operation.  
-h, --help help for init  
  
  
Global Flags:  
--debug Enable debug mode.

## Step
Run command to init  
$ rosa init

## Expect
The init will succeed  
[xueli@xueli-work ~]$ rosa init  
I: Logged in as 'sdqe-regular01' on 'https://api.stage.openshift.com'  
I: Validating AWS credentials...  
I: AWS credentials are valid!  
I: Validating SCP policies...  
I: AWS SCP policies ok  
I: Validating AWS quota...  
I: AWS quota ok. If cluster installation fails, validate actual AWS resource usage against https://docs.openshift.com/rosa/rosa_getting_started/rosa-required-aws-service-quotas.html  
I: Ensuring cluster administrator user 'osdCcsAdmin'...  
I: Admin user 'osdCcsAdmin' already exists!  
I: Validating SCP policies for 'osdCcsAdmin'...  
I: AWS SCP policies ok  
I: Validating cluster creation...  
I: Cluster creation valid  
I: Verifying whether OpenShift command-line tool is available...  
I: Current OpenShift Client Version: 4.8.0-fc.2

## Step
Run command to create cluster  
$ rosa create cluster -c xuelirosa

## Expect
-interactive mode for role selection will be started automatically

## Step
Run command to create non-sts cluster  
$ rosa create cluster -c xuelirosa --sts=false

## Expect
There will be error message like below:  
[xueli@xueli-work ~]$ rosa create cluster -c xuelirosa --sts=false  
E: Since your AWS credentials are returning an STS ARN you can only create STS clusters. Otherwise, switch to IAM credentials.

## Step
Run correct command like below to create cluster  
$ rosa create cluster \  
-c ${name} \  
--region ${region} \  
--version ${version}-${channel_group} \  
--channel-group ${channel_group} \  
--role-arn arn:aws:iam::${aws_account_id}:role/OSDCCSAdmin \  
--tags cluster-name:${name},cluster-version:${version}-${channel_group} \  
${roles}  
How to prepare roles: [How to prepare roles](<https://docs.google.com/document/d/1p1cQiL_KfcYHN5Xf_PJDf2fMY2jBJCGgr3hvHFOmkpE/edit#heading=h.1plbpfbj8i3o>)

## Expect
- The cluster will be created successfully  
[xueli@xueli-work ~]$ rosa create cluster -c xuelirosa  
W: More than one Installer role found  
? Installer role ARN: [Use arrows to move, type to filter, ? for more help]  
> arn:aws:iam::301721915996:role/account-for-ms-etsv-Installer-Role  
arn:aws:iam::301721915996:role/account-for-ms-oatm-Installer-Role  
arn:aws:iam::301721915996:role/account-for-ms-ukfy-Installer-Role  
arn:aws:iam::301721915996:role/account-for-yz-Installer-Role  
arn:aws:iam::301721915996:role/QEAuto-account-20220905-knhx-Installer-Role  
arn:aws:iam::301721915996:role/QEAuto-account-20220905-mqmj-Installer-Role  
arn:aws:iam::301721915996:role/QEAuto-account-20220905-nppy-Installer-Role

## Step
Run command to list clusters  
$ rosa list clusters

## Expect
- The cluster will be listed  
[xueli@xueli-work ~]$ rosa list clusters  
ID NAME STATE  
1l1r3fnejm3ifu92ehkfm0aj2v6nkhbi xuelirosa pending

## Step
Run command to describe the cluster  
$ rosa describe cluster -c xuelirosa

## Expect
The cluster will be described successfully  
[xueli@xueli-work ~]$ rosa describe cluster -c xuelirosa  
Name: xuelirosa  
ID: 1l1r3fnejm3ifu92ehkfm0aj2v6nkhbi  
External ID:   
OpenShift Version:   
Channel Group: stable  
DNS: xuelirosa.rud6.s1.devshift.org  
AWS Account: 301721915996  
API URL:   
Console URL:   
Region: us-east-1  
Multi-AZ: false  
Nodes:  
- Master: 3  
- Infra: 2  
- Compute: 2  
Network:  
- Service CIDR: 172.30.0.0/16  
- Machine CIDR: 10.0.0.0/16  
- Pod CIDR: 10.128.0.0/14  
- Host Prefix: /23  
State: pending (Waiting for OIDC configuration)  
Private: No  
Created: Jun 1 2021 09:37:05 UTC  
Details Page: https://qaprodauth.cloud.redhat.com/openshift/details/s/1tLEyjtz0A9fI2KcLhDSL79fVKj  
OIDC Endpoint URL: https://rh-oidc-staging.s3.us-east-1.amazonaws.com/1l1r3fnejm3ifu92ehkfm0aj2v6nkhbi

## Step
Configure IDPs according to below doc  
How to prepare roles: [How to prepare roles](<https://docs.google.com/document/d/1p1cQiL_KfcYHN5Xf_PJDf2fMY2jBJCGgr3hvHFOmkpE/edit#heading=h.1plbpfbj8i3o>)

## Expect

## Step
Wait for cluster ready

## Expect
Cluster will be ready in 2 hours
