# Setup
Log in the rosa tool and prepare one rosa hypershift ready cluster

# Test

## Step
Prepare ROSA Hypershift cluster

## Expect
Cluster is ready

## Step
Run command to record the machine pools
```bash
rosa list machinepool -c <cluster name>
```

## Expect
- The machine pools returned
```
ID AUTOSCALING REPLICAS INSTANCE TYPE AVAILABILITY ZONE SUBNET NODEPOOL
workers No 2 m5.xlarge us-west-2a subnet-093ef2e9cd69cb74d am-hp-workers
```

## Step
Run command to create default machine pools in interactive mode
```bash
rosa create machinepool -c <cluster name> -i
```

## Expect
```
I: Enabling interactive mode
? Machine pool name: new-mp
? Enable autoscaling (optional): No
? Replicas: 1
I: Fetching instance types
? Instance type: m5.xlarge
I: Machine pool 'new-mp' created successfully on hosted cluster 'qe-hp-54413-rot'
I: To view all machine pools, run 'rosa list machinepools -c qe-hp-54413-rot'
```

## Step
Check the machine pool with command
```bash
rosa list machinepool -c <cluster name>
```

## Expect
The machine pool should be created and all of the information should exactly match the input
```
ID AUTOSCALING DESIRED REPLICAS CURRENT REPLICAS INSTANCE TYPE AVAILABILITY ZONE SUBNET MESSAGE
workers No 2 0 m5.xlarge us-west-2a subnet-0915a80a77f8bf0eb WaitingForAvailableMachines: NodeProvisioning
new-mp No 1 0 m5.xlarge us-west-2a subnet-0915a80a77f8bf0eb WaitingForAvailableMachines: NodeProvisioning
```

## Step
Run command to create default machine pools in interactive mode with boundary value ("0", "90")
```bash
rosa create machinepool -c <cluster name> -i
```

## Expect
```
I: Enabling interactive mode
? Machine pool name: min-rep
? Enable autoscaling (optional): No
? Replicas: 0
? Labels (optional): u=i
? Taints (optional): key=value:NoSchedule
I: Fetching instance types
? Instance type: m5.xlarge
```


```
I: Machine pool 'min-rep' created successfully on hosted cluster 'qe-hp-54413-rot'
I: To view all machine pools, run 'rosa list machinepools -c qe-hp-54413-rot'
~ >
~ > rosa create machinepool -c qe-hp-54413-rot
I: Enabling interactive mode
? Machine pool name: max-rep
? Enable autoscaling (optional): No
? Replicas: 90
I: Fetching instance types
? Instance type: m5.xlarge
I: Machine pool 'max-rep' created successfully on hosted cluster 'qe-hp-54413-rot'
I: To view all machine pools, run 'rosa list machinepools -c qe-hp-54413-rot'
NOTE: from SDA-8219, the labels and taints will show in the interactive mode
```

## Step
Check the machine pool with command
```bash
rosa list machinepool -c <cluster name>
```

## Expect
The machine pool should be created and all of the information should exactly match the input
```
ID AUTOSCALING DESIRED REPLICAS CURRENT REPLICAS INSTANCE TYPE AVAILABILITY ZONE SUBNET MESSAGE
min-rep No 0 0 m5.xlarge us-west-2a subnet-0915a80a77f8bf0eb
max-rep No 90 0 m5.xlarge us-west-2a subnet-0915a80a77f8bf0eb
workers No 2 0 m5.xlarge us-west-2a subnet-0915a80a77f8bf0eb WaitingForAvailableMachines: NodeStartupTimeout,NodeProvisioning
new-mp No 1 0 m5.xlarge us-west-2a subnet-0915a80a77f8bf0eb WaitingForAvailableMachines: NodeProvisioning
NOTE: from SDA-8219, the labels and taints will show in the output
```

## Step
Try to create a new machine pool with the autoscaling enable by the interactive mode.

## Expect
```
I: Enabling interactive mode
? Machine pool name: auto
? Enable autoscaling (optional): Yes
? Min replicas: 3
? Max replicas: 6
I: Fetching instance types
? Instance type: m5.xlarge
I: Machine pool 'auto' created successfully on hosted cluster 'qe-hp-54413-rot'
I: To view all machine pools, run 'rosa list machinepools -c qe-hp-54413-rot'
NOTE: from SDA-8219, the labels and taints will show in the interactive mode
```

