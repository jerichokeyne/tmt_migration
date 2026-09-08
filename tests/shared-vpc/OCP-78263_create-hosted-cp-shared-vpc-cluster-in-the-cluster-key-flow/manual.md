# Test

## Step
With cluster owner aws account login:  

  1. Create account-roles for hcp shared-vpc cluster.
  2. Create dns-domain with '--hosted-cp' flag

## Expect

## Step
With the VPC aws account login:  
1. route53 role with the following permissions:  
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
3. Add the 'HCP-ROSA-Installer-Role','openshift-ingress-operator-cloud-credentials','kube-system-control-plane-operator' roles in the route53 shared vpc role's trust relationship; + Add the 'HCP-ROSA-Installer-Role','kube-system-control-plane-operator' roles in the vpc-endpoints shared vpc role's trust relationship. NOTE: in the cluster key flow, the operator-roles arn should be added after the operator-roles created later.  
  
4. Create VPC including the subnet to share with cluster owner account.  
5. Create two private hosted zones. Private Hosted Zone is named with "rosa.[cluster-name].[base-domain]" and Local Hosted Zone is name with "[cluster-name].hypershift.local". Associate the VPC to both of them. Record 'Private Hosted Zone' ID used as'Ingress private hosted zone ID' by rosacli later; Record 'Local Hosted Zone' ID used as 'Hosted Control Plane internal communication hosted zone ID' by rosacli later  
  
6. Create a resource share resouse. Add all subnets of the VPC in the shared resource + add cluster owener AWS account ID in 'shared principles'  
  
7. Login in AWS with the cluster owner AWS account, tagg with either kubernetes.io/role/elb='' (for public subnets) or kubernetes.io/role/internal-elb='' (for private subnets) on above shared subnet. NOTE: any tags that were set on the subnets in the VPC owner account do not transfer to the cluster creator account when shared

## Expect

## Step
Create cluster in the interactive mode

## Expect
- The cluster will be created and keep in waiting status.  
- There are rosacli commands to create operator-roles   
  
I: Run the following commands to continue the cluster creation:  
  
  
rosa create operator-roles --cluster yuwan-1211svh --route53-role-arn arn:aws:iam::641733028092:role/yuwan-sharevpc-route53-role --hosted-cp --vpc-endpoint-role-arn arn:aws:iam::641733028092:role/yuwan-sharevpc-vpc-endpoint-role

## Step
Create the operator-roles by cluster key using the commands in last step

## Expect
Choose/Use manual mode:  
- Aws commnads are prompted to create operator-roles.  
- The commands to attach assume role policies should use the policies arns correctly and with the same path with route53-role-arn and vpc-endpoint-role-arn  
- Execute the commands, all commands should succeed and the operator-roles for hcp shared vpc should be created successfully  
  
Choose/Use auto mode:  
- the operator-roles for hcp shared vpc should be created successfully and the cluster will be changed to installing status then to be ready

## Step
Delete the cluster then Create hosted-cp shared vpc cluster with all required flags and '--mode maual'

## Expect
- Aws commnads are prompted to create operator-roles.  
- The commands to attach assume role policies should use the policies arns correctly and with the same path with route53-role-arn and vpc-endpoint-role-arn  
- Execute the commands, all commands should succeed and the operator-roles for hcp shared vpc should be created successfully

## Step
Delete the cluster then Create hosted-cp shared vpc cluster with all required flags and '--mode maual'

## Expect
- the operator-roles for hcp shared vpc should be created successfully and the cluster will be changed to installing status then to be ready
