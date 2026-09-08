# Test

## Step
Run below command to check the rosa cluster creation help  
$--availability-zones strings The availability zones to use when installing a non-BYOVPC cluster. Format should be a comma-separated list. Leave empty for the installer to pick availability zones

## Expect
There will be flag  
--availability-zones strings The availability zones to use when installing a non-BYOVPC cluster. Format should be a comma-separated list. Leave empty for the installer to pick availability zones

## Step
Run below command to create a cluster on indicated zone  
$ rosa create cluster --availability-zones us-west-2b -c xuelirosa

## Expect
zhewang@fedora:~$ rosa create cluster --availability-zones us-east-1a,us-east-1b,us-east-1c --region us-east-1 -c zwant1  
W: In a future release STS will be the default mode.  
W: --sts flag won't be necessary if you wish to use STS.  
W: --non-sts/--mint-mode flag will be necessary if you do not wish to use STS.  
I: Creating cluster 'zwant1'  
I: To view a list of clusters and their status, run 'rosa list clusters'  
I: Cluster 'zwant1' has been created.  
I: Once the cluster is installed you will need to add an Identity Provider before you can login into the cluster. See 'rosa create idp --help' for more information.  
  
Name: zwant1  
Domain Prefix: zwant1  
Display Name: zwant1  
ID: 2braqi9o3st899jogrsst1mie1qiri1d  
External ID:   
Control Plane: Customer Hosted  
OpenShift Version:   
Channel Group: stable  
DNS: Not ready  
AWS Account: 301721915996  
API URL:   
Console URL:   
Region: us-east-1  
Multi-AZ: true  
  
Nodes:  
- Control plane: 3  
- Infra: 3  
- Compute: 3  
Network:  
- Type: OVNKubernetes  
- Service CIDR: 172.30.0.0/16  
- Machine CIDR: 10.0.0.0/16  
- Pod CIDR: 10.128.0.0/14  
- Host Prefix: /23  
EC2 Metadata Http Tokens: optional  
State: pending (Preparing account)  
Private: No  
Delete Protection: Disabled  
Created: Jun 12 2024 01:35:08 UTC  
User Workload Monitoring: Enabled  
Details Page: https://qaprodauth.console.redhat.com/openshift/details/s/2hl62LRkdU4r7ggiZKvkc11Ih20  
  
I: To determine when your cluster is Ready, run 'rosa describe cluster -c zwant1'.  
I: To watch your cluster installation logs, run 'rosa logs install -c zwant1 --watch'.

## Step
Wait for cluster ready

## Expect

## Step
List the machinepool of the cluster and check the Default one  
$ rosa list machinepool -c xuelirosa

## Expect
The default machine pool should use the indicated zone  
zhewang@fedora:~$ rosa list machinepool -c 2braqi9o3st899jogrsst1mie1qiri1d  
ID AUTOSCALING REPLICAS INSTANCE TYPE LABELS TAINTS AVAILABILITY ZONES SUBNETS SPOT INSTANCES DISK SIZE SG IDs  
worker No 3-6 m5.xlarge us-east-1a, us-east-1b, us-east-1c No 300 GiB

## Step
Create a machinepool to the cluster  
$ rosa create machinepool --mane mp1 -c xuelirosa

## Expect
The machinepool should be created successfully

## Step
List the machinepool again

## Expect
The machinepool should be created in the zone
