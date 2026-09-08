# Test

## Step
Create basic multi AZ Hosted cluster  
  
Example:  
./rosa create cluster --cluster-name yuwan-bhs1 --sts --role-arn arn:aws:iam::301721915996:role/yw0921accrhs1-Installer-Role --support-role-arn arn:aws:iam::301721915996:role/yw0921accrhs1-Support-Role --controlplane-iam-role arn:aws:iam::301721915996:role/yw0921accrhs1-ControlPlane-Role --worker-iam-role arn:aws:iam::301721915996:role/yw0921accrhs1-Worker-Role --operator-roles-prefix yuwan-bhs1-h3b1 --region us-west-2 --replicas 3--subnet-ids <private-subnet-1>,<private-subnet-2>,<private-subnet-3>,<public-subnet-1> --hosted-cp -y --mode auto

## Expect
Checklist:  
- Cluster ready  
- Describe cluster and check:  
- billing account  
- version used (should be latest)  
- operator roles list  
- Machinepool ready  
- 3 machinepool should be created with 1 replica on each given subnet  
- Cluster Operators ready

## Step
Delete the Hypershift cluster by `rosa delete cluster`

## Expect
- The cluster can be deleted  
- All resource on AWS should be deleted.

## Step
Delete operator roles

## Expect
- The operator roles are deleted from AWS  
- There are readable message shown about the role deletion

## Step
Delete oidc provider

## Expect
- The oidc-provider are deleted from AWS  
- There are readable message shown about the oidc-provider deletion
