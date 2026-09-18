# Test

## Step

1. Check the help message.

```bash
rosa create network --help
```

## Expect

```
Available parameters in default template:
  AZ1
  AZ2
  AZ3
  AZ4
  AvailabilityZoneCount
  Name
  Region
  VpcCidr
  Tags

Usage:
  rosa create network [flags]

Aliases:
  network, networks

Examples:
  # Create a AWS cloudformation stack
  rosa create network <template-name> --param Param1=Value1 --param Param2=Value2

  # ROSA quick start HCP VPC example with one availability zone
  rosa create network rosa-quickstart-default-vpc --param Region=us-west-2 --param Name=quickstart-stack --param AvailabilityZoneCount=1 --param VpcCidr=10.0.0.0/16

  # ROSA quick start HCP VPC example with two explicit availability zones
  rosa create network rosa-quickstart-default-vpc --param Region=us-west-2 --param Name=quickstart-stack --param AZ1=us-west-2b --param AZ2=us-west-2d --param VpcCidr=10.0.0.0/16

  # To delete the AWS cloudformation stack
  aws cloudformation delete-stack --stack-name <name> --region <region>

# TEMPLATE_NAME:
Specifies the name of the template to use. This should match the name of a directory
under the path specified by '--template-dir' or the 'OCM_TEMPLATE_DIR' environment variable.
The directory should contain a YAML file defining the custom template structure.

If no TEMPLATE_NAME is provided, or if no matching directory is found, the default
built-in template 'rosa-quickstart-default-vpc' will be used.

Flags:
  -h, --help                  help for network
  -m, --mode string           How to perform the operation. Valid options are:
                              auto: Resource changes will be automatic applied using the current AWS account
                              manual: Commands necessary to modify AWS resources will be output to be run manually
      --param stringArray     List of parameters
      --template-dir string   Use a specific template directory, overriding the OCM_TEMPLATE_DIR environment variable.

Global Flags:
      --color string     Surround certain characters with escape sequences to display them in color on the terminal. Allowed options are [auto never always] (default "auto")
      --debug            Enable debug mode.
      --profile string   Use a specific AWS profile from your credential file.
      --region string    Use a specific AWS region, overriding the AWS_REGION environment variable.
  -y, --yes              Automatically answer yes to confirm operation.
```

## Step

1. Create network resources with a template and parameters.

```bash
rosa create network rosa-quickstart-default-vpc --param=Name=aaraj --param=Region=us-west-2 --param AvailabilityZoneCount=3 --template-dir /home/aaraj/rosa/cmd/create/network/templates/
```

The maximum supported `AvailabilityZoneCount` is 4 (OCM-14846).

## Expect

- Resources are created in the stack.
- Three private and three public subnets are created according to the availability zones in the supplied region.
- All resources are created correctly in the AWS console with correct information and tags.

## Step

1. Set `AvailabilityZoneCount` to two and set tags through a parameter.

```bash
rosa create network rosa-quickstart-default-vpc --param=Name=aaraj --param=Region=us-west-2 --param AvailabilityZoneCount=2 --template-dir /home/aaraj/rosa/cmd/create/network/templates/ --param=Tags=foo=bar
```

## Expect

- Two private and two public subnets are created according to the availability zones in the supplied region.
- The tags passed through `--param` are set on all created resources.

## Step

1. Create network resources in manual mode.

```bash
./rosa-1.2.47-rc2 create network rosa-quickstart-default-vpc --param=Name=aaraj --param=Region=us-west-2 --param AvailabilityZoneCount=2 --template-dir /home/aaraj/rosa/cmd/create/network/templates/ --param=Tags=foo=bar --mode manual
```

## Expect

```
I: Run the following command to create the stack manually:
aws cloudformation create-stack --stack-name aaraj --template-body file:///home/aaraj/rosa/cmd/create/network/templates//rosa-quickstart-default-vpc/cloudformation.yaml --param ParameterKey=AvailabilityZoneCount,ParameterValue=2 ParameterKey=Name,ParameterValue=aaraj ParameterKey=Region,ParameterValue=us-west-2 --tags Key=foo,Value=bar --region us-west-2
```

