# Test

## Step
Prepare a ready ROSA cluster

## Expect

## Step
Create a spot machine pool to the cluster via command  
$ rosa create machinepool --use-spot-instance -i

## Expect
-It will go into interactive mode  
- There will Spot instance max price option after other options  
[xueli@xueli-work linux]$ rosa create machinepool -c sdqe-m-rosa --use-spot-instances -i  
? Machine pool name: aaa  
? Enable autoscaling (optional): No  
X Sorry, your reply was invalid: Value is required  
? Replicas: 2  
? Instance type: m5.xlarge  
? Labels (optional):   
? Taints (optional):   
? Spot instance max price: 0.3

## Step
Check the help message of the Spot instance max price

## Expect
- It shows   
? Max price for spot instance. If empty use the on-demand price.

## Step
Input valid value and press Enter

## Expect
- The machine pool is created successfully  
The machinepool can be listed with correct value in column "SPOT INSTANCES"

## Step
Repeat the interactive mode again

## Expect

## Step
Input negative max price and press Enter

## Expect
There will be error message  
E: Spot max price must be positive

## Step
Repeat the interactive mode without --use-spot-instance set(For now use current design, but for future release,use-spot-instance should be an option in the interactive mode )

## Expect
- There will be no Spot max price option when --use-spot-instance not set
