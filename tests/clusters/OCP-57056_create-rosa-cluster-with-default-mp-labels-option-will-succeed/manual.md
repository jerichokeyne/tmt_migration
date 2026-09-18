# Test

## Step

Log in with the rosa tool

## Expect

## Step

Check the help info for 'rosa create cluster -h'

## Expect

There is the help info for '--default-mp-labels'
--default-mp-labels string Labels for the default machine pool. Format should be a comma-separated list of 'key=value'. This list will overwrite any modifications made to Node labels on an ongoing basis.

## Step

Create a ROSA cluster with the --default-mp-labels flag:
Format should be a comma-separated list of 'key=value'. name part must consist of alphanumeric characters, '-', '_' or '.', and must start and end with an alphanumeric character
I.e.
```bash
rosa create cluster --cluster-name am-label-2 --sts --role-arn arn:aws:iam::425464789085:role/<role-prefix>-Installer-Role --support-role-arn arn:aws:iam::425464789085:role/<role-prefix>-Support-Role --controlplane-iam-role arn:aws:iam::425464789085:role/<role-prefix>-ControlPlane-Role --worker-iam-role arn:aws:iam::425464789085:role/<role-prefix>-Worker-Role --operator-roles-prefix am-label-2-q0w0 --region us-west-1 --version 4.11.18 --replicas 2 --compute-machine-type m5.xlarge --machine-cidr 10.0.0.0/16 --service-cidr 172.30.0.0/16 --pod-cidr 10.128.0.0/14 --host-prefix 23 --default-mp-labels aaa=bbb
```

## Expect

- The cluster created successfully

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
```bash
rosa create cluster --cluster-name am-label-3 --sts --role-arn arn:aws:iam::425464789085:role/<role-prefix>-Installer-Role --support-role-arn arn:aws:iam::425464789085:role/<role-prefix>-Support-Role --controlplane-iam-role arn:aws:iam::425464789085:role/<role-prefix>-ControlPlane-Role --worker-iam-role arn:aws:iam::425464789085:role/<role-prefix>-Worker-Role --operator-roles-prefix am-label-2-q0w0 --region us-west-1 --version 4.11.18 --replicas 2 --compute-machine-type m5.xlarge --machine-cidr 10.0.0.0/16 --service-cidr 172.30.0.0/16 --pod-cidr 10.128.0.0/14 --host-prefix 23 --default-mp-labels aaa=bbb,t=test
```

## Expect

The cluster created successfully

## Step

Check the labels are set correctly
```bash
rosa list machinepool -c am-label-3
```

## Expect

ID AUTOSCALING REPLICAS INSTANCE TYPE LABELS TAINTS AVAILABILITY ZONES SUBNETS SPOT INSTANCES
Default No 2 m5.xlarge aaa=bbb,t=test us-west-1a N/A

## Step

Create a ROSA cluster with the --default-mp-labels flag and autoscale enabled, i.e.
```bash
rosa create cluster --cluster-name am-label-4 --sts --role-arn arn:aws:iam::425464789085:role/<role-prefix>-Installer-Role --support-role-arn arn:aws:iam::425464789085:role/<role-prefix>-Support-Role --controlplane-iam-role arn:aws:iam::425464789085:role/<role-prefix>-ControlPlane-Role --worker-iam-role arn:aws:iam::425464789085:role/<role-prefix>-Worker-Role --operator-roles-prefix am-label-2-q0w0 --region us-west-1 --version 4.11.18 --enable-autoscaling --min-replicas 2 --max-replicas 4 --compute-machine-type m5.xlarge --machine-cidr 10.0.0.0/16 --service-cidr 172.30.0.0/16 --pod-cidr 10.128.0.0/14 --host-prefix 23 --default-mp-labels aaa=bbb
```

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

Create a ROSA cluster with the --default-mp-labels flagwith empty value, i.e.
```bash
rosa create cluster --cluster-name am-label-5 --sts --role-arn arn:aws:iam::425464789085:role/<role-prefix>-Installer-Role --support-role-arn arn:aws:iam::425464789085:role/<role-prefix>-Support-Role --controlplane-iam-role arn:aws:iam::425464789085:role/<role-prefix>-ControlPlane-Role --worker-iam-role arn:aws:iam::425464789085:role/<role-prefix>-Worker-Role --operator-roles-prefix am-label-2-q0w0 --region us-west-1 --version 4.11.18 --enable-autoscaling --min-replicas 2 --max-replicas 4 --compute-machine-type m5.xlarge --machine-cidr 10.0.0.0/16 --service-cidr 172.30.0.0/16 --pod-cidr 10.128.0.0/14 --host-prefix 23 --default-mp-labels test=
```

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

## Step

Create a ROSA cluster with the --default-mp-labels flag with slash sign
```bash
rosa create cluster --cluster-name am-label-5 --sts --role-arn arn:aws:iam::425464789085:role/<role-prefix>-Installer-Role --support-role-arn arn:aws:iam::425464789085:role/<role-prefix>-Support-Role --controlplane-iam-role arn:aws:iam::425464789085:role/<role-prefix>-ControlPlane-Role --worker-iam-role arn:aws:iam::425464789085:role/<role-prefix>-Worker-Role --operator-roles-prefix am-label-2-q0w0 --region us-west-1 --version 4.11.18 --enable-autoscaling --min-replicas 2 --max-replicas 4 --compute-machine-type m5.xlarge --machine-cidr 10.0.0.0/16 --service-cidr 172.30.0.0/16 --pod-cidr 10.128.0.0/14 --host-prefix 23 --default-mp-labels Create a ROSA cluster with the --default-mp-labels flagwith empty value, i.e.
rosa create cluster --cluster-name am-label-5 --sts --role-arn arn:aws:iam::425464789085:role/<role-prefix>-Installer-Role --support-role-arn arn:aws:iam::425464789085:role/<role-prefix>-Support-Role --controlplane-iam-role arn:aws:iam::425464789085:role/<role-prefix>-ControlPlane-Role --worker-iam-role arn:aws:iam::425464789085:role/<role-prefix>-Worker-Role --operator-roles-prefix am-label-2-q0w0 --region us-west-1 --version 4.11.18 --enable-autoscaling --min-replicas 2 --max-replicas 4 --compute-machine-type m5.xlarge --machine-cidr 10.0.0.0/16 --service-cidr 172.30.0.0/16 --pod-cidr 10.128.0.0/14 --host-prefix 23 --default-mp-labels submariner.io/gateway=bbb
```

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
Default Yes 2-4 m5.xlarge submariner.io/gateway=bbb us-west-2a N/A
