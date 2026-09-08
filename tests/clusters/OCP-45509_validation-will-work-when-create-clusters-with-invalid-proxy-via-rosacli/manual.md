# Test

## Step
Assign label `capability.organization.create_cluster_proxy to the organization used for proxy testing`

## Expect

## Step
Login via rosacli

## Expect

## Step
Create rosa cluster which has proxy with no existing vpc set by command

## Expect
It will return error with message  
`Cluster-wide proxy is only supported for BYO-VPC clusters`

## Step
Create ccs existing cluster with invalid http_proxy set  
\# rosa create cluster --cluster-name yw-1029-t1 --region us-east-2 --version 4.8.14 --compute-nodes 2 --machine-cidr 10.0.0.0/16 --service-cidr 172.30.0.0/16 --pod-cidr 10.128.0.0/14 --host-prefix 23 --subnet-ids subnet-0c518f8745554ad64,subnet-0c2da2f8b694f6729 --additional-trust-bundle-file /root/workplace/rosa/additional_trust_bundle.ca --region us-east-1 --http_proxy "aaavvv"

## Expect
It will return error with message  
`Invalid 'proxy.http_proxy' attribute`

## Step
Create ccs existing cluster with invalid http_proxy not started with http  
\# rosa create cluster --cluster-name yw-1029-t1 --region us-east-2 --version 4.8.14 --compute-nodes 2 --machine-cidr 10.0.0.0/16 --service-cidr 172.30.0.0/16 --pod-cidr 10.128.0.0/14 --host-prefix 23 --subnet-ids subnet-0c518f8745554ad64,subnet-0c2da2f8b694f6729 --additional-trust-bundle-file /root/workplace/rosa/additional_trust_bundle.ca --region us-east-1 --http_proxy "https://aaavvv.test.nohttp.com"

## Expect
It will return error with message  
`Attribute 'proxy.http_proxy'` `prefix is not 'http'`

## Step
Create ccs existing cluster with invalid https_proxy set  
\# rosa create cluster --cluster-name yw-1029-t1 --region us-east-2 --version 4.8.14 --compute-nodes 2 --machine-cidr 10.0.0.0/16 --service-cidr 172.30.0.0/16 --pod-cidr 10.128.0.0/14 --host-prefix 23 --subnet-ids subnet-0c518f8745554ad64,subnet-0c2da2f8b694f6729 --additional-trust-bundle-file /root/workplace/rosa/additional_trust_bundle.ca --region us-east-1 --https_proxy="aaavvv"

## Expect
It will return error with message  
`Invalid 'proxy.https_proxy' attribute '%s'`

## Step
Create wide-proxy cluster with invalid additional_trust_bundle set

## Expect
It will return error with message  
`Failed to parse additional_trust_bundle`

## Step
Create wide-proxy cluster with invalid additional_trust_bundle set path

## Expect
It should fail with some error message, like 'no such file or directory'

## Step
Create wide-proxy cluster with no_proxy set  
1.no http/https proxy+no-proxy  
2.http/https proxy + no_proxy: "*"

## Expect
It will return error with message

## Step
Repeat all above steps in the interactive mode

## Expect
the result should be same with the above ones
