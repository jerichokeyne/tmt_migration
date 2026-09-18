# Test

## Step

Log in the rosa tool

## Expect

## Step

Try to create a ROSA cluster with the --worker-mp-labels flag and invalid key
```bash
rosa create cluster --cluster-name am-label-2 --sts --role-arn arn:aws:iam::425464789085:role/<role-prefix>-Installer-Role --support-role-arn arn:aws:iam::425464789085:role/<role-prefix>-Support-Role --controlplane-iam-role arn:aws:iam::425464789085:role/<role-prefix>-ControlPlane-Role --worker-iam-role arn:aws:iam::425464789085:role/<role-prefix>-Worker-Role --operator-roles-prefix am-label-2-q0w0 --region us-west-1 --version 4.11.18 --replicas 2 --compute-machine-type m5.xlarge --machine-cidr 10.0.0.0/16 --service-cidr 172.30.0.0/16 --pod-cidr 10.128.0.0/14 --host-prefix 23**-- worker-mp-labels** p*=test
```

## Expect

```
E: name part must consist of alphanumeric characters, '-', '_' or '.', and must start and end with an alphanumeric character (e.g. 'MyName', or 'my.name', or '123-abc', regex used for validation is '([A-Za-z0-9][-A-Za-z0-9_.]*)?[A-Za-z0-9]')
```

## Step

Try to create a ROSA cluster with the --worker-mp-labels flag and empty key
--worker-mp-labels =test

## Expect

```
E: name part must consist of alphanumeric characters, '-', '_' or '.', and must start and end with an alphanumeric character (e.g. 'MyName', or 'my.name', or '123-abc', regex used for validation is '([A-Za-z0-9][-A-Za-z0-9_.]*)?[A-Za-z0-9]')
```

## Step

Try to create a ROSA cluster with the --worker-mp-labels flag without any value
--worker-mp-labels

## Expect

Help is shown with the error:
Failed to execute root command: flag needs an argument: --worker-mp-labels

## Step

Try to create a ROSA cluster with the --worker-mp-labels flag and >63 character label key
abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234=test

## Expect

```
E: name part must consist of alphanumeric characters, '-', '_' or '.', and must start and end with an alphanumeric character (e.g. 'MyName', or 'my.name', or '123-abc', regex used for validation is '([A-Za-z0-9][-A-Za-z0-9_.]*)?[A-Za-z0-9]')
```

## Step

Try to create a ROSA cluster with the --worker-mp-labels flag and >63 character label value
test=abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234

## Expect

```
E: name part must consist of alphanumeric characters, '-', '_' or '.', and must start and end with an alphanumeric character (e.g. 'MyName', or 'my.name', or '123-abc', regex used for validation is '([A-Za-z0-9][-A-Za-z0-9_.]*)?[A-Za-z0-9]')
```

## Step

Try to create a ROSA cluster with the --worker-mp-labels flags and duplicated key
--worker-mp-labels test=test1,test=test2

## Expect

```
E: Duplicated label key 'test' used
```

## Step

Try to create a ROSA cluster with the --worker-mp-labels flag with Hypershift cluster
```bash
rosa create cluster -c hp-test --hosted-cp --sts --subnet-ids subnet-02e06022c6f3a07fd,subnet-0d32fc4d534c1e820 --channel-group candidate --region us-west-2 --role-arn arn:aws:iam::301721915996:role/<role-prefix>-20221215-Installer-Role --support-role-arn arn:aws:iam::301721915996:role/<role-prefix>-20221215-Support-Role --controlplane-iam-role arn:aws:iam::301721915996:role/<role-prefix>-20221215-ControlPlane-Role --worker-iam-role arn:aws:iam::301721915996:role/<role-prefix>-20221215-Worker-Role --worker-mp-labels /=bbb
```

## Expect

```
E: Invalid label key '/': prefix part must be non-empty; name part must be non-empty; name part must consist of alphanumeric characters, '-', '_' or '.', and must start and end with an alphanumeric character (e.g. 'MyName', or 'my.name', or '123-abc', regex used for validation is '([A-Za-z0-9][-A-Za-z0-9_.]*)?[A-Za-z0-9]'
```
