# Test

## Step
1. Verify "rosa list instance-types -h" will display help message

## Expect
List Instance types that are available for use with ROSA.  
  
  
Usage:  
rosa list instance-types [flags]  
  
  
Aliases:  
instance-types, instancetypes  
  
  
Examples:  
\# List all instance types  
rosa list instance-types  
  
  
Flags:  
--external-id string An optional unique identifier that might be required when you assume a role in another account.  
-h, --help help for instance-types  
--hosted-cp Enable the use of Hosted Control Planes  
-o, --output string Output format. Allowed formats are [json yaml]  
--region string Use a specific AWS region, overriding the AWS_REGION environment variable.  
--role-arn string STS Role ARN with get secrets permission.  
-y, --yes Automatically answer yes to confirm operation.  
  
  
Global Flags:  
--color string Surround certain characters with escape sequences to display them in color on the terminal. Allowed options are [auto never always] (default "auto")  
--debug Enable debug mode.  
--profile string Use a specific AWS profile from your credential file.

## Step
2. Verify available instances in a given region:  
rosa list instance-types --region us-east-1 --role-arn $installer_role_arn

## Expect
ID CATEGORY CPU_CORES MEMORY  
dl1.24xlarge accelerated_computing 96 768.0 GiB  
g4dn.12xlarge accelerated_computing 48 192.0 GiB  
g4dn.16xlarge accelerated_computing 64 256.0 GiB  
g4dn.2xlarge accelerated_computing 8 32.0 GiB  
g4dn.4xlarge accelerated_computing 16 64.0 GiB  
g4dn.8xlarge accelerated_computing 32 128.0 GiB  
g4dn.metal accelerated_computing 96 384.0 GiB  
g4dn.xlarge accelerated_computing 4 16.0 GiB  
g5.12xlarge accelerated_computing 48 192.0 GiB  
g5.16xlarge accelerated_computing 64 256.0 GiB  
g5.24xlarge accelerated_computing 96 384.0 GiB  
  
....

## Step
3. Verify available instances with interactive mode:  
rosa list instance-types --region us-east-1

## Expect
Same output as step 2

## Step
4. "rosa list instance-types --region xxxx" will return error message about unsupported region

## Expect
rosa list instance-types --region xxxx  
E: Unsupported region 'xxxx', available regions: [ap-east-1, eu-west-1, eu-west-2, eu-west-3, sa-east-1, us-east-1, us-east-2, us-west-1, us-west-2, af-south-1, ap-south-1, ap-south-2, eu-north-1, eu-south-1, eu-south-2, me-south-1, ca-central-1, eu-central-1, eu-central-2, il-central-1, me-central-1, us-gov-east-1, us-gov-west-1, ap-northeast-1, ap-northeast-2, ap-northeast-3, ap-southeast-1, ap-southeast-2, ap-southeast-3, ap-southeast-4]
