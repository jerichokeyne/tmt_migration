# Test

## Step
Create HCP cluster with invalid --no-cni value

## Expect
It should return with error message

## Step
Create classic cluster with --no-cni

## Expect
It should return with error message

## Step
Create HCP cluster with --no-cni and "--network-type={OVNKubernetes, OpenshiftSDN}" (hidden para) at same time

## Expect
It should return with error message

## Step
Create HCP cluster with --no-cni and --network-type=OVNKubernetes

## Expect
It should return with error message
