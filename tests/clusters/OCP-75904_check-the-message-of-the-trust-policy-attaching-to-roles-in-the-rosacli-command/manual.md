# Test

## Step
Create ocm-role and user role in auto mode

## Expect
I: Attached trust policy to role 'yw0828ocmr-OCM-Role-13849960(https://console.aws.amazon.com/iam/home?#/roles/yw0828ocmr-OCM-Role-13849960)': {"Version": "2012-10-17", "Statement": [{"Action": ["sts:AssumeRole"], "Effect": "Allow", "Condition": {"StringEquals": {"sts:ExternalId": "1jlfDskrR39egznAq3T18Ul0Xxv"}}, "Principal": {"AWS": ["arn:aws:iam::644306948063:role/RH-Managed-OpenShift-Installer"]}}]}  
  
I: Attached trust policy to role 'yw0828usr-User-ocmqe-yuwan-Role(https://console.aws.amazon.com/iam/home?#/roles/yw0828usr-User-ocmqe-yuwan-Role)': {"Version": "2012-10-17", "Statement": [{"Action": ["sts:AssumeRole"], "Effect": "Allow", "Condition": {"StringEquals": {"sts:ExternalId": "2czM1RgRysFOZp63HkxS7USOvnA"}}, "Principal": {"AWS": ["arn:aws:iam::644306948063:role/RH-Managed-OpenShift-Installer"]}}]}  
  
The output should contains above message to tell customers the trust policy attaching to the role

## Step
Create account-roles in auto mode

## Expect
The output should contains above message to tell customers the trust policy attaching to each roles  
  
.......  
I: Attached trust policy to role 'yw0828art3-Installer-Role(https://console.aws.amazon.com/iam/home?#/roles/yw0828art3-Installer-Role)': {"Version": "2012-10-17", "Statement": [{"Action": ["sts:AssumeRole"], "Effect": "Allow", "Principal": {"AWS": ["arn:aws:iam::644306948063:role/RH-Managed-OpenShift-Installer"]}}]}  
.......

## Step
Create the account-roles when the they has already exsited

## Expect
No output should contains above message to tell customers the trust policy attaching to each roles

## Step
Create the account-roles when the support roles trust policy are updated manually.  
For example, on stage env, update the Principal:AWS with the account used on production env,710019948333

## Expect
1. Only the support role has the message to tell customers the trust policy attaching to the support role.  
2. There are two entries of the old and new trust policy  
{  
"Version": "2012-10-17",  
"Statement": [  
{  
"Effect": "Allow",  
"Principal": {  
"AWS": [  
"arn:aws:iam::710019948333:role/RH-Technical-Support-13849960",  
"arn:aws:iam::644306948063:role/RH-Technical-Support-13849960"  
]  
},  
"Action": "sts:AssumeRole"  
}  
]  
}

## Step
Delete some account-roles then create again.

## Expect
Only the missing roles have the message to tell customers the trust policy attaching to the roles.

## Step
Create operator-roles by prefix

## Expect
The output should contains above message to tell customers the trust policy attaching to each roles

## Step
Create operator-roles by cluster_id

## Expect
The output should contains above message to tell customers the trust policy attaching to each roles

## Step
Create cluster with the shared operator-roles in auto mode

## Expect
No output should contains above message to tell customers the trust policy attaching to each operator roles

## Step
Create cluster with the byo oidc flow in auto mode

## Expect
The output should contains above message to tell customers the trust policy attaching to each operator roles

## Step
Create cluster with clasisic oidc flow in auto mode

## Expect
The output should contains above message to tell customers the trust policy attaching to each operator roles
