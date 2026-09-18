# Test

## Step

Create a hypershift cluster via rosacli
```bash
rosa create cluster --sts --hosted-cp --version 4.11.6 -c xuelihp2 --region us-west-2 --subnet-ids subnet-0465497173d6a8be7,subnet-05e11e7f9393b3600
```

## Expect

The cluster will be created successfully

## Step

Describe the cluster detail
```bash
rosa describe cluster -c xuelihp2
```

## Expect

- There will be detailed information showed
- There is information show "Control Plane: ROSA Service Hosted "
- There is no nodes section instead NodePools
- No Nodes.Control plane and Nodes.infra sections- Under NodePools, list each NodePool with

  * NodePool name
  * AZ
  * If non-autoscaling: replica count
  * If autoscaling: min-max values


[xueli@xueli-work rosa]$ rosa describe cluster -c xuelihp2
Name: xuelihp2
ID: 1v7e8f6lgft45uakb4pvec1qagqmf3m7
External ID:
Control Plane: ROSA Service Hosted
OpenShift Version:
Channel Group: stable
DNS: xuelihp2.
AWS Account:
API URL:
Console URL:
Region: us-west-2
Multi-AZ: false
Availability:
- Control Plane: MultiAZ
- Data Plane: SingleAZ
Nodes:
- Compute (desired): 2
- Compute (current): 0
Network:
- Type: OVNKubernetes
- Service CIDR: 172.30.0.0/16
- Machine CIDR: 10.0.0.0/16
- Pod CIDR: 10.128.0.0/14
- Host Prefix: /23
STS Role ARN: arn:aws:iam::301721915996:role/test/xue/xueli-Installer-Role
Support Role ARN: arn:aws:iam::301721915996:role/test/xue/xueli-Support-Role
Instance IAM Roles:
- Control plane: arn:aws:iam::301721915996:role/test/xue/xueli-ControlPlane-Role
- Worker: arn:aws:iam::301721915996:role/test/xue/xueli-Worker-Role
Operator IAM Roles:
- arn:aws:iam::301721915996:role/test/xue/xuelihp2-n8w9-openshift-cloud-credential-operator-cloud-credenti
- arn:aws:iam::301721915996:role/test/xue/xuelihp2-n8w9-openshift-image-registry-installer-cloud-credentia
- arn:aws:iam::301721915996:role/test/xue/xuelihp2-n8w9-openshift-ingress-operator-cloud-credentials
- arn:aws:iam::301721915996:role/test/xue/xuelihp2-n8w9-openshift-cluster-csi-drivers-ebs-cloud-credential
- arn:aws:iam::301721915996:role/test/xue/xuelihp2-n8w9-kube-system-control-plane-operator
- arn:aws:iam::301721915996:role/test/xue/xuelihp2-n8w9-openshift-cloud-network-config-controller-cloud-cr
- arn:aws:iam::301721915996:role/test/xue/xuelihp2-n8w9-kube-system-kube-controller-manager
- arn:aws:iam::301721915996:role/test/xue/xuelihp2-n8w9-openshift-machine-api-aws-cloud-credentials
- arn:aws:iam::301721915996:role/test/xue/xuelihp2-n8w9-kube-system-capa-controller-manager
State: waiting (failed to assume role: operation error STS: AssumeRole, https response error StatusCode: 403, RequestID: 1b7dd71e-90eb-4308-b7cb-fa20606a21b6, api error AccessDenied: User: arn:aws:sts::644306948063:assumed-role/RH-Managed-OpenShift-Installer/OCM is not authorized to perform: sts:AssumeRole on resource: arn:aws:iam::301721915996:role/test/xue/xueli-Installer-Role)
Private: No
Created: Oct 8 2022 08:18:06 UTC
Details Page: https://qaprodauth.console.redhat.com/openshift/details/s/2FqQMQERvZoJwwQ4npooRF2h4sE
OIDC Endpoint URL: https://d3gt1gce2zmg3d.cloudfront.net/1v7e8f6lgft45uakb4pvec1qagqmf3m7
