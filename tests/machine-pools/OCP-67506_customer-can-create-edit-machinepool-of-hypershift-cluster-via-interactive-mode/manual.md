# Test

## Step
Prepare a hosted cluster

## Expect

## Step
Create a nodepool with below command to go into interactive mode
```bash
rosa creat machinepool -c <cluster name> -i
```

## Expect
It will goes into interactive mode

## Step
Fill in the machinepool name
Select a version
Choose Y for the subnet choosing

## Expect
The subnet will be listed and check the subnets
- Only private subnets listed
- Only subnets in the machineCIDR listed
- Only the subnet in same VPC listed

## Step
There won't be net avaliable zone set option with subnet setting
Otherwise there should be a question for available zone choosing

## Expect

## Step
Select enable autoscaling
? Enable autoscaling (optional): Yes

## Expect
There will be question ask for min replicas
? Min replicas: [? for help]

## Step
Fill 0 to the min replicas

## Expect
There will be error message
? Enable autoscaling (optional): Yes
X Sorry, your reply was invalid: min-replicas must be greater than zero
? Min replicas: [? for help]

## Step
Fill in correct number

## Expect

## Step
And Check next questions

## Expect
lixue@Xue-Lis-MacBook-Pro ~ % rosa create machinepool -c ying-hcp2 -i
? Machine pool name: xuelitest
? OpenShift version: 4.13.10
? Select subnet for a hosted machine pool (optional): No
? AWS availability zone: us-west-2a
? Enable autoscaling (optional): Yes
X Sorry, your reply was invalid: min-replicas must be greater than zero
? Min replicas: 1
X Sorry, your reply was invalid: max-replicas must be greater or equal to min-replicas
? Max replicas: 2
? Labels (optional):
? Taints (optional): aaa=dddd:NoSchedule
```
I: Fetching instance types
```

## Step
Check the fetched instance types

## Expect
Only instance types match the zone be listed

## Step
Select the Node drain grace period

## Expect
-There will be question ask for Node drain grace period
-The parameter is optional
-Input ? to get help message
-Input invalid value, it will prompt error message but not exit
-./rosa create machinepool -c ying-hcp-auth2 -i
? Machine pool name: test1
? OpenShift version (default = '4.16.0-0.nightly-2024-03-20-061740'): 4.16.0-0.nightly-2024-03-20-061740
? Select subnet for a hosted machine pool: No
? AWS availability zone (default = 'us-west-2a'): us-west-2a
? Enable autoscaling: No
X Sorry, your reply was invalid: Value is required
? Replicas: 1
? Labels (optional):
? Taints (optional):
? Additional 'Machine Pool' Security Group IDs (optional):
```
I: Checking available instance types for machine pool 'test1'
? Instance type (default = 'm5.xlarge'): m5.xlarge
? Autorepair: Yes
? Node drain grace period (optional): 20
```

## Step
The machinepool will be created

## Expect

## Step
Repeat above steps with and replicas 0
? Enable autoscaling (optional): No

## Expect
The machinepool will be created

## Step
Edit the machinepool in interactive mode too

## Expect
0 replicas will be allowed
0 min replicas is not allowed
