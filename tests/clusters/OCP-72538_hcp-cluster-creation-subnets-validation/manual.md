# Test

## Step

(dry-run) Create a public cluster with 1 private subnet and 1 public subnet

## Expect

It should succeed

>rosa create cluster --cluster-name tr-ocm6253 [...] --dry-run --subnet-ids <private-subnet-az1>,<public-subnet>
[...]
**I: Creating cluster 'tr-ocm6253' should succeed. Run without the '--dry-run' flag to create the cluster.**

## Step

(dry-run) Create a public cluster with 3 private subnets and 1 public subnet

## Expect

It should succeed

>rosa create cluster --cluster-name tr-ocm6253 [...] --dry-run --subnet-ids <private-subnet-az1>,<private-subnet-az2>,<private-subnet-az3>,<public-subnet>
[...]
**I: Creating cluster 'tr-ocm6253' should succeed. Run without the '--dry-run' flag to create the cluster.**

## Step

(dry-run) Create a public cluster with 2 private subnets from same AZ and 1 public subnet

## Expect

It should fail

>rosa create cluster --cluster-name tr-ocm6253 [...] --dry-run --subnet-ids <private-subnet-az1>,<other-private-subnet-az1>,<public-subnet>
[...]
**E: Creating cluster 'tr-ocm6253' should fail: Availability zone us-west-2a has more than one private subnet. Check the subnets and try again.**

## Step

(dry-run) Create a public cluster with 4 private subnets (2 subnets from same AZ) and 1 public subnet

## Expect

It should fail

>rosa create cluster --cluster-name tr-ocm6253 [...] --dry-run --subnet-ids <private-subnet-az1>,<other-private-subnet-az1>,<private-subnet-az2>,<private-subnet-az3>,<public-subnet>
[...]
**E: Creating cluster 'tr-ocm6253' should fail: Availability zone us-west-2a has more than one private subnet. Check the subnets and try again.**

## Step

(dry-run) Create a public cluster with 1 private subnet and 2 public subnet from same AZ

## Expect

It should succeed

>rosa create cluster --cluster-name tr-ocm6253 [...] --dry-run --subnet-ids <private-subnet-az1>,<public-subnet-az1>,<other-public-subnet-az1>
[...]
**I: Creating cluster 'tr-ocm6253' should succeed. Run without the '--dry-run' flag to create the cluster.**

## Step

(dry-run) Create a private cluster with 1 private subnet

## Expect

It should succeed

>rosa create cluster --cluster-name tr-ocm6253 [...] --dry-run --private --subnet-ids <private-subnet-az1>
[...]
**I: Creating cluster 'tr-ocm6253' should succeed. Run without the '--dry-run' flag to create the cluster.**

## Step

(dry-run) Create a private cluster with 3 private subnets

## Expect

It should succeed

>rosa create cluster --cluster-name tr-ocm6253 [...] --dry-run --private --subnet-ids <private-subnet-az1>,<private-subnet-az2>,<private-subnet-az3>
[...]
**I: Creating cluster 'tr-ocm6253' should succeed. Run without the '--dry-run' flag to create the cluster.**

## Step

(dry-run) Create a private cluster with 2 private subnets from same AZ

## Expect

It should fail

>rosa create cluster --cluster-name tr-ocm6253 [...] --dry-run --private --subnet-ids <private-subnet-az1>,<other-private-subnet-az1>
[...]
**E: Creating cluster 'tr-ocm6253' should fail: Availability zone us-west-2a has more than one private subnet. Check the subnets and try again.**

## Step

(dry-run) Create a private cluster with 4 private subnets (2 subnets from same AZ)

## Expect

It should fail

>rosa create cluster --cluster-name tr-ocm6253 [...] --dry-run --private --subnet-ids <private-subnet-az1>,<other-private-subnet-az1>,<private-subnet-az2>,<private-subnet-az3>
[...]
**E: Creating cluster 'tr-ocm6253' should fail: Availability zone us-west-2a has more than one private subnet. Check the subnets and try again.**

## Step

(dry-run) Create a private cluster with 1 private subnet and 1 public subnet

## Expect

It should fail

>rosa create cluster --cluster-name tr-ocm6253 [...] --dry-run --private --subnet-ids <private-subnet-az1>,<public-subnet>
[...]
**W: The following subnets have been excluded because they have an Internet Gateway Targetded Route and the Cluster choice is private: [subnet-0d2fdecbd250e3fc0]
```
E: Could not find the following subnet provided in region 'us-west-2': subnet-0d2fdecbd250e3fc0
**
```
