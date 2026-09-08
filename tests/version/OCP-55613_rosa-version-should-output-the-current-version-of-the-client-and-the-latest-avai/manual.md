# Test

## Step
Install not the latest ROSACLI release from here <https://mirror.openshift.com/pub/openshift-v4/x86_64/clients/rosa/>   
Follow the instructions to install

## Expect
ROSA CLI is installed

## Step
Verify the the rosacli version installed r without user being logged in  
$ rosa version

## Expect
1.2.8  
There is a newer release version, please consider updating: https://github.com/openshift/rosa/releases/tag/v1.2.9

## Step
$ rosa verify rosa

## Expect
There is a newer release version, please consider updating: https://github.com/openshift/rosa/releases/tag/v1.2.9

## Step
Login to ROSA CLI with [TOKEN](<https://qaprodauth.console.redhat.com/openshift/token/rosa/show#>)   
$ rosa login --token="..."

## Expect
logged in successfully

## Step
Verify the the rosacli version installed with user being logged in  
$ rosa version

## Expect
1.2.8  
There is a newer release version, please consider updating: https://github.com/openshift/rosa/releases/tag/v1.2.9

## Step
$ rosa verify rosa

## Expect
There is a newer release version, please consider updating: https://github.com/openshift/rosa/releases/tag/v1.2.9

## Step
Update to the latest version  
$ rosa download rosa

## Expect
I: Downloading https://mirror.openshift.com/pub/openshift-v4/clients/rosa/latest/rosa-linux.tar.gz to your current directory  
Downloading... 19 MB complete   
I: Successfully downloaded rosa-linux.tar.gz

## Step
Verify it is the same version as published here <https://mirror.openshift.com/pub/openshift-v4/x86_64/clients/rosa/latest/>

## Expect

## Step
Verify the the rosacli version installed  
$ rosa version

## Expect
1.2.9  
Your ROSA CLI is up to date.

## Step
$ rosa verify rosa

## Expect
Your ROSA CLI is up to date.
