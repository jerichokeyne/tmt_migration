# Setup
{
      "name": "testoct27",
      "flavour": {
        "id": "osd-4"
      },
      "nodes": {
        "compute": 3,
        "availability_zones": ["us-west-1a"]
      },
      "region": {
        "id": "us-west-1"
      },
      "ccs": {
        "enabled": true
      },
      "aws": {
        "account_id": "765374464689",
        "access_key_id": "<key>",
        "secret_access_key": "<secret>",
        "subnet_ids": ["<subnet_id>", "<subnet_id>"]
      },
      "version": {
        "id": "openshift-v4.5.13"
      },
      "managed": true
    }

# Test

## Step
Login with the ROSA cluster and check the help message of the 'rosa create cluster -h'

## Expect
There is the help info of the '--subnet-ids' as bellow  
--subnet-ids strings The Subnet IDs to use when installing the cluster. SubnetIDs should come in pairs; two per availability zone, one private and one public. Subnets are comma separated, for example: --subnet-ids=subnet-1,subnet-2.Leave empty for installer provisioned subnet IDs.

## Step
Prepare two valid subnet on AWS in same VPC

## Expect
The subnet should be created successfully

## Step
Create a single-az cluster with the interactive mode

## Expect
1. There is an option of"? Install into an existing VPC (optional): [? for help] (y/N) "  
2. There is a list of subnets on the region and users can choose them.  
? Subnet IDs (optional): [Use arrows to move, space to select, <right> to all, <left> to none, type to filter, ? for more help]  
[ ] subnet-0273e91d7332e2959 (us-east-2b)  
[ ] subnet-0e59f003e06cb4f28 (us-east-2c)  
> [ ] subnet-09011bb53c4504103 (us-east-2b)  
[ ] subnet-03046269bf8a09a34 (us-east-2a)  
[ ] subnet-00b6c352e8dec7bdd (us-east-2b)  
[ ] subnet-0a33f39dafe5da257 (us-east-2b)  
[ ] subnet-06637939383184340 (us-east-2a)  
  
3. The cluster should be created successfully

## Step
Wait for cluster ready and do some check:  
1.Launch cluster console and check the node IPs  
2.Launch HIVE to checkthe install-config secret

## Expect
- All of the nodes should be in the subnet CIDR blocks  
- Check that the install-config secret contains the subnets under the "Subnets" field.

## Step
Scale up the cluster and check the nodes IPs

## Expect
- The cluster should can be scale up successfully  
- The new created nodes should be in the subnet CIDR block

## Step
Create machine pool to the cluster

## Expect
- The machine pool can be created successfully  
- The new created nodes should be in the subnet CIDR block

## Step
Prepare another 6 subnets

## Expect

## Step
Create another multi_az cluster with the subnets with the interactive mode

## Expect
The result should be same with the one in step 3

## Step
Repeat setp 4~6

## Expect
The result should be same with the above ones

## Step
Delete the first cluster in step 3,Wait for a moment and launch AWS to check

## Expect
- Cluster will be deleted successfully from OCM in 1 hour  
- All of the nodes related to the cluster is deleted  
- The subnet won't be affected  
- The Multi_az cluster won't be affected

## Step
Repeat step 3 and step 8 with the cli command.  
\# rosa create cluster --cluster-name yuwan-1130-sm1 --multi-az --subnet-ids a,b,c,d,r,f  
\# rosa create cluster --cluster-name yuwan-1130-sm2 --subnet-ids a,b

## Expect
The result should be same with the above ones

## Step
Repeat all above steps on different OS

## Expect
The result should be same with the above ones
