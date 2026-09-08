# Test

## Step
Check the help message   
$ rosa create network --help

## Expect
yuwan@yuwan-mac rosa % ./rosa create network -h  
Available parameters in default template:  
AvailabilityZoneCount  
AZ1  
AZ2  
AZ3  
AZ4  
Region  
Name  
VpcCidr  
Tags  
  
  
Usage:  
rosa create network [flags]  
  
  
Aliases:  
network, networks  
  
  
Examples:  
\# Create a AWS cloudformation stack  
rosa create network <template-name> --param Param1=Value1 --param Param2=Value2   
  
  
\# ROSA quick start HCP VPC example  
rosa create network rosa-quickstart-default-vpc --param Region=us-west-2 --param Name=quickstart-stack --param AvailabilityZoneCount=1 --param AZ1=us-west-2b --param AZ2=us-west-2d --param VpcCidr=10.0.0.0/16  
  
  
\# To delete the AWS cloudformation stack  
aws cloudformation delete-stack --stack-name <name> --region <region>  
  
  
\# TEMPLATE_NAME:  
Specifies the name of the template to use. This should match the name of a directory   
under the path specified by '--template-dir' or the 'OCM_TEMPLATE_DIR' environment variable.  
The directory should contain a YAML file defining the custom template structure.  
  
  
If no TEMPLATE_NAME is provided, or if no matching directory is found, the default   
built-in template 'rosa-quickstart-default-vpc' will be used.  
  
  
Flags:  
-h, --help help for network  
-m, --mode string How to perform the operation. Valid options are:  
auto: Resource changes will be automatic applied using the current AWS account  
manual: Commands necessary to modify AWS resources will be output to be run manually  
--param stringArray List of parameters  
--template-dir string Use a specific template directory, overriding the OCM_TEMPLATE_DIR environment variable.  
  
  
Global Flags:  
--color string Surround certain characters with escape sequences to display them in color on the terminal. Allowed options are [auto never always] (default "auto")  
--debug Enable debug mode.  
--profile string Use a specific AWS profile from your credential file.  
--region string Use a specific AWS region, overriding the AWS_REGION environment variable.  
-y, --yes Automatically answer yes to confirm operation.  
  
  
yuwan@yuwan-mac rosa %

## Step
Try to create network resources with providing template and param.  
$rosa create network rosa-quickstart-default-vpc --param=Name=aaraj --param=Region=us-west-2 --param AvailabilityZoneCount=3 --template-dir /home/aaraj/rosa/cmd/create/network/templates/  
  
from OCM-14846 , the max supported AvailabilityZoneCount is 4

## Expect
The resources should be created in the stack.  
Check that 3 private and 3 public subnets are created a/c to the availabilty zones in the provided region.  
  
Please check that all the resources are created correctly inside the aws console, with correct info and tags set.

## Step
Try the above command by setting AvailabiltyZoneCount param value to be 2. and try to set tags using param.  
$rosa create network rosa-quickstart-default-vpc --param=Name=aaraj --param=Region=us-west-2 --param AvailabilityZoneCount=2 --template-dir /home/aaraj/rosa/cmd/create/network/templates/ --param=Tags=foo=bar

## Expect
Check that 2 private and 2 public subnets are created a/c to the availabilty zones in the provided region.  
  
Check that the tags passed through the --param flag are set to all the created resources.

## Step
Try using the manual mode to create the network resources  
$ ./rosa-1.2.47-rc2 create network rosa-quickstart-default-vpc --param=Name=aaraj --param=Region=us-west-2 --param AvailabilityZoneCount=2 --template-dir /home/aaraj/rosa/cmd/create/network/templates/ --param=Tags=foo=bar --mode manual

## Expect
I: Run the following command to create the stack manually:  
aws cloudformation create-stack --stack-name aaraj --template-body file:///home/aaraj/rosa/cmd/create/network/templates//rosa-quickstart-default-vpc/cloudformation.yaml --param ParameterKey=AvailabilityZoneCount,ParameterValue=2 ParameterKey=Name,ParameterValue=aaraj ParameterKey=Region,ParameterValue=us-west-2 --tags Key=foo,Value=bar --region us-west-2  
  
Run the command and check that all resources are created successfully.  
  
$ aws cloudformation create-stack --stack-name aaraj --template-body file:///home/aaraj/rosa/cmd/create/network/templates//rosa-quickstart-default-vpc/cloudformation.yaml --param ParameterKey=AvailabilityZoneCount,ParameterValue=2 ParameterKey=Name,ParameterValue=aaraj ParameterKey=Region,ParameterValue=us-west-2 --tags Key=foo,Value=bar --region us-west-2  
{  
"StackId": "arn:aws:cloudformation:us-west-2:301721915996:stack/aaraj/ab2345b0-94e2-11ef-a683-02eb4ee947d7"  
}

