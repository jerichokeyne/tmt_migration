# Test

## Step
Prepare one ROSA cluster

## Expect

## Step
Delete the ingress of cluster without indicated cluster Name or ID  
$ rosa delete ingress  
$ rosa delete ingress -c <cluster name>

## Expect
Failed with error:  
Expected exactly one command line argument or flag containing the name or identifier of the cluster  
<usage>

## Step
Delete a non-existed ingress  
$ rosa delete ingress <non existed> -c <cluster name>

## Expect
Failed with error:  
Failed to delete ingress 'xueli-rosa2': There is no ingress with identifier or name 'xueli-rosa2'

## Step
Delete with invalid ingress id  
$ rosa delete ingress p3s7aaa -c xueli-rosa

## Expect
Failed with error:  
Ingress identifier 'p3s7aaa' isn't valid: it must contain only four letters or digits

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
