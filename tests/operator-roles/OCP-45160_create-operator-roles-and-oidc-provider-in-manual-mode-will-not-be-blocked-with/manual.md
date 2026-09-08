# Test

## Step
Login via rosacli

## Expect

## Step
Prepare accounts on AWS via command  
$rosa create account-roles

## Expect
The accounts will be prepared successfully

## Step
Create rosa cluster with the command output by last step

## Expect

## Step
Create operator-roles via rosa with the account without enough permission  
$ rosa create operator-roles -c <clustername> --prefix <policy prefix> --mode manual -y --permissions-boundary <boundary policy>

## Expect
The roles are not created, but the 'I: Run the following commands to create the operator roles:' is shown for the user to create them manually.  
There is no ERROR prompted.

## Step
Create oidc-provider via rosa for the cluster with the account without enough permission  
$ rosa create oidc-provider -c xuelirosa4 -y

## Expect
The oidc-providers are not created, but the 'I: Run the following commands to create the OIDC provider:' is shown for the user to create them manually.  
There is no ERROR prompted.

## Step
Create the roles with the commands

## Expect
All of the roles created successfully
