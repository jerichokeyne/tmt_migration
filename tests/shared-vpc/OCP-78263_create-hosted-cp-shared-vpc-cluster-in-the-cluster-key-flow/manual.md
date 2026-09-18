# Test

## Step
With the cluster owner AWS account logged in:

1. Create account roles for an HCP shared-VPC cluster.
2. Create a DNS domain with the `--hosted-cp` flag.

## Expect

## Step
With the VPC AWS account logged in:

1. Create a Route 53 role with the following permissions:

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

2. Create a VPC endpoints role with the following permissions:

   ```json
   {
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
   }
   ```

3. Add the `HCP-ROSA-Installer-Role`, `openshift-ingress-operator-cloud-credentials`, and `kube-system-control-plane-operator` roles to the Route 53 shared-VPC role's trust relationship. Add the `HCP-ROSA-Installer-Role` and `kube-system-control-plane-operator` roles to the VPC endpoints shared-VPC role's trust relationship. In the cluster key flow, add the operator-role ARNs after the operator roles are created later.
4. Create a VPC, including the subnet to share with the cluster owner account.
5. Create two private hosted zones. Name the private hosted zone `rosa.[cluster-name].[base-domain]` and the local hosted zone `[cluster-name].hypershift.local`. Associate the VPC with both. Record the private hosted zone ID for the ROSA CLI Ingress private hosted zone ID, and the local hosted zone ID for the ROSA CLI Hosted Control Plane internal communication hosted zone ID.
6. Create a resource share. Add all VPC subnets to the shared resource and add the cluster owner AWS account ID to shared principals.
7. Log in to AWS with the cluster owner AWS account and tag the shared subnet with either `kubernetes.io/role/elb=''` for public subnets or `kubernetes.io/role/internal-elb=''` for private subnets. Tags set in the VPC owner account do not transfer to the cluster creator account when shared.

## Expect

## Step
Create a cluster in interactive mode.

## Expect
- The cluster is created and remains in waiting status.
- ROSA CLI commands to create operator roles are displayed.

```bash
rosa create operator-roles --cluster yuwan-1211svh --route53-role-arn arn:aws:iam::641733028092:role/yuwan-sharevpc-route53-role --hosted-cp --vpc-endpoint-role-arn arn:aws:iam::641733028092:role/yuwan-sharevpc-vpc-endpoint-role
```

## Step
Create the operator roles by cluster key using the commands in the previous step.

## Expect
Manual mode:
- AWS commands to create operator roles are displayed.
- Commands to attach assume-role policies use the policy ARNs correctly and with the same path as `route53-role-arn` and `vpc-endpoint-role-arn`.
- Executing the commands succeeds and creates the operator roles for HCP shared VPC.

Auto mode:
- The operator roles for HCP shared VPC are created successfully, and the cluster changes to installing status and then ready.

## Step
Delete the cluster, then create an HCP shared-VPC cluster with all required flags and `--mode maual`.

## Expect
- AWS commands to create operator roles are displayed.
- Commands to attach assume-role policies use the policy ARNs correctly and with the same path as `route53-role-arn` and `vpc-endpoint-role-arn`.
- Executing the commands succeeds and creates the operator roles for HCP shared VPC.

## Step
Delete the cluster, then create an HCP shared-VPC cluster with all required flags and `--mode maual`.

## Expect
- The operator roles for HCP shared VPC are created successfully, and the cluster changes to installing status and then ready.
