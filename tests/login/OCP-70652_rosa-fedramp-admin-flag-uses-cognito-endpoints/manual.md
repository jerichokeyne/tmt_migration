# Setup
**
  * Tester must be FedRAMP onboarded  

  * Must be connected to FedRAMP environment using AppGate VPN   

  * Must have credentials in cognito  

  * Rosa CLI must be 1.2.24 or higher  

  * AWS Govcloud CLI access must be setup  

  * Do NOT use any proxy  

**

# Test

## Step
Ensure user can log into production environment using admin flag  
  
Capture token from  
<https://api-admin.openshiftusgov.com/auth>   
  
Log into production using the token  
rosa login --env production --govcloud --admin --token <TOKEN>

## Expect
Login should be successful and show the api-admin url:  
  
  
I: Logged in as 'ccrum' on 'https://api-admin.openshiftusgov.com'

## Step
Ensure rosa command in production is successful  
  
rosa whoami

## Expect
**AWS ARN: arn:aws-us-gov:iam::asdasd**  
AWS Account ID: asd  
AWS Default Region: us-gov-east-1  
OCM API: https://api.int.openshiftusgov.com  
OCM Account Email: asf  
OCM Account ID: asf  
OCM Account Name: TEst Test  
OCM Account Username: chad.crum@openshiftusgov.com  
OCM Organization External ID: 2222  
OCM Organization ID: asdasdasdasddsa  
OCM Organization Name: qe-idp

## Step
Ensure user can log into integration environment using admin flag  
  
Capture token from  
https://api-admin.int.openshiftusgov.com/auth  
  
Log into integration using the token  
rosa login --env integration --govcloud --admin --token <TOKEN>

## Expect
Login should be successful and show the api-admin url:  
  
  
I: Logged in as 'ccrum' on 'https://api-admin.integration.openshiftusgov.com'

## Step
Ensure rosa command in integration is successful  
  
rosa whoami

## Expect
AWS ARN: arn:aws-us-gov:iam::asdasd  
AWS Account ID: asd  
AWS Default Region: us-gov-east-1  
OCM API: https://api.int.openshiftusgov.com  
OCM Account Email: asf  
OCM Account ID: asf  
OCM Account Name: TEst Test  
OCM Account Username: chad.crum@openshiftusgov.com  
OCM Organization External ID: 2222  
OCM Organization ID: asdasdasdasddsa  
OCM Organization Name: qe-idp

## Step
Ensure user can log into stage environment using admin flag  
  
Capture token from  
https://api-admin.stage.openshiftusgov.com/auth  
  
Log into stage using the token  
rosa login --env stage --govcloud --admin --token <TOKEN>

## Expect
Login should be successful and show the api-admin url:  
  
  
I: Logged in as 'ccrum' on 'https://api-admin.stage.openshiftusgov.com'

## Step
Ensure rosa command in stage is successful  
  
rosa whoami

## Expect
AWS ARN: arn:aws-us-gov:iam::asdasd  
AWS Account ID: asd  
AWS Default Region: us-gov-east-1  
OCM API: https://api.int.openshiftusgov.com  
OCM Account Email: asf  
OCM Account ID: asf  
OCM Account Name: TEst Test  
OCM Account Username: chad.crum@openshiftusgov.com  
OCM Organization External ID: 2222  
OCM Organization ID: asdasdasdasddsa  
OCM Organization Name: qe-idp
