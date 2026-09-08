# Test

## Step
Log in the moactl

## Expect

## Step
Prepare the aws config and credential with aws profiles

## Expect

## Step
Run 'rosa init' then delete the 'osdCcsAdmin' user then run 'rosa init' again

## Expect
It should fail to 'Validating SCP policies for 'osdCcsAdmin'' with bellow error message:  
E: Failed to verify permissions for user 'osdCcsAdmin': iamClient.GetUser: osdCcsAdmin  
To reset the 'NoSuchEntity: The user with name osdCcsAdmin cannot be found.  
status code: 404, request id: aaffbba4-ef0b-4f1c-9a73-35264fc5b7ec' account, run 'rosa init --delete-stack' and try again

## Step
Make some getClientDetails error during 'rosa init'

## Expect
It should fail with the bellow error message:  
E:getClientDetails: %v\n"+"Run 'rosa init' and try again

## Step
Run 'rosa init' then delete the 'osdCcsAdmin' user then try to create a cluster

## Expect
It should fail with the bellow error message:  
E:Failed to get access keys for user <aws.AdminUserName>: <err>\n"

## Step
Make sure that there is no AWS credential configed and run 'rosa init'

## Expect
\# rosa init  
E: Error creating AWS client: Failed to find credentials. Check your AWS configuration and try again

## Step
Try to run init with bellow:  
1. no oc client  
2. no aws client  
3. no credential  
4. no config  
5. invalid credential  
6.invalid config  
7.too low version oc client

## Expect
There should be some error message to hint
