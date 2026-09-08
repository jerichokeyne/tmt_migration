# Test

## Step
Prepare a HCP cluster

## Expect

## Step
List the kubeletconfig when cluster has no one

## Expect

## Step
Create kubeletconfig without name with --pod pids limit setting

## Expect
~~The kubeletconfig should be created There will be message show the creation success~~ It goes into interactive mode asking name to be specified

## Step
List the kubeletconfig

## Expect
The created kubeletconfig should be listed with correct information  
The name should be automated generated

## Step
Create kubeletconfig with name specified with flag --name

## Expect
The creation will work well

## Step
List the kubeletconfig

## Expect
The kubeletconfig should be listed with correct setting

## Step
Edit the kubeletconfig with pid pids limit value  
$ rosa edit kubeletconfig --name <name> -c <cluster> --pod-pids-limit 12345

## Expect
It shows the edit succeeded

## Step
Describe the kubeletconfig  
$ rosa describe kubeletconfig --name <name> -c <cluster>

## Expect

## Step
Delete the created kubeletconfigs  
$ rosa delete kubeletconfig --name <kubeletconfig name> -c <cluster>

## Expect
The deletion will succeed

## Step
Describe the kubelet config again

## Expect
It shows the kubeletconfig not found
