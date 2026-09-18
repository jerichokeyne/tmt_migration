# Test

## Step

Log in via rosacli and run `rosa create -h`

## Expect

- There is no '--sts' flag any more
- There are '--non-sts' and '--mint-mode' flag
....
--non-sts Use legacy way of creating clusters (IAM mode).
--mint-mode Use legacy way of creating clusters (IAM mode). This is an alias for --non-sts.

....

## Step

Create cluster without setting '--sts'/'--non-sts'/'--mint-mode' flags but with the account-roles arns set.
```bash
rosa create cluster --cluster-name yuwan-psts2 --mode auto --role-arn arn:aws:iam::301721915996:role/role/1102accrwp1/yw1102accrwp1-Installer-Role --support-role-arn arn:aws:iam::301721915996:role/role/1102accrwp1/yw1102accrwp1-Support-Role --controlplane-iam-role arn:aws:iam::301721915996:role/role/1102accrwp1/yw1102accrwp1-ControlPlane-Role --worker-iam-role arn:aws:iam::301721915996:role/role/1102accrwp1/yw1102accrwp1-Worker-Role --operator-roles-prefix yuwan-psts2-r0v8 --region us-east-2 --version 4.11.9 --replicas 2 --compute-machine-type m5.xlarge --machine-cidr 10.0.0.0/16 --service-cidr 172.30.0.0/16 --pod-cidr 10.128.0.0/14 --host-prefix 23 -y
```

## Expect

The STS cluster will be used.

## Step

Create cluster with setting '--sts'

## Expect

- There should be hint message tell the '--sts' flag is deprecated.

## Step

Create cluster with setting '--non-sts' flag

## Expect

The NON-sts cluster will be created.

## Step

Create cluster with setting '--mint-mode' flag

## Expect

The NON-sts cluster will be created.
