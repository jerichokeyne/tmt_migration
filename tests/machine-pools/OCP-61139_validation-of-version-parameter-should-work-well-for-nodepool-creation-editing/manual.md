# Test

## Step
Deploy hosted cluster

## Expect

## Step
Create a nodepool with version greater than cluster's version

## Expect
E: Expected a valid OpenShift version: A valid version number must be specified  
Valid versions: 4.12.5 4.12.4 4.12.3 4.12.2 4.12.1 4.12.0

## Step
Create a nodepool with version channel-group different with the cluster's channel group

## Expect
E: Expected a valid OpenShift version: A valid version number must be specified  
Valid versions: 4.12.5 4.12.4 4.12.3 4.12.2 4.12.1 4.12.0

## Step
Create nodepool who's major version is not same with the cluster's major version  
like 3.14.x to 4.0.y

## Expect
E: Expected a valid OpenShift version: A valid version number must be specified  
Valid versions: 4.12.5 4.12.4 4.12.3 4.12.2 4.12.1 4.12.0

## Step
Create nodepool has less than 2 minor version to the cluster   
like 4.3.x to 4.6.y

## Expect
E: Expected a valid OpenShift version: A valid version number must be specified  
Valid versions: 4.12.5 4.12.4 4.12.3 4.12.2 4.12.1 4.12.0

## Step
Create nodepool with version lower than 4.12

## Expect
E: Expected a valid OpenShift version: A valid version number must be specified  
Valid versions: 4.12.5 4.12.4 4.12.3 4.12.2 4.12.1 4.12.0

## Step
Create nodepool with version lower than 4.14 if the minimal version for HCP is 4.14  
The new minimal version for HCP is 4.14.x, so the minimal version for node pool is 4.14.x.(toggle:hypershift-enable-additional-minimal-version)  
4.12 is only used for IBM LH users

## Expect
./rosa create machinepool -c ying-hcp-a --version 4.13.10 --name mp-1 --replicas 1   
E: Expected a valid OpenShift version: A valid version number must be specified  
Valid versions: 4.14.1 4.14.0

## Step
Create nodepool with not existing version

## Expect
E: Expected a valid OpenShift version: A valid version number must be specified  
Valid versions: 4.12.5 4.12.4 4.12.3 4.12.2 4.12.1 4.12.0
