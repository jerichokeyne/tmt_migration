# Test

## Step
1.Create HCP cluster

## Expect
cluster is created

## Step
2.check for root principal available in cluster:  
ocm get /api/clusters_mgmt/v1/clusters/2n2cco1fo9e12kcisu77l89h4bs77f7l/resources/live | grep additional

## Expect
root principal is visible  
{\"aws\":{\"additionalAllowedPrincipals\":[\"arn:aws:iam::644306948063:root\"

## Step
3.Try to duplicate root principal via live resources

## Expect
it should fail, as no duplicate is allowed

## Step
4.check for root principal still available in cluster:  
ocm get /api/clusters_mgmt/v1/clusters/2n2cco1fo9e12kcisu77l89h4bs77f7l/resources/live | grep additional

## Expect
