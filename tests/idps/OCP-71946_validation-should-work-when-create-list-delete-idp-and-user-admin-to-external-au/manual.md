# Test

## Step
Prepare HCP cluster with  --external-auth-providers-enabled  
Then do below actions  
rosa create/delete/ admin -c <cluster_name>  
rosa create/delete idp -c <cluster_name>  
rosa list idps -c <cluster_name>  
rosa list user -c <cluster_name>

## Expect
It will return clear and readable error message
