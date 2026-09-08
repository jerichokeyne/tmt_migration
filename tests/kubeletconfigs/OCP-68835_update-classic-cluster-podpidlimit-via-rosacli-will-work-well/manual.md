# Test

## Step
Prepare a rosa cluster

## Expect

## Step
Check the help message of rosacli edit

## Expect
There will be introduction of  kubeletconfig Create a custom kubeletconfig for a cluster  
lixue@Xue-Lis-MacBook-Pro rosa % rosa edit -h  
Edit a specific resource  
  
Usage:  
rosa edit [command]  
  
Aliases:  
edit, update  
  
Available Commands:  
addon Edit add-on installation parameters on cluster  
autoscaler Edit the autoscaler of a cluster  
cluster Edit cluster  
ingress Edit a cluster ingress (load balancer)  
kubeletconfig Edit the custom kubeletconfig for a cluster  
machinepool Edit machine pool  
tuning-configs Edit tuning config  
  
Flags:  
-h, --help help for edit  
-i, --interactive Enable interactive mode.  
--profile string Use a specific AWS profile from your credential file.  
--region string Use a specific AWS region, overriding the AWS_REGION environment variable.  
-y, --yes Automatically answer yes to confirm operation.  
  
Global Flags:  
--color string Surround certain characters with escape sequences to display them in color on the terminal. Allowed options are [auto never always] (default "auto")  
--debug Enable debug mode.  
  
Use "rosa edit [command] --help" for more information about a command.

## Step
Check the help message to kubeletconfig edit command

## Expect
No typo errors, all descriptions are clear  
lixue@Xue-Lis-MacBook-Pro rosa % rosa edit kubeletconfig -h  
Edit the custom kubeletconfig for a cluster.  
  
Usage:  
rosa edit kubeletconfig [flags]  
  
Aliases:  
kubeletconfig, kubelet-config  
  
Examples:  
\# Edit a custom kubeletconfig to have a pod-pids-limit of 10000  
rosa edit kubeletconfig --cluster=mycluster --pod-pids-limit=10000  
  
  
Flags:  
-c, --cluster string Name or ID of the cluster.  
-i, --interactive Enable interactive mode.  
--pod-pids-limit int Sets the requested pod_pids_limit for your custom KubeletConfig. Must be an integer in the range 4096 - 16,384. (default -1)  
-h, --help help for kubeletconfig  
  
Global Flags:  
--color string Surround certain characters with escape sequences to display them in color on the terminal. Allowed options are [auto never always] (default "auto")  
--debug Enable debug mode.  
--profile string Use a specific AWS profile from your credential file.  
--region string Use a specific AWS region, overriding the AWS_REGION environment variable.  
-y, --yes Automatically answer yes to confirm operation.

## Step
Edit the kubeletconfig to the cluster before it is created

## Expect
Get an error  
lixue@Xue-Lis-MacBook-Pro rosa % rosa edit kubeletconfig -c yunjiang-lx  
E: No KubeletConfig for cluster 'yunjiang-lx' has been found. You should first create it via 'rosa create kubeletconfig'

## Step
Create a kubeletconfig to the cluster

## Expect

## Step
Run the command to edit the kubeletconfig to the cluster  
lixue@Xue-Lis-MacBook-Pro ~ % rosa edit kubeletconfig -c trad-class --pod-pids-limit 12345

## Expect
There will be warning message pop out to tell customer   
lixue@Xue-Lis-MacBook-Pro ~ % rosa edit kubeletconfig -c trad-class --pod-pids-limit 12345  
? Updating the custom KubeletConfig for cluster '27d9uge7mvjd9dhmjb7l9ed6mvcdf0kn' will cause all non-Control Plane nodes to reboot. This may cause outages to your applications. Do you wish to continue? (y/N)   
I: Creation of custom KubeletConfig for cluster '27d9uge7mvjd9dhmjb7l9ed6mvcdf0kn' aborted.

## Step
Run the command to ignore the warning  
lixue@Xue-Lis-MacBook-Pro ~ % rosa edit kubeletconfig -c trad-class --pod-pids-limit 12345 -y

## Expect
It will be updated  
lixue@Xue-Lis-MacBook-Pro rosa % rosa edit kubeletconfig -c yunjiang-lx --pod-pids-limit 12346 -y  
I: Successfully updated custom KubeletConfig for cluster '27dlmit7s04t5ovoesfcmajmn9ua7n4a'

## Step
Describe the kubeletconfig

## Expect
It will show the updated configuration of the kubeletconfig  
lixue@Xue-Lis-MacBook-Pro ~ % rosa describe kubeletconfig -c trad-class   
  
Pod Pids Limit: 12345

## Step
Pick a machinepool and update the machinepool with --kubelet-configs set

## Expect
It will show error message that it is not supported for classic cluster
