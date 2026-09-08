# Test

## Step
Prepare a ready ROSA cluster

## Expect

## Step
Create a spot machine pool to the cluster via command with negative price  
$ rosa create machinepool spot1 --spot-max-price -10.2 -c sdqe-m-rosa --replicas 1

## Expect
_ the machinepool creation will fail  
- The error message will show that spot-max-price need to be positive

## Step
Create a spot machine pool to the cluster with use-spot-machine=false but spot-max-price valid  
$ rosa create machinepool spot1 --spot-max-price 10.2 -c sdqe-m-rosa --replicas 1 --use-spot-instances=false

## Expect
- There should be error message that spot-max-price only can be used when use-spot-instances set to true
