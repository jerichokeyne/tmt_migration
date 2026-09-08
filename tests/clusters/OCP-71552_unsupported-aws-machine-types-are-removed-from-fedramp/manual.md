# Test

## Step
Run the following command to get a list of available machine types. This command purposefully triggers and error to get the machine list.  
  
**Note:** --subnet-ids must be a valid subnet or the command will fail without showing the list of available machines.  
  
`rosa create cluster -y --compute-machine-type asdasd --cluster-name test --region us-gov-east-1 `--version 4.13.19 --subnet-ids=**$PRIVATE_SUBNET** --private-link --machine-cidr=10.0.0.0/16 --sts 2>&1 >/dev/null | grep 'Available machine type list' | tr " " "\n" | sort

## Expect
List of available machine types  
  
[truncated]  
i3.16xlarge  
i3.2xlarge  
i3.4xlarge  
i3.8xlarge  
i3en.12xlarge  
i3en.24xlarge  
i3en.2xlarge  
i3en.3xlarge  
i3en.6xlarge  
i3en.metal  
i3en.xlarge  
i3.metal  
i3.xlarge  
m5d.12xlarge  
m5d.16xlarge  
[truncated]

## Step
None of the machines from [this MR](<https://gitlab.cee.redhat.com/service/uhc-clusters-service/-/merge_requests/6542/diffs#3afdc0a6237091a324595731bdf48bf1f5ee08c5>) (also listed below) should be in the list of machines identified in the previous step.   
  
  
Full list of machines which are NOT supported:  
c5ad.12xlarge  
c5ad.16xlarge  
c5ad.24xlarge  
c5ad.2xlarge  
c5ad.4xlarge  
c5ad.8xlarge  
c5ad.xlarge  
c6a.12xlarge  
c6a.16xlarge  
c6a.24xlarge  
c6a.2xlarge  
c6a.32xlarge  
c6a.4xlarge  
c6a.8xlarge  
c6a.xlarge  
dl1.24xlarge  
g5.12xlarge  
g5.16xlarge  
g5.24xlarge  
g5.2xlarge  
g5.48xlarge  
g5.4xlarge  
g5.8xlarge  
g5.xlarge  
m5zn.12xlarge  
m5zn.2xlarge  
m5zn.3xlarge  
m5zn.6xlarge  
m5zn.metal  
m5zn.xlarge  
m6a.12xlarge  
m6a.16xlarge  
m6a.24xlarge  
m6a.2xlarge  
m6a.32xlarge  
m6a.48xlarge  
m6a.4xlarge  
m6a.8xlarge  
m6a.metal  
m6a.xlarge  
r5b.12xlarge  
r5b.16xlarge  
r5b.24xlarge  
r5b.2xlarge  
r5b.4xlarge  
r5b.8xlarge  
r5b.metal  
r5b.xlarge  
r6a.12xlarge  
r6a.16xlarge  
r6a.24xlarge  
r6a.2xlarge  
r6a.32xlarge  
r6a.48xlarge  
r6a.4xlarge  
r6a.8xlarge  
r6a.xlarge  
u-12tb1.metal  
u-18tb1.metal  
u-24tb1.metal  
u-6tb1.metal  
u-9tb1.metal  
x2iezn.12xlarge  
x2iezn.2xlarge  
x2iezn.4xlarge  
x2iezn.6xlarge  
x2iezn.8xlarge  
x2iezn.metal  
z1d.12xlarge  
z1d.2xlarge  
z1d.3xlarge  
z1d.6xlarge  
z1d.metal  
z1d.xlarge

## Expect
rosa cli command that outputs available machine types should not include any unsupported types.
