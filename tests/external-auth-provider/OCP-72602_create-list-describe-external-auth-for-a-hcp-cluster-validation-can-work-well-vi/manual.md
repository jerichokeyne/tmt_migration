# Test

## Step
Prepare HCP cluster with  --external-auth-providers-enabled

## Expect

## Step
Create/List external_provider to HCP cluster that external_auth_config is not enable

## Expect
it should return readable and actionable error message  
./rosa create external-auth-provider -c sdq-ci-bgzwy   
E: external authentication configuration is not enabled for cluster 'sdq-ci-bgzwy'  
Create a hosted control plane with '--external-auth-providers-enabled' parameter to enabled the configuration

## Step
Create external_provider to the cluster   
--without attribute id/issuer/issuer.audiences/issuer.url/claim one by one for external_auth request--(It will goto interactive mode)

## Expect
it should return readable and actionable error message

## Step
Create/List non HCP cluster with external_auth_config and external_auths

## Expect
it should return readable and actionable error message  
rosa create external-auth-provider -c sdq-ci-izzxi   
E: external authentication provider is only supported for Hosted Control Planes
