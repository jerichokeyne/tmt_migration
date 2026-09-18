# Test

## Step

Log in with the rosa tool

## Expect

## Step

~~Check the help info for 'rosa create cluster-h'~~

## Expect

~~There is the help info for 'channel-group'. --channel-group string Channel group is the name of the group where this image belongs, for example "stable" or "fast". (default "stable")'~~

## Step

Try to create MOA cluster with setting --channel-group

## Expect

The default 'stable' channel should be used

## Step

Try to create MOA cluster with version matched the channel-group

## Expect

The cluster should be create successfully

## Step

Try to create MOA cluster with version not in the channel-group

## Expect

It should be failed to create the cluster.
```bash
rosa create cluster --cluster-name=yuwan-test-0929-m1 --version=v4.6.0-0.nightly-2020-09-25-150713-nightly
```
```
E: Expected a valid OpenShift version: A valid version number must be specified
Valid versions: 4.5.11 4.3.25 4.4.11 4.4.16
```
