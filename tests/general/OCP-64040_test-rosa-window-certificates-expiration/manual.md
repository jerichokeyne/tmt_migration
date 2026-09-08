# Setup
refer link :<https://decoder.link/sslchecker>

# Test

## Step
Check the two domains certificates expiration   
api.openshift.com:443  
sso.redhat.com:443

## Expect
It will fail if the time is shorter than 1 month  
(Open a Jira card to ask DEV update certificate for windows manually)

## Step
Check the two domains certificates and compare it with sdk repo windows certificates  
api.openshift.com:443 / sso.redhat.com:443  
<https://raw.githubusercontent.com/openshift-online/ocm-sdk-go/main/internal/system_cas_windows.go>

## Expect
It should be same   
If there is an update for the domains, it should update in ocm-sdk repo
