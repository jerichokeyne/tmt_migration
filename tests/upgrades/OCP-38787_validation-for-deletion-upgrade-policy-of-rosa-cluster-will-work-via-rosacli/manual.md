# Test

## Step
Prepare one ROSA cluster in low version

## Expect

## Step
Delete the ingress of cluster without indicated cluster Name or ID  
$ rosa delete upgrade

## Expect
Failed with error:  
Expected exactly one command line argument or flag containing the name or identifier of the cluster  
<usage>

## Step
Delete a non-existed upgrade when cluster have no scheduled policy  
$ rosa delete upgrade -c <cluster name>

## Expect
warining with:  
[xueli@xueli-work tmp]$ rosa delete upgrade -c xueli-rosa -y  
W: There are no scheduled upgrades on cluster 'xueli-rosa'

## Step
Check other options in help message should work  
--profile  
-v

## Expect

## Step
Delete with unknown flag --interactive

## Expect
It will show  
Error: unknown flag: --interactive  
<usage>
