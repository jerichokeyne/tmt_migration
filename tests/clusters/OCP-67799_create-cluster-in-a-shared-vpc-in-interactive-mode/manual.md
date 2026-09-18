# Test

## Step

(For reference) Shared VPC STS cluster steps
<https://docs.google.com/document/d/1cJbD_3OkIXTnmCFoKspFq89sXUfZo-blgRe8_o6xhOo/edit>

## Expect

## Step

Create shared-vpc cluster in interactive mode using default operator prefix

? Cluster name: yunjiang-25a
? Deploy cluster with Hosted Control Plane: No
? Create cluster admin user: No
W: In a future release STS will be the default mode.
W: --sts flag won't be necessary if you wish to use STS.
W: --non-sts/--mint-mode flag will be necessary if you do not wish to use STS.
? OpenShift version: 4.13.17
? Configure the use of IMDSv2 for ec2 instances optional/required: optional
W: More than one Installer role found
? Installer role ARN: arn:aws:iam::301721915996:role/yunjiang-25a-Installer-Role
time=2023-10-25T09:49:04+08:00 level=warning msg=Throttling Rate limit exceeded. Retrying the request again
I: Using arn:aws:iam::301721915996:role/yunjiang-25a-Support-Role for the Support role
I: Using arn:aws:iam::301721915996:role/yunjiang-25a-ControlPlane-Role for the ControlPlane role
time=2023-10-25T09:49:11+08:00 level=warning msg=Throttling Rate limit exceeded. Retrying the request again
I: Using arn:aws:iam::301721915996:role/yunjiang-25a-Worker-Role for the Worker role
? External ID (optional):
? Operator roles prefix: yunjiang-25a-t9k7
? Deploy cluster using pre registered OIDC Configuration ID: Yes
? OIDC Configuration ID: 272odkduta6hsbnafdj61dera8rqk5v9 | https://d3gt1gce2zmg3d.cloudfront.net/272odkduta6hsbnafdj61dera8rqk5v9
? Tags (optional):
? Multiple availability zones: No
? AWS region: us-east-1
? PrivateLink cluster: No
? Machine CIDR: 10.0.0.0/16
? Service CIDR: 172.30.0.0/16
? Pod CIDR: 10.128.0.0/14
? Install into an existing VPC: Yes
W: The following subnets were excluded because they belong to a VPC that is managed by Red Hat: [subnet-016a1d6bd34963256, subnet-028f67358f7d5e909, subnet-035b367fc789b8727, subnet-056d76d82d41a1c7c, subnet-09db88f7bdd842c23, subnet-09efa451622271197, subnet-0a6b09a7ee8d05d06, subnet-0b3ea90a0ba9ba332, subnet-0c928de65a906eb39, subnet-0f4ead7b435af9774, subnet-0ff1760dc60061f64]
? Subnet IDs (optional): subnet-006884391bd68d609 ('','vpc-093dc6a086823e549','us-east-1c', Owner ID: '641733028092'), subnet-011ee882240875b7c ('','vpc-093dc6a086823e549','us-east-1c', Owner ID: '641733028092')
I: Subnet with ID 'subnet-006884391bd68d609' is shared by AWS account '641733028092', the cluster will be installed into a shared VPC. For more details https://docs.openshift.com/rosa/rosa_install_access_delete_clusters/rosa-shared-vpc-config.html.
? Private hosted zone ID: Z00076243JZDNG4AFZJP8
? Shared VPC role ARN: arn:aws:iam::641733028092:role/yunjiang-25a-shared-vpc-rol1
? Base Domain: 53kf.s1.devshift.org
? Enable Customer Managed key: No
? Compute nodes instance type: m5.xlarge
? Enable autoscaling: No
? Compute nodes: 2
? Worker machine pool labels (optional):
? Host prefix: 23
? Machine pool root disk size (GiB or TiB): 300 GiB
? Enable FIPS support: No
? Encrypt etcd data: No
? Disable Workload monitoring: No
? Use cluster-wide proxy: No
? Additional trust bundle file path (optional):
I: Creating cluster 'yunjiang-25a'
I: To create this cluster again in the future, you can run:
```bash
rosa create cluster --cluster-name yunjiang-25a --sts --role-arn arn:aws:iam::301721915996:role/yunjiang-25a-Installer-Role --support-role-arn arn:aws:iam::301721915996:role/yunjiang-25a-Support-Role --controlplane-iam-role arn:aws:iam::301721915996:role/yunjiang-25a-ControlPlane-Role --worker-iam-role arn:aws:iam::301721915996:role/yunjiang-25a-Worker-Role --operator-roles-prefix yunjiang-25a-t9k7 --oidc-config-id 272odkduta6hsbnafdj61dera8rqk5v9 --region us-east-1 --version 4.13.17 --replicas 2 --compute-machine-type m5.xlarge --machine-cidr 10.0.0.0/16 --service-cidr 172.30.0.0/16 --pod-cidr 10.128.0.0/14 --host-prefix 23 --subnet-ids subnet-006884391bd68d609,subnet-011ee882240875b7c --private-hosted-zone-id Z00076243JZDNG4AFZJP8 --shared-vpc-role-arn arn:aws:iam::641733028092:role/yunjiang-25a-shared-vpc-rol1 --base-domain 53kf.s1.devshift.org
```
I: To view a list of clusters and their status, run 'rosa list clusters'
E: Failed to create cluster: Failed to find role 'arn:aws:iam::301721915996:role/yunjiang-25a-t9k7-openshift-ingress-operator-cloud-credentials', to create a cluster in shared VPC with a reusable OIDC config, please create the operator roles prior to the cluster creation

