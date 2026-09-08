# Setup
<https://docs.google.com/document/d/1HaEaQKzzQqNMiPxovnYWasLB2yVjHnsfSIs1q8BWD2Q/edit#heading=h.gskk0wlq4f39>

# Test

## Step
Prepare a HCP cluster with " --external-auth-providers-enabled"

## Expect

## Step
Check the help message  
$rosa create break-glass-credential--help

## Expect
./rosa create/list/describe/revoke --help  
...  
break-glass-credential Create a break glass credential for a cluster  
...  
./rosa create break-glass-credential --help  
Create a break glass credential for a hosted control plane cluster with external authentication enabled.  
  
  
Usage:  
rosa create break-glass-credential [flags]  
  
  
Aliases:  
break-glass-credential, break-glass-credentials, breakglasscredential, breakglasscredentials  
  
  
Examples:  
\# Interactively create a break glass credential to a cluster named "mycluster"  
rosa create break-glass-credential --cluster=mycluster --interactive  
  
  
Flags:  
-c, --cluster string Name or ID of the cluster.  
--expiration duration Expire the break glass credential after a relative duration like 2h, 8h. The expiration duration needs to be at least 10 minutes from now and to be at maximum 24 hours.  
-h, --help help for break-glass-credential  
-i, --interactive Enable interactive mode.  
--username string Username for the break glass credential.  
  
  
Global Flags:  
--color string Surround certain characters with escape sequences to display them in color on the terminal. Allowed options are [auto never always] (default "auto")  
--debug Enable debug mode.  
--profile string Use a specific AWS profile from your credential file.  
--region string Use a specific AWS region, overriding the AWS_REGION environment variable.  
-y, --yes Automatically answer yes to confirm operation.  
  
./rosa revoke break-glass-credential --help

## Step
Create a break glass credential to the cluster  
$rosa create break-glass-credential --username test --expiration 2h  
$rosa create break-glass-credential --expiration 15m  
$rosa create break-glass-credential --username test  
$rosa create break-glass-credential

## Expect
-If without expiration, the expiration time should be after 24 hours  
-If without username, it will be configured with a random string

## Step
List the credentials  
$rosa list break-glass-credential -c 2a83k03lilf22l1d4kqkkt96i0hfgpbr

## Expect
./rosa list break-glass-credential -c 2a83k03lilf22l1d4kqkkt96i0hfgpbr   
ID USERNAME STATUS  
2ackprr73vpnnfgaefu3s8slauc9hbkt e4965625-f0b3-11ee-943a-0a580a830b20 issued  
  
-If there is no credentials,  
./rosa list break-glass-credential --cluster=sdq-ci-bzoci  
I: there are no break glass credentials for this cluster

## Step
Describe the credential   
$rosa describe break-glass-credential -c 2a83k03lilf22l1d4kqkkt96i0hfgpbr --id 2ackprr73vpnnfgaefu3s8slauc9hbkt

## Expect
./rosa describe break-glass-credential -c 2a83k03lilf22l1d4kqkkt96i0hfgpbr --id 2ackprr73vpnnfgaefu3s8slauc9hbkt  
**I: To retrieve only the kubeconfig for this credential use: 'rosa describe break-glass-credential 2ackprr73vpnnfgaefu3s8slauc9hbkt -c cms-lzdyc --kubeconfig'**  
  
  
ID: 2ackprr73vpnnfgaefu3s8slauc9hbkt  
Username: e4965625-f0b3-11ee-943a-0a580a830b20  
Expire at: Apr 2 2024 07:43:12 UTC  
Status: issued

## Step
Use the command in "describe" output to get the credential  
$rosa describe break-glass-credential -c 2a83k03lilf22l1d4kqkkt96i0hfgpbr --id 2ackprr73vpnnfgaefu3s8slauc9hbkt --kubeconfig

## Expect
-It can login cluster with the credential

## Step
Delete the credential   
$rosa revoke break-glass-credential -c 2a83k03lilf22l1d4kqkkt96i0hfgpbr

## Expect
-All the credentials will be revoked  
./rosa revoke break-glass-credential -c cms-lzdyc  
? Are you sure you want to revoke all the break glass credentials on cluster 'cms-lzdyc'? Yes  
I: Successfully revoked all break glass credentials from cluster 'cms-lzdyc'  
  
  
./rosa list break-glass-credential -c cms-lzdyc  
ID USERNAME STATUS  
2ackprr73vpnnfgaefu3s8slauc9hbkt e4965625-f0b3-11ee-943a-0a580a830b20 awaiting_revocation  
2acl0aaec25u0f976lmf6okppm9mnkl2 test awaiting_revocation
