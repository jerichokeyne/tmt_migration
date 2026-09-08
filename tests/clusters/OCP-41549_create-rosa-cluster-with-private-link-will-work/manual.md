# Setup
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

# Test

## Step
Get the latest rosa cli

## Expect

## Step
Create rosa cluster with rosa cli with command  
$ rosa create cluster -c <cluster_name> --subnet-ids <subnets> --private-link

## Expect
The cluster will be created successfully

## Step
Describe the cluster

## Expect
The cluster detail will show the private-link:true

## Step
Create another rosa cluster with interactive mode

## Expect
There should be private link and subnets options in the interactive mode

## Step
Describe the cluster

## Expect
The private_link and subnet should be described in cluster detail

## Step
Wait for cluster ready

## Expect
Cluster will be ready in 2 hours

## Step
Launch cluster console

## Expect
Cluster console will not be reached due to the private cluster
