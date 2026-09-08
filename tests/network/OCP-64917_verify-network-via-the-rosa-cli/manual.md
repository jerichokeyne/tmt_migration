# Test

## Step
Check the help message  
\# rosa verify -h  
\# rosa verify network -h

## Expect
yuwan1-mac:rosa yuwan$ ./rosa verify   
Verify resources are configured correctly for cluster install  
  
  
Usage:  
rosa verify [command]  
  
  
Available Commands:  
network   
openshift-client Verify OpenShift client tools  
permissions Verify AWS permissions are ok for non-STS cluster install  
quota Verify AWS quota is ok for cluster install  
rosa-client Verify ROSA client tools  
  
  
Flags:  
-h, --help help for verify  
  
  
Global Flags:  
--color string Surround certain characters with escape sequences to display them in color on the terminal. Allowed options are [auto never always] (default "auto")  
--debug Enable debug mode.  
  
  
Use "rosa verify [command] --help" for more information about a command.  
  
./rosa verify network --help  
Verify that the VPC subnets are configured correctly.  
  
  
Usage:  
rosa verify network [flags]  
  
  
Examples:  
\# Verify two subnets  
rosa verify network --subnet-ids subnet-03046a9b92b5014fb,subnet-03046a9c92b5014fb  
  
  
Flags:  
-c, --cluster string Name or ID of the cluster.  
-h, --help help for network  
--hosted-cp Run network verifier with hosted control plane platform configuration  
--region string Use a specific AWS region, overriding the AWS_REGION environment variable.  
--role-arn string STS Role ARN with get secrets permission.  
-s, --status-only Check status of previously submitted subnets.  
--subnet-ids strings The Subnet IDs to verify. Format should be a comma-separated list.  
--tags strings Supply custom tags to the network verifier. Tags will default to cluster tags if a cluster is supplied. Tags are comma separated, for example: 'key value, foo bar'  
-w, --watch Watch network verification progress.  
  
  
Global Flags:  
--color string Surround certain characters with escape sequences to display them in color on the terminal. Allowed options are [auto never always] (default "auto")  
--debug Enable debug mode.

## Step
Verify network with subnet ids  
NOTE: This step should be tested one subnet id and multiple subnet ids  
~~How to prepare subnet id which will fail the verification: create a VPC,then add deny rules in VPC Network ACLs(eg:deny 443 port) and rule number is less than 100 (Migrate the step to OCP-70370)~~

## Expect
yuwan1-mac:rosa yuwan$ ./rosa verify network --subnet-ids subnet-0ce53302e769cdc1d --role-arn arn:aws:iam::301721915996:role/as/sdf/yw0705accr1-Installer-Role --region us-west-2  
I: Verifying the following subnet IDs are configured correctly: [subnet-0ce53302e769cdc1d]  
I: subnet-0ce53302e769cdc1d: pending  
I: Run the following command to wait for verification to complete:  
rosa verify network --watch --status-only --subnet-ids subnet-0ce53302e769cdc1d  
yuwan1-mac:rosa yuwan$ ./rosa verify network --watch --status-only --subnet-ids subnet-0ce53302e769cdc1d  
I: Verifying the following subnet IDs are configured correctly: [subnet-0ce53302e769cdc1d]  
I: subnet-0ce53302e769cdc1d: passed  
  
