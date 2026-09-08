# Test

## Step
Log in with the rosa tool and prepare one ready single-az rosa cluster

## Expect

## Step
Check the help message of './rosa create machinepool -h'

## Expect
It should contain bellow message:  
Examples:  
....  
\# Add a machine pool mp-1 with autoscaling enabled and 3 to 6 replicas of m5.xlarge to a cluster  
rosa create machinepool --cluster=mycluster --name=mp-1 --enable-autoscaling   
--min-replicas=3 --max-replicas=6 --instance-type=m5.xlarge  
....  
Flags:  
....  
--enable-autoscaling Enable autoscaling for the machine pool.  
.....  
--max-replicas int Maximum number of machines for the machine pool.  
--min-replicas int Minimum number of machines for the machine pool.

## Step
Try to create a new machine pool with the autoscaling enable by the interactive mode.  
\# ./rosa create machinepool -c 1i264fjuslcbrulqmdhnlhq7p4m4nemo -i  
? Machine pool name: t2  
? Machine pool name: t2  
? Enable autoscaling (optional): [? for help] (y/N) y  
? Enable autoscaling (optional): Yes  
? Min replicas: [? for help] 3  
? Min replicas: 3  
? Max replicas: [? for help] 6  
? Max replicas: 6  
? Instance type: [Use arrows to move, type to filter, ? for more help]  
> m5.xlarge  
r5.xlarge  
m5.2xlarge  
c5.2xlarge  
r5.2xlarge  
m5.4xlarge  
c5.4xlarge  
? Instance type: m5.xlarge  
? Labels (optional): [? for help]   
? Labels (optional):   
? Taints (optional): [? for help]   
? Taints (optional):   
I: Machine pool 't2' created successfully on cluster '1i264fjuslcbrulqmdhnlhq7p4m4nemo'

## Expect
1.It should succeed without any error.  
2.There are ClusterAutoscaler and MachineAutoscaler objects created on the cluster console.  
\#oc get ClusterAutoscaler  
\#oc get MachineAutoscaler -n openshift-machine-api  
3.When describe the MachineAutoscaler, there should the max_replicas and min-replicas info like bellow  
Spec:  
Max Replicas: 100  
Min Replicas: 4  
4.Check if the autoscaling can be trigerred(OCP-28108)  
5. The result of 'rosa list machinepool' should be like bellow:  
\# ./rosa list machinepool -c 1i264fjuslcbrulqmdhnlhq7p4m4nemo  
ID AUTOSCALING REPLICAS INSTANCE TYPE LABELS TAINTS AVAILABILITY ZONES  
default No 3 m5.xlarge us-east-2a  
t1 Yes 3-6 m5.xlarge us-east-2a  
t2 Yes 3-6 m5.xlarge us-east-2a

## Step
~~Repeat step3 with the command line and check the help message for the '/rosa edit machinepools'. # ./rosa edit machinepool default --enable-autoscaling --min-replicas=3 max-replicas=6 -c 1i28ed2fq17dpmtc8ks59g2l22mr2rq2~~

## Expect
1.There should be bellow example message:  
....  
\# Enable autoscaling and Set 3-5 replicas on machine pool 'mp1' on cluster 'mycluster'  
rosa edit machinepool --enable-autoscaling --min-replicas=3 max-replicas=5 --cluster=mycluster mp1  
....  
2.There should be the help message for the flags:  
....  
--enable-autoscaling Enable autoscaling for the machine pool.  
....  
--max-replicas int Maximum number of machines for the machine pool.  
--min-replicas int Minimum number of machines for the machine pool.  
.....  
3.The result should be same with the step3

## Step
Create additional machine pool with one of the min-replicas and max-replicas, or without both

## Expect
The tool should prompt them with the interactive mode
