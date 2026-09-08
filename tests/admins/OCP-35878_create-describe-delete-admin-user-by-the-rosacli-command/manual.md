# Test

## Step
Log in the rosa and prepare a MOA cluster

## Expect

## Step
Try to describe the admin.  
1. with the incorrect cluster_id  
2. with the correct cluster_id

## Expect
1.E: Failed to get cluster '1iekajbm5j6ps8hh5ddjdpe64880c1q6aaa': There is no cluster with identifier or name '1iekajbm5j6ps8hh5ddjdpe64880c1q6aaa'  
  
2.# ./rosa describe admin -c 1iekajbm5j6ps8hh5ddjdpe64880c1q6  
W: There is no admin on cluster '1iekajbm5j6ps8hh5ddjdpe64880c1q6'. To create it run the following command:  
rosa create admin -c 1iekajbm5j6ps8hh5ddjdpe64880c1q6

## Step
Create an admin user by 'rosa create admin' command

## Expect
\# ./rosa create admin -c 1talgnqd8jfb5edhj9p292olv1rgg4r0  
I: Admin account has been added to cluster '1talgnqd8jfb5edhj9p292olv1rgg4r0'.  
I: Please securely store this generated password. If you lose this password you can delete and recreate the cluster admin user.  
I: To login, run the following command:  
  
oc login https://api.yuwan-sr1.mfmf.s1.devshift.org:6443 --username cluster-admin --password oWtxR-7rIUD-PXy3C-Chmtj  
  
I: It may take up to a minute for the account to become active.  
  
- The cluster-admin is created successfully and the 'oc login' coomand is prompted.  
- One Htpaswd idp named 'cluster-admin' is created,.  
- One 'cluster-admin' user will be added in the 'cluster-admins' group ~~but will not show in the 'rosa list user' ~~ # ./rosa list idp -c 29s3jso196qk5t1kvfrktru5dpuegdcm  
NAME TYPE  
cluster-admin HTPasswd   
\# ./rosa list user -c 29s3jso196qk5t1kvfrktru5dpuegdcm  
ID GROUPS   
cluster-admin cluster-admins

## Step
Check if the admin user is added

## Expect
* It should succeed to login with the oc login command shown in the last step.And the username has the cluster admin permission.
  * The 'cluster-admin' user should be listed by "rosa list user".
  *   *

## Step
Describe the admin.

## Expect
\# ./rosa describe admin -c 1iekajbm5j6ps8hh5ddjdpe64880c1q6  
I: There is an admin on cluster '1iekajbm5j6ps8hh5ddjdpe64880c1q6'. To login, run the following command:  
oc login https://api.yuwan-0126-sr1.igqy.s2.devshift.org:6443 --username cluster-admin

## Step
Delete admin

## Expect
- The cluster-admin user is removed from the group  
- The htpasswd idp will be deleted.

## Step
Create a HTPasswd idp then create a cluster-admin

## Expect
- It will succeed without any error  
- One 'cluster-admin' user will be added in the 'cluster-admins' group under the existing idp but will not show in the 'rosa list user'

## Step
Delete admin

## Expect
- The cluster-admin user is removed from the group  
- The htpasswd idp will NOT be deleted as the htpasswd list is not empty

## Step
Create another admin user by the command.

## Expect
It should fail with some error message:  
"User 'cluster-admin' already exists on group 'cluster-admins' for cluster"

## Step
Try to delete the admin  
\#rosa delete admin -c <cluster_id>  
1. delete the admin with the correct cluster_id  
2. delete the admin with the incorrect cluster_id

## Expect
1.There is a confirmation hint, input y to delete and input n to cancel:  
\# ./rosa delete admin -c 1talhgv5kjfmite8pk5cmlr979t4vu38  
? Are you sure you want to delete cluster-admin user on cluster 1talhgv5kjfmite8pk5cmlr979t4vu38? Yes  
I: Admin user 'cluster-admin' has been deleted from cluster '1talhgv5kjfmite8pk5cmlr979t4vu38'  
  
2.E: Failed to get cluster 'aaa': There is no cluster with identifier or name 'aaa'
