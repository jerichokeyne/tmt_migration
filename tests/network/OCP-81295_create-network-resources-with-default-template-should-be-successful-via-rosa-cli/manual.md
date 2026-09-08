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
Try to create network resources without providing template and any param.  
$ rosa create network  
  
INFO[0173] Resources created in stack:    
INFO[0173] Resource: AttachGateway, Type: AWS::EC2::VPCGatewayAttachment, ID: IGW|vpc-091eb7c2790c897c8   
INFO[0173] Resource: EC2VPCEndpoint, Type: AWS::EC2::VPCEndpoint, ID: vpce-03f9a3e71d43c57af   
INFO[0173] Resource: EcrApiVPCEndpoint, Type: AWS::EC2::VPCEndpoint, ID: vpce-0329a35e2d5599d9b   
INFO[0173] Resource: EcrDkrVPCEndpoint, Type: AWS::EC2::VPCEndpoint, ID: vpce-00bda8409ba05d22f   
INFO[0173] Resource: ElasticIP1, Type: AWS::EC2::EIP, ID: 18.189.5.54   
INFO[0173] Resource: ElasticIP2, Type: AWS::EC2::EIP, ID: 18.119.70.205   
INFO[0173] Resource: InternetGateway, Type: AWS::EC2::InternetGateway, ID: igw-04b2b47ecf85b066a   
INFO[0173] Resource: KMSVPCEndpoint, Type: AWS::EC2::VPCEndpoint, ID: vpce-0e7d518e4df4afb95   
INFO[0173] Resource: NATGateway1, Type: AWS::EC2::NatGateway, ID: nat-0ce0b7674527dae49   
INFO[0173] Resource: PrivateRoute, Type: AWS::EC2::Route, ID: rtb-0320152085b532635|0.0.0.0/0   
INFO[0173] Resource: PrivateRouteTable, Type: AWS::EC2::RouteTable, ID: rtb-0320152085b532635   
INFO[0173] Resource: PrivateSubnetRouteTableAssociation1, Type: AWS::EC2::SubnetRouteTableAssociation, ID: rtbassoc-097d3a0400ace1723   
INFO[0173] Resource: PublicRoute, Type: AWS::EC2::Route, ID: rtb-0a9b8060344541f4c|0.0.0.0/0   
INFO[0173] Resource: PublicRouteTable, Type: AWS::EC2::RouteTable, ID: rtb-0a9b8060344541f4c   
INFO[0173] Resource: PublicSubnetRouteTableAssociation1, Type: AWS::EC2::SubnetRouteTableAssociation, ID: rtbassoc-094262caa9582a2af   
INFO[0173] Resource: S3VPCEndpoint, Type: AWS::EC2::VPCEndpoint, ID: vpce-0963c076b855daa78   
INFO[0173] Resource: STSVPCEndpoint, Type: AWS::EC2::VPCEndpoint, ID: vpce-02dc9401355b36450   
INFO[0173] Resource: SecurityGroup, Type: AWS::EC2::SecurityGroup, ID: sg-03e09ab180b579b5e   
INFO[0173] Resource: SubnetPrivate1, Type: AWS::EC2::Subnet, ID: subnet-0ba10b3f620eb71af   
INFO[0173] Resource: SubnetPublic1, Type: AWS::EC2::Subnet, ID: subnet-0dac78960acf69097   
INFO[0173] Resource: VPC, Type: AWS::EC2::VPC, ID: vpc-091eb7c2790c897c8

## Expect
The output should contain below info:  
  
I: Name not provided, using default name 301721915996  
I: Region not provided, using default region us-east-2  
I: Template command not provided, using default template rosa-quickstart-default-vpc  
  
INFO[0173] Stack rosa-network-stack-301721915996 created   
  
Availability Zone must have taken 1 as default value (Check that only 1 Private and 1 public subnet is created).  
  
VpcCidr must taken 10.0.0.0/16 value as default.

## Step
Try to create network resources with params bellow.  
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
