# Setup
<https://docs.google.com/document/d/1z-Ss8xWYadX30tpA5sbmVlHqJkTTJf-UEuAzGSA1wQ8/edit?tab=t.0#heading=h.bupciudrwmna>
<https://gitlab.cee.redhat.com/service/uhc-clusters-service/-/blob/master/docs/hcp/shared_vpc.md>

# Test

## Step

With cluster owner aws account login:

  1. Create account-roles for hcp shared-vpc cluster.
  2. Create operator-roles for hcp shared-vpc cluster.
  3. Create dns-domain with '--hosted-cp' flag

## Expect

## Step

With the VPC aws account login:
1. route53 role with the following permissions:
```json
{
"Version": "2012-10-17",
"Statement": [
{
"Effect": "Allow",
"Action": [
"route53:ChangeResourceRecordSets",
"route53:ListHostedZones",
"route53:ListHostedZonesByName",
"route53:ListResourceRecordSets",
"route53:ChangeTagsForResource",
"route53:GetAccountLimit",
"route53:GetChange",
"route53:GetHostedZone",
"route53:ListTagsForResource",
"route53:UpdateHostedZoneComment",
"tag:GetResources",
"tag:UntagResources"
],
"Resource": "*"
}
]
}
```

2. vpc-endpoints role with the following permissions:
"Effect": "Allow",
"Action": [
"ec2:CreateVpcEndpoint",
"ec2:DescribeVpcEndpoints",
"ec2:ModifyVpcEndpoint",
"ec2:DeleteVpcEndpoints",
"ec2:CreateTags",
"ec2:CreateSecurityGroup",
"ec2:AuthorizeSecurityGroupIngress",
"ec2:AuthorizeSecurityGroupEgress",
"ec2:DeleteSecurityGroup",
"ec2:RevokeSecurityGroupIngress",
"ec2:RevokeSecurityGroupEgress",
"ec2:DescribeSecurityGroups",
"ec2:DescribeVpcs",
"route53:ListHostedZones",
"route53:ChangeResourceRecordSets",
"route53:ListResourceRecordSets"
],
"Resource": "*"
3. Add the 'HCP-ROSA-Installer-Role','openshift-ingress-operator-cloud-credentials','kube-system-control-plane-operator' roles in the route53 shared vpc role's trust relationship; + Add the 'HCP-ROSA-Installer-Role','kube-system-control-plane-operator' roles in the vpc-endpoints shared vpc role's trust relationship

4. Create VPC including the subnet to share with cluster owner account.
5. Create two private hosted zones. Private Hosted Zone is named with "rosa.[cluster-name].[base-domain]" and Local Hosted Zone is name with "[cluster-name].hypershift.local". Associate the VPC to both of them. Record 'Private Hosted Zone' ID used as'Ingress private hosted zone ID' by rosacli later; Record 'Local Hosted Zone' ID used as 'Hosted Control Plane internal communication hosted zone ID' by rosacli later

6. Create a resource share resouse. Add all subnets of the VPC in the shared resource + add cluster owener AWS account ID in 'shared principles'

7. Login in AWS with the cluster owner AWS account, tagg with either kubernetes.io/role/elb='' (for public subnets) or kubernetes.io/role/internal-elb='' (for private subnets) on above shared subnet. NOTE: any tags that were set on the subnets in the VPC owner account do not transfer to the cluster creator account when shared

## Expect

## Step

