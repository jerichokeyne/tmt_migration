# Test

## Step
Login with rosacli and init  
$ rosa login --token $<token>; rosa init

## Expect
It will init successfully

## Step
Create a cluster with a too small volume size set  
% rosa create cluster -c xuelivo --worker-disk-size 10GiB

## Expect
**For classical cluster, minimum disk size is 128GiB  
For HCP cluster, minimum disk size is 75GiB**  
  
The cluster won't be created. There will be error message  
lixue@Xue-Lis-MacBook-Pro ~ % rosa create cluster -c xuelivo --worker-disk-size 10GiB  
W: In a future release STS will be the default mode.  
W: --sts flag won't be necessary if you wish to use STS.  
W: --non-sts/--mint-mode flag will be necessary if you do not wish to use STS.  
I: Creating cluster 'xuelivo'  
I: To view a list of clusters and their status, run 'rosa list clusters'  
E: Failed to create cluster: Invalid root disk size: 10 GiB. Must be between <minimum disk size> and 16384 GiB ~~1024 GiB~~.

## Step
Create a cluster with a large volume size set  
% rosa create cluster -c xuelivo --worker-disk-size 20000GiB

## Expect
The cluster won't be created. There will be error message  
lixue@Xue-Lis-MacBook-Pro ~ % rosa create cluster -c xuelivo --worker-disk-size 10000GiB  
W: In a future release STS will be the default mode.  
W: --sts flag won't be necessary if you wish to use STS.  
W: --non-sts/--mint-mode flag will be necessary if you do not wish to use STS.  
I: Creating cluster 'xuelivo'  
I: To view a list of clusters and their status, run 'rosa list clusters'  
E: Failed to create cluster: Invalid root disk size: 10000 GiB. Must be between <minimum disk size> and 16384 GiB1~~024 GiB~~.

## Step
Create a cluster with an invalid volume size set  
% rosa create cluster -c xuelivo --worker-disk-size invalid

## Expect
The cluster won't be created. There will be error message  
lixue@Xue-Lis-MacBook-Pro ~ % rosa create cluster -c xuelivo --worker-disk-size invalid   
W: In a future release STS will be the default mode.  
W: --sts flag won't be necessary if you wish to use STS.  
W: --non-sts/--mint-mode flag will be necessary if you do not wish to use STS.  
E: Expected a valid machine pool root disk size value: invalid disk size format: invalid. accepted units are Giga or Tera in the form of g, G, GB, GiB, Gi, t, T, TB, TiB, Ti
