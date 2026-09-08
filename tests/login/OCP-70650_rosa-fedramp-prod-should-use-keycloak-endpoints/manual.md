# Setup
**
  * Tester must be FedRAMP onboarded  

  * Rosa CLI must be 1.2.33 or higher  

  * AWS Govcloud CLI access must be setup  

  * Do NOT use any proxy  

**

# Test

## Step
Rosa client uses FedRAMP keycloak endpoints when connecting to FedRAMP production environment  
  
Browse to production environment and get token  
https://console.openshiftusgov.com/openshift/token  
  
Use token with non-aliased endpoint  
rosa login --govcloud --token <token>

## Expect
**Login should be successful:  
  
**  
II: Logged in as 'chad.crum@openshiftusgov.com' on 'https://api.openshiftusgov.com'

## Step
Ensure rosa command is successful  
  
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
