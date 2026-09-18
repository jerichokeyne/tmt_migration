# Test

## Step

check the help message
```bash
rosa create cluster -h
```

## Expect

-There is the help message
...
--registry-config-allowed-registries strings A comma-separated list of registries for which image pull and push actions are allowed.
--registry-config-insecure-registries strings A comma-separated list of registries which do not have a valid TLS certificate or only support HTTP connections.
--registry-config-blocked-registries strings A comma-separated list of registries for which image pull and push actions are denied.
--registry-config-allowed-registries-for-import string Limits the container image registries from which normal users can import images. The format should be a comma-separated list of 'domainName:insecure'. 'domainName' specifies a domain name for the registry. 'insecure' indicates whether the registry is secure or insecure.
--registry-config-additional-trusted-ca string A json file containing the registry hostname as the key, and the PEM-encoded certificate as the value, for each additional registry CA to trust.
...

## Step

create hcp with registry config parameters
```bash
rosa create cluster --cluster-name ying-0924-r1 --hosted-cp --registry-config-allowed-registries insecure1.io,insecure2.io,insecure3.io --registry-config-insecure-registries insecure7.io,insecure6.io --registry-config-allowed-registries-for-import test.com:true,test2.com:false --registry-config-additional-trusted-ca test/ca ....
```

## Expect

-it can create successfully
-The configured value should be shown
Name: ying-0924-r1
Domain Prefix: ying-0924-r1
Display Name: ying-0924-r1
ID: 2dvvolla7nucnauj6c0lriksk7eni3mf
External ID: 0fdc57fb-2daf-44d1-9960-679e4e3a4571
Control Plane: ROSA Service Hosted
OpenShift Version: 4.16.13
Channel Group: candidate
DNS: Not ready
AWS Account: 301721915996
AWS Billing Account: 301721915996
API URL:
Console URL:
Region: us-west-2
Availability:
- Control Plane: MultiAZ
- Data Plane: MultiAZ

Nodes:
- Compute (desired): 3
- Compute (current): 0
Network:
- Type: OVNKubernetes
- Service CIDR: 172.30.0.0/16
- Machine CIDR: 10.0.0.0/16
- Pod CIDR: 10.128.0.0/14
- Host Prefix: /23
- Subnets: subnet-09a6d23849299a403, subnet-049f02de006b3666c, subnet-008b1cf5e54042240, subnet-00572844cfae3f946, subnet-0797315e51cb947f8, subnet-0b60e428719a2088e
EC2 Metadata Http Tokens: optional
Role (STS) ARN: arn:aws:iam::301721915996:role/pkjhukiecuqvpey-HCP-ROSA-Installer-Role
Support Role ARN: arn:aws:iam::301721915996:role/pkjhukiecuqvpey-HCP-ROSA-Support-Role
Instance IAM Roles:
- Worker: arn:aws:iam::301721915996:role/pkjhukiecuqvpey-HCP-ROSA-Worker-Role
Operator IAM Roles:
- arn:aws:iam::301721915996:role/pkjhukiecuqvpey-oper-kube-system-kms-provider
- arn:aws:iam::301721915996:role/pkjhukiecuqvpey-oper-kube-system-kube-controller-manager
- arn:aws:iam::301721915996:role/pkjhukiecuqvpey-oper-kube-system-capa-controller-manager
- arn:aws:iam::301721915996:role/pkjhukiecuqvpey-oper-openshift-image-registry-installer-cloud-cr
- arn:aws:iam::301721915996:role/pkjhukiecuqvpey-oper-openshift-ingress-operator-cloud-credential
- arn:aws:iam::301721915996:role/pkjhukiecuqvpey-oper-openshift-cluster-csi-drivers-ebs-cloud-cre
- arn:aws:iam::301721915996:role/pkjhukiecuqvpey-oper-openshift-cloud-network-config-controller-c
- arn:aws:iam::301721915996:role/pkjhukiecuqvpey-oper-kube-system-control-plane-operator
Managed Policies: Yes
State: waiting (Waiting for user action)
Private: No
Delete Protection: Disabled
Created: Sep 24 2024 05:12:58 UTC
User Workload Monitoring: Enabled
Details Page: https://console.dev.redhat.com/openshift/details/s/2mVHMjPeGS0iBvwrmHVKh14V2Mk
OIDC Endpoint URL: https://oidc.os1.devshift.org/2dtfcjodgkc23b9va3iidm8im3vheal4 (Managed)
Audit Log Forwarding: Disabled
External Authentication: Disabled
Etcd Encryption: Disabled
Registry Configuration:
- Allowed Registries: insecure1.io,insecure2.io,insecure3.io
- Insecure Registries: insecure7.io,insecure6.io
- Allowed Registries for Import:
- Domain Name: test.com
- Insecure: true
- Domain Name: test2.com
- Insecure: false

## Step

Describe cluster to check registry config value
```bash
rosa describe cluster -c <>
```

## Expect

-All configured value should be shown
...
Registry Configuration:
- Allowed Registries: insecure1.io,insecure2.io,insecure3.io
- Insecure Registries: insecure7.io,insecure6.io
- Allowed Registries for Import:
- Domain Name: test.com
- Insecure: true
- Domain Name: test2.com
- Insecure: false
...
