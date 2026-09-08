# Test

## Step
Log in the rosa tool

## Expect

## Step
Try to create a ROSA cluster with the --default-mp-labels flag and invalid key  
> rosa create cluster -i  
I: Interactive mode enabled.  
Any optional fields can be left empty and a default will be selected.  
? Cluster name: am-label-2  
? Deploy cluster using AWS STS: Yes  
W: In a future release STS will be the default mode.  
W: --sts flag won't be necessary if you wish to use STS.  
W: --non-sts/--mint-mode flag will be necessary if you do not wish to use STS.  
? OpenShift version: 4.11.18  
W: More than one Installer role found  
? Installer role ARN: arn:aws:iam::425464789085:role/hac-ecosystem-Installer-Role  
I: Using arn:aws:iam::425464789085:role/hac-ecosystem-ControlPlane-Role for the ControlPlane role  
I: Using arn:aws:iam::425464789085:role/hac-ecosystem-Worker-Role for the Worker role  
I: Using arn:aws:iam::425464789085:role/hac-ecosystem-Support-Role for the Support role  
? External ID (optional):   
? Operator roles prefix: test-cluster-d7r3  
? Multiple availability zones (optional): No  
? AWS region: us-west-2  
? PrivateLink cluster (optional): No  
? Install into an existing VPC (optional): No  
? Select availability zones (optional): No  
? Enable Customer Managed key (optional): No  
? Compute nodes instance type: m5.xlarge  
? Enable autoscaling (optional): No  
? Compute nodes: 2  
? Default machine pool labels (optional): [? for help]**p*=test**

## Expect
E: name part must consist of alphanumeric characters, '-', '_' or '.', and must start and end with an alphanumeric character

## Step
Try to create a ROSA cluster with the --default-mp-labels flag and empty key  
--default-mp-labels =test

## Expect
E: name part must consist of alphanumeric characters, '-', '_' or '.', and must start and end with an alphanumeric character

## Step
Try to create a ROSA cluster with the --default-mp-labels flag and >63 character label key  
? Default machine pool labels (optional): [? for help]abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234=test

## Expect
E: Failed to create cluster: Invalid label key 'abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234': name part must be no more than 63 characters

## Step
Try to create a ROSA cluster with the --default-mp-labels flag and string parameter  
? Default machine pool labels (optional): [? for help] 1-2-3

## Expect
E: Expected key=value format for labels

## Step
Try to create a ROSA cluster with the --default-mp-labels flag and >63 character label value  
? Default machine pool labels (optional): [? for help]test=abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234

## Expect
E: Failed to create cluster: Invalid label value 'abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234': at key: 'test': must be no more than 63 characters

## Step
Try to create a ROSA cluster with the --default-mp-labels flag and kubernetes.io/ labels, which is reserved for [Kubernetes](<https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/>) core components
    
    ? Default machine pool labels (optional): [? for help] volume.beta.kubernetes.io/storage-provisioner=test

## Expect
E: Failed to create cluster: Invalid label key

## Step
Try to create a ROSA cluster with the --default-mp-labels flag and kubernetes.io/ labels, which is reserved for [Kubernetes](<https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/>) core components
    
    ? Default machine pool labels (optional): [? for help] volume.beta.k8s.io/storage-provisioner=test

## Expect
E: Failed to create cluster: Invalid label key

## Step
Try to create a ROSA cluster with the --default-mp-labels flag and duplicated keys  
? Default machine pool labels (optional): [? for help] test=test1,test=test2

## Expect
X Sorry, your reply was invalid: Duplicated label key 'test' used

## Step
The preserved labels can't be used   
? Default machine pool labels (optional): [? for help]kubernetes.io=test  
or  
? Default machine pool labels (optional): [? for help] k8s.io=test  
or  
? Default machine pool labels (optional): [? for help]openshift.io=test

## Expect
E: Failed to create cluster: Invalid label key

## Step
Try to create a ROSA cluster with the --default-mp-labels flag with Hypershift cluster  
? Default machine pool labels (optional): [? for help] 1a=2b

## Expect
E: Setting the default machine pool labels is not supported for hosted clusters
