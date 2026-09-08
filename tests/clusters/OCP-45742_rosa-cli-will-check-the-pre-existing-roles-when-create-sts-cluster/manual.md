# Test

## Step
Run command to prepare account-roles  
$ rosa create account-roles --mode auto -y

## Expect
The account roles will be created successfully

## Step
Create an sts cluster with operator-role prefix set  
$ rosa create cluster --sts -c xuelirosa ---operator-roles-prefix xuelidup

## Expect
The cluster will be created successfully with correct roles prefix set

## Step
Create the operator-roles for the cluster  
$ rosa create operator-roles -c xuelirosa --mode auto -y

## Expect
The roles will be created on AWS successfully

## Step
Create cluster again with the same operator role prefix  
$ rosa create cluster --sts -c xuelirosa2 ---operator-roles-prefix xuelidup

## Expect
There should be error output  
E: Error validating role: A role named 'xuelidup-openshift-cluster-csi-drivers-ebs-cloud-credentials' already exists. Please delete the existing role, or provide a different prefix
