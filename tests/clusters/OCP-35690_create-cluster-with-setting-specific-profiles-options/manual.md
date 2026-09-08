# Test

## Step
Log in the moactl

## Expect

## Step
Prepare the aws config and credential with aws profiles, like bellow  
[default]  
output = table  
region = us-east-2  
[profile yuwan]  
output = table  
region = us-east-2

## Expect

## Step
~~Check the '--profile' in all commands help info~~

## Expect
~~It should contains "--profile string Use a specific AWS profile from your credential file."~~

## Step
Try to create one cluster with specific profile

## Expect
It should works.  
NOTE: The tool uses the config following the order bellow,CLI option then AWS_PROFILE variable after that using defaults