## Step
Run command to check the machine pools
```bash
rosa list machinepool -c <cluster name>
```

## Expect
The machine pool should be created and all of the information should exactly match the input
```
ID AUTOSCALING DESIRED REPLICAS CURRENT REPLICAS INSTANCE TYPE AVAILABILITY ZONE SUBNET MESSAGE
min-rep No 0 0 m5.xlarge us-west-2a subnet-0915a80a77f8bf0eb
max-rep No 90 0 m5.xlarge us-west-2a subnet-0915a80a77f8bf0eb WaitingForAvailableMachines: WaitingForInfrastructure,WaitingForNodeRef
workers No 2 0 m5.xlarge us-west-2a subnet-0915a80a77f8bf0eb WaitingForAvailableMachines: InstanceNotReady,NodeProvisioning
auto Yes 3-6 0 m5.xlarge us-west-2a subnet-0915a80a77f8bf0eb
new-mp No 1 0 m5.xlarge us-west-2a subnet-0915a80a77f8bf0eb WaitingForAvailableMachines: NodeProvisioning
NOTE: from SDA-8219, the labels and taints will show in the output
```

## Step
Create additional machine pool with one of the min-replicas and max-replicas, or without both

## Expect
The tool should prompt them with the interactive mode

## Step
Create additional machine pool, verify that only supported machinetypes are shown, choose non-default one

You can check what kind of instance types are supported by a specified zone via
```bash
ocm post /api/clusters_mgmt/v1/aws_inquiries/machine_types <<EOF
```
```json
{
"aws": {
"access_key_id": "********************",
"secret_access_key": "****************************************"
},
"availability_zones": [
"us-east-2a"
],
"region": {
"kind": "CloudRegion",
"id": "us-east-2"
}
}
```
EOF

## Expect

## Step
Run command to create the machine pools in interactive mode with negative values
$> rosa create machinepool -c <cluster name> -i
- string
- negative
- > than max value

## Expect
? Compute nodes instance type: m5.xlarge
? Enable autoscaling (optional): **ggf**
X Sorry, your reply was invalid: "ggf" is not a valid answer, please try again.

? Compute nodes instance type: m5.xlarge
? Enable autoscaling (optional): No
? Replicas: www
```
E: Expected a valid number of replicas: strconv.Atoi: parsing "www": invalid syntax
```

? Compute nodes instance type: m5.xlarge
? Enable autoscaling (optional): No
? Replicas: -1
```
E: Failed to add machine pool to hosted cluster 'am-hp': Attribute 'replicas' must be a non-negative integer.
```

? Compute nodes instance type: m5.xlarge
? Enable autoscaling (optional): No
? Replicas: 181
```
E: Failed to add machine pool to hosted cluster 'am-hp': The number of compute nodes requested 181 exceeds the maximum allowed: 90
```

## Step
Input invalid input for Replicas (string):

## Expect
? Enable autoscaling (optional): No
? Replicas: www
```
E: Expected a valid number of replicas: strconv.Atoi: parsing "www": invalid syntax
```

## Step
Run command to check the machine pools
```bash
rosa list machinepool -c <cluster name>
```

## Expect
- no new machinepools created

The machine pool should be created and all of the information should exactly match the input
```
ID AUTOSCALING DESIRED REPLICAS CURRENT REPLICAS INSTANCE TYPE AVAILABILITY ZONE SUBNET MESSAGE
min-rep No 0 0 m5.xlarge us-west-2a subnet-0915a80a77f8bf0eb
max-rep No 90 0 m5.xlarge us-west-2a subnet-0915a80a77f8bf0eb WaitingForAvailableMachines: WaitingForInfrastructure,WaitingForNodeRef
workers No 2 0 m5.xlarge us-west-2a subnet-0915a80a77f8bf0eb WaitingForAvailableMachines: InstanceNotReady,NodeProvisioning
auto Yes 3-6 0 m5.xlarge us-west-2a subnet-0915a80a77f8bf0eb
new-mp No 1 0 m5.xlarge us-west-2a subnet-0915a80a77f8bf0eb WaitingForAvailableMachines: NodeProvisioning
NOTE: from SDA-8219, the labels and taints will show in the output
```

## Step
Wait for the Ready nodepool status
List the nodepools
```bash
rosa list machinepool -c <cluster-name> -o yaml
```

## Expect
- The MESSAGE is empty after MAX 20 minutes
