# Test

## Step
Log in the rosa tool and prepare one ready cluster

## Expect

## Step
Run command to check the help information  
$ rosa edit machine pool --help

## Expect
- The help message will show  
- No typo issue in the message  
[xueli@xueli-work tmp]$ rosa edit machinepool --help  
Edit the additional machine pool from a cluster.  
  
  
Usage:  
rosa edit machinepool [flags]  
  
  
Aliases:  
machinepool, machinepools, machine-pool, machine-pools  
  
  
Examples:  
\# Set 4 replicas on machine pool 'mp1' on cluster 'mycluster'  
rosa edit machinepool --replicas=4 --cluster=mycluster mp1  
\# Enable autoscaling and Set 3-5 replicas on machine pool 'mp1' on cluster 'mycluster'  
rosa edit machinepool --enable-autoscaling --min-replicas=3 max-replicas=5 --cluster=mycluster mp1  
  
  
Flags:  
-c, --cluster string Name or ID of the cluster to add the machine pool to (required).  
--enable-autoscaling Enable autoscaling for the machine pool.  
-h, --help help for machinepool  
--max-replicas int Maximum number of machines for the machine pool.  
--min-replicas int Minimum number of machines for the machine pool.  
--replicas int Count of machines for this machine pool.  
  
  
Global Flags:  
--debug Enable debug mode.  
-i, --interactive Enable interactive mode.  
--profile string Use a specific AWS profile from your credential file.  
-v, --v Level log level for V logs  
.

## Step
Run command to record the machine pools  
$ rosa list machinepool -c <cluster name>

## Expect
- The machine pools returned

## Step
Run command to edit default machine pools  
$ rosa edit machinepool default -c <cluster name> --replicas 3 --enable-autoscaling=false

## Expect
- There will be succeeded message output  
$ rosa edit machinepool default -c xueli-rosa --replicas 3 --enable-autoscaling=false

## Step
Run command to check the machine pools  
$ rosa list machinepool -c <cluster name>

## Expect
- The updated machine pool should be listed  
- The ID/replica should be default/0 and instance type should be m5.xlarge by default, the availability zones should be same with the default one  
ID AUTOSCALING REPLICAS INSTANCE TYPE LABELS TAINTS AVAILABILITY ZONES  
default No 3 m5.8xlarge us-east-1a, us-east-1b, us-east-1c  
default No 0 m5.xlarge us-east-1a, us-east-1b, us-east-1c

## Step
Run command to edit an advanced machine pools  
$ rosa edit machinepool --enable-autoscaling --min-replicas=3 max-replicas=6--cluster=mycluster default  
NOTE: SDA-8272, empty taints value is support ,--taints key=:NoSchedule

## Expect
- There will be succeeded message output

## Step
Run command to check the machine pools  
$ rosa list machinepool -c <cluster name>

## Expect
- The updated machine pool should be listed  
- The ID/replica should be default/0 and instance type should be m5.xlarge by default, the availability zones should be same with the default one  
[xueli@xueli-work tmp]$ rosa list machinepool -c xueli-rosa  
ID AUTOSCALING REPLICAS INSTANCE TYPE LABELS TAINTS AVAILABILITY ZONES  
default Yes 3-6 m5.8xlarge us-east-1a, us-east-1b, us-east-1c  
default No 0 m5.xlarge us-east-1a, us-east-1b, us-east-1c  
autoscale2 Yes 3-3 m5.xlarge aaa=bbb us-east-1a, us-east-1b, us-east-1c

## Step
Prepare another additional machine pool

## Expect

## Step
Run command to enable autoscaling and set the min-replicas to 0  
$ rosa edit machinepool --enable-autoscaling --min-replicas=0 max-replicas=6--cluster=mycluster <mp-name>

## Expect
- There will be succeeded message output

## Step
Run command to check the machine pools  
$ rosa list machinepool -c <cluster name>

## Expect

## Step
Edit machinepool by setting only min-replicas or max-replicas  
$ rosa edit machinepool --min-replicas=3 --cluster=mycluster <mp-name>

## Expect

## Step
Run command to check the machine pools  
$ rosa list machinepool -c <cluster name>

## Expect

## Step
Repeat above steps

## Expect
It should work as expected

## Step
Launch AWS console to check the instances created by the machine pools

## Expect
All of the instances should be AMI instances
