# Test

## Step
Log in the rosa tool and prepare one ready cluster

## Expect

## Step
Run command to check the help information  
$ rosa create machine pool --help

## Expect
- The help message will show  
- No typo issue in the message  
[xueli@xueli-work tmp]$ rosa create machinepool --help  
Add a machine pool to the cluster.  
Usage:  
rosa create machinepool [flags]  
Aliases:  
machinepool, machinepools, machine-pool, machine-pools  
Examples:  
\# Interactively add a machine pool to a cluster named "mycluster"  
rosa create machinepool --cluster=mycluster --interactive  
\# Add a machine pool mp-1 with 3 replicas of m5.xlarge to a cluster  
rosa create machinepool --cluster=mycluster --name=mp-1 --replicas=3 --instance-type=m5.xlarge  
\# Add a machine pool mp-1 with autoscaling enabled and 3 to 6 replicas of m5.xlarge to a cluster  
rosa create machinepool --cluster=mycluster --name=mp-1 --enable-autoscaling   
--min-replicas=3 --max-replicas=6 --instance-type=m5.xlarge  
\# Add a machine pool with labels to a cluster  
rosa create machinepool -c mycluster --name=mp-1 --replicas=2 --instance-type=r5.2xlarge --labels =foo=bar,bar=baz"  
Flags:  
-c, --cluster string Name or ID of the cluster to add the machine pool to (required).  
--enable-autoscaling Enable autoscaling for the machine pool.  
-h, --help help for machinepool  
--instance-type string Instance type that should be used. (default "m5.xlarge")  
--labels string Labels for machine pool. Format should be a comma-separated list of 'key=value'. This list will overwrite any modifications made to Node labels on an ongoing basis.  
--max-replicas int Maximum number of machines for the machine pool.  
--min-replicas int Minimum number of machines for the machine pool.  
--name string Name for the machine pool (required).  
--replicas int Count of machines for the machine pool (required when autoscaling is disabled).  
--taints string Taints for machine pool. Format should be a comma-separated list of 'key=value:ScheduleType'. This list will overwrite any modifications made to Node taints on an ongoing basis.  
Global Flags:  
--debug Enable debug mode.  
-i, --interactive Enable interactive mode.  
--profile string Use a specific AWS profile from your credential file.  
-v, --v Level log level for V logs  
-y, --yes Automatically answer yes to confirm operation.

## Step
Run command to record the machine pools  
$ rosa list machinepool -c <cluster name>

## Expect
- The machine pools returned

## Step
List machinepool with flags '--dedicated-host','--all','--win-li','az-type'

## Expect
- If '--all' flag is set, the output will have 'AZ TYPE','WIN-LI ENABLED','DEDICATED HOST' column and values should be correct. and if set '--all' all columns should be shown even the value is empty  
- If any of '--dedicated-host','--win-li','az-type' or combination of them are set, the corresponding colume will be shown and other columns with empty information will not be shown

## Step
Run command to create default machine pools  
$ rosa create machine -c <cluster name> --replicas 0 --name default

## Expect
- There will be succeeded message output  
[xueli@xueli-work tmp]$ rosa create machinepool -c xueli-rosa --name default --replicas 0  
I: Machine pool 'default' created successfully on cluster 'xueli-rosa'

## Step
Run command to check the machine pools  
$ rosa list machinepool -c <cluster name>

## Expect
- The created machine pool should be listed  
- The ID/replica should be default/0 and instance type should be m5.xlarge by default, the availability zones should be same with the default one  
ID AUTOSCALING REPLICAS INSTANCE TYPE LABELS TAINTS AVAILABILITY ZONES  
default No 3 m5.8xlarge us-east-1a, us-east-1b, us-east-1c  
default No 0 m5.xlarge us-east-1a, us-east-1b, us-east-1c

## Step
Run command to create an advanced machine pools  
$ rosa create machinepool -c <cluster name> --name default2 --replicas 3 --labels "m5.xlarge/test=aaa,bbb=ccc,ddd=fff,test.label.openshift/label=mmm" --taints "#$%^&*Key1=value1:NoExecute, openshift.taints.com/test=value2:NoSchedule" --instance-type m5.2xlarge  
NOTE: SDA-8272, empty taints value is support ,--taints key=:NoSchedule need to update the automated TC

## Expect
- There will be succeeded message output  
[xueli@xueli-work tmp]$ rosa create machinepool -c xueli-rosa --name default --replicas 0  
I: Machine pool '<machine pool name>' created successfully on cluster 'xueli-rosa'

## Step
Run command to check the machine pools  
$ rosa list machinepool -c <cluster name>

## Expect
- The created machine pool should be listed  
- The ID should be default3  
- The Autoscaling should be no  
- The replica should be 3  
- The instance type should be m5.2xlarge  
- the labels should be correct  
- The taints should be correct  
- The available zones should be correct

## Step
Run below command to create an auto scaling machine pools  
$ rosa create machinepool -c xueli-rosa --name autoscale --enable-autoscaling --max-replicas 6 --min-replicas 3 --labels "aaa=bbb"

## Expect
- There will be succeeded message output  
[xueli@xueli-work tmp]$ rosa create machinepool -c xueli-rosa --name default --replicas 0  
I: Machine pool '<machine pool name>' created successfully on cluster 'xueli-rosa'

## Step
Run command to check the machine pools  
$ rosa list machinepool -c <cluster name>

## Expect
- The created machine pool should be listed  
- The ID should be autoscale  
- The Autoscaling should be yes  
- The replica should be <min>-<max> like 3-6  
- The instance type should be m5.xlarge  
- the labels should be correct  
- The taints should be correct  
- The available zones should be correct

## Step
Launch AWS console to check the instances created by the machine pools

## Expect
All of the instances should be AMI instances
