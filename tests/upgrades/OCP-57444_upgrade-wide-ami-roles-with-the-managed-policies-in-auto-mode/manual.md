# Test

## Step
Create STS cluster with the account roles with managed account-role policies then-->Create sts cluster with the account-roles with the version has upgrade path,  
NOTE: 4.9.z -4.10.z is especial as the 4.10.z cluster needs the additional operator role

## Expect

## Step
Wait the cluster ready then upgrade the roles  
\# rosa upgrade roles -c <>  
\# rosa upgrade roles -c <> --version <upgrading cluster version>

## Expect
- If there is no additional role or no '--version' specified, noting will be done and some message shown:  
I: Account roles with the prefix 'yw0113mpaccr2' have attached managed policies.  
I: Cluster 'yuwan-ists2' operator roles have attached managed policies  
  
- If there is some addition roles needed and the '--version' specified, the aws commands to create the role and to attach the manage policies will show in the manual mode, and the additional role will be created in the auto mode.  
yuwan1-mac:rosa yuwan$ ./rosa upgrade operator-roles -c yuwan-ists1 --mode manual -y --version 4.10.46  
I: Starting to upgrade the operator IAM roles  
I: Run the following commands to create the operator roles:  
  
aws iam create-role \  
--assume-role-policy-document file://operator_cloud_network_config_controller_cloud_credentials_policy.json \  
--role-name yuwan-ists1-h8o1-openshift-cloud-network-config-controller-cloud \  
--tags Key=red-hat-managed,Value=true Key=rosa_managed_policies,Value=true Key=rosa_role_prefix,Value=yw0113mpaccr1 Key=operator_name,Value=cloud-credentials Key=rosa_cluster_id,Value=217absatic5737n7fulo7reif6jo0kbt Key=operator_namespace,Value=openshift-cloud-network-config-controller  
  
aws iam attach-role-policy \  
--policy-arn arn:aws:iam::301721915996:policy/ROSACloudNetworkConfigOperator \  
--role-name yuwan-ists1-h8o1-openshift-cloud-network-config-controller-cloud

## Step
Upgrade the cluster in the auto mode,

## Expect
- The additional role will be created automatically if it is needed  
- The cluster will be updated to the desired version  
  
For HCP cluster, below message should be shown if no additional roles are needed  
zhewang@fedora:~$ rosa upgrade roles -c zwant9 --cluster-version 4.16.0-ec.5 -m auto -y  
I: Account roles with the prefix 'zwant-up4' have attached managed policies.  
I: Cluster 'zwant9' operator roles have attached managed policies. An upgrade isn't needed
