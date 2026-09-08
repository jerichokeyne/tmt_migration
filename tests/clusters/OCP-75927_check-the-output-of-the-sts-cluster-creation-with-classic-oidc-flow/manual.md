# Test

## Step
Create cluster with classic oidc flow in auto mode which don't set oidc-config-id

## Expect
The output should contains above message to tell customers the trust policy attaching to each operator roles  
.......  
I: Attached trust policy to role 'yw0828art3-Installer-Role(https://console.aws.amazon.com/iam/home?#/roles/yw0828art3-Installer-Role)': {"Version": "2012-10-17", "Statement": [{"Action": ["sts:AssumeRole"], "Effect": "Allow", "Principal": {"AWS": ["arn:aws:iam::644306948063:role/RH-Managed-OpenShift-Installer"]}}]}  
.......
