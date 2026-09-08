# Test

## Step
Check the validations  
- No NON-BYO VPC cluster  
- No role-arn is set  
- cluster id doesn't exist

## Expect
- E: No subnets on cluster  
- E: role-arn is required  
- E: Error verifying subnets: The subnet ID 'subnet-03046a9b92b5014fb' does not exist  
  
- E: Failed to get cluster 'yuwan-j5hp2-j6r5': There is no cluster with identifier or name 'yuwan-j5hp2-j6r5'

## Step
Check the network for cluster with invalid tags

## Expect
It should return error message  
[yingzhan@localhost rosa]$ ./rosa verify network -c sdq-ci-ngdrb --tags aa=bb  
I: Verifying the following subnet IDs are configured correctly: [subnet-0829f6ddbab53bc0c subnet-005a1e3e4d3586893 subnet-052827033925f9f91 subnet-04b1e06f6f3cf0da7 subnet-018dbeca35a828d07 subnet-01acf1800fcef659a]  
E: invalid tag format for tag '[aa=bb]'. Expected tag format: 'key:value'

## Step
Check the network for cluster with --hosted-cp

## Expect
It should return error message  
./rosa verify network -c sdq-ci-fjfer --hosted-cp  
I: Verifying the following subnet IDs are configured correctly: [subnet-0461e28d37d13fa0f subnet-08d21d7b3efe40d6f subnet-0d0c82ce04b761d46 subnet-0045a2f7711cb6368 subnet-07b418826c7ea969b subnet-0473de62a7e215ffb]  
E: '--hosted-cp' flag is not required when running the network verifier with cluster

## Step
- The subnet ids don't exist  
- The role-arn doesn't exist  
- The role arn without enough permission or trust relationship  
- Cluster is in waiting/validating/pending/uninstalling state

## Expect
- readable error message  
- readable error message  
- readable error message
