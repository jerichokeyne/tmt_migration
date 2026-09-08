# Test

## Step
Prepare the byo oidc config via `rosa create oidc-config --mode auto` command

## Expect

## Step
~~Create STS cluster by setting 'oidc-private-key-secret-arn' and 'oidc-endpoint-url' with the available value ~~

## Expect
~~The cluster will be created with the byo oidc.~~

## Step
Create another byo oidc cluster with the existing operator roles prefix same with the one in step2

## Expect
The cluster will be created successfully  
When creating the operator roles, expect to see the following output for each of the roles created. Specifically, pay attention to ensure that the trust policies output the content of their policy and that the roles output a link to their AWS console page:  
I: Attached trust policy to role 'oa-test-0904-l2l8-openshift-ingress-operator-cloud-credentials(https://console.aws.amazon.com/iam/home?#/roles/oa-test-0904-l2l8-openshift-ingress-operator-cloud-credentials)': {"Version": "2012-10-17", "Statement": [{"Action": ["sts:AssumeRoleWithWebIdentity"], "Effect": "Allow", "Condition": {"StringEquals": {"oidc.oi1.devshift.org/2dj277ipdtvointq44d4rdufaguccoel:sub": ["system:serviceaccount:openshift-ingress-operator:ingress-operator"]}}, "Principal": {"Federated": "arn:aws:iam::301721915996:oidc-provider/oidc.oi1.devshift.org/2dj277ipdtvointq44d4rdufaguccoel"}}]}  
I: Created role 'oa-test-0904-l2l8-openshift-ingress-operator-cloud-credentials' with ARN 'arn:aws:iam::301721915996:role/oa-test-0904-l2l8-openshift-ingress-operator-cloud-credentials'  
I: Attached policy 'arn:aws:iam::301721915996:policy/oa-test-openshift-ingress-operator-cloud-credentials' to role 'oa-test-0904-l2l8-openshift-ingress-operator-cloud-credentials(https://console.aws.amazon.com/iam/home?#/roles/oa-test-0904-l2l8-openshift-ingress-operator-cloud-credentials)'

## Step
Create another byo oidc cluster with other existing operator roles prefix which roles have no the oidc-provider trust relationship

## Expect
It fails to create the cluster:  
E: Operator role 'arn:aws:iam::xxx:role/yuwan-ssts2-r8p1-openshift-cloud-network-config-controller-cloud' does not have trusted relationship to 'https://yw0301byocc2-oidc-o5q7.s3.us-east-2.amazonaws.com' issuer URL

## Step
Repeat the step2~3 on hypershift cluster

## Expect
The result should be same

## Step
Repeat step3 to re-use the operator roles which are not compatible with the creating one.  
- re-use the operator roles for 4.9.z cluster to create 4.10.z cluster  
- re-use the NON-hypershift opetator roles to create hypershift cluster.

## Expect
- It fails to create the cluster, and some error message shown:  
E: NoSuchEntity: The role with name yuwan-sts491-l6i1-openshift-cloud-network-config-controller-clou cannot be found.  
status code: 404, request id: 319da73c-1635-40d6-8ef0-a73bb4f016c6
