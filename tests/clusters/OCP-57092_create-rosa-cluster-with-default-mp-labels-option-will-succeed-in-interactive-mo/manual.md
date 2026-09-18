# Test

## Step

Log in with the rosa tool

## Expect

## Step

Check the help info for 'Default machine pool labels (optional)'
```bash
rosa create cluster -i
```
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
? Default machine pool labels (optional): [? for help] **?**

## Expect

```
? Labels for the default machine pool. Format should be a comma-separated list of 'key=value'. This list will overwrite any modifications made to Node labels on an ongoing basis.
```

## Step

Create a ROSA cluster with the --default-mp-labels flag:
? Default machine pool labels (optional): [? for help] aaa=bbb
...

## Expect

- --default-mp-labels flag should be shown in the command when creating the cluster in interactive mode

    I: To create this cluster again in the future, you can run:
    ....
     --default-mp-labels aaa=bbb

-The cluster created successfully

## Step

Check the labels are set correctly
```bash
rosa list machinepool -c am-label-2
```

## Expect

ID AUTOSCALING REPLICAS INSTANCE TYPE LABELS TAINTS AVAILABILITY ZONES SUBNETS SPOT INSTANCES
Default No 2 m5.xlarge aaa=bbb us-west-1a N/A

## Step

Create a ROSA cluster with the --default-mp-labels flag, add multiple labels, i.e.
? Default machine pool labels (optional): [? for help] aaa=b,t=test

## Expect

The cluster created successfully

## Step

Check the labels are set correctly
```bash
rosa list machinepool -c am-label-3
```

## Expect

ID AUTOSCALING REPLICAS INSTANCE TYPE LABELS TAINTS AVAILABILITY ZONES SUBNETS SPOT INSTANCES
Default No 2 m5.xlarge aaa=b,t=test us-west-1a N/A

## Step

Create a ROSA cluster with the --default-mp-labels flag and autoscale enabled, i.e.
? Enable autoscaling (optional): Yes
? Default machine pool labels (optional): [? for help] aaa=bbb

## Expect

The cluster created successfully

## Step

Check the labels are set correctly
```bash
rosa list machinepool -c am-label-4
```

## Expect

```bash
rosa list machinepool -c am-label-4
```
ID AUTOSCALING REPLICAS INSTANCE TYPE LABELS TAINTS AVAILABILITY ZONES SUBNETS SPOT INSTANCES
Default Yes 2-4 m5.xlarge aaa=bbb us-west-2a N/A

## Step

Create a ROSA cluster with the --default-mp-labels flag with empty value, i.e.
? Default machine pool labels (optional): [? for help] test=

## Expect

The cluster created successfully

## Step

Check the labels are set correctly
```bash
rosa list machinepool -c am-label-5
```

## Expect

```bash
rosa list machinepool -c am-label-5
```
ID AUTOSCALING REPLICAS INSTANCE TYPE LABELS TAINTS AVAILABILITY ZONES SUBNETS SPOT INSTANCES
Default Yes 2-4 m5.xlarge test= us-west-2a N/A
