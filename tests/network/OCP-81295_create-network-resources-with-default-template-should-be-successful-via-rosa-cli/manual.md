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

1. Create network resources without a template or parameters.

```bash
rosa create network
```

## Expect

```
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
```

- The output contains `I: Name not provided, using default name 301721915996`, `I: Region not provided, using default region us-east-2`, and `I: Template command not provided, using default template rosa-quickstart-default-vpc`.
- The output contains `INFO[0173] Stack rosa-network-stack-301721915996 created`.
- The default Availability Zone count is one; one private and one public subnet are created.
- The default `VpcCidr` value is `10.0.0.0/16`.

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
