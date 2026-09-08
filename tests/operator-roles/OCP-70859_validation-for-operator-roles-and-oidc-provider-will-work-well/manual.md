# Test

## Step
Prepare a ready sts cluster

## Expect

## Step
Create operator roles to the cluster again  
$rosa create operator-roles -c <cluster name> -y --mode auto

## Expect
There will be waring show like below  
./rosa create operator-roles --cluster ying-sts -y --mode auto  
W:Operator roles already exists

## Step
Create oidc config to the cluster again  
$rosa create oidc-provider -c <cluster name> -y --mode auto

## Expect
There will be waring show like below  
./rosa create oidc-provider --cluster ying-sts  
? OIDC provider creation mode (default = 'auto'): auto  
W: OIDC provider already exists.

## Step
Delete the oidc-provider to the cluster  
./rosa delete oidc-provider -c ying-sts

## Expect
./rosa delete oidc-provider -c ying-sts   
? OIDC provider deletion mode (default = 'auto'): auto  
E: Cluster '28n92nd7ejigaih957kci3g3og887vkt' is in 'ready' state. OIDC provider can be deleted only for the uninstalled clusters

## Step
Delete the operator-roles to the cluster  
./rosa delete operator-roles -c ying-sts

## Expect
./rosa delete operator-roles -c ying-sts   
? Operator roles deletion mode (default = 'auto'): auto  
E: Cluster '28n92nd7ejigaih957kci3g3og887vkt' is in 'ready' state. Operator roles can be deleted only for the uninstalled clusters

## Step
Repeat above steps with oidc-config-id  
rosa create/delete oidc-provider --oidc-config-id <id> -y --mode auto  
rosa create/delete operator-roles --oidc-config-id <id> -y --mode auto

## Expect
There will be message show like below  
./rosa delete oidc-provider --oidc-config-id 27ph8clcaj8ibddo7aqijs2meh5k0sin --mode auto -y  
I: Provider 'https://oidc.s1.devshift.org/27ph8clcaj8ibddo7aqijs2meh5k0sin' not found.

## Step
Try to create operator roles with cluster id and oidc config id passing at the same time  
$ rosa create operator-roles -c 2c8jo22d7jqatgvou7a9ogptm4c9c07s --oidc-config-id 2aa6vevftb5co79ov2megv53mvvuii2g

## Expect
E: A cluster key for STS cluster and an OIDC configuration ID cannot be specified alongside each other.(OCM-7851).
