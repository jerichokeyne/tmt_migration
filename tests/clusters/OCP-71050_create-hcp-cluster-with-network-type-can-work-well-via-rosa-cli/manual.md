# Test

## Step

Check cluster create cluster help information
./rosa create cluster --help

## Expect

-There is 'no-cni' flag
...
--no-cni Disable CNI creation to let users bring their own CNI.
...

~~EDIT: Since CLI 1.2.35, `no-cni` is hidden.<https://issues.redhat.com/browse/OCM-6120>~~

## Step

Create ROSA HCP cluster with --no-cni

## Expect

-The cluster can be created successfully
-The flag is in the created cluster command

## Step

Describe the cluster
```bash
rosa describe cluster -c <>
```

## Expect

-The Network type should be Other

## Step

E2E test can refer to
<https://hypershift-docs.netlify.app/how-to/aws/other-sdn-providers/#cilium>

## Expect

## Step

Create cluster with flag
--no-cni=false
--no-cni=true

## Expect

-If --no-cni=false, the network type is 'OVNKubernetes'
-If --no-cni-true, the network type is 'Other'
