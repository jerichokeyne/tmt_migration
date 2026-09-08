# Setup
$ rosa create cluster -c ${name}aa --region ${region} --version ${version}-${channel_group} --channel-group ${channel_group} --role-arn arn:aws:iam::${aws_account_id}:role/OSDCCSAdmin --tags cluster-name:${name},cluster-version:${version}-${channel_group} ${roles} --external-id "<external_id>"

# Test

## Step
Get the latest version of rosacli

## Expect
Support sts from version 1.0.6

## Step
Create roles with command   
$ rosa create account --version 4.8 --prefix foo

## Expect
It will go into roles creation interactive mode

## Step
Select "yes" for all of the roles and policies creation

## Expect
All of the roles and policies will be created on AWS  
There will be output like below to ask user create cluster with below command  
[xueli@xueli-work rosa]$ rosa init account --prefix boo  
I: Logged in as 'sdqe-sre' on 'https://api.openshift.com'  
I: Validating AWS credentials...  
I: AWS credentials are valid!  
I: Validating AWS quota...  
I: AWS quota ok. If cluster installation fails, validate actual AWS resource usage against https://docs.openshift.com/rosa/rosa_getting_started/rosa-required-aws-service-quotas.html  
I: Verifying whether OpenShift command-line tool is available...  
I: Current OpenShift Client Version: 4.8.0-fc.2  
? OpenShift version: 4.7  
? Role prefix: boo  
? Role creation mode: auto  
I: Creating roles using 'arn:aws:iam::301721915996:user/xueli'  
? Are you sure you want to create the 'boo-Installer-Role' role? Yes  
I: Created role 'boo-Installer-Role' with ARN 'arn:aws:iam::301721915996:role/boo-Installer-Role'  
? Are you sure you want to create the 'boo-ControlPlane-Role' role? Yes  
I: Created role 'boo-ControlPlane-Role' with ARN 'arn:aws:iam::301721915996:role/boo-ControlPlane-Role'  
? Are you sure you want to create the 'boo-Worker-Role' role? Yes  
I: Created role 'boo-Worker-Role' with ARN 'arn:aws:iam::301721915996:role/boo-Worker-Role'  
? Are you sure you want to create the 'boo-Support-Role' role? Yes  
I: Created role 'boo-Support-Role' with ARN 'arn:aws:iam::301721915996:role/boo-Support-Role'  
? Are you sure you want to create the operator policies for OpenShift 4.7? Yes  
I: Creating policy 'boo-openshift-machine-api-aws-cloud-credentials'  
I: Creating policy 'boo-openshift-cloud-credential-operator-cloud-credential-operato'  
I: Creating policy 'boo-openshift-image-registry-installer-cloud-credentials'  
I: Creating policy 'boo-openshift-ingress-operator-cloud-credentials'  
I: Creating policy 'boo-openshift-cluster-csi-drivers-ebs-cloud-credentials'  
I: To create a cluster with these roles, run the following command:  
rosa create cluster --sts

## Step
Create the cluster by the command above.  
\# rosa create cluster --sts

## Expect
The interactive mode should be prompted if there are are more than one role-arn/master-iam-role/worker-iam-role/support-role-arn.  
- The roles will be listed in the output  
- The roles will be listed in the output  
The cluster will be created  
If the rosacli version >=1.1.3, the cluster will stay in 'waiting' status,waiting (Waiting for OIDC configuration)

## Step
Repeat to create another cluster with the arn/role flag without setting operator-role prefix  
$ rosa create cluster -c xuelirosa --operator-roles-prefix xuelirosa\  
--role-arn arn:aws:iam::301721915996:role/boo-Installer-Role \  
--master-iam-role arn:aws:iam::301721915996:role/boo-ControlPlane-Role \  
--worker-iam-role arn:aws:iam::301721915996:role/boo-Worker-Role \  
--support-role-arn arn:aws:iam::301721915996:role/boo-Support-Role

## Expect
- The cluster will be created successfully  
- The roles will be listed in the output  
- The roles will be listed in the output  
- The operator roles prefix will be in format "<cluster name>-<random chars>"

## Step
Describe the cluster  
$ rosa describe cluster -c xuelirosa

## Expect
- There should be OIDC Endpoint URL in the detail  
- The roles will be listed in the output

## Step
Create the operator roles via command  
$ rosa create operator-roles -c xuelirosa --prefix foo

## Expect
All of the roles should be created successfully。  
If the rosacli version >=1.1.3, the cluster will stay in 'waiting' status,waiting (Waiting for OIDC configuration)

## Step
Check the resource on Hive

## Expect
During 'waiting' only the secrets/configmaps necessary for the OIDC configuration are sent to  
Hive. The accountclaim and the rest of the resources are created once  
the cluster reaches 'pending' state.

## Step
Waiting for a while and check the cluster status by describe the cluster  
$ rosa describe cluster -c xuelirosa

