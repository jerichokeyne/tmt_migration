# Setup
AWSTemplateFormatVersion: 2010-09-09  
Description:  
This template deploys a single vpc in us-west-2 region.  
Parameters:  
AvailabilityZoneCount:  
Type: Number  
Description: "Number of Availability Zones to use"  
Default: 1  
MinValue: 1  
MaxValue: 3  
Name:  
Type: String  
Description: "Name prefix for resources"  
VpcCidr:  
Type: String  
Description: CIDR block for the VPC  
Default: '10.0.0.0/16'  
Resources:  
VPC:  
Type: AWS::EC2::VPC  
Properties:  
CidrBlock: !Ref VpcCidr  
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

# Test

## Step
Try to create network without passing any argument to --param flag  
$ rosa create network --param

## Expect
Error: flag needs an argument: --param

## Step
Try to create network passing invalid param format.  
$ rosa create network --param=

## Expect
E: invalid parameter format

## Step
Try to create network with invalid param set  
$ rosa create network --param=Namwe= --template-dir /home/aaraj/rosa/cmd/create/network/templates/

## Expect
E: failed to create stack, operation error CloudFormation: CreateStack, https response error StatusCode: 400, RequestID: a911e259-9906-4525-b605-971f6b66c098, api error ValidationError: Parameters: [Namwe] do not exist in the template

## Step
Try to create network with invalid --template-dir set  
$ rosa create network --template-dir /home/aaraj/rosa/cmd/create/network/

## Expect
E: unable to read template file, open /home/aaraj/rosa/cmd/create/network//rosa-quickstart-default-vpc/cloudformation.yaml: no such file or directory

## Step
Try to create network with invalid flag set  
$ rosa create network --invallid

## Expect
Error: unknown flag: --invallid

## Step
Try to create network with duplicate tag key set  
$ rosa create network --template-dir /home/aaraj/rosa/cmd/create/network/templates/ --param=Tags=key1=value1,key1=value2

## Expect
E: duplicate tag key key1

## Step
Try to create network with non-existent template file name  
$ rosa create network non-existent --param=Name=aaraj --param=Region=us-west-2

## Expect
E: unable to read template file, open cmd/create/network/templates/non-existent/cloudformation.yaml: no such file or directory

## Step
Create a template cloudformation.yaml file without Region parameter and then try to create network  
$ ./rosa-1.2.47-rc2 create network aaraj-template --template-dir /home/aaraj/rosa-cli-releases/templates/  
  
Note: Template file short example given in the setup field.

## Expect
E: failed to create stack, operation error CloudFormation: CreateStack, https response error StatusCode: 400, RequestID: b1efe94c-3576-490c-a2bc-44c41325f6b3, api error ValidationError: Parameters: [Region] do not exist in the template

## Step
Create a template cloudformation.yaml file without Name parameter and then try to create network  
$ ./rosa-1.2.47-rc2 create network aaraj-template --template-dir /home/aaraj/rosa-cli-releases/templates/

## Expect
E: failed to create stack, operation error CloudFormation: CreateStack, https response error StatusCode: 400, RequestID: 3b6f0ce7-4fdb-45c8-8cf5-83467965387f, api error ValidationError: Parameters: [Name] do not exist in the template

## Step
Try to produce rollback error for creating the network resources  
Eg:- Create vpc without sending cidr value to the resources in the template file  
VPC:  
Type: AWS::EC2::VPC  
Properties:  
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

## Expect
INFO[0025] Resource: rosa-network-stack-301721915996, Status: ROLLBACK_IN_PROGRESS, Reason: The following resource(s) failed to create: [VPC].  
Rollback requested by user.   
INFO[0025] Resource: VPC, Status: CREATE_FAILED, Reason: Resource handler returned message: "Either CIDR Block or IPv4 IPAM Pool and IPv4 Netmask Length must be provided" (RequestToken: f9c565b9-6714-1a1d-69c8-1306f5bd717a, HandlerErrorCode: InvalidRequest)   
  
E: failed to wait for stack creation, waiter state transitioned to Failure

