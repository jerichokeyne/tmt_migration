# Setup
<https://docs.google.com/document/d/1HaEaQKzzQqNMiPxovnYWasLB2yVjHnsfSIs1q8BWD2Q/edit>

# Test

## Step
Prepare a HCP cluster with 
    
    --external-auth-providers-enabled

## Expect

## Step
Create external-auth-provider in the interactive mode.  
\#rosa create external-auth-provider -c <clusrer_id>  
\#rosa create external-auth-provider -c <clusrer_id> -i  
  
\#type ? to check the help message  
  
\#Input invalid value

## Expect
-It will go into interactive mode and ask for input  
-The external auth provider should be created successfully and work well.  
-The help message in the interactive should be correct.  
-All properties that are not required are followed by the optional tag  
-If input invalid value, it will prompt error message  
-There will be default value for group and username Claim mapping  
  
./rosa create external-auth-provider -c sdq-ci-poras   
I: Enabling interactive mode  
? Name: test  
? Issuer audiences: 123456789  
X Sorry, your reply was invalid: parse "~!": invalid URI for request  
? The serving url of the token issuer: https://login.microsoftonline.com/fa5d3dd8-b8ec-4407-a55c-ced639f1c8c5/v2.0  
? CA file path (optional):   
X Sorry, your reply was invalid: Value is required  
? Claim mapping username: email  
? Claim mapping groups: group1  
? Claim validation rule (optional):   
? Console client id (optional):   
I: Successfully created an external authentication provider for cluster '2a3beqcih252218o1mqgudi0o63491f6'

## Step
Delete external-auth-provider in the interactive mode.

## Expect
It will go into interactive mode and confirm if delete  
/rosa delete external-auth-provider test -c sdq-ci-izzxi   
? Are you sure you want to delete external authentication provider test on cluster sdq-ci-izzxi? (y/N)
