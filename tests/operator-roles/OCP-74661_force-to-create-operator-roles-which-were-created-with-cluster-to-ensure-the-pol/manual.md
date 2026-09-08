# Test

## Step
Create a sts cluster then remove some actions of the operator roles policies

## Expect
Expect each trust policy to include its contents in the output. Each operator role should include a link to is AWS Console web page:  
  
I: Attached trust policy to role 'oa-0905-z2w5-openshift-image-registry-installer-cloud-credential(https://console.aws.amazon.com/iam/home?#/roles/oa-0905-z2w5-openshift-image-registry-installer-cloud-credential)': {"Version": "2012-10-17", "Statement": [{"Action": ["sts:AssumeRoleWithWebIdentity"], "Effect": "Allow", "Condition": {"StringEquals": {"oidc.oi1.devshift.org/2djnh56bk8sc3s7l5935c3u52bn13mqm:sub": ["system:serviceaccount:openshift-image-registry:cluster-image-registry-operator" , "system:serviceaccount:openshift-image-registry:registry"]}}, "Principal": {"Federated": "arn:aws:iam::301721915996:oidc-provider/oidc.oi1.devshift.org/2djnh56bk8sc3s7l5935c3u52bn13mqm"}}]}  
I: Created role 'oa-0905-z2w5-openshift-image-registry-installer-cloud-credential' with ARN 'arn:aws:iam::301721915996:role/oa-0905-z2w5-openshift-image-registry-installer-cloud-credential'  
I: Attached policy 'arn:aws:iam::301721915996:policy/oa-test-openshift-image-registry-installer-cloud-credentials' to role 'oa-0905-z2w5-openshift-image-registry-installer-cloud-credential(https://console.aws.amazon.com/iam/home?#/roles/oa-0905-z2w5-openshift-image-registry-installer-cloud-credential)'

## Step
Create the operator-roles with the same prefix with -f flag

## Expect
- The missing actions are added back

## Step
Repeat step1 then delete some policy then Create the operator-roles with the same prefix with -f flag

## Expect
- The missing policies are added back

## Step
Repeat step 4~5 with the operator-roles with path setting

## Expect
The result should be same
