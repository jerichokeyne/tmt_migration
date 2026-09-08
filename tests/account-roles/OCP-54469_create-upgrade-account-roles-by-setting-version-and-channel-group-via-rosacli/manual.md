# Test

## Step
Log in via rosa-cli using the command <<rosa login>>  
Note: It is recommended that you use the SDQE rosa account as your personal one may not have channel-groups enabled

## Expect
r rosa login  
To login to your Red Hat account, get an offline access token at https://console.redhat.com/openshift/token/rosa  
I: Logged in as 'sdqe-rosa' on 'https://api.openshift.com'

## Step
Create account-roles in different version and channel-group  
Command: rosa create account-roles --prefix <prefix> --mode auto--version <specific_version> --channel-group <channel_group>  
NOTE: [4.11, 4.10, 4.9, 4.8, 4.7] are supported till now  
  
potential channel groups are [listed here](<https://docs.openshift.com/container-platform/4.13/updating/understanding-upgrade-channels-release.html>)

## Expect
- The account-roles with specific version are created, and the role and policy are tagged with the version.  
- channel-group should works if a new version released in specific channel.  
  
rosa create account-roles --prefix oaharoni --mode auto --channel-group fast  
I: Logged in as 'sdqe-rosa' on 'https://api.openshift.com'  
I: Validating AWS credentials...  
I: AWS credentials are valid!  
I: Validating AWS quota...  
I: AWS quota ok. If cluster installation fails, validate actual AWS resource usage against https://docs.openshift.com/rosa/rosa_getting_started/rosa-required-aws-service-quotas.html  
I: Verifying whether OpenShift command-line tool is available...  
I: Current OpenShift Client Version: 4.14.6  
I: Creating account roles  
I: By default, the create account-roles command creates two sets of account roles, one for classic ROSA clusters, and one for Hosted Control Plane clusters.  
In order to create a single set, please set one of the following flags: --classic or --hosted-cp  
I: Creating classic account roles using 'arn:aws:iam::301721915996:user/oaharoni'  
I: Created role 'oaharoni-Support-Role' with ARN 'arn:aws:iam::301721915996:role/oaharoni-Support-Role'  
I: Created role 'oaharoni-Installer-Role' with ARN 'arn:aws:iam::301721915996:role/oaharoni-Installer-Role'  
I: Created role 'oaharoni-ControlPlane-Role' with ARN 'arn:aws:iam::301721915996:role/oaharoni-ControlPlane-Role'  
I: Created role 'oaharoni-Worker-Role' with ARN 'arn:aws:iam::301721915996:role/oaharoni-Worker-Role'  
I: Creating hosted CP account roles using 'arn:aws:iam::301721915996:user/oaharoni'  
I: Created role 'oaharoni-HCP-ROSA-Installer-Role' with ARN 'arn:aws:iam::301721915996:role/oaharoni-HCP-ROSA-Installer-Role'  
I: Created role 'oaharoni-HCP-ROSA-Support-Role' with ARN 'arn:aws:iam::301721915996:role/oaharoni-HCP-ROSA-Support-Role'  
I: Created role 'oaharoni-HCP-ROSA-Worker-Role' with ARN 'arn:aws:iam::301721915996:role/oaharoni-HCP-ROSA-Worker-Role'

## Step
Upgrade the account-roles from a lower version to higher one by setting the '--version' and 'channel-group' flags

## Expect
- The account-roles with specific version are upgraded, and the role and policy are tagged with the version.  
- channel-group should works if a new version released in specific channel.

## Step
Repeat step2~3 with the manual mode. It will be the same command but mode will be manual  
Command: rosa create account-roles --prefix <prefix> --path <path> --mode manual --version <specific_version> --channel-group <channel_group>

## Expect
Then results should be same with the above ones