## Expect

```
E: Failed to create cluster: Failed to find role 'arn:aws:iam::301721915996:role/yunjiang-25a-t9k7-openshift-ingress-operator-cloud-credentials', to create a cluster in shared VPC with a reusable OIDC config, please create the operator roles prior to the cluster creation
```

## Step

Create shared-vpc cluster in interactive mode

`rosa create cluster --sts -i
I: Interactive mode enabled.
Any optional fields can be left empty and a default will be selected.
? Cluster name: yunjiang-ho
? Deploy cluster with Hosted Control Plane: No
? Create cluster admin user: No
W: In a future release STS will be the default mode.
W: --sts flag won't be necessary if you wish to use STS.
W: --non-sts/--mint-mode flag will be necessary if you do not wish to use STS.
? OpenShift version: 4.13.13
? Configure the use of IMDSv2 for ec2 instances optional/required: optional
W: More than one Installer role found
? Installer role ARN: arn:aws:iam::301721915996:role/yunjiang-ho-Installer-Role
I: Using arn:aws:iam::301721915996:role/yunjiang-ho-ControlPlane-Role for the ControlPlane role
time=2023-09-28T10:36:25+08:00 level=warning msg=Throttling Rate limit exceeded. Retrying the request again
I: Using arn:aws:iam::301721915996:role/yunjiang-ho-Worker-Role for the Worker role
I: Using arn:aws:iam::301721915996:role/yunjiang-ho-Support-Role for the Support role
? External ID (optional):
? Operator roles prefix: yunjiang-ho
? Deploy cluster using pre registered OIDC Configuration ID: Yes
? OIDC Configuration ID: 26fcjvkco5lvqrciq5fu55qvnmc918iq | https://d3gt1gce2zmg3d.cloudfront.net/26fcjvkco5lvqrciq5fu55qvnmc918iq
I: Reusable OIDC Configuration detected. Validating trusted relationships to operator roles:
I: Using 'arn:aws:iam::301721915996:role/yunjiang-ho-openshift-cluster-csi-drivers-ebs-cloud-credentials'
I: Using 'arn:aws:iam::301721915996:role/yunjiang-ho-openshift-cloud-network-config-controller-cloud-cred'
I: Using 'arn:aws:iam::301721915996:role/yunjiang-ho-openshift-machine-api-aws-cloud-credentials'
I: Using 'arn:aws:iam::301721915996:role/yunjiang-ho-openshift-cloud-credential-operator-cloud-credential'
I: Using 'arn:aws:iam::301721915996:role/yunjiang-ho-openshift-image-registry-installer-cloud-credentials'
I: Using 'arn:aws:iam::301721915996:role/yunjiang-ho-openshift-ingress-operator-cloud-credentials'
? Tags (optional):
? Multiple availability zones: No
? AWS region: us-east-1
? PrivateLink cluster: No
? Machine CIDR: 10.0.0.0/16
? Service CIDR: 172.30.0.0/16
? Pod CIDR: 10.128.0.0/14
? Install into an existing VPC: Yes
` `? Subnet IDs (optional): subnet-0ce103770cdb96482 ('','vpc-0bbcf4d627c99e5b1','us-east-1c', Owner ID: '641733028092'), subnet-08e4950127c356a80 ('','vpc-0bbcf4d627c99e5b1','us-east-1c', Owner ID: '641733028092')
I: Subnet with ID 'subnet-0ce103770cdb96482' is shared by AWS account '641733028092', the cluster will be installed into a shared VPC. For more details https://docs.openshift.com/rosa/rosa_install_access_delete_clusters/rosa-shared-vpc-config.html.``
X Sorry, your reply was invalid: Value is required
` `? Private hosted zone ID: Z088936834LJ8JQU618SP
X Sorry, your reply was invalid: Invalid ARN: arn: invalid prefix
? Shared VPC role ARN: arn:aws:iam::641733028092:role/yunjiang-ho-shared-vpc-rol1``
` `? Base Domain: 432j.s1.devshift.org``
? Enable Customer Managed key: No
? Compute nodes instance type: m5.xlarge
? Enable autoscaling: No
? Compute nodes: 2
? Default machine pool labels (optional):
? Host prefix: 23
? Machine pool root disk size (GiB or TiB): 300 GiB
? Enable FIPS support: No
? Encrypt etcd data: No
? Disable Workload monitoring: No
? Use cluster-wide proxy: No
? Additional trust bundle file path (optional):
`