## Expect
There will be error message show the oidc connections status  
lixue@Xue-Lis-MacBook-Pro Workspace % rosa describe cluster -c xuelists   
Name: xuelists  
ID: 1ntebao0hin7m54s5v5h7kbmmm019jlm  
External ID:   
OpenShift Version:   
Channel Group: stable  
DNS: xuelists.t0jm.s1.devshift.org  
AWS Account: 301721915996  
API URL:   
Console URL:   
Region: us-east-2  
Multi-AZ: false  
Nodes:  
- Master: 3  
- Infra: 2  
- Compute: 2  
Network:  
- Service CIDR: 172.30.0.0/16  
- Machine CIDR: 10.0.0.0/16  
- Pod CIDR: 10.128.0.0/14  
- Host Prefix: /23  
STS Role ARN: arn:aws:iam::301721915996:role/ManagedOpenShift-Installer-Role  
Support Role ARN: arn:aws:iam::301721915996:role/ManagedOpenShift-Support-Role  
Instance IAM Roles:  
- Master: arn:aws:iam::301721915996:role/ManagedOpenShift-ControlPlane-Role  
- Worker: arn:aws:iam::301721915996:role/ManagedOpenShift-Worker-Role  
Operator IAM Roles:  
- arn:aws:iam::301721915996:role/xuelists-k4s0-openshift-machine-api-aws-cloud-credentials  
- arn:aws:iam::301721915996:role/xuelists-k4s0-openshift-cloud-credential-operator-cloud-credenti  
- arn:aws:iam::301721915996:role/xuelists-k4s0-openshift-image-registry-installer-cloud-credentia  
- arn:aws:iam::301721915996:role/xuelists-k4s0-openshift-ingress-operator-cloud-credentials  
- arn:aws:iam::301721915996:role/xuelists-k4s0-openshift-cluster-csi-drivers-ebs-cloud-credential  
**State: waiting (InvalidIdentityToken: No OpenIDConnect provider found in your account for https://rh-oidc-staging.s3.us-east-1.amazonaws.com/1ntebao0hin7m54s5v5h7kbmmm019jlm)**  
Private: No  
Created: Oct 18 2021 08:43:26 UTC  
Details Page: https://qaprodauth.cloud.redhat.com/openshift/details/s/1zfkc4l0japdoBxSPr3pOKLEm4f  
OIDC Endpoint URL: https://rh-oidc-staging.s3.us-east-1.amazonaws.com/1ntebao0hin7m54s5v5h7kbmmm019jlm

## Step
Create the oidc-provider for the cluster  
  
$ rosa create oidc-provider -c xuelirosa -y

## Expect
The provider will created with arn as output  
[xueli@xueli-work rosa]$ rosa create oidc-provider -c xuelirosa  
? Role creation mode: auto  
I: Creating OIDC provider using 'arn:aws:iam::301721915996:user/xueli'  
? Are you sure you want to create the OIDC provider for cluster 'xuelirosa'? Yes  
I: Created OIDC provider with ARN 'arn:aws:iam::301721915996:oidc-provider/rh-oidc.s3.us-east-1.amazonaws.com/1m5udpar7tocgq6emicblicpoqqtqpc7'

## Step
Describe the cluster again  
$ rosa describe cluster -c xueli-stsaa

## Expect
The status will be changed to  
State: pending(Preparing Account)  
or  
State: Installing(DNS Setup in Progress)  
[xueli@xueli-work script]$ rosa describe cluster -c xueli-stsaa  
Name: xueli-stsaa  
ID: 1knvhgd2bu00q9140t0ktpup0ir6kudo  
External ID:   
OpenShift Version:   
Channel Group: candidate  
DNS: xueli-stsaa.zzjd.s2.devshift.org  
AWS Account: 301721915996  
API URL:   
Console URL:   
Region: us-east-1  
Multi-AZ: false  
Nodes:  
- Master: 3  
- Infra: 2  
- Compute: 2  
Network:  
- Service CIDR: 172.30.0.0/16  
- Machine CIDR: 10.0.0.0/16  
- Pod CIDR: 10.128.0.0/14  
- Host Prefix: /23  
State: pending (Waiting for OIDC configuration)  
Private: No  
Created: May 17 2021 10:34:45 UTC  
Details Page: https://qaprodauth.cloud.redhat.com/openshift/details/1knvhgd2bu00q9140t0ktpup0ir6kudo  
OIDC Endpoint URL: https://1knvhgd2bu00q9140t0ktpup0ir6kudo-oidc.s3.us-east-1.amazonaws.com

## Step
Wait for cluster ready

## Expect
Cluster will be ready in 2 hours

## Step
scale up/down the cluster

## Expect
Cluster will be scale up/down successfully

## Step
Delete the cluster

## Expect
Cluster will be deleted successfully

## Step
Do the post clean steps after the cluster deprovision is finished  
- delete operator-roles  
- delete oidc-privider

## Expect
- The cluster is deprovisioned.  
- The operator-role is deleted.  
- The oidc-provider is deleted.

## Step
Create another sts cluster with operator-roles prefix set  
rosa create cluster --sts -c xuelists3 --operator-roles-prefix xuelists

## Expect
- The operator roles will be with prefix set
