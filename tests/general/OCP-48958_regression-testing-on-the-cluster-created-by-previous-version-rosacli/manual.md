# Test

## Step
Log in with the rosa cli of the previous version, then create an advanced rosa cluster and wait it ready.  
NOTE: It needs to cover n-1 and n-2 version rosacli at least

## Expect

## Step
Have a smoke test including bellow actions with the latest version rosacli.  

  * Create resources
  * Delete resources
  * Upgrade cluster
  * Edit resources

## Expect
It should work well

## Step
Repeat step1~2 on STS cluster.

## Expect
It should work well

## Step
Create 4.10.x sts cluster via the rosacli of the version lower than v1.1.11  
NOTE: This case needs cover all rosacli version lower than v1.1.11

## Expect
It should fail with bellow error message.  
E: Failed to create cluster: Creating STS clusters on OpenShift openshift-v4.10.0-candidate requires ROSA 1.1.10 or higher. Go to https://console.redhat.com/openshift/downloads#tool-rosa to download the latest version.

## Step
Check if it uses cloudfront to create the OIDC with the rosacli version >= 1.2.7 when create STS cluster

## Expect
- The OIDC provider should use cloudFront, the OIDC endpoint URL should contain 'cloudfront.net' if rosacli veriosn is >=1.2.7 version and login with the account which org enable the 'oidc-s3-cloudfront' toggle -  
- If not, The OIDC provider should NOT use cloudFront, the OIDC endpoint URL should contain 'rh-oidc'  
From OCM-1540, new url DNS CNAMES should be in the url:  

  * [oidc.op1.openshiftapps.com](<http://oidc.op1.openshiftapps.com/> "Follow link") -> dvbwgdztaeq9o.cloudfront.net
  * [oidc.os1.devshift.org](<http://oidc.os1.devshift.org/> "Follow link") -> d3gt1gce2zmg3d.cloudfront.net
  * [oidc.oi1.devshift.org](<http://oidc.is1.devshift.org/> "Follow link") -> d1b0cha94ris3q.cloudfront.net
