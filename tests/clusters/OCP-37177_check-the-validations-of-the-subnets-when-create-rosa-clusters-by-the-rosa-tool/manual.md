# Setup
```json
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
```

# Test

## Step

Login with the rosa tool

## Expect

## Step

Create cluster with non-existed subnets on AWS
\#rosa create cluster --cluster-name yuwan-1130-sm3 --subnet-ids a,b

## Expect

It should fail to create the cluster with some readable error message
```
E: Failed to create cluster: The total number of subnets received does not match 2 per zone as require
```

## Step

Create cluster with subnets not existed on current region

## Expect

It should fail to create the cluster with some readable error message
```
E: Failed to create cluster: The total number of subnets received does not match 2 per zone as require
```

## Step

Create multi_az cluster with subnet which only support 1 zone

## Expect

It should fail to create the cluster with some readable error message
```
E: Failed to create cluster: The total number of subnets received does not match 2 per zone as require
```

## Step

Create single_az cluster with 1 subnet set

## Expect

It should fail to create the cluster with some readable error message

    2 subnet ids should be specified for a Single AZ cluster, instead found: 1

## Step

Create single_az cluster with 3 subnet set

## Expect

It should return 400 with readable error message

    "2 subnet ids should be specified for a Single AZ cluster, instead found: 3

## Step

Create single_az cluster with multiple zones set

## Expect

It should return 400 with readable error message

    "Only a single availability zone can be provided to a single-availability-zone cluster, instead received 3

## Step

Create multi_az cluster with 5 subnet set

## Expect

It should return 400 with readable error message

    6 subnet ids should be specified for a Multi AZ cluster, instead found: 5

## Step

Create multi_az cluster with 7 subnet set

## Expect

It should return 400 with readable error message

    6 subnet ids should be specified for a Multi AZ cluster, instead found: 7

## Step

Create multi_az cluster with only 1 zone set

## Expect

It should return 400 with readable error message

    The number of Availability Zones for a Multi AZ cluster should be 3, instead received:

## Step

Create with duplicate zones
\#rosa create cluster --cluster-name yuwan-1130-sm3 --subnet-ids a,a

## Expect

Found duplicate Availability Zone: us-east-2a

## Step

Repeat all above steps on different OSs

## Expect

The result should be same with the above ones