## Step
Try to create network using AvailabilityZoneCount param value to be less than one or more than 3  
$ rosa create network --param=AvailabilityZoneCount=10 --template-dir /home/aaraj/rosa/cmd/create/network/templates/

## Expect
E: failed to create stack, operation error CloudFormation: CreateStack, https response error StatusCode: 400, RequestID: c7846c57-df8e-4a61-8dad-1491fa68a2fa, api error ValidationError: Parameter 'AvailabilityZoneCount' must be a number not greater than 3

## Step
$ ./rosa create network --param=AvailabilityZoneCount=0 --template-dir /home/aaraj/rosa/cmd/create/network/templates/

## Expect
E: failed to create stack, operation error CloudFormation: CreateStack, https response error StatusCode: 400, RequestID: 82981089-115c-4acc-a809-cf68b0caf496, api error ValidationError: Parameter 'AvailabilityZoneCount' must be a number not less than 1

## Step
Try to create network using wrong region param  
$ ./rosa create network --param=Region=ind-west-2 --template-dir /home/aaraj/rosa/cmd/create/network/templates/

## Expect
E: failed to create stack, operation error CloudFormation: CreateStack, https response error StatusCode: 0, RequestID: , request send failed, Post "https://cloudformation.ind-west-2.amazonaws.com/": dial tcp: lookup cloudformation.ind-west-2.amazonaws.com on 10.75.5.25:53: no such host

## Step
Try to create network using invalid value for name param  
$ ./rosa create network --param=Name=$#aaraj --template-dir /home/aaraj/rosa/cmd/create/network/templates/

## Expect
E: failed to create stack, operation error CloudFormation: CreateStack, https response error StatusCode: 400, RequestID: f5941ed5-9cca-4c22-b26a-c93c49b1d00f, api error ValidationError: 1 validation error detected: Value '0aaraj' at 'stackName' failed to satisfy constraint: Member must satisfy regular expression pattern: [a-zA-Z][-a-zA-Z0-9]*

## Step
Try to create network using invalid value for VpcCidr param  
$ ./rosa-1.2.47-rc3 create network --param=VpcCidr=10.0. --template-dir /home/aaraj/rosa/cmd/create/network/templates/

## Expect
Resource: VPC, Status: CREATE_FAILED, Reason: Resource handler returned message: "Value (10.0.) for parameter cidrBlock is invalid.  
  
Status: ROLLBACK_IN_PROGRESS  
  
E: failed to wait for stack creation, waiter state transitioned to Failure

## Step
Validations and negative scenarios for AvailabilityZones param  
- create with AvailabilityZoneCount and invalid AvailabilityZones  
- create with AvailabilityZoneCount>4  
(Since OCM-14846, 2025/03/26)

## Expect
- It will report readable error in the output like bellow:  
INFO[0026] Resource: SubnetPrivate1, Status: CREATE_FAILED, Reason: Resource handler returned message: "Value (us-west-2p) for parameter availabilityZone is invalid.  
Subnets can currently only be created in the following availability zones: us-east-2a, us-east-2b, us-east-2c.  
(Service: Ec2, Status Code: 400, Request ID: 20416f42-c520-48f3-98d8-005201ebede4) (SDK Attempt Count: 1)" (RequestToken: 2b4137a3-6917-1c2a-f070-2bc3ee72e1f7, HandlerErrorCode: InvalidRequest)   
INFO[0026] Resource: SubnetPublic1, Status: CREATE_FAILED, Reason: Resource handler returned message: "Value (us-west-2p) for parameter availabilityZone is invalid.  
Subnets can currently only be created in the following availability zones: us-east-2a, us-east-2b, us-east-2c.  
(Service: Ec2, Status Code: 400, Request ID: e743fbfa-875f-49fc-98b8-22b88ce19c3f) (SDK Attempt Count: 1)" (RequestToken: 190247b1-1ad4-6d10-d154-18c80e8aa434, HandlerErrorCode: InvalidRequest)   
  
  
- It will report error:  
E: failed to create stack, operation error CloudFormation: CreateStack, https response error StatusCode: 400, RequestID: 59eb42d9-3900-4a92-b2db-0a84a1df2626, api error ValidationError: Parameter 'AvailabilityZoneCount' must be a number not greater than 4
