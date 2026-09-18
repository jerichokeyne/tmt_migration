# Test

## Step
Log in the rosa tool and prepare one ROSA Hypershift ready cluster

## Expect

## Step
Run command to record the machine pools
```bash
rosa list machinepool -c <cluster name>
```

## Expect
- The machine pools returned
D AUTOSCALING REPLICAS INSTANCE TYPE AVAILABILITY ZONE SUBNET NODEPOOL
20icp0qlb0voc1olfgghs5ri3nu2a2so No 2 m5.xlarge us-west-2a subnet-093ef2e9cd69cb74d am-hp-workers
NOTE: from SDA-8219, the labels and taints will show in the output

## Step
Run command to create default machine pools
```bash
rosa edit machinepool <machinepool name> -c <cluster name> --interactive
```

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
- From SDA-8219, the labels and taints will show in the interactive mode
From SDA-8220 - Autorepair is shown (default is True)

## Step
Check the machine pool with command
```bash
rosa list machinepool -c <cluster name>
```

## Expect
The machine pool should be updated and all of the information should exactly match the input
```
ID AUTOSCALING REPLICAS INSTANCE TYPE AVAILABILITY ZONE SUBNET NODEPOOL
20icp0qlb0voc1olfgghs5ri3nu2a2so No 2 m5.xlarge us-west-2a subnet-093ef2e9cd69cb74d am-hp-workers
20ielhc6mjrc4vo8sj953ddu624mo86e No 9 m5.xlarge us-west-2a subnet-093ef2e9cd69cb74d am-hp-workers1
NOTE: from SDA-8219, the labels and taints will show in the output
```

## Step
Create another machine pool with command
```bash
rosa edit machinepool <machinepool name>-c <cluster name> --replicas 5 --interactive
```

## Expect
D AUTOSCALING REPLICAS INSTANCE TYPE AVAILABILITY ZONE SUBNET NODEPOOL
20icp0qlb0voc1olfgghs5ri3nu2a2so No 2 m5.xlarge us-west-2a subnet-093ef2e9cd69cb74d am-hp-workers
20ielhc6mjrc4vo8sj953ddu624mo86e No 5 m5.xlarge us-west-2a subnet-093ef2e9cd69cb74d am-hp-workers1
NOTE: from SDA-8219, the labels and taints will show in the output

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
```bash
rosa edit machinepool <machinepool name> -c <cluster name>
```

## Expect
It will go into interactive mode automatically
