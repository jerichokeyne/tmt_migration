# Test

## Step
Check the 'rosa verify -h' help message

## Expect
[root@yuwan rosa]# ./rosa verify  
Verify resources are configured correctly for cluster install  
  
  
Usage:  
rosa verify [command]  
  
  
Available Commands:  
openshift-client Verify OpenShift client tools  
permissions Verify AWS permissions are ok for non-STS cluster install  
quota Verify AWS quota is ok for cluster install  
  
  
Flags:  
-h, --help help for verify  
  
  
Global Flags:  
--debug Enable debug mode.  
  
  
Use "rosa verify [command] --help" for more information about a command.  
[root@yuwan rosa]# ./rosa verify permissions -h  
Verify AWS permissions needed to create a non-STS cluster are configured as expected  
  
  
Usage:  
rosa verify permissions [flags]  
  
  
Aliases:  
permissions, scp  
  
  
Examples:  
\# Verify AWS permissions are configured correctly  
rosa verify permissions  
  
  
\# Verify AWS permissions in a different region  
rosa verify permissions --region=us-west-2  
  
  
Flags:  
-h, --help help for permissions  
--profile string Use a specific AWS profile from your credential file.  
--region string Use a specific AWS region, overriding the AWS_REGION environment variable.  
  
  
Global Flags:  
--debug Enable debug mode.  
[root@yuwan rosa]# ./rosa verify openshift-client -h  
Verify that the OpenShift client tools is installed and compatible.  
  
  
Usage:  
rosa verify openshift-client [flags]  
  
  
Aliases:  
openshift-client, oc, openshift  
  
  
Examples:  
\# Verify oc client tools  
rosa verify oc  
  
  
Flags:  
-h, --help help for openshift-client  
  
  
Global Flags:  
--debug Enable debug mode.  
[root@yuwan rosa]# ./rosa verify quota -h  
Verify AWS quota needed to create a cluster is configured as expected  
  
  
Usage:  
rosa verify quota [flags]  
  
  
Examples:  
\# Verify AWS quotas are configured correctly  
rosa verify quota  
  
  
\# Verify AWS quotas in a different region  
rosa verify quota --region=us-west-2  
  
  
Flags:  
-h, --help help for quota  
--profile string Use a specific AWS profile from your credential file.  
--region string Use a specific AWS region, overriding the AWS_REGION environment variable.  
  
  
Global Flags:  
--debug Enable debug mode.

## Step
Configure the AWS config with all permission and quota and have openshift-client on local env.  
Then verify them.

## Expect
[root@yuwan rosa]# ./rosa verify permissions  
I: Verifying permissions for non-STS clusters  
I: Validating SCP policies...  
I: AWS SCP policies ok  
[root@yuwan rosa]# ./rosa verify quota  
I: Validating AWS quota...  
I: AWS quota ok. If cluster installation fails, validate actual AWS resource usage against https://docs.openshift.com/rosa/rosa_getting_started/rosa-required-aws-service-quotas.html  
[root@yuwan rosa]# ./rosa verify openshift-client  
I: Verifying whether OpenShift command-line tool is available...  
I: Current OpenShift Client Version: 4.8.0-fc.2

## Step
Try to verify the permission/quota/openshift-client when missing them.

## Expect
There should be some error message.

## Step
Check the roascli version `rosa verson`

## Expect
- If the version is latest,  
$ ./rosa version  
1.2.35 (Build: 16391706)  
I: Your ROSA CLI is up to date.  
- If the version is not latest,  
$ ./rosa version  
1.2.24(Build: 16391706)  
I: There is a newer release version '1.2.26', please consider updating: https://console.redhat.com/openshift/downloads#tool-rosa  
  
- The output should contain GIt SHA from OCM-5782

## Step
Repeat the steps on Windows/MacOS/Linux

## Expect
- The function should work well  
- The output should display well
