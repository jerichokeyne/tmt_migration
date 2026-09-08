# Test

## Step
Create rosa cluster with setting 'fips' flag but '--etcd-encryption=false'

## Expect
Error message displayed as below.  
zhewang@localhost:~$ rosa create cluster -c zwant --fips --etcd-encryption=false  
W: In a future release STS will be the default mode.  
W: --sts flag won't be necessary if you wish to use STS.  
W: --non-sts/--mint-mode flag will be necessary if you do not wish to use STS.  
E: etcd encryption cannot be disabled on clusters with FIPS mode
