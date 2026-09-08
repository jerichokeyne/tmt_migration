# Test

## Step
Log in the rosa tool and prepare one multi zone ready cluster

## Expect

## Step
Run command to record the machine pools  
$ rosa list machinepool -c <cluster name>

## Expect
- The machine pools returned

## Step
Run command to create default machine pools  
$ rosa edit machinepool <machinepool name> -c <cluster name> --interactive

## Expect
- It will go into interaction mode

## Step
Input and press "Enter" key for the questions  
? Enable autoscaling (optional): No  
? Replicas: 9

## Expect
- The input value will show to behind the question  
- For optional question, default value will show behind when tap "Enter" key  
? Enable autoscaling (optional): No  
? Replicas: 9

## Step
Check the machine pool with command  
$ rosa list machinepool -c <cluster name>

## Expect
The machine pool should be updated and all of the information should exactly match the input

## Step
Create another machine pool with command  
$rosa edit machinepool <machinepool name>-c <cluster name> --replicas 9 --interactive

## Expect

## Step
input invalid   
enable autoscaling  
replicas  
Min replicas  
Max replicas

## Expect
- Correct error message will show  
- The process should't break

## Step
Edit machine pool without "--interactive" and required options  
$ rosa edit machinepool <machinepool name> -c <cluster name>

## Expect
It will go into interactive mode automatically
