# Setup
**
  * Tester must be FedRAMP onboarded  

  * Must be connected to FedRAMP environment using AppGate VPN   

  * Rosa CLI must be 1.2.24 or higher  

  * AWS Govcloud CLI access must be setup  

  * Do NOT use any proxy  

**

# Test

## Step
Rosa can log into an environment using a non-aliased endpoint  
  
Browse to production environment and get token  
https://console.openshiftusgov.com/openshift/token  
  
Use token with non-aliased endpoint  
rosa login --govcloud \  
--env https://api.openshiftusgov.com \  
--token-url https://sso.openshiftusgov.com/realms/redhat-external/protocol/openid-connect/token \  
--token $TOKEN \  
--client-id console-dot --region us-gov-east-1  
  
Note: https://api-temp.openshiftusgov.com will switch to https://api.openshiftusgov.com after migration on Jan 17 2024

## Expect
Login should be successful:  
  
  
II: Logged in as 'chad.crum@openshiftusgov.com' on 'https://api-temp.openshiftusgov.com'

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