## Expect

1. provide shared subnet ids, follow info is printed:
`Subnet with ID 'subnet-0ce103770cdb96482' is shared by AWS account '641733028092', the cluster will be installed into a shared VPC. For more details https://docs.openshift.com/rosa/rosa_install_access_delete_clusters/rosa-shared-vpc-config.html.`

2. Provide invalid Shared VPC role ARN
`Sorry, your reply was invalid: Invalid ARN: arn: invalid prefix`

## Step

Check output of creating cluster

`I: Creating cluster 'yunjiang-ho'
I: To create this cluster again in the future, you can run:
```bash
rosa create cluster --cluster-name yunjiang-ho --sts --role-arn arn:aws:iam::301721915996:role/yunjiang-ho-Installer-Role --support-role-arn arn:aws:iam::301721915996:role/yunjiang-ho-Support-Role --controlplane-iam-role arn:aws:iam::301721915996:role/yunjiang-ho-ControlPlane-Role --worker-iam-role arn:aws:iam::301721915996:role/yunjiang-ho-Worker-Role --operator-roles-prefix yunjiang-ho --oidc-config-id 26fcjvkco5lvqrciq5fu55qvnmc918iq --region us-east-1 --version 4.13.13 --replicas 2 --compute-machine-type m5.xlarge --machine-cidr 10.0.0.0/16 --service-cidr 172.30.0.0/16 --pod-cidr 10.128.0.0/14 --host-prefix 23 --subnet-ids subnet-0ce103770cdb96482,subnet-08e4950127c356a80 --private-hosted-zone-id Z088936834LJ8JQU618SP --shared-vpc-role-arn arn:aws:iam::641733028092:role/yunjiang-ho-shared-vpc-rol1 --base-domain 432j.s1.devshift.org
```
I: To view a list of clusters and their status, run 'rosa list clusters'
I: Cluster 'yunjiang-ho' has been created.
I: Once the cluster is installed you will need to add an Identity Provider before you can login into the cluster. See 'rosa create idp --help' for more information.


Name: yunjiang-ho
ID: 26h9meu75hkant45q5ithlsk66jmb7h8
External ID:
Control Plane: Customer Hosted
OpenShift Version:
Channel Group: stable
DNS: Not ready
AWS Account: 301721915996
API URL:
Console URL:
Region: us-east-1
Multi-AZ: false
Nodes:
- Control plane: 3
- Infra: 2
- Compute: 2
Network:
- Type: OVNKubernetes
- Service CIDR: 172.30.0.0/16
- Machine CIDR: 10.0.0.0/16
- Pod CIDR: 10.128.0.0/14
- Host Prefix: /23
Workload Monitoring: Enabled
Ec2 Metadata Http Tokens: optional
STS Role ARN: arn:aws:iam::301721915996:role/yunjiang-ho-Installer-Role
Support Role ARN: arn:aws:iam::301721915996:role/yunjiang-ho-Support-Role
Instance IAM Roles:
- Control plane: arn:aws:iam::301721915996:role/yunjiang-ho-ControlPlane-Role
- Worker: arn:aws:iam::301721915996:role/yunjiang-ho-Worker-Role
Operator IAM Roles:
- arn:aws:iam::301721915996:role/yunjiang-ho-openshift-cluster-csi-drivers-ebs-cloud-credentials
- arn:aws:iam::301721915996:role/yunjiang-ho-openshift-cloud-network-config-controller-cloud-cred
- arn:aws:iam::301721915996:role/yunjiang-ho-openshift-machine-api-aws-cloud-credentials
- arn:aws:iam::301721915996:role/yunjiang-ho-openshift-cloud-credential-operator-cloud-credential
- arn:aws:iam::301721915996:role/yunjiang-ho-openshift-image-registry-installer-cloud-credentials
- arn:aws:iam::301721915996:role/yunjiang-ho-openshift-ingress-operator-cloud-credentials
Managed Policies: No
State: waiting (Waiting for OIDC configuration)
Private: No
Created: Sep 28 2023 02:47:25 UTC
Details Page: https://qaprodauth.console.redhat.com/openshift/details/s/2W0UyPTRz4xxYRWGzYoYpWeujot
OIDC Endpoint URL: https://d3gt1gce2zmg3d.cloudfront.net/26fcjvkco5lvqrciq5fu55qvnmc918iq (Managed)
Private Hosted Zone:
- ID: Z088936834LJ8JQU618SP
- Role ARN: arn:aws:iam::641733028092:role/yunjiang-ho-shared-vpc-rol1`