Run the command and confirm all resources are created successfully.

```bash
aws cloudformation create-stack --stack-name aaraj --template-body file:///home/aaraj/rosa/cmd/create/network/templates//rosa-quickstart-default-vpc/cloudformation.yaml --param ParameterKey=AvailabilityZoneCount,ParameterValue=2 ParameterKey=Name,ParameterValue=aaraj ParameterKey=Region,ParameterValue=us-west-2 --tags Key=foo,Value=bar --region us-west-2
```

```json
{
  "StackId": "arn:aws:cloudformation:us-west-2:301721915996:stack/aaraj/ab2345b0-94e2-11ef-a683-02eb4ee947d7"
}
```

## Step

1. Create a template file that creates a single VPC.

```bash
vim /home/aaraj/rosa-cli-releases/templates/aaraj-template/cloudformation.yaml
```

```yaml
AWSTemplateFormatVersion: 2010-09-09
Description: This template deploys a single vpc in us-west-2 region.
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
```

Export `OCM_TEMPLATE_DIR` to the template path, then create network resources.

```bash
export OCM_TEMPLATE_DIR=/home/aaraj/rosa-cli-releases/templates/
rosa create network aaraj-template --param=Name=aaraj1 --param=Region=us-west-2
```

## Expect

```
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
```

The stack is created successfully. The template directory follows `<template-name>/cloudformation.yaml`; here it is `/home/aaraj/rosa-cli-releases/templates/aaraj-template/cloudformation.yaml`.

## Step

1. Override the template path with `--template-dir`.

```bash
./rosa-1.2.47-rc3 create network rosa-quickstart-default-vpc --param=Name=aaraj1 --param=Region=us-west-2 --template-dir /home/aaraj/rosa/cmd/create/network/templates/
```

## Expect

The `--template-dir` path overrides the exported `OCM_TEMPLATE_DIR` value.

## Step

1. Create public, private, and zero-egress HCP clusters through the created subnets. Also create a ROSA BYO VPC cluster.

## Expect

- Clusters are created successfully.
- There is no inflight check failure.

## Step

1. Verify the network for the created subnets.

```bash
rosa verify network --watch --status-only --region us-west-2 --subnet-ids subnet-0b2910f08042aa61e,subnet-02629b38f4000d9b0
```

## Expect

```
I: Checking the status of the following subnet IDs: [subnet-0b2910f08042aa61e subnet-02629b38f4000d9b0]
I: subnet-0b2910f08042aa61e, platform: aws-classic, tags: {"Name":"osd-network-verifier","osd-network-verifier":"owned","red-hat-managed":"true"}: passed
I: subnet-02629b38f4000d9b0, platform: aws-classic, tags: {"Name":"osd-network-verifier","osd-network-verifier":"owned","red-hat-managed":"true"}: passed
```

## Step

1. Create a network with the default CloudFormation template and explicit Availability Zone parameters.

```bash
./rosa create network rosa-quickstart-default-vpc --param Region=us-west-2 --param Name=yuwanqss3 --param AvailabilityZoneCount=2 --param VpcCidr=10.0.0.0/16 --param AZ1=us-west-2d --param AZ2=us-west-2a --param AZ3=us-west-2c --param AZ4=us-west-2d
```

1. Create a network with the default CloudFormation template without Availability Zone parameters.
1. Create a network with `AvailabilityZoneCount` greater than or less than the number of availability zones.

Since OCM-14846.

## Expect

- The CloudFormation stack is created and subnets are created in the availability zones set through `--param`.
- Without Availability Zone parameters, subnets are created in the first ordered availability zones.
- With availability-zone parameters, subnets are created in the `AZ(n)` zones supplied.
- `--param AvailabilityZoneCount=2 --param AZ4=<az>` creates one availability zone using `AZ4`.
- `--param AvailabilityZoneCount=2 --param AZ1=<az> --param AZ2=<az> --param AZ3=<az> --param AZ4=<az>` creates four availability zones using `AZ1` through `AZ4`.
