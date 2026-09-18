# Setup
```json
{
"name":"xuelipri2",
"ccs":{
"enabled":true
},
"nodes":{
"availability_zones":[
"us-east-2a"
]
},
"region":{
"id":"us-east-2"
},
"aws":{
"account_id":"301721915996",
"access_key_id":"<access key>",
"secret_access_key":"<secret key>",
"private_link":true,
"subnet_ids":[
"subnet-063478a2fe60bf3f4"
]
}
}
```

# Test

## Step

Get the latest rosa cli

## Expect

## Step

Create rosa cluster with rosa cli with command with invalid private-link value
```bash
rosa create cluster -c <cluster_name> --subnets <subnets> --private-link
```

## Expect

It will fail with error message
Expected a valid private-link value

## Step

Create rosa private link cluster with 2 subnets

## Expect

It will fail with error message
To install into an existing VPC you need to ensure that your VPC is configured with
two subnets for each availability zone that you want the cluster installed into.
For PrivateLink clusters, only a private subnet per availability zone is needed.

## Step

Create private link cluster and create ingress to the cluster

## Expect

It will return error Cluster '<id>' is PrivateLink and does not support creating new ingresses

## Step

Change cluster to public

## Expect

It will return error Cluster '<id>' is PrivateLink and does not support updating ingresses