I: When using reusable OIDC Config and resources have been created prior to cluster specification, this step is not required.
Run the following commands to continue the cluster creation:


```bash
rosa create operator-roles --cluster yunjiang-ho
rosa create oidc-provider --cluster yunjiang-ho
```


I: To determine when your cluster is Ready, run 'rosa describe cluster -c yunjiang-ho'.
I: To watch your cluster installation logs, run 'rosa logs install -c yunjiang-ho --watch'.

## Expect

Shared VPC info is printed:
`Private Hosted Zone:
- ID: Z088936834LJ8JQU618SP
- Role ARN: arn:aws:iam::641733028092:role/yunjiang-ho-shared-vpc-rol1`

## Step

Cluster is created successfully.

## Expect

## Step

Following the same process as above
* Do not enable auto mode
* Use default operator prefix which is not created while creating cluster.

## Expect

Cluster will go into wait state, see the last step in

* Manually create operator roles
* Manually create oidc provider
* Manually add ingress operator role to trust police of shared vpc role

cluster will be created successfully

## Step

Following the same process as above,:
* Enable auto mode (-m auto)
* Use default operator prefix which is not created while creating cluster.

## Expect

* operator roles and oidc providers will be created automatically by CS backend
* Manually add ingress operator role to trust police of shared vpc role

cluster will be created successfully
