# Test

## Step
Create byo oidc config then create cluster test1 with the byo oidc config by commnad

## Expect
- The cluster is created

## Step
Delete the cluster then delete the operator-roles with operator-roles prefix  
\# rosa delete operator-roles --prefix <prefix>  
NOTE: both in manual mode and auto mode

## Expect
- There are some hint message to users:  
? You are running delete operation from 'staging' environment. Please ensure there are no clusters using these operator roles in the production. Are you sure you want to proceed? (Y/n)   
? You are running delete operation from 'staging' environment. Please ensure there are no clusters using these operator roles in the production. Are you sure you want to proceed? Yes  
  
- in auto mode: The operator-roles will be deleted, if the policies are not used, they are all deleted from AWS. -- auto mode step has been automated in 60971  
- In manual mode: the commands to delete the operator-roles and policies will be prompted, and the roles and polices will be deleted with the commands.

## Step
Delete the oidc-provider with the 'oidc-config-id'  
NOTE: both in manual mode and auto mode

## Expect
- In auto mode: the oidc-provider will be deleted.  
- In manual mode: the command to delete the oidc-provider will be prompted, the oidc-provider will be deleted with the command.

## Step
Cluster two clusters with the same shared oidc-provider and operator-roles

## Expect

## Step
Delete the cluster then delete the operator-roles with operator-roles prefix  
\# rosa delete operator-roles --prefix <prefix>  
Delete the oidc-provider with the 'oidc-endpoint-url'  
NOTE: both in manual mode and auto mode

## Expect
- Same with the step 2~3  
- If the oidc-provider is used by other clusters, it will fail to delete it with erorr,  
E: There are clusters using OIDC config 'https://yw0308byocc1-oidc-t6s9.s3.us-east-2.amazonaws.com', can't delete the provider

## Step
Delete operator-roles and oidc-provider with not-exist entrance

## Expect
There will be some readable message

## Step
Check the validation for the prefix when delete oidc-provider  
- oidc-endpoint-url is with http:// scheme  
- other invalid url, like 'aaa' 'test.com'

## Expect
There should be failed with readable error message:  
E: Expected OIDC endpoint URL 'http://yw0308byocc1-oidc-t6s9.s3.us-east-2.amazonaws.com' to use an https:// scheme
