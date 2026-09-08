# Test

## Step
Prepare a rosa cluster

## Expect

## Step
Check the help message of rosacli delete

## Expect
There will be introduction of  kubeletconfig Create a custom kubeletconfig for a cluster  
lixue@Xue-Lis-MacBook-Pro ~ % rosa delete  
Delete a specific resource  
  
Usage:  
rosa delete [command]  
  
Aliases:  
delete, remove  
  
Available Commands:  
account-roles Delete Account Roles  
admin Deletes the admin user  
autoscaler Delete autoscaler for cluster  
cluster Delete cluster  
dns-domain Delete DNS domain  
idp Delete cluster IDPs  
ingress Delete cluster ingress  
kubeletconfig Delete the custom kubeletconfig for a cluster  
machinepool Delete machine pool  
ocm-role Delete ocm role  
oidc-config Delete OIDC Config  
oidc-provider Delete OIDC Provider  
operator-roles Delete Operator Roles  
tuning-configs Delete tuning config  
upgrade Cancel cluster upgrade  
user-role Delete user role  
  
Flags:  
-h, --help help for delete  
--profile string Use a specific AWS profile from your credential file.  
--region string Use a specific AWS region, overriding the AWS_REGION environment variable.  
-y, --yes Automatically answer yes to confirm operation.  
  
Global Flags:  
--color string Surround certain characters with escape sequences to display them in color on the terminal. Allowed options are [auto never always] (default "auto")  
--debug Enable debug mode.  
  
Use "rosa delete [command] --help" for more information about a command.

## Step
Check the help message to kubeletconfig delete command

## Expect
No typo errors, all descriptions are clear  
lixue@Xue-Lis-MacBook-Pro ~ % rosa delete kubeletconfig -h  
Delete the custom kubeletconfig for a cluster  
  
Usage:  
rosa delete kubeletconfig [flags]  
  
Aliases:  
kubeletconfig, kubelet-config  
  
Examples:  
\# Delete the custom kubeletconfig for cluster 'foo'  
rosa delete kubeletconfig --cluster foo  
  
Flags:  
-c, --cluster string Name or ID of the cluster.  
-h, --help help for kubeletconfig  
-y, --yes Automatically answer yes to confirm operation.  
  
Global Flags:  
--color string Surround certain characters with escape sequences to display them in color on the terminal. Allowed options are [auto never always] (default "auto")  
--debug Enable debug mode.  
--profile string Use a specific AWS profile from your credential file.  
--region string Use a specific AWS region, overriding the AWS_REGION environment variable.

## Step
Delete the kubeletconfig to the cluster before it is created

## Expect
Get an error  
lixue@Xue-Lis-MacBook-Pro ~ % rosa delete kubeletconfig -c sdq-ci-longname-xcvmk  
? Deleting the custom KubeletConfig for cluster '27dpunj8rqemiknurji3i4md2jqqos5b' will cause all non-Control Plane nodes to reboot. This may cause outages to your applications. Do you wish to continue? Yes  
E: Failed to delete custom KubeletConfig for cluster '27dpunj8rqemiknurji3i4md2jqqos5b': 'KubeletConfig for cluster with ID '27dpunj8rqemiknurji3i4md2jqqos5b' is not found'

## Step
Create a kubeletconfig to the cluster

## Expect

## Step
Run the command to delete the kubeletconfig to the cluster  
lixue@Xue-Lis-MacBook-Pro ~ % rosa edit kubeletconfig -c trad-class --pod-pids-limit 12345

## Expect
There will be warning message pop out to tell customer   
lixue@Xue-Lis-MacBook-Pro ~ % rosa delete kubeletconfig -c sdq-ci-longname-xcvmk   
? Deleting the custom KubeletConfig for cluster '27dpunj8rqemiknurji3i4md2jqqos5b' will cause all non-Control Plane nodes to reboot. This may cause outages to your applications. Do you wish to continue? Yes  
I: Successfully deleted custom KubeletConfig for cluster '27dpunj8rqemiknurji3i4md2jqqos5b'

## Step
Run the command to ignore the warning  
lixue@Xue-Lis-MacBook-Pro ~ % rosa delete kubeletconfig -c trad-class -y

## Expect
It will be deleted  
lixue@Xue-Lis-MacBook-Pro ~ % rosa delete kubeletconfig -c sdq-ci-longname-xcvmk -y  
I: Successfully deleted custom KubeletConfig for cluster '27dpunj8rqemiknurji3i4md2jqqos5b'

## Step
Describe the kubeletconfig again

## Expect
% rosa describe kubeletconfig -c 27dpunj8rqemiknurji3i4md2jqqos5b  
I: No custom KubeletConfig exists for cluster '27dpunj8rqemiknurji3i4md2jqqos5b'

## Step
Delete to a hosted cluster

## Expect
Error message returns  
lixue@Xue-Lis-MacBook-Pro ~ % rosa delete kubeletconfig -c sdq-ci-wanze   
E: Hosted Control Plane clusters do not support KubeletConfig configuration
