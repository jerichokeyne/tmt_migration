# Setup
<https://issues.redhat.com/browse/OCM-158>

| Hypershift is not supported.
Requires oc and rosa cli tools.

\---
|
\---
Starting with rosacli 1.2.29 we can no longer specify the cluster admin username, username will be called cluster-admin

# Test

## Step

Try creating a hosted control plane cluster with specifying cluster admin username and password on command line:

`rosa create cluster --cluster-name mytest --create-admin-user --cluster-admin-password <password> --regio`n us-east-1 --version 4.13.5 --replicas 2 --compute-machine-type m5.xlarge --machine-cidr 10.0.0.0/16 --service-cidr 172.30.0.0/16 --pod-cidr 10.128.0.0/14 --host-prefix 23 --hosted-cp --subnet-ids subnet-0d9be71f8f9e4caae,subnet-27421333d623efb4,subnet-061f8d26e03b93c98,subnet-0a044c7f6158
831ae,subnet-024b06c99cface4b0,subnet-0c70fa99d478a81d1

## Expect

This should fail immediately because the cluster admin user and password options are not supported for hcp clusters at install time.
```
E: `Setting Cluster Admin is only supported in classic ROSA clusters`
```

~~See:<https://issues.redhat.com/browse/OCM-3181> Due to this bug we currently create the cluster but no IDP is configured.~~

## Step

~~Attempt to create a classic cluster with invalid username:` rosa create cluster --cluster-name mytest --cluster-admin-user ad/min --cluster-admin-password C0rrect-battery-horse --regi`on us-east-1 --version 4.13.5 --replicas 2 --compute-machine-type m5.xlarge --machine-cidr 10.0.0.0/16 --service-cidr 172.30.0.0/16 --pod-cidr 10. 128.0.0/14 --host-prefix 23~~`
`

## Expect

`~~E:` invalid username 'ad/min': username must not contain /, :, or %~~

## Step

~~Attempt to create a classic STS cluster with invalid username:` rosa create cluster --cluster-name mytest --cluster-admin-user ad/min --cluster-admin-password C0rrect-battery-horse --regi`on us-east-1 --version 4.13.5 --replicas 2 --compute-machine-type m5.xlarge --machine-cidr 10.0.0.0/16 --service-cidr 172.30.0.0/16 --pod-cidr 10.128.0.0/14 --host-prefix 23 --sts~~`
`

## Expect

`E:` invalid username 'ad/min': username must not contain /, :, or %

## Step

Attempt to create a classic cluster with invalid password:
`[m@fedora 15:35:01 ~]$ rosa create cluster --cluster-name mytest --create-admin-user --cluster-admin-password pa55w0rd --region us-east-1 -`
-version 4.13.5 --replicas 2 --compute-machine-type m5.xlarge --machine-cidr 10.0.0.0/16 --service-cidr 172.30.0.0/16 --pod-cidr 10.128.0.0/14 --h
ost-prefix 23

## Expect

`E:` password must be at least 14 characters (ASCII-standard) without whitespaces

## Step

Attempt to create a classic STS cluster with invalid password:
`[m@fedora 15:35:01 ~]$ rosa create cluster --cluster-name mytest --create-admin-user --cluster-admin-password pa55w0rd --region us-east-1 -`
-version 4.13.5 --replicas 2 --compute-machine-type m5.xlarge --machine-cidr 10.0.0.0/16 --service-cidr 172.30.0.0/16 --pod-cidr 10.128.0.0/14 --h
ost-prefix 23

## Expect

`E:` password must be at least 14 characters (ASCII-standard) without whitespaces

# Cleanup
not needed, if any steps create a cluster despite unsupported/invalid options please open a bug and remove the clusters.