- The info message shows as above  
- The command of "Run the following command to wait for verification to complete" should be correct  
- The result should be returned from CS correctly  
- The status should one of pending/passed/failed  
./rosa verify network --watch --status-only --subnet-ids subnet-0d0b68279e57a0e07,subnet-0961ae61201ce0e59,subnet-0f0ac9fef60d8c2f7  
I: Verifying the following subnet IDs are configured correctly: [subnet-0d0b68279e57a0e07 subnet-0961ae61201ce0e59 subnet-0f0ac9fef60d8c2f7]  
I: subnet-0d0b68279e57a0e07: failed Unable to verify egress to: [pull.q1w2.quay.rhcloud.com:443 cart-rhcos-ci.s3.amazonaws.com:443 openshift.org:443 quay.io:443 events.us-west-2.amazonaws.com:443 cloud.redhat.com:443 infogw.api.openshift.com:443 api.openshift.com:443 api.access.redhat.com:443 registry.access.redhat.com:443 sso.redhat.com:443 api.deadmanssnitch.com:443 observatorium.api.openshift.com:443 registry.redhat.io:443 ec2.amazonaws.com:443 route53.amazonaws.com:443 sts.amazonaws.com:443 sts.us-west-2.amazonaws.com:443 http-inputs-osdsecuritylogs.splunkcloud.com:443 elasticloadbalancing.us-west-2.amazonaws.com:443 nosnch.in:443 events.pagerduty.com:443 inputs1.osdsecuritylogs.splunkcloud.com:9997 ocm-quay-production-s3.s3.amazonaws.com:443 iam.amazonaws.com:443 quayio-production-s3.s3.amazonaws.com:443 console.redhat.com:80 tagging.us-east-1.amazonaws.com:443 quay-registry.s3.amazonaws.com:443 mirror.openshift.com:443 ec2.us-west-2.amazonaws.com:443 sso.redhat.com:80 console.redhat.com:443 cert-api.access.redhat.com:443]

## Step
Verify network with cluster id

## Expect
[yingzhan@localhost rosa]$ ./rosa verify network --cluster ying-hcp-a   
I: Verifying the following subnet IDs are configured correctly: [subnet-03399d0847258e86e subnet-0a07b4eaceca39405 subnet-03e7db0cafd0e1f61 subnet-05eae08c0cfbd1e3f subnet-02394f7afd63b20f5 subnet-0be58182739fcb9dd]  
I: subnet-03399d0847258e86e: pending  
I: subnet-0a07b4eaceca39405: passed  
I: subnet-03e7db0cafd0e1f61: pending  
I: subnet-05eae08c0cfbd1e3f: passed  
I: subnet-02394f7afd63b20f5: pending  
I: subnet-0be58182739fcb9dd: passed  
I: Run the following command to wait for verification to all subnets to complete:  
rosa verify network --watch --status-only --region us-west-2 --subnet-ids subnet-03399d0847258e86e,subnet-0a07b4eaceca39405,subnet-03e7db0cafd0e1f61,subnet-05eae08c0cfbd1e3f,subnet-02394f7afd63b20f5,subnet-0be58182739fcb9dd  
  
  
- The subnets of the cluster should be selected automatically by rosacli to verify  
- Others same as the results in step2  
-The check e2e result can refer to    
-If HCP cluster, the platform type should be hostedcluster  
-If Classic cluster,the platform type should be AWS

## Step
Verify network with subnet-ids and tag  
/rosa verify network --subnet-ids subnet-0ce53302e769cdc1d --role-arn <arn> --region us-west-2 --tags t2:v2

## Expect
-The tags parameters should be set in response with default tags  
"tags": {  
"Name": "osd-network-verifier",  
"osd-network-verifier": "owned",  
"red-hat-managed": "true",  
"t2": "v2"  
}  
-It should be set in AWS instance for the verifier

## Step
Verify network with cluster id and tag  
/rosa verify network --cluster <> --tags t2:v2

## Expect
-The tags parameters should be set in response with default tags  
For tags: it will show the default tags+cluster.aws.tags+custom tags added via OCM  
-It should be set in AWS instance for the verifier check

## Step
Verify network with subnet-ids  
with --hosted-cp   
without --hosted-cp

## Expect
-If --hosted-cp The platform type should be hostedcluster   
.. "platform": "aws-hosted-cp"...  
-If without --hosted-cp The platform type should be aws  
.. "platform": "aws-classic"...

## Step
Check if --status-only and --watch works well and --region

## Expect
- it will return the status of previously submitted subnets when use --status-only flag;  
- It will print info message if there is no previously submitted query,"I: subnet-0931cb67194a01f74: Network verification for subnet 'subnet-0931cb67194a01f74' not found"  
- It will check the subnet ids based on the --region, and using the default configured region if the flag is not set  
- --watch will watch and wait the verification progress and return the status at last

## Step
Repeat the steps on Windows/MacOS/Linux

## Expect
- The function should work well  
- The output should display well
