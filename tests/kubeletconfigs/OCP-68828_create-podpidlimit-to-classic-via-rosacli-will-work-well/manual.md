# Test

## Step
Prepare a rosa cluster

## Expect

## Step
Check the help message of rosacli

## Expect
There will be introduction of  kubeletconfig Create a custom kubeletconfig for a cluster  
lixue@Xue-Lis-MacBook-Pro ~ % rosa create -h  
Create a resource from stdin  
  
Usage:  
rosa create [command]  
  
Aliases:  
create, add  
  
Available Commands:  
account-roles Create account-wide IAM roles before creating your cluster.  
admin Creates an admin user to login to the cluster  
autoscaler Create an autoscaler for a cluster  
cluster Create cluster  
dns-domain Create DNS Domain.  
idp Add IDP for cluster  
ingress Add Ingress (load balancer) to the cluster  
kubeletconfig Create a custom kubeletconfig for a cluster  
machinepool Add machine pool to cluster  
ocm-role Create role used by OCM  
oidc-config Create OIDC config compliant with OIDC protocol.  
oidc-provider Create OIDC provider for an STS cluster.  
operator-roles Create operator IAM roles for a cluster.  
tuning-configs Add tuning config  
user-role Create user role to verify account association  
  
Flags:  
-h, --help help for create  
--profile string Use a specific AWS profile from your credential file.  
--region string Use a specific AWS region, overriding the AWS_REGION environment variable.  
-y, --yes Automatically answer yes to confirm operation.  
  
Global Flags:  
--color string Surround certain characters with escape sequences to display them in color on the terminal. Allowed options are [auto never always] (default "auto")  
--debug Enable debug mode.  
  
Use "rosa create [command] --help" for more information about a command.

## Step
Check the help message to kubeletconfig create command

## Expect
No typo errors, all descriptions are clear  
lixue@Xue-Lis-MacBook-Pro ~ % rosa create kubeletconfig -h  
Create a custom kubeletconfig for a cluster  
  
Usage:  
rosa create kubeletconfig [flags]  
  
Aliases:  
kubeletconfig, kubelet-config  
  
Examples:  
\# Create a custom kubeletconfig with a pod-pids-limit of 5000  
rosa create kubeletconfig --cluster=mycluster --pod-pids-limit=5000  
  
  
Flags:  
--pod-pids-limit int Sets the requested pod_pids_limit for your custom KubeletConfig. Must be an integer in the range 4096 - 16,384. (default -1)  
-c, --cluster string Name or ID of the cluster.  
-i, --interactive Enable interactive mode.  
-h, --help help for kubeletconfig  
  
Global Flags:  
--color string Surround certain characters with escape sequences to display them in color on the terminal. Allowed options are [auto never always] (default "auto")  
--debug Enable debug mode.  
--profile string Use a specific AWS profile from your credential file.  
--region string Use a specific AWS region, overriding the AWS_REGION environment variable.  
-y, --yes Automatically answer yes to confirm operation.

## Step
Run the command to create a kubeletconfig to the cluster  
lixue@Xue-Lis-MacBook-Pro ~ % rosa create kubeletconfig -c trad-class --pod-pids-limit 12345

## Expect
There will be warning message pop out to tell customer   
lixue@Xue-Lis-MacBook-Pro ~ % rosa create kubeletconfig -c trad-class --pod-pids-limit 12345  
? Creating the custom KubeletConfig for cluster '27d9uge7mvjd9dhmjb7l9ed6mvcdf0kn' will cause all non-Control Plane nodes to reboot. This may cause outages to your applications. Do you wish to continue? (y/N)   
I: Creation of custom KubeletConfig for cluster '27d9uge7mvjd9dhmjb7l9ed6mvcdf0kn' aborted.

## Step
Run the command to ignore the warning  
lixue@Xue-Lis-MacBook-Pro ~ % rosa create kubeletconfig -c trad-class --pod-pids-limit 12345 -y

## Expect
It will be created  
lixue@Xue-Lis-MacBook-Pro ~ % rosa create kubeletconfig -c trad-class --pod-pids-limit 12345 -y  
I: Successfully created custom KubeletConfig for cluster '27d9uge7mvjd9dhmjb7l9ed6mvcdf0kn'

## Step
Describe the kubeletconfig

## Expect
It will show the configuration of the kubeletconfig  
lixue@Xue-Lis-MacBook-Pro ~ % rosa describe kubeletconfig -c trad-class   
  
Pod Pids Limit: 12345

## Step
Create a kubeletconfig with --name again

## Expect
It will return error that the kubeletconfig already existing

## Step
Create machinepool with --kubelet-configs setting

## Expect
It should return error for classic cluster
