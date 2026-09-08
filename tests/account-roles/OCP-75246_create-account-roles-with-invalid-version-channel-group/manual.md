# Test

## Step
Log in via rosa-cli using the command <<rosa login>>  
Note: It is recommended that you use the SDQE rosa account as your personal one may not have channel-groups enabled

## Expect
rosa login  
To login to your Red Hat account, get an offline access token at https://console.redhat.com/openshift/token/rosa  
I: Logged in as 'sdqe-rosa' on 'https://api.openshift.com'

## Step
Check the validation for the version flag when creating account-roles:  
- invalid version 4.20  
- invalid channel-group, fakecg  
- invalid format of the version, 4.11.1.(Only support x.y)

## Expect
It should fail with error message.  
E: Error getting version: a valid version number must be specified  
Valid versions: [4.8, 4.7, 4.11, 4.10, 4.9]  
  
E: Error getting version: could not find versions for the provided channel-group: 'fakecg'  
  
E: Error getting version: A valid policy version number must be specified  
Valid versions: [4.10, 4.11, 4.12, 4.13, 4.14]
