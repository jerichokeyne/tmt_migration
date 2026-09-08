# Test

## Step
Prepare a rosa hcp cluster

## Expect

## Step
~~try to update the billing account via rosa cli for the prepared cluster without capability allow_billing_account_change~~

## Expect
~~respond clear error message~~

## Step
~~add capability allow_billing_account_change we do not need capability after OCM-9897~~

## Expect

## Step
try to change an invalid billing account, such as 123/qweD3

## Expect
respond clear error message  
E: Provided billing account number 123 is not valid. Rerun the command with a valid billing account number

## Step
try to change with an empty billing account

## Expect
respond 200 but no value updated

## Step
try to change the billing account for the non-hcp cluster, for example, rosa classic cluster

## Expect
respond clear error message  
E: Billing accounts are only supported for Hosted Control Plane clusters

## Step
retry with interactive mode of changing an invalid billing account, such as 123/qweD3

## Expect
cannot be select and cannot continue
