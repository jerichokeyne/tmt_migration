# Test

## Step
All deletion command need a confirmation.  
\# rosa delete account-roles   
\# rosa delete admin   
\# rosa delete cluster   
\# rosa delete idp   
\# rosa delete ingress   
\# rosa delete machinepool   
\# rosa delete ocm-role   
\# rosa delete oidc-provider   
\# rosa delete operator-roles  
\# rosa delete upgrade   
\# rosa delete user-role

## Expect

## Step
For the commands which need many parameters in the interactive mode, eg, `rosa cluster cluster`, it's better prompt the related command if the request is failed as last.

## Expect

## Step
It should prompt the parameter input again if the invalid para is input in the interactive mode  
\#rosa create account-roles   
\#rosa create admin   
\#rosa create cluster   
\#rosa create idp   
\#rosa create ingress   
\#rosa create machinepool   
\#rosa create ocm-role   
\#rosa create oidc-provider   
\#rosa create operator-roles  
\#rosa create user-role   
  
\#rosa edit addon   
\#rosa edit cluster   
\#rosa edit ingress   
\#rosa edit machinepool  
  
\#rosa install addon  
  
\#rosa revode user  
\#rosa grant user  
\# rosa upgrade cluster

## Expect

## Step
For any operation , rosacli should contain all commands for a whole workflow including creation,deletion/list/describe/edit if no design is indicated specifically.  
- machinepool  
- idp  
- upgrade  
- addon  
- ocm-role user-role account-role operator-roles oidc-provider  
- ingress  
- admin

## Expect

## Step
There should a message returning the result for all operations

## Expect

## Step
It should retry if it meets network issue during the request

## Expect

## Step
For the operation including more than one step, there should be a rollback step if it meets error in the later steps  
- rosa create admin

## Expect

## Step
There should be some wait time and retry steps when it meets condition race, for example, multi users send request at the same time

## Expect
