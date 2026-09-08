# Test

## Step
Prepare one BYOC-OIDC STS/hosted-cp cluster

## Expect

## Step
Create some iamserviceaccount

## Expect

## Step
Delete iamserviceaccount in the interactive mode

## Expect
- It will ask "? Service account name" ,"? Namespace:" and "? IAM service account role deletion mode:"   
  
% ./rosa delete iamserviceaccount -c 2l3pivkhljpenrod2lm1hcmp19vhq3ke -i  
? Service account name: test-iamsa1  
? Namespace: testns  
? IAM service account role deletion mode: auto  
I: Role details:  
Name: jkeyne-0904-31-testns-test-iamsa1-role  
ARN: arn:aws:iam::090777400063:role/aa/cc/jkeyne-0904-31-testns-test-iamsa1-role  
Service Account: testns/test-iamsa1  
Attached Policies: 2  
- arn:aws:iam::090777400063:policy/yuwan-test-policy  
- arn:aws:iam::090777400063:policy/yuwan-test-policy2  
? Delete IAM role 'jkeyne-0904-31-testns-test-iamsa1-role' and all associated policies? Yes  
I: Successfully deleted IAM service account role 'jkeyne-0904-31-testns-test-iamsa1-role'  
  
  
- The iamserviceaccount can be successful to delete with auto and manual mode  
  
- If the command contains --role-name, there will be "? IAM role name" promoted
