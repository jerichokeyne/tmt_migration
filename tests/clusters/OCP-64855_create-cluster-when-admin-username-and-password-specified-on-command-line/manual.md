# Setup
<https://issues.redhat.com/browse/OCM-158> - Case requires creation of new sts or non-sts cluster, Hypershift is not supported.  
Requires oc and rosa cli tools.  
rosacli 1.2.29 no longer allows setting of the cluster username, name is now cluster-admin

# Test

## Step
`rosa create cluster -h`

## Expect
$ ./rosa create cluster -h  
......  
--create-admin-user Create cluster admin named "cluster-admin"  
~~--cluster-admin-user string Username of Cluster Admin. Username must not contain /, :, or %%~~  
--cluster-admin-password string The password must  
.....

## Step
Create a classic ROSA cluster using the command line options to specify --create-admin-user a~~nd --cluster-admin-user~~ and --cluster-admin-password  
`rosa create cluster --cluster-name <name> --create-admin-user ~~--cluster-admin-user <name>` --cluster-admin-password <password> --region <region> --version 4.13.3 --replicas 2 --compute-machine-type m5.xlarge --machine-cidr 10.0.0.0/16 --s~~  
ervice-cidr 172.30.0.0/16 --pod-cidr 10.128.0.0/14 --host-prefix 23  
  
~~NOTE: the`--cluster-admin-user should cover both 'cluster-admin' and any other customized name`~~

## Expect
- Cluster is created successfully  
- The cluster-admin user with the specified name(cluster-admin) and password is created with the cluster.   
rosa list idp -c <cluster_id> : One HTPasswd idp named 'cluster-admin' is created with the cluster  
rosa list user -c <cluster_id>: One used with the specified name(cluster-admin) under 'cluster-admins' group is created with the cluster.  
~~rosa describe admin -c <cluster_id> : if the `-cluster-admin-user is 'cluster-admin', the output should be "There is 'cluster-admin' user on cluster 'yuwan-0321ns1'. To login, run the following command....`" , else the name is not 'cluster-admin', the outpout should be "W: There is no 'cluster-admin' user on cluster 'yuwan-0321ns1'. To create it run the following command:~~"`  
- `rosa describe admin` will show "I: There is 'cluster-admin' user on cluster '2al9cuvp93kl6qmroe1ovsmajvgfaod6'. To login, run the following command:`"  
- Log into the cluster with the admin username and password provided.login should successful  
oc login -u <admin_username> -p <password> <API URL>  
- oc get user

## Step
Create a classic ROSA cluster using the command line options to specify only --create-admin-user but no --~~cluster-admin-user and~~ --cluster-admin-password

## Expect
- The cluster-admin user name will be used the default one 'cluster-admin', the password will be auto-generated one  
- Other results should be same with the ones in step2

## Step
Create a classic ROSA cluster using the command line options to specify only --cluster-admin-user or only --cluster-admin-password, without --create-admin-user or

## Expect
~~- If no --cluster-admin-user is set, it will use 'cluster-admin' as the default one~~  
- if no --cluster-admin-password is set, it will use one auto-generated one  
- Other results should be same with the ones in step2

## Step
Create a new cluster using interactive mode to confirm ~~admin username and~~ password are accepted in interactive mode.  
  
`rosa create cluster --cluster-name <name> --region <region> --version 4.13.3 --replicas 2 --compute-machine-type m5.xlarge --machine-cidr 10.0.0.0/16 --s`  
ervice-cidr 172.30.0.0/16 --pod-cidr 10.128.0.0/14 --host-prefix 23 -i  
  
should prompt for creation ~~of admin user account then username and~~ password.

## Expect
`Any optional fields can be left empty and a default will be selected.`  
**?** **Cluster name:** mycluster  
**?** **Deploy cluster with Hosted Control Plane (optional):** No  
**?** **Create cluster admin user:** Yes  
**~~? Username: [? for help] mycluster-admin~~  
? Create custom password for cluster admin: No**  
**I: cluster admin user is mycluster-admin  
I: cluster admin password is h5Yf5-RagLE-zWMW7-tcquU  
**   
  
Confirm that cluster is accesable using steps 2 results  
  
~~- The Username is required. - If choose yes at "~~**Create custom password for cluster admin** " it will guide user to input the password and use it; If choose No, will use one auto-genrated one and have readable INFO message of the password

## Step
Repeat the same procedure as above but choose STS cluster instead

## Expect
cluster is created and accessable

## Step
Repeat the same procedure as above but choose hosted-cp cluster instead

## Expect
cluster is created and accessable

# Cleanup
Remove cluster and associated roles and oidc providers and other resources or use cluster for further testing.
