# Test

## Step
Prepare a rosa cluster

## Expect

## Step
Create a kubeletconfig to the cluster without --pod-pid-limit set

## Expect
It will go into interactive mode and ask for input  
lixue@Xue-Lis-MacBook-Pro ~ % rosa create kubeletconfig -c 27dpunj8rqemiknurji3i4md2jqqos5b  
I: Enabling interactive mode  
? Pod Pids Limit?: [? for help]

## Step
type ? to check the help message

## Expect
Help message show correctly  
lixue@Xue-Lis-MacBook-Pro ~ % rosa create kubeletconfig -c 27dpunj8rqemiknurji3i4md2jqqos5b  
I: Enabling interactive mode  
? Set the Pod Pids Limit field to a value between 4096 and 16,384  
? Pod Pids Limit?:

## Step
Type invalid 1

## Expect
Error message show  
lixue@Xue-Lis-MacBook-Pro ~ % rosa create kubeletconfig -c 27dpunj8rqemiknurji3i4md2jqqos5b  
I: Enabling interactive mode  
X Sorry, your reply was invalid: '1' is less than the permitted minimum of '4096'  
? Set the Pod Pids Limit field to a value between 4096 and 16,384  
? Pod Pids Limit?:

## Step
Type invalid out of max 16,384

## Expect
There should be correct error message

## Step
Type correct value between 4096 and 16,384

## Expect
The creation will succeed

## Step
Edit the kubeletconfig in interactive mode

## Expect

## Step
Repeat above actions

## Expect
Work as expected
