# Test

## Step
Log in with rosacil and prepare account-roles with the low version 4.9

## Expect

## Step
Create STS cluster in the 4.9.z version which has a upgrade path to 4.10.z

## Expect

## Step
Try to upgrade the account-roles with --mode auto

## Expect
Log in aws console to check the account-roles and policies tagged with the default openshift version(X.Y)  
  
NOTE: When upgrade to 4.10 there is a new operator policy will be created 'openshift-cluster-csi-drivers-storage-ebs-cloud-cred' and the the permissions should be same with the one changed in <https://github.com/openshift/rosa/pull/610/files>

## Step
Try to upgrade operator-roles with --mode auto with setting the cluster upgrading version

## Expect
Log in aws console to check the policies tagged with the default openshift version(X.Y)  
  
NOTE: When upgrade to 4.10.* there is a new operator policy will be created 'openshift-cluster-csi-drivers-storage-ebs-cloud-cred' and the the permissions should be same with the one changed in <https://github.com/openshift/rosa/pull/610/files>   
  
- The 4.10.z cluster new added operator-roles and policy will be created.

## Step
Upgrade the cluster to 4.10.z

## Expect
The cluster upgrade should succeed
