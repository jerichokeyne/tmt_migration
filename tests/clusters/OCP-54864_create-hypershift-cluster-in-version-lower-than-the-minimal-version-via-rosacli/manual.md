# Test

## Step
Launch rosacli with latest version build on staging env

## Expect

## Step
Create a hosted hypershift cluster via rosacli with lower version than 4.13.0  
$ rosa create cluster --sts --hosted-cp --version 4.11.13 -c xuelihp2 --region us-west-2 --subnet-ids subnet-0465497173d6a8be7,subnet-05e11e7f9393b3600

## Expect
There will be error message like below that the version is not supported for hypershift cluster  
[xueli@xueli-work rosa]$ rosa create cluster --sts --hosted-cp --version 4.11.13 -c xuelihp --region us-west-2  
...  
E: Expected a valid OpenShift version: version '4.11.13' is not supported for hosted clusters

## Step
Try with a version in higher or equal version with the minimal version  
If hypershift-enable-additional-minimal-version enable, the minimal version is 4.14.x  
If not enable, the minimal version is 4.13(Used for IBM LH users)

## Expect
It will succeed and cluster will be created successfully
