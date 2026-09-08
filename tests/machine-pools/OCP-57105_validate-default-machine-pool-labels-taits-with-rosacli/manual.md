# Test

## Step
Log in with the rosa tool and create ROSA cluster

## Expect

## Step
Run command to record the machine pools  
$ rosa list machinepool -c <cluster name>

## Expect
- The machine pools returned  
- The ID/replica should be default/0 and instance type should be m5.xlarge by default, the availability zones should be same with the default one  
ID AUTOSCALING REPLICAS INSTANCE TYPE LABELS TAINTS AVAILABILITY ZONES SUBNETS SPOT INSTANCES  
Default No 2 m5.xlarge us-west-2a N/A

## Step
Run command to edit default machine pool in interactive mode and add label with invalid key  
$ rosa edit machinepool Default -c <cluster name> --labels**p*=test**

## Expect
E: Failed to update machine pool 'Default' on cluster 'am-label-13': Invalid label key 'd*': name part must consist of alphanumeric characters, '-', '_' or '.', and must start and end with an alphanumeric character (e.g. 'MyName', or 'my.name', or '123-abc', regex used for validation is '([A-Za-z0-9][-A-Za-z0-9_.]*)?[A-Za-z0-9]')

## Step
Run command to edit default machine pool in interactive mode and add label with empty key  
$ rosa edit machinepool Default -c <cluster name> --labels =test

## Expect
E: Failed to update machine pool 'Default' on cluster 'am-label-13': Invalid label key '': name part must be non-empty; name part must consist of alphanumeric characters, '-', '_' or '.', and must start and end with an alphanumeric character (e.g. 'MyName', or 'my.name', or '123-abc', regex used for validation is '([A-Za-z0-9][-A-Za-z0-9_.]*)?[A-Za-z0-9]')

## Step
Run command to edit default machine pool in interactive mode and add labels with duplicated key  
$ rosa edit machinepool Default -c <cluster name> --labels test=test1,test=test2

## Expect
E: Duplicated label key 'test' used

## Step
Run command to edit default machine pool in interactive mode and add label with >63 character label key  
$ rosa edit machinepool Default -c <cluster name> --labelsabcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234=test

## Expect
E: Failed to update machine pool 'Default' on cluster 'am-label-13': Invalid label key 'abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234': name part must be no more than 63 characters

## Step
Try to create a ROSA cluster with the --default-mp-labels flag and string parameter  
$ rosa edit machinepool Default -c <cluster name> --labels 1-2-3

## Expect
E: Expected key=value format for labels

## Step
Run command to edit default machine pool in interactive mode and add label with >63 character label value  
$ rosa edit machinepool Default -c <cluster name> --labelstest=abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234

## Expect
E: Failed to update machine pool 'Default' on cluster 'am-label-13': Invalid label value 'abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234': at key: 'test': must be no more than 63 characters

## Step
Try to create a ROSA cluster with the --default-mp-labels flag and kubernetes.io/ labels, which is reserved for [Kubernetes](<https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/>) core components
    
    $ rosa edit machinepool Default -c <cluster name> --labelskubernetes.io=test  
    or  
     k8s.io=test  
    or  
    openshift.io=test

## Expect
E: Failed to create cluster: Invalid label key

## Step
Run command to record the machine pools  
$ rosa list machinepool -c <cluster name>

## Expect
- The machine pools returned  
- The ID/replica should be default/0 and instance type should be m5.xlarge by default, the availability zones should be same with the default one  
- No labels added  
ID AUTOSCALING REPLICAS INSTANCE TYPE LABELS TAINTS AVAILABILITY ZONES SUBNETS SPOT INSTANCES  
Default No 2 m5.xlarge us-west-2a N/A

## Step
Check validation for tains:

## Expect
- E: Failed to update machine pool 'ji' on hosted cluster '22a5ecqkb1d1rabclbb9ga134gpeh9i2': At least one NodePool needs to have no taints.  
- E: Failed to add machine pool to hosted cluster '22a5ecqkb1d1rabclbb9ga134gpeh9i2': Taint at index 0 is incorrect: Unrecognized taint effect 'ScheduleType', only the following effects are supported: 'NoExecute', 'NoSchedule', 'PreferNoSchedule'.
