# Setup
Before OCM-9166, it will failed with 500 error when using duplicated account-roles or operator-roles arns during cluster creation.  
500 error from cs cid='2c8hjp8up0fiib6imtrbl6ab82ipr40h'] An error occurred trying to persist role policy bindings for cluster '2c8hjp8up0fiib6imtrbl6ab82ipr40h': pq: duplicate key value violates unique constraint "aws_rpb_clusters_roles_pkey"

# Test

## Step
Create account-roles and operator-roles for testing

## Expect

## Step
Create cluster via command, using same support arn for 'controlplane-iam-role' value.  
\# ./rosa create cluster --cluster-name yuwan-0702s1 --sts --mode auto --role-arn arn:aws:iam::301721915996:role/yw0701accr-Installer-Role --support-role-arn arn:aws:iam::301721915996:role/yw0701accr-Support-Role --controlplane-iam-role arn:aws:iam::301721915996:role/yw0701accr-Support-Role --worker-iam-role arn:aws:iam::301721915996:role/yw0701accr-Worker-Role --operator-roles-prefix yuwan-0702s1-kgjn --region us-east-2 -y

## Expect
E: ROSA IAM roles must have unique ARNs and should not be shared with other IAM roles within the same cluster. Duplicated ARN: arn:aws:iam::301721915996:role/yw0701accr-Support-Role

## Step
Create cluster via command, using some duplicated operator-roles arn.  
NOTE: '--operator-iam-roles' has been deprecated, this step is compatibility testing for old version rosacli.  
  
\# ./rosa create cluster --cluster-name yuwan-0702h1 --sts --mode auto --role-arn arn:aws:iam::301721915996:role/yw0702accr-HCP-ROSA-Installer-Role --support-role-arn arn:aws:iam::301721915996:role/yw0702accr-HCP-ROSA-Support-Role --worker-iam-role arn:aws:iam::301721915996:role/yw0702accr-HCP-ROSA-Worker-Role --oidc-config-id 2c67dd8ir8aqjk82q5oqakt69gj9u5sd --region us-west-2 --replicas 3 --compute-machine-type m5.xlarge --machine-cidr 10.0.0.0/16 --service-cidr 172.30.0.0/16 --pod-cidr 10.128.0.0/14 --host-prefix 23 --subnet-ids subnet-077720ef25355f90f,subnet-068e52aca21b8d765,subnet-0dfcb389edfab560f,subnet-0789dcc39fde09492,subnet-0391021de7f51c120,subnet-057d3a5bf78e6464a --hosted-cp --billing-account 301721915996 -y --operator-iam-roles "cloud-credentials,openshift-cloud-network-config-controller,arn:aws:iam::301721915996:role/yw0702shareoph1-openshift-cloud-network-config-controller-cloud-" --operator-iam-roles "installer-cloud-credentials,openshift-image-registry,arn:aws:iam::301721915996:role/yw0702shareoph1-openshift-image-registry-installer-cloud-credent" --operator-iam-roles "cloud-credentials,openshift-ingress-operator,arn:aws:iam::301721915996:role/yw0702shareoph1-openshift-ingress-operator-cloud-credentials" --operator-iam-roles "ebs-cloud-credentials,openshift-cluster-csi-drivers,arn:aws:iam::301721915996:role/yw0702shareoph1-kube-system-capa-controller-manager" --operator-iam-roles "kube-controller-manager,kube-system,arn:aws:iam::301721915996:role/yw0702shareoph1-kube-system-kube-controller-manager" --operator-iam-roles "capa-controller-manager,kube-system,arn:aws:iam::301721915996:role/yw0702shareoph1-kube-system-capa-controller-manager" --operator-iam-roles "control-plane-operator,kube-system,arn:aws:iam::301721915996:role/yw0702shareoph1-kube-system-control-plane-operator" --operator-iam-roles "kms-provider,kube-system,arn:aws:iam::301721915996:role/yw0702shareoph1-kube-system-kms-provider"

## Expect
E: ROSA IAM roles must have unique ARNs and should not be shared with other IAM roles within the same cluster. Duplicated ARN: arn:aws:iam::301721915996:role/yw0702shareoph1-kube-system-capa-controller-manager
