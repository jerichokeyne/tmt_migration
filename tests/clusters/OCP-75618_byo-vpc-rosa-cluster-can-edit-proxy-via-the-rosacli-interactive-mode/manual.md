# Test

## Step
**Repeat all above steps of OCP-46308 via the interactive mode**

## Expect
The proxy options are prompted.  
The clusters should be updated successfully.  
\# ./rosa edit cluster -c 1omvtrv71ir13i1idugj5el76b8cliac -i  
I: Interactive mode enabled.  
Any optional fields can be ignored and will not be updated.  
? Private cluster (optional): No  
? Disable Workload monitoring (optional): No  
? Update cluster-wide proxy (optional): Yes  
? To remove any existing cluster-wide proxy value or an existing additional-trust-bundle value, enter a set of double quotes ("")  
? HTTP proxy: http://x1x.com  
? HTTPS proxy: https://y2y.com  
?No proxy:test.com  
? Update additional trust bundle (optional): No  
I: Updated cluster '1omvtrv71ir13i1idugj5el76b8cliac'  
  
Existing issue:  
OCPBUGS-37792

## Step
**Check the proxy is works.**  
NOTE:Follow the steps of OCP-75616

## Expect
The proxy is working.