## Step
Create a template file to create a single vpc  
$ vim /home/aaraj/rosa-cli-releases/templates/aaraj-template/cloudformation.yaml   
AWSTemplateFormatVersion: 2010-09-09  
Description:  
This template deploys a single vpc in us-west-2 region.  
  
  
Parameters:  
Region:  
Type: String  
Description: "AWS Region"  
Default: "us-west-2"  
Name:  
Type: String  
Description: "Name prefix for resources"  
  
  
Resources:  
VPC:  
Type: AWS::EC2::VPC  
Properties:  
CidrBlock: "10.0.0.0/16"  
EnableDnsSupport: true  
EnableDnsHostnames: true  
Tags:  
- Key: Name  
Value: !Ref Name  
- Key: 'rosa_managed_policies'  
Value: 'true'  
- Key: 'rosa_hcp_policies'  
Value: 'true'  
- Key: 'service'  
Value: 'ROSA'  
  
export OCM_TEMPLATE_DIR varaible to the template path  
$ export OCM_TEMPLATE_DIR=/home/aaraj/rosa-cli-releases/templates/  
  
Then try to create network resources through the command  
$ rosa create network aaraj-template --param=Name=aaraj1 --param=Region=us-west-2

## Expect
INFO[0003] Creating CloudFormation client   
INFO[0003] Creating CloudFormation stack   
INFO[0016] ---------------------------------------------   
INFO[0016] Resource: VPC, Status: CREATE_IN_PROGRESS, Reason: Resource creation Initiated   
INFO[0016] Resource: aaraj1, Status: CREATE_IN_PROGRESS, Reason: User Initiated   
INFO[0026] ---------------------------------------------   
INFO[0026] Resource: aaraj1, Status: CREATE_COMPLETE, Reason:   
INFO[0026] Resource: VPC, Status: CREATE_COMPLETE, Reason:   
INFO[0036] ---------------------------------------------   
INFO[0036] Resource: aaraj1, Status: CREATE_COMPLETE, Reason:   
INFO[0036] Resource: VPC, Status: CREATE_COMPLETE, Reason:   
INFO[0036] --------------------------------   
INFO[0036] Resources created in stack:   
INFO[0036] Resource: VPC, Type: AWS::EC2::VPC, ID: vpc-0ba31f7d65ce7d106   
INFO[0036] Stack aaraj1 created   
  
  
  
Stack should be created successfully.  
  
Note: The template dir should be created in the format  
<template-name>/cloudformation.yaml  
  
In my case it is /home/aaraj/rosa-cli-releases/templates/aaraj-template/cloudformation.yaml.

## Step
Try to override template path via using --template-dir flag  
$ ./rosa-1.2.47-rc3 create network rosa-quickstart-default-vpc --param=Name=aaraj1 --param=Region=us-west-2 --template-dir /home/aaraj/rosa/cmd/create/network/templates/

## Expect
The template path passed with --template-dir flag will be used, overriding the value of OCM_TEMPLATE_DIR exported env variable.

## Step
Try to create public, private and zero egress hcp cluster through the subnets created  
Also try to create the rosa BYO VPC setting cluster should be successful

## Expect
Cluster should be created successfully.  
Check that there is no inflight check failure.

## Step
Verify the network for the created subnets  
$ rosa verify network --watch --status-only --region us-west-2 --subnet-ids subnet-0b2910f08042aa61e,subnet-02629b38f4000d9b0

## Expect
I: Checking the status of the following subnet IDs: [subnet-0b2910f08042aa61e subnet-02629b38f4000d9b0]  
I: subnet-0b2910f08042aa61e, platform: aws-classic, tags: {"Name":"osd-network-verifier","osd-network-verifier":"owned","red-hat-managed":"true"}: passed  
I: subnet-02629b38f4000d9b0, platform: aws-classic, tags: {"Name":"osd-network-verifier","osd-network-verifier":"owned","red-hat-managed":"true"}: passed

## Step
- Create network with default CF template and setting specific AvailabilityZones param.  
./rosa create network rosa-quickstart-default-vpc --param Region=us-west-2 --param Name=yuwanqss3 --param AvailabilityZoneCount=2 --param VpcCidr=10.0.0.0/16 --param AZ1=us-west-2d --param AZ2=us-west-2a --param AZ3=us-west-2c --param AZ4=us-west-2d  
  
- Create network with default CF template without setting AvailabilityZones param  
- Create network with default CF template with the params which AvailabilityZoneCount>len(AvailabilityZones) or AvailabilityZoneCount<len(AvailabilityZones  
  
  
(SInce OCM-14846)

## Expect
- The CF will be created, and the subnets are created at the specific available zones as --param flag setting.  
- It should succeed, the subnets should be created on first ordered AZs  
- It should succeed, there are subnets created on the AZs as the AZ(n) param setting  
- It should succeed, there are subnets created on the AZs as the AZ(n) param setting  
  
1. --param AvailabilityZoneCount=2 --param AZ4=<az>, will create on 1 AZ as AZ4 setting  
2. --param AvailabilityZoneCount=2 --param AZ1=<az> --param AZ2=<az> --param AZ3=<az> --param AZ4=<az>, will create on 4AZs as AZ1~AZ4 param setting
