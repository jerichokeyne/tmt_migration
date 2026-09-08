# Test

## Step
Log in via rosacli with account which has capability.organization.fips_cluster capability.

## Expect

## Step
Create rosa cluster with setting 'fips' flag  
rosa create cluster -c ys-1125-fips2 --fips

## Expect
1.Check the if the FIPS mode is enanled.   
Follow   
2. The etcd-encryption should be enabled automatically

## Step
~~Repeat step2 with an account which has no capability.organization.fips_cluster capability.~~

## Expect
~~[root@yuwan rosa]# ./rosa create cluster -c ys-1125-fips --fips I: Creating cluster 'ys-1125-fips' I: To view a list of clusters and their status, run 'rosa list clusters' E: Failed to create cluster: 'fips_cluster' capability is not set for this organization [root@yuwan rosa]# ~~

## Step
~~Create rosa cluster with setting 'fips' flag but '--etcd-encryption=false~~'

## Expect
~~[root@yuwan rosa]# ./rosa create cluster -c ys-1125-fips2 --fips --etcd-encryption=false E: etcd encryption cannot be disabled on clusters with FIPS mode~~
