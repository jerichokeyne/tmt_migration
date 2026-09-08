# Test

## Step
Create the Hypershift one AZ cluster in the interactive and in auto mode

## Expect
- In the interactive mode, it should prompt the BYO VPC guide options by default.  
-For hosted cluster, if there are some Technology Preview messages, it will show here(This time is to show the message before ROSA HCP GA Dec 4th)  
I: NOTE: Hosted control planes are currently in Technology Preview (https://access.redhat.com/support/offerings/techpreview). Any Technology Preview clusters will need to be destroyed and recreated prior to general availability.  
- For hosted-cp is true, this message will be not prompted  
WARN: In a future release STS will be the default mode.  
WARN: --sts flag won't be necessary if you wish to use STS.  
WARN: --non-sts/--mint-mode flag will be necessary if you do not wish to use STS.  
- The cluster should be created successfully  
- Only the Hosted cp account roles can be listed  
- Only support region are shown in the region list  
- Only supported versions are shown in the version list .The default version is same with ‘rosa list version --hosted-cp’  
(check by 'rosa list version --hosted-cp' command)  
- Compute nodes instance type is shown with all valid options  
- No Default machine pool labels option  
- The billing_account_id should all listed and selectable which is bound with the cluster|byoc|moa|marketplace quota  
Note: the billing account id is hidden before the end_date in `ocm get /api/clusters_mgmt/v1/products/rosa/technology_previews/hcp-billing`, after the end_date the billing account id should show in the interactive mode  
Note: if select different billing account than infrastructure AWS account  
I: The selected AWS billing account is a different account than your AWS infrastructure account.The AWS billing account will be charged for subscription usage. The AWS infrastructure account will be used for managing the cluster.

## Step
Create the Hypershift one AZ cluster in the interactive and in manual mode

## Expect
- In the interactive mode, it should prompt the BYO VPC guide options by default.  
- The cluster should be created successfully

## Step
Create the Hypershift different AZ cluster in the interactive and in auto mode  
add autoscaling option  
2private+1 public  
Replicas should be multiple to number of zones (x2 in this case)

## Expect
The cluster should be created successfully  
- The list of subnet should contains the subnet_name ,vcp_id and az info.If the subnet name is empty , it will show as ''  
  
? Subnet IDs (optional): [Use arrows to move, space to select, <right> to all, <left> to none, type to filter, ? for more help]  
> [ ] subnet-02cb3bbb9a1b2d0b4 ('vprashar-224236-tgzdr-private-us-east-2b','vpc-004c4567177cfd7c2','us-east-2b')  
[ ] subnet-07c35fcef49e2395a ('vprashar-224236-tgzdr-public-us-east-2a','vpc-004c4567177cfd7c2','us-east-2a')  
[ ] subnet-0e5aa5f9e03862164 ('vprashar-224236-tgzdr-private-us-east-2c','vpc-004c4567177cfd7c2','us-east-2c')  
[ ] subnet-0f219e1850ea41ad2 ('vprashar-224236-tgzdr-private-us-east-2a','vpc-004c4567177cfd7c2','us-east-2a')  
[ ] subnet-0fe0364ff819f4f1e ('vprashar-224236-tgzdr-public-us-east-2b','vpc-004c4567177cfd7c2','us-east-2b')  
[ ] subnet-0fd46e9f50b4feb0e ('vprashar-224236-tgzdr-public-us-east-2c','vpc-004c4567177cfd7c2','us-east-2c')  
[ ] subnet-0376ed93e368f81a2 ('minl-aws0809-b6sxq-private-us-east-2b','vpc-0116f969f68f5a12f','us-east-2b')

## Step
Create the Private Hypershift different AZ cluster in the interactive and in auto mode  
3 private subnets  
Replicas should be multiple x3

## Expect

## Step
Create the Hypershift different AZ cluster in the interactive and in manual mode

## Expect
The cluster should be created successfully

## Step
Create the Hypershift cluster with specific instance type (non-default) in the interactive and in manual mode

## Expect
The cluster should be created successfully

## Step
Create the Hypershift cluster in the interactive with the account roles and operator roles which have role and policy path

## Expect
- In the interactive mode, it should prompt the BYO VPC guide options by default.  
- The cluster should be created successfully

## Step
Create the Hypershift cluster in the interactive with billing account id  
Note: the billing account id is hidden before the end_date in `ocm get /api/clusters_mgmt/v1/products/rosa/technology_previews/hcp-billing`, after the end_date the billing account id should show in the interactive mode

## Expect
- The cluster should be created successfully, and the billing account id record correctly in cluster and subscription endpoint

## Step
Create cluster into a BYOVPC which has no subnet (e.g. to region=ap-east-1)

## Expect
- The warning message should be clear as follow:  
./rosa create cluster --cluster-name=yisun-test1 -i  
I: Interactive mode enabled.  
Any optional fields can be left empty and a default will be selected.  
? Cluster name: yisun-test1  
...  
? Install into an existing VPC (optional): Yes  
W: No subnets found in current region that are valid for the chosen CIDR ranges  
? **Continue with default? A new RH Managed VPC will be created for your cluster (y/N)**

## Step
Create cluster with "no-cni" is true interactive

## Expect
-It will be prompt if set '--no-cni'  
-The cluster type is set with 'Other'

## Step
Create one cluster the KMS encryption via the interactive mode.  
\# rosa create cluster -i

## Expect
1. There should be bellow items prompted in the interactive mode.  
? Encrypt etcd data: Yes  
? Etcd encryption KMS ARN: arn:aws:kms:us-east-1:301721915996:key/3ead7012-a878-4bc5-a14e-7962d8d5d540  
  
2. The cluster should be created successfully.

## Step
Delete the created clusters

## Expect

## Step
Delete operator roles

## Expect

## Step
Enter aws console and verify that roles are deleted

## Expect

## Step
Delete oidc provider

## Expect

## Step
Enter aws console and verify that providers are deleted

## Expect
