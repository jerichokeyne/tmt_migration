# Test

## Step

Log in with the rosa tool

## Expect

## Step

Check the help info for 'rosa create cluster-h'

## Expect

There is the help info for '--disable-scp-checks'.
--disable-scp-checks Indicates if cloud permission checks are disabled when attempting installation of the cluster.

## Step

Try to create a MOA cluster with the --disable-scp-checks flag

## Expect

The cluster is created successfully

## Step

Check if the --disable-scp-checks flag works.
run the bellow command:
zhewang@fedora:~$ rosa describe cluster -c <cluster_id> -o yaml

## Expect

There should be:
disable_scp_checks: true

## Step

Create another cluster without the --disable-scp-checks flag and repeat the previous step.

## Expect

There should be:
disable_scp_checks: false
