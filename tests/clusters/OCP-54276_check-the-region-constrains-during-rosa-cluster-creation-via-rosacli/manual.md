# Test

## Step
Check the region constrain config map at <https://gitlab.cee.redhat.com/service/app-interface/-/blob/master/resources/services/ocm/stage/region-constraints.configmap.yaml>

## Expect

## Step
Create ROSA NON-STS cluster with the version< the min_version in the config map via rosacli in the interactive mode

## Expect
The regions which are in the region constrain cm will be not shown in the 'AWS region' list in the interactive mode

## Step
Create ROSA STS cluster with the version< the min_version in the config map via rosacli in the interactive mode

## Expect
The regions which are in the region constrain cm will be not shown in the 'AWS region' list in the interactive mode

## Step
Create ROSA NON-STS cluster with the version< the min_version in the config map via rosacli by the rosacli commands

## Expect
It should be failed with the error message like bellow:  
E: Region 'ap-southeast-3' is not supported for this AWS account --- TBD: E: Region 'ap-southeast-3' is not supported for this AWS version

## Step
Create ROSA STS cluster with the version< the min_version in the config map via rosacli by the rosacli commands

## Expect
It should be failed with the error message like bellow:  
E: Region 'ap-southeast-3' is not supported for this AWS account --- TBD: E: Region 'ap-southeast-3' is not supported for this AWS version

## Step
Create ROSA non-sts/sts cluster with the version>= the min_version in the interactive mode

## Expect
The region can be chosen and the creation should succeed

## Step
Create ROSA non-sts/sts cluster with the version>= the min_version by the rosa command

## Expect
The region can be chosen and the creation should succeed

## Step
Check the restraints for the version for an HCP cluster in this region are higher than the min version:  
rosa create cluster --cluster-name eld1 --sts --role-arn arn:aws:iam::425464789085:role/eld2-Installer-Role --support-role-arn arn:aws:iam::425464789085:role/eld2-Support-Role --worker-iam-role arn:aws:iam::425464789085:role/eld2-Worker-Role --operator-roles-prefix eld2-label-1bg123-q0w0 --oidc-config-id 252co0eaghmh6ohdhovfo2vnvtnevj88 --region ap-southeast-3 --version 4.12.21 --replicas 2 --compute-machine-type m5.xlarge --machine-cidr 10.0.0.0/16 --service-cidr 172.30.0.0/16 --pod-cidr 10.128.0.0/14 --host-prefix 23 --subnet-ids subnet-0ef71fb42b20cc43c,subnet-0c28fe19063b652f1 --hosted-cp

## Expect
E: Failed to create cluster: Only version '4.12.23' and newer are supported in region 'ap-southeast-3'
