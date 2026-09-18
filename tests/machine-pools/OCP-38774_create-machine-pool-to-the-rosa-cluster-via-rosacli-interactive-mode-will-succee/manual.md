# Test

## Step
Log in the rosa tool and prepare one multi zone ready cluster

## Expect

## Step
Run command to record the machine pools
```bash
rosa list machinepool -c <cluster name>
```

## Expect
- The machine pools returned

## Step
Run command to create default machine pools
```bash
rosa create machinepool -c <cluster name> --interactive
```

## Expect
- It will go into interaction mode

## Step
Input and press "Enter" key for the questions
? Machine pool name: aaaaaaaaaaaaaaaaaaaaaaaaa
? Enable autoscaling (optional): No
? Replicas: 9
? Instance type: m5.xlarge
? Labels (optional):
? Taints (optional):

## Expect
- The input value will show to behind the question
- For optional question, default value will show behind when tap "Enter" key

## Step
Check the machine pool with command
```bash
rosa list machinepool -c <cluster name>
```

## Expect
The machine pool should be created and all of the information should exactly match the input

## Step
Create another machine pool with command
```bash
rosa create machinepool -c xueli-rosa --replicas 9 --interactive
```

## Expect

## Step
Input "%^&" as machine pool name

## Expect
- There will be error message show "Expected a valid name for the machine pool"
- The process should not exit

## Step
Input a valid machine pool name and Enter

## Expect
- Enable autoscaling optional should be hidden due to pre-set replica
- The replicas should be 9 as default

## Step
check instance type
type "r5.xlarge"

## Expect
- It can be select by arrows move
- only the matched instance type show when type filter strings

## Step
type "?" for labels

## Expect
- It will show detailed information for machine pool labels

## Step
input invalid labels

## Expect
- Correct error message will show
- The process should't break

## Step
input invalid taint

## Expect
- Correct error message will show
- The process should't break

## Step
input correct value and go next step

## Expect

## Step
There will be a question for disk size, input "?" to check the help message

## Expect
It show the help message
And default value is 300GiB(It comes from flavour. Once flavour changed, the it has to be changed)

## Step
input invalid disk size like %$^

## Expect
- Correct error message will show
- The process should't break

## Step
Input correct value of "350 GiB"

## Expect
It will be finally used for machinepool creation
lixue@Xue-Lis-MacBook-Pro ~ % rosa create machinepool -c xueli -i
? Machine pool name: aaa
? Enable autoscaling (optional): Yes
? Min replicas: 3
? Max replicas: 6
```
I: Fetching instance types
? Instance type: m5zn.metal
? Labels (optional):
? Taints (optional): aaaa=ddd:NoSchedule
? Use spot instances (optional): Yes
? Spot instance max price: 50
? Root disk size (GiB or TiB): 0.5 TB
I: Machine pool 'aaa' created successfully on cluster 'xueli'
I: To view all machine pools, run 'rosa list machinepools -c xueli'
```

## Step
There will be a question to ask for tags input

## Expect
lixue@Xue-Lis-MacBook-Pro rosa % rosa create machinepool -c 2atmfocid44m1621kdbsle5lpqimv1bh -i
? Machine pool name: aaa
? Create multi-AZ machine pool: Yes
? Enable autoscaling: No
? Replicas: 0
? Additional 'Machine Pool' Security Group IDs (optional):
```
I: Checking available instance types for machine pool 'aaa'
? Instance type (default = 'm5.xlarge'): m5.xlarge
? Labels (optional):
? Taints (optional):
? Use spot instances: No
X Sorry, your reply was invalid: invalid tag format for tag '[键]'. Expected tag format: 'key:value'
? Tags (optional): 键:zhi
? Root disk size (GiB or TiB): 300 GiB
```

## Step
Type "?" will show the help message of the tags

## Expect

## Step
Type some invalid values like "aaa"

## Expect
It will show the correct error message that the format is wrong

## Step
Type correct tags

## Expect
It will go to next step

## Step
Create machine pool without "--interactive" and required options
```bash
rosa create machinepool -c <cluster name>
```

## Expect
It will go into interactive mode automatically

## Step
Prepare a multi zone cluster

## Expect

## Step
Create machinepool with interactive mode

## Expect
There will be a question to confirm if "Create multi-AZ machine pool"
```
[xueli@xueli-work ~]$ rosa create machinepool -c xuelimz
I: Enabling interactive mode
? Machine pool name: aaa
? Create multi-AZ machine pool: No
? AWS availability zone: us-east-2b
? Enable autoscaling (optional): No
X Sorry, your reply was invalid: Value is required
? Replicas: 2
? Instance type: m6a.12xlarge
? Labels (optional):
? Taints (optional):
? Use spot instances (optional): No
```

## Step
input "N" for the question

## Expect
There will be selection of available zones for the machinepool
The zones listed should be the zones where the cluster provisioned

## Step
Fill all of the required element and create

## Expect
The single zone machinepool will be created successfully

## Step
Create machinepool to the cluster again

## Expect

## Step
Selete Yes to question "Create multi-AZ machine pool:"

## Expect
There won't be zone selection show.
