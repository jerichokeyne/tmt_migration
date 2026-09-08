# Test

## Step
Create hypershift account roles,  
\# rosa create account-roles --hosted-cp

## Expect
Three hypershift account roles are created  
<prefix>-HCP-Installer-Role  
<prefix>-HCP-Support-Role  
<prefix>-HCP-Worker-Role

## Step
Create hypershift cluster setting --role-arn --support-role-arn --worker-iam-role with the value in step1 in auto mode

## Expect
- The cluster can be created with the three account roles  
- The Operator roles will be created with attaching the managed policies  
- There are 8 operator roles are created as bellow,  
  
Operator IAM Roles:  
- arn:aws:iam::301721915996:role/yuwan-hpm1-n4p9-openshift-cluster-csi-drivers-ebs-cloud-credenti  
- arn:aws:iam::301721915996:role/yuwan-hpm1-n4p9-kube-system-kube-controller-manager  
- arn:aws:iam::301721915996:role/yuwan-hpm1-n4p9-kube-system-capa-controller-manager  
- arn:aws:iam::301721915996:role/yuwan-hpm1-n4p9-kube-system-control-plane-operator  
- arn:aws:iam::301721915996:role/yuwan-hpm1-n4p9-kube-system-kms-provider  
- arn:aws:iam::301721915996:role/yuwan-hpm1-n4p9-openshift-cloud-network-config-controller-cloud-  
- arn:aws:iam::301721915996:role/yuwan-hpm1-n4p9-openshift-image-registry-installer-cloud-credent  
- arn:aws:iam::301721915996:role/yuwan-hpm1-n4p9-openshift-ingress-operator-cloud-credentials

## Step
Create hypershift cluster setting --role-arn --support-role-arn --worker-iam-role with the value in step1 in manual mode  
NOTE: the interactive mode TC will be separated to another TC later when automation

## Expect
- The aws commands to create the operator roles should just be the ones to create roles and attach managed polices, there are no ones for creating policies.  
- The aws commands can be executed successully  
- The cluster can be created after create operator roles and oidc-provider manually

## Step
Repeat step2 with setting existed operator prefix which roles are created by `rosa create cluster --prefix <prefix> --hosted-cp`

## Expect
The result should be same with the ones in step2

## Step
Create hypershift cluster in interative mode in auto mode  
NOTE: the interactive mode TC will be separated to another TC later when automation

## Expect
- After choose the hypershift acount-roles, only three account-roles are selected.  
- Others same with ones in step2

## Step
Create hypershift cluster in interactive mode in manual mode  
NOTE: the interactive mode TC will be separated to another TC later when automation

## Expect
The result is same with the one of step3

## Step
~~Create hypershift cluster with setting '--controlplane-iam-role'~~

## Expect
~~TBD: The cluster will be also created successfully~~
