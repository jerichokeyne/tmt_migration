# Test

## Step
Create/list/revoke break-glass-credential to non-HCP cluster

## Expect
It returns error message  
./rosa create break-glass-credential -c sdq-ci-longname-tgrbgcmxcjxsyyjtswqzwtaytnmetzxtnimoqu   
E: external authentication provider is only supported for Hosted Control Planes

## Step
Create/list/revoke break-glass-credential to external-auth-providers-enabled not enable

## Expect
It returns error message  
./rosa create break-glass-credential -c aaraj-hcp   
E: External authentication configuration is not enabled for cluster 'aaraj-hcp'  
Create a hosted control plane with '--external-auth-providers-enabled' parameter to enabled the configuration

## Step
Create break-glass-credential with invalid --username and --expiration

## Expect
It returns error message

## Step
Create break-glass-credential with --expiration is less than 10min

## Expect
It returns error message  
./rosa create break-glass-credential --expiration="1s" --username="" -c sdq-ci-bzoci  
E: failed to create a break glass credential for cluster 'sdq-ci-bzoci': Expiration needs to be at least 10 minutes from now
