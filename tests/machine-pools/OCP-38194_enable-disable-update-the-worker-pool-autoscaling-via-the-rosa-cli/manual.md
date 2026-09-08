# Test

## Step
Log in with the rosa tool and prepare one ready single-az rosa cluster

## Expect

## Step
Try to enable the autoscaling with the interactive mode.  
\# rosa edit machinepools worker -c <cluster_id> --enable-autoscaling --min-replicas 3 --max-replicas 6

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
5. The info can be list by 'rosa list machinepool'

## Step
Repeat step2 to update the autoscaling config.

## Expect
1.It should succeed without any error.  
2.There are ClusterAutoscaler and MachineAutoscaler objects created on the cluster console.  
\#oc get ClusterAutoscaler  
\#oc get MachineAutoscaler -n openshift-machine-api  
3.When describe the MachineAutoscaler, there should the max_replicas and min-replicas info like bellow  
Spec:  
Max Replicas: 50  
Min Replicas: 10  
4.Check if the autoscaling can be trigerred(OCP-28108)  
5. The info can be list by 'rosa list machinepool'

## Step
Repeat step2 with the command line and check the help message for the '/rosa edit machinepools'.  
\# ./rosa edit machinepool default --enable-autoscaling --min-replicas=3 max-replicas=6 -c 1i28ed2fq17dpmtc8ks59g2l22mr2rq2  
NOTE: if not both of min-replicas and max-replicas provided, the tool will prompt them with the interactive mode.

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
3.The result should be same with the step2

## Step
Repeat step4 to update the autoscaling config by the command line

## Expect
The result should be same with the one in step4

## Step
Disable the cluster autoscaling by the interactive mode.  
\# ./rosa edit machinepool default -c 1i264fjuslcbrulqmdhnlhq7p4m4nemo -i  
? Enable autoscaling: [? for help] (Y/n) n  
? Enable autoscaling: No  
? Replicas: [? for help] 3  
? Replicas: 3

## Expect
1.It should succeed to patch and there is no 'nodes.autoscale_compute'  
2.The ClusterAutoscaler and MachineAutoscaler objects should be deleted on the cluster console.  
\#oc get ClusterAutoscaler (TBD)  
No resources found.  
\#oc get MachineAutoscaler -n openshift-machine-api  
No resources found.

## Step
Disable the cluster autoscaling by the command line.  
\# ./rosa edit machinepool --replicas=6 -c 1i28ed2fq17dpmtc8ks59g2l22mr2rq2 default

## Expect
The result should be same with the one in the last step

## Step
Repeat step 2~5 on the additional machine pool

## Expect
The results should be same as the above one

## Step
~~Enable the autoscaling when creating a new rosa cluster with the interactive mode.~~

## Expect
~~0. There should be some prompt step for enabling the autoscaling: ? Enable autoscaling (optional): [? for help] (y/N) y ? Enable autoscaling (optional): Yes ? Min replicas: [? for help] (2) 2 ? Min replicas: 2 ? Max replicas: [? for help] (2) 5 ? Max replicas: 5 1.It should succeed without any error. 2.There are ClusterAutoscaler and MachineAutoscaler objects created on the cluster console. #oc get ClusterAutoscaler #oc get MachineAutoscaler -n openshift-machine-api 3.When describe the MachineAutoscaler, there should the max_replicas and min-replicas info like bellow Spec: Max Replicas: 50 Min Replicas: 10 4.Check if the autoscaling can be trigerred(OCP-28108) 5. The info can be list by 'rosa list machinepool'~~

## Step
~~Repeat all step on the rosa multi-az clusters~~

## Expect
~~The result should be same with the above ones~~

## Step
~~Enable the autoscaling during cluster creation.~~

## Expect
~~The cluster should be created successfully with the autoscaling enable~~
