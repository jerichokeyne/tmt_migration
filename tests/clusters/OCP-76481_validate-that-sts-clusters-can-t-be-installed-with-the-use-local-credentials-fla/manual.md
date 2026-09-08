# Test

## Step
Attempt to create an STS cluster with the use-local-credentials flag set  
  
rosa create cluster --dry-run -c ocp-76481 --use-local-credentials --sts --mode=auto -y

## Expect
There should be an error that says:  
  
E: Local credentials are not supported for STS clusters
