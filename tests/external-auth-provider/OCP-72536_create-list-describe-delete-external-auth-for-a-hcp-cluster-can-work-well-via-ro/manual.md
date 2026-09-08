# Setup
<https://docs.google.com/document/d/1HaEaQKzzQqNMiPxovnYWasLB2yVjHnsfSIs1q8BWD2Q/edit#heading=h.c1k2r73eamsh>   
[OCP-71561](</polarion/#/project/OSE/workitem?id=OCP-71561>)

# Test

## Step
Check if the capability is enable for test org  
echo '{"feature": "capability.organization.hcp_allow_external_authentication"}'|ocm post /api/authorizations/v1/self_feature_review

## Expect

## Step
Prepare a HCP cluster with
    
    --external-auth-providers-enabled

## Expect

## Step
Check help information  
**rosa** create/list/descirbe/delete external-auth-provider --help

## Expect
The information should be readable and clear  
./rosa create/list/describe/delete -h  
...  
external-auth-provider Show details of an external authentication provider on a cluster  
...  
  
./rosa create/list/describe/delete external-auth-provider -h  
Show details of an external authentication provider on a cluster.  
  
  
Usage:  
rosa describe external-auth-provider [flags]  
  
  
Aliases:  
external-auth-provider, externalauthproviders, externalauthprovider, external-auth-providers  
  
  
Examples:  
\# Show details of an external authentication provider named "exauth" on a cluster named "mycluster"  
rosa describe external-auth-provider exauth --cluster=mycluster

## Step
Create external auth to the cluster  
**rosa** create external-auth-provider \  
--cluster=lponce-local-01 \  
--name=microsoft-entra-id \  
--issuer-url=<https://login.microsoftonline.com/fa5d3dd8-b8ec-4407-a55c-ced639f1c8c5/v2.0> \  
--issuer-audiences=a9464024-b142-4bdf-86c0-a153109cdb14 \  
--claim-mapping-username-claim=email \  
--claim-mapping-groups-claim=groups \  
--claim-validation-rule claim1:rule1

## Expect
-It can create successfully  
I: Successfully created an external authentication provider for cluster '2a2qh276107ljep597jmjrd7f6kn2ol1'  
-It will give a message like this:  
It may take several minutes for this access to become active

## Step
List the external-auth-provider to cluster  
./rosa list external-auth-provider -c sdq-ci-ylgck

## Expect
-It can get the created external auth provider  
./rosa list external-auth-provider -c sdq-ci-ylgck  
NAME ISSUER URL  
microsoft-entra-id https://login.microsoftonline.com/fa5d3dd8-b8ec-4407-a55c-ced639f1c8c5/v2.0

## Step
Describe external-auth-provider to cluster

## Expect
./rosa describe external-auth-provider --name microsoft-entra-id -c sdq-ci-ylgck  
ID: microsoft-entra-id  
Cluster ID: 2a2qh276107ljep597jmjrd7f6kn2ol1  
Issuer audiences:   
- a9464024-b142-4bdf-86c0-a153109cdb14  
Issuer Url: https://login.microsoftonline.com/fa5d3dd8-b8ec-4407-a55c-ced639f1c8c5/v2.0  
Claim mappings group: groups  
Claim mappings username: email

## Step
Delete the external-auth-provider to cluster

## Expect
-It can be deleted successfully  
./rosa delete external-auth-provider microsoft-entra-id -c sdq-ci-ylgck -y  
I: Successfully deleted external authentication provider 'microsoft-entra-id' from cluster 'sdq-ci-ylgck'  
  
/rosa list external-auth-provider -c sdq-ci-ylgck  
E: there are no external authentication providers for this cluster

## Step
Create a new external_auth with CA for a cluster with external_auth_config using the CLI  
  
./rosa create external-auth-provider -c sdq-ci-ylgck --name=microsoft-entra-id --issuer-url=https://login.microsoftonline.com/fa5d3dd8-b8ec-4407-a55c-ced639f1c8c5/v2.0 --issuer-audiences=a9464024-b142-4bdf-86c0-a153109cdb14 --issuer-ca-file=/home/yingzhan/mytest/rosa/mitm-ca.pem --claim-mapping-username-claim=email --claim-mapping-groups-claim=groups  
  
-Describe the external_auth_config

## Expect
-It can create successfully  
-It should contain CA related information  
./rosa describe external-auth-provider --name microsoft-entra-id -c sdq-ci-ylgck  
  
  
ID: microsoft-entra-id  
Cluster ID: 2a2qh276107ljep597jmjrd7f6kn2ol1  
Issuer audiences:   
- a9464024-b142-4bdf-86c0-a153109cdb14  
Issuer Url: https://login.microsoftonline.com/fa5d3dd8-b8ec-4407-a55c-ced639f1c8c5/v2.0  
Claim mappings group: groups  
Claim mappings username: email

## Step
Create a new external_auth for a cluster with client parameters  
**rosa** create external-auth-provider \  
--cluster=lponce-local-01 \  
--name=microsoft-entra-id \  
--issuer-url=<https://login.microsoftonline.com/fa5d3dd8-b8ec-4407-a55c-ced639f1c8c5/v2.0> \  
--issuer-audiences=a9464024-b142-4bdf-86c0-a153109cdb14,8a769b34-13c9-4f5b-9933-ec439700ec6 \  
--claim-mapping-username-claim=email \  
--claim-mapping-groups-claim=groups \  
--console-client-id=8a769b34-13c9-4f5b-9933-ec439700ec6 \  
--console-client-secret=****************************************   
  
-Describe the external_auth_config

## Expect
-It can create successfully  
-It should contain client id  
./rosa describe external-auth-provider --name microsoft-entra-id-a -c sdq-ci-ylgck  
  
  
ID: microsoft-entra-id-a  
Cluster ID: 2a2qh276107ljep597jmjrd7f6kn2ol1  
Issuer audiences:   
- a9464024-b142-4bdf-86c0-a153109cdb14  
- 8a769b34-13c9-4f5b-9933-ec439700ec6  
Issuer Url: https://login.microsoftonline.com/fa5d3dd8-b8ec-4407-a55c-ced639f1c8c5/v2.0  
Claim mappings group: groups  
Claim mappings username: email  
Console client id: 8a769b34-13c9-4f5b-9933-ec439700ec6
