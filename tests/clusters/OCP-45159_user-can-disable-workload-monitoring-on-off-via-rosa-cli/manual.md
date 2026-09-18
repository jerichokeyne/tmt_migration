# Test

## Step

Log in via rosacli

## Expect

## Step

Create a cluster with
`--disable-workload-monitoring option`

## Expect

- The cluster will be created successfully
- There is 'User Workload Monitoring: disabled' in the cluster description

## Step

Wait until the cluster DNS ready or have a cluster uuid

## Expect

## Step

Launch HIVE according to steps [How to access to the Second HIVE of OCM](<https://docs.google.com/document/d/1EDFE_azzoMxpDxWF2cROUNSAzmWO2etxCR5ckNbtLic/edit>)

## Expect

## Step

Check the clusterdeployment

## Expect

- There will be label `ext-managed.openshift.io/uwm-disabled:true`

## Step

Wait until cluster is ready

## Expect

## Step

Launch cluster console

## Expect

When check the configmap/cluster-monitoring-config There will be not
data:
config.yaml: "enableUserWorkload: true

## Step

Launch HIVE and check clusterdeployment

## Expect

- There will be label `ext-managed.openshift.io/uwm-disabled:true`

## Step

From OCM-18528, edit UWM should fail on hosted-cp cluster

## Expect

```
E: User Workload Monitoring configuration is not supported for Hosted Control Plane clusters
```
