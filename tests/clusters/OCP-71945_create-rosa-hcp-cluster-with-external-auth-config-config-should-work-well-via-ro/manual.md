# Test

## Step

Check cluster create cluster help information
./rosa create cluster --help

## Expect

~~It is hidden now~~ It will contain 'external-auth-providers-enabled' description

## Step

Create ROSA HCP cluster with

    --external-auth-providers-enabled

## Expect

-The cluster can be created successfully
-The flag is in the created cluster command

## Step

Describe cluster

## Expect

-There will be External Authentication information in cluster response
./rosa describe cluster -c ying-hcp-o1


Name: ying-hcp-o1
Display Name: ying-hcp-o1
ID: 29l0f0logaitlunfqaabseffv7mplr1v
External ID: ddaa52e9-35a2-4095-bd5c-850932f0cb6b
Control Plane: ROSA Service Hosted
OpenShift Version: 4.15.0-rc.8
Channel Group: candidate
DNS: ying-hcp-o1.3jye.s3.devshift.org
AWS Account: 301721915996
AWS Billing Account: 301721915996
API URL: https://api.ying-hcp-o1.3jye.s3.devshift.org:443
Console URL: https://console-openshift-console.apps.rosa.ying-hcp-o1.3jye.s3.devshift.org
Region: us-west-2
Availability:
- Control Plane: MultiAZ
- Data Plane: MultiAZ


Nodes:
- Compute (desired): 3
- Compute (current): 3
Network:
- Type: OVNKubernetes
- Service CIDR: 172.30.0.0/16
- Machine CIDR: 10.0.0.0/16
- Pod CIDR: 10.128.0.0/14
- Host Prefix: /23
- Subnets: subnet-0cfd42c0ee4a65c48, subnet-074136369ce6bd5ed, subnet-0cbfd26dd851442bc, subnet-0b2afc686f9d8dffa, subnet-0d475efe199a06585, subnet-09609abda03ad1819
EC2 Metadata Http Tokens: optional
Role (STS) ARN: arn:aws:iam::301721915996:role/sdq-ci-uwqyp-HCP-ROSA-Installer-Role
Support Role ARN: arn:aws:iam::301721915996:role/sdq-ci-uwqyp-HCP-ROSA-Support-Role
Instance IAM Roles:
- Worker: arn:aws:iam::301721915996:role/sdq-ci-uwqyp-HCP-ROSA-Worker-Role
Operator IAM Roles:
- arn:aws:iam::301721915996:role/ying-hcp-o1-x4f2-kube-system-capa-controller-manager
- arn:aws:iam::301721915996:role/ying-hcp-o1-x4f2-kube-system-control-plane-operator
- arn:aws:iam::301721915996:role/ying-hcp-o1-x4f2-kube-system-kms-provider
- arn:aws:iam::301721915996:role/ying-hcp-o1-x4f2-openshift-image-registry-installer-cloud-creden
- arn:aws:iam::301721915996:role/ying-hcp-o1-x4f2-openshift-ingress-operator-cloud-credentials
- arn:aws:iam::301721915996:role/ying-hcp-o1-x4f2-openshift-cluster-csi-drivers-ebs-cloud-credent
- arn:aws:iam::301721915996:role/ying-hcp-o1-x4f2-openshift-cloud-network-config-controller-cloud
- arn:aws:iam::301721915996:role/ying-hcp-o1-x4f2-kube-system-kube-controller-manager
Managed Policies: Yes
State: ready
Private: No
Created: Feb 26 2024 09:10:30 UTC
User Workload Monitoring: Enabled
Details Page: https://qaprodauth.console.redhat.com/openshift/details/s/2ctlCpptfBPzIfaMFIf6cohnAua
OIDC Endpoint URL: https://oidc.os1.devshift.org/28qf5nunbs41jgsmdcv2ne6ctalju745 (Managed)
Audit Log Forwarding: Disabled
External Authentication: Enabled

## Step

Create cluster with flag
--external-auth-providers-enabled=false
--external-auth-providers-enabled=true

## Expect

-If --external-auth-providers-enabled=false, the External Authentication is Disabled
-If --external-auth-providers-enabled=true, the External Authentication is Enable
