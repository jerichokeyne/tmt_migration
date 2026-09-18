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
Run command to create machine pool
```bash
rosa create machinepool -c <cluster name> --name <mp-name> --replicas 3 --enable-autoscaling=false --labels <labels> --taints <tains> --autorepair false
```

## Expect
- There will be succeeded message output

## Step
Run command to check the machine pools
```bash
rosa list machinepool -c <cluster name>
```

## Expect
- The updated machine pool should be listed
- The ID/replica should be default/0 and instance type should be m5.xlarge by default, the availability zones should be same with the default one
D AUTOSCALING REPLICAS INSTANCE TYPE AVAILABILITY ZONE SUBNET NODEPOOL
20icp0qlb0voc1olfgghs5ri3nu2a2so No 2 m5.xlarge us-west-2a subnet-093ef2e9cd69cb74d am-hp-workers
20ielhc6mjrc4vo8sj953ddu624mo86e No 3 m5.xlarge us-west-2a subnet-093ef2e9cd69cb74d am-hp-workers1
NOTE: from SDA-8219, the labels and taints will show in the output
FROM SDA-8220 - Autorepair is shown

## Step
Run command to edit an advanced machine pools
```bash
rosa edit machinepool --enable-autoscaling --min-replicas=3 max-replicas=6--cluster=mycluster <machinepool-id> --labels <labels> --taints <tains> --autorepair true
```

## Expect
- There will be succeeded message output

## Step
Run command to check the machine pools
```bash
rosa list machinepool -c <cluster name>
```

## Expect
- The updated machine pool should be listed
- The ID/replica should be default/0 and instance type should be m5.xlarge by default, the availability zones should be same with the default one
D AUTOSCALING REPLICAS INSTANCE TYPE AVAILABILITY ZONE SUBNET NODEPOOL
20icp0qlb0voc1olfgghs5ri3nu2a2so No 2 m5.xlarge us-west-2a subnet-093ef2e9cd69cb74d am-hp-workers
20ielhc6mjrc4vo8sj953ddu624mo86e Yes 3-6 m5.xlarge us-west-2a subnet-093ef2e9cd69cb74d am-hp-workers1
NOTE: from SDA-8219, the labels and taints will show in the output

## Step
Run command to enable autoscaling and set the min-replicas to 1
```bash
rosa edit machinepool --enable-autoscaling --min-replicas=1 max-replicas=6 --cluster=mycluster <mp-name>
```

## Expect
There will be succeeded message output

## Step
Try to edit machinepool with just --autorepair flag.
```bash
rosa edit machinepool -c <cluster-name> <mp-name> --autorepair=false
```

## Expect
The machinepool should be updated successfully without going into interactive mode and asking for min or max replicas
```
I: Updated machine pool 'mp-4597' on hosted cluster 'aaraj-hcp'(OCM-5186)
```

## Step
Run command to check the machine pools
```bash
rosa list machinepool -c <cluster name>
```

## Expect

## Step
Prepare another additional machine pool

## Expect

## Step
Repeat above steps

## Expect
It should work as expected

## Step
Launch AWS console to check the instances created by the machine pools

## Expect
All of the instances should be AMI instances