Using the cluster owner account login:
Create hosted-cp shared-vpc cluster by command.
`rosa create cluster --cluster-name yuwan-1201svh1 --sts --role-arn arn:aws:iam::301721915996:role/aa/bb/yw1210svpc1-HCP-ROSA-Installer-Role --support-role-arn arn:aws:iam::301721915996:role/aa/bb/yw1210svpc1-HCP-ROSA-Support-Role --worker-iam-role arn:aws:iam::301721915996:role/aa/bb/yw1210svpc1-HCP-ROSA-Worker-Role --operator-roles-prefix yuwan1210svs1 --oidc-config-id 2fi6cq486tehf0092q9g21k309at0pc8 --region us-east-2 --version 4.17.6 --ec2-metadata-http-tokens optional --replicas 3 --compute-machine-type m5.xlarge --machine-cidr 10.0.0.0/16 --service-cidr 172.30.0.0/16 --pod-cidr 10.128.0.0/14 --host-prefix 23 --subnet-ids subnet-0b9a607bec8b7f33f,subnet-008f36d3236e218ae,subnet-084e7202d8177e677,subnet-01930557911f91ba5,subnet-077530dc629d59672,subnet-017d053b0e51688e5 --private-hosted-zone-id Z023190924YLH6AF57C5E --shared-vpc-role-arn arn:aws:iam::641733028092:role/yuwan-sharevpc-r53-role --base-domain by7t.s3.devshift.org --hcp-internal-communication-hosted-zone-id Z02575151LT539DALXKEN --vpc-endpoint-role-arn arn:aws:iam::641733028092:role/yuwan-sharevpc-vpc-endpoint-role --etcd-encryption --billing-account 301721915996 --additional-allowed-principals arn:aws:iam::641733028092:role/yuwan-sharevpc-r53-role,arn:aws:iam::641733028092:role/yuwan-sharevpc-vpc-endpoint-role`


  * operator-roles-prefix : the operator prefix same with the one in step 1
  * oidc-config-id: the same one using to create operator-roles in step1
  * subnet-ids : the shared subnets create in step2
  * private-hosted-zone-id(ingress-private-hosted-zone-id) : the one created in step 2
  * hcp-internal-communication-hosted-zone-id: the one created in step 2
  * shared-vpc-role-arn(route53-role-arn): the one created in step 2
  * vpc-endpoint-role-arn: the one created in step 2
  * base-domain: the one created in step 1
  * additional-allowed-principals: The ARNs of shared-vpc-role-arn and vpc-endpoint-role-arn

The flags in yellow(orange) color are the required ones for hosted-cp shared vpc

## Expect

The cluster should be created successfuly then to be ready status.

## Step

Validations:
- invalid frmat for all ARNs
- missing required flags for shared-vpc(rosacli detects the shared subnet to decide if the passed command is used for shared vpc)
- The additional-allowed-principals don't contain the route53 and vpc-endpoint roles

## Expect

- report error to tell valid ARN format
- will call the interactive mode to ask customers to input the required flags.
- will report error from backend
```
E: Failed to create cluster: status is 400, identifier is '400', code is 'CLUSTERS-MGMT-400', at '2024-12-10T03:34:47Z' and operation identifier is 'eb49b86b-e756-4e51-9551-e18714c161e3': To install a HCP cluster into Shared VPC it is required to include both 'aws.vpc_endpoint_role_arn' and 'aws.private_hosted_zone_role_arn' as additional allowed principals
```

## Step

Describe cluster

## Expect

.......
Shared VPC Config:
- Ingress Private HZ ID: Z07433436IGT5MBBJ7GB
- Internal Comms. HZ ID: Z0362243U411D0DQFAFX
- Route53 Role ARN: arn:aws:iam::641733028092:role/yuwan-sharevpc-r53-role
- VPC Endpoint Role ARN: arn:aws:iam::641733028092:role/yuwan-sharevpc-vpc-endpoint-role
.......
Additional Principals: arn:aws:iam::641733028092:role/yuwan-sharevpc-r53-role,arn:aws:iam::641733028092:role/yuwan-sharevpc-vpc-endpoint-role
.......

## Step

Edit cluster

## Expect

additional-allowed-principals is a new parameter which can be edit

## Step

Delete the cluster

## Expect

The cluster will be deleted, the commands to delete the operator-roles and oidc-provider will be prompted as before
