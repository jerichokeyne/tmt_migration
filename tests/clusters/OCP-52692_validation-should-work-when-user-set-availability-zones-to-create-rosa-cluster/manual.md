# Test

## Step

Create cluster with the zone not available in the region
[xueli@xueli-work rosa]$ rosa create cluster --availability-zones us-east-2e -c xuelirosa

## Expect

There should be error returned
zhewang@fedora:~$ rosa create cluster --availability-zones us-east-2e -c xuelirosa
```
W: In a future release STS will be the default mode.
W: --sts flag won't be necessary if you wish to use STS.
W: --non-sts/--mint-mode flag will be necessary if you do not wish to use STS.
E: Expected a valid availability zone, 'us-east-2e' doesn't belong to region 'us-east-2' availability zones
```

## Step

Create cluster with zones not match region

```bash
rosa create cluster --availability-zones us-west-2b -c xuelirosa --region us-east-2
```

## Expect

zhewang@fedora:~$ rosa create cluster --availability-zones us-west-2b -c xuelirosa --region us-east-2
```
W: In a future release STS will be the default mode.
W: --sts flag won't be necessary if you wish to use STS.
W: --non-sts/--mint-mode flag will be necessary if you do not wish to use STS.
E: Expected a valid availability zone, 'us-west-2b' doesn't belong to region 'us-east-2' availability zones
```

## Step

Create cluster with dup zones set
```bash
rosa create cluster --availability-zones us-west-2b,us-west-2b,us-west-2b -c xuelirosa --region us-west-2
```

## Expect

zhewang@fedora:~$ rosa create cluster --availability-zones us-west-2b,us-west-2b,us-west-2b -c xuelirosa --region us-west-2
```
W: In a future release STS will be the default mode.
W: --sts flag won't be necessary if you wish to use STS.
W: --non-sts/--mint-mode flag will be necessary if you do not wish to use STS.
E: status is 400, identifier is '400', code is 'CLUSTERS-MGMT-400' and operation identifier is '41ef4eee-3fd4-4ee4-b9a1-308f93ca0688': Found duplicate Availability Zone: us-west-2b
```

## Step

Create cluster with both zone and subnet set

## Expect

There will be error shows that zone and subnet cannot be set at same time, cluster will be created according to the subnet
[xueli@xueli-work rosa]$ rosa create cluster --availability-zones us-west-2b -c xuelirosa --multi-az --subnet-ids subnet-039f2a2a2d2d83e7f
```
E: Setting availability zones is not supported for BYO VPC. ROSA autodetects availability zones from subnet IDs provided
I: Creating cluster 'xuelirosa'
I: To view a list of clusters and their status, run 'rosa list clusters'
```
