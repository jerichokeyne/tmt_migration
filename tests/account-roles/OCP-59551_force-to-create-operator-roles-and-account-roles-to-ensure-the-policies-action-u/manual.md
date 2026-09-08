# Test

## Step
Create account-roles and remove some actions of the role policies and also delete some policies

## Expect

## Step
Create the account-roles with the same prefix with -f flag

## Expect
- The missing actions permission are added back  
- The missing policies are added back  
  
The roles should contain a link to their AWS Console web page and policies should include their ARN. If it is a trust policy, it should also include its content in the output. Managed policies should instead include a link to their public AWS docs:  
  
  
I: Created role 'oa-417-Installer-Role' with ARN 'arn:aws:iam::301721915996:role/oa-417-Installer-Role'  
I: Attached policy 'arn:aws:iam::301721915996:policy/oa-417-Installer-Role-Policy' to role 'oa-417-Installer-Role(https://console.aws.amazon.com/iam/home?#/roles/oa-417-Installer-Role)'  
  
I: Attached trust policy to role 'oa-417-HCP-ROSA-Worker-Role(https://console.aws.amazon.com/iam/home?#/roles/oa-417-HCP-ROSA-Worker-Role)': {"Version": "2012-10-17", "Statement": [{"Action": ["sts:AssumeRole"], "Effect": "Allow", "Principal": {"Service": ["ec2.amazonaws.com"]}}]}  
I: Created role 'oa-417-HCP-ROSA-Worker-Role' with ARN 'arn:aws:iam::301721915996:role/oa-417-HCP-ROSA-Worker-Role'  
I: Attached policy 'ROSAWorkerInstancePolicy(https://docs.aws.amazon.com/aws-managed-policy/latest/reference/ROSAWorkerInstancePolicy)' to role 'oa-417-HCP-ROSA-Worker-Role(https://console.aws.amazon.com/iam/home?#/roles/oa-417-HCP-ROSA-Worker-Role)'

## Step
Repeat step 1~2 with the account-roles with path setting

## Expect
The result should be same

## Step
~~Create a sts cluster then remove some actions of the operator roles policies~~

## Expect

## Step
~~Create the operator-roles with the same prefix with -f flag~~

## Expect
~~- The missing actions are added back~~

## Step
Repeat step 4~5 with the operator-roles with path setting

## Expect
The result should be same

## Step
Repeat step 4~6 on hypershift cluster

## Expect
The result should be same

## Step
Validation(TBD): Run create account-roles command with '-f' and '--managed' flags at the same time

## Expect
There should be some validation for that.

## Step
Validation for '-f' and '--mode manual'

## Expect
W: Forcing creation of policies only works in auto mode

## Step
Update the operator roles created prior to the cluster spec

## Expect
- It should succeed, new version of the operator policies are added, the operator policies are updated.

## Step
Check if the url endpoint of the oidc config is as the trust relationshift of the operator roles

## Expect
- If no, it should fail with error:  
E: There was a problem retrieving OIDC Config 'https://yw0515byooc1-oidc-c2t2.s3.us-east-2.amazonaws.com': The requested resource '/api/clusters_mgmt/v1/oidc_configs/https:/yw0515byooc1-oidc-c2t2.s3.us-east-2.amazonaws.com' doesn't exist
