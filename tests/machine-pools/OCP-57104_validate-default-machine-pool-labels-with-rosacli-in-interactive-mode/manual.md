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
$ rosa edit machinepool Default -c <cluster name>  
? Enable autoscaling (optional): No  
? Labels: **p*=test**

## Expect
E: Failed to update machine pool 'Default' on cluster 'am-label-13': Invalid label key 'd*': name part must consist of alphanumeric characters, '-', '_' or '.', and must start and end with an alphanumeric character (e.g. 'MyName', or 'my.name', or '123-abc', regex used for validation is '([A-Za-z0-9][-A-Za-z0-9_.]*)?[A-Za-z0-9]')

## Step
Run command to edit default machine pool in interactive mode and add label with empty key  
? Labels: =test

## Expect
E: Failed to update machine pool 'Default' on cluster 'am-label-13': Invalid label key '': name part must be non-empty; name part must consist of alphanumeric characters, '-', '_' or '.', and must start and end with an alphanumeric character (e.g. 'MyName', or 'my.name', or '123-abc', regex used for validation is '([A-Za-z0-9][-A-Za-z0-9_.]*)?[A-Za-z0-9]')

## Step
Run command to edit default machine pool in interactive mode and add labels with duplicated key  
? Labels: test1=test_1,test1=test_2

## Expect
E: Duplicated label key 'test' used

## Step
Run command to edit default machine pool in interactive mode and add label with >63 character label key  
? Labels: abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234=test

## Expect
E: Failed to update machine pool 'Default' on cluster 'am-label-13': Invalid label key 'abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234': name part must be no more than 63 characters

## Step
Try to create a ROSA cluster with the --default-mp-labels flag and string parameter  
? Labels: 1-2-3

## Expect
E: Expected key=value format for labels

## Step
Run command to edit default machine pool in interactive mode and add label with >63 character label value  
? Labels: test=abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234

## Expect
E: Failed to update machine pool 'Default' on cluster 'am-label-13': Invalid label value 'abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234': at key: 'test': must be no more than 63 characters

## Step
Try to create a ROSA cluster with the --default-mp-labels flag and kubernetes.io/ labels, which is reserved for [Kubernetes](<https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/>) core components
    
    ? Labels: kubernetes.io=test  
    or  
    ? Labels:  k8s.io=test  
    or  
    ? Labels: openshift.io=test

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
