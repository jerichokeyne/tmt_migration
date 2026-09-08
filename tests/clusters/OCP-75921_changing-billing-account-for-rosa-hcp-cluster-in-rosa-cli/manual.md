# Test

## Step
~~Prepare a org with capability allow_billing_account_change~~

## Expect

## Step
Prepare a rosa hcp cluster

## Expect

## Step
update billing account for the cluster via rosa cli  
./rosa edit cluster -c 29poabi7ve8hc2ndogv2lccrspoib6ne --billing-account xxx

## Expect
success

## Step
check the billing acccount in `rosa describe cluster`

## Expect
the billing account set as changed value

## Step
~~check the billing accounts in cluster and subscription endpoint~~

## Expect
~~the billing account set as changed value~~

## Step
~~check the billing accounts in subscription reserved resources endpoint~~

## Expect
~~the billing account set as changed value~~

## Step
~~check the service log of the cluster~~

## Expect
~~a new service_logs item generated, description like "Billing account has been updated to 'xxx'"~~

## Step
create a new node pool

## Expect
success

## Step
retry with interactive mode

## Expect
same with above  
all of the billing accounts which are bound with the org can be listed for selection  
  
./rosa edit cluster -c xxx -i  
I: Interactive mode enabled.  
Any optional fields can be ignored and will not be updated.  
? Private cluster, check this command's help for possible impacts: No  
? Disable Workload monitoring: Yes  
? Update cluster-wide proxy: No  
? Update additional trust bundle: No  
? Update additional allowed principals: No  
? Update existing audit log forwarding role 'arn:aws:iam::301721915996:role/sdq-ci-dmjvc': No  
? Disable Audit Log: No  
? Enable registries config: No  
? Enable cluster deletion protection: No  
? Update billing account (current = '301721915996'): 361660083367  
I: The AWS billing account you selected is different from your AWS infrastructure account. The AWS billing account will be charged for subscription usage. The AWS infrastructure account contains the ROSA infrastructure.  
I: Updated cluster '29poabi7ve8hc2ndogv2lccrspoib6ne'
