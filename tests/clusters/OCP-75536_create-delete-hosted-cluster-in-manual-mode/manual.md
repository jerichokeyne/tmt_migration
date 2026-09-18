# Test

## Step

Create a Hosted cluster in manual mode

Example:
./rosa create cluster --cluster-name yuwan-bhs1 --sts --role-arn arn:aws:iam::301721915996:role/yw0921accrhs1-Installer-Role --support-role-arn arn:aws:iam::301721915996:role/yw0921accrhs1-Support-Role --controlplane-iam-role arn:aws:iam::301721915996:role/yw0921accrhs1-ControlPlane-Role --worker-iam-role arn:aws:iam::301721915996:role/yw0921accrhs1-Worker-Role --operator-roles-prefix yuwan-bhs1-h3b1 --region us-west-2 --replicas 2 --subnet-ids <private-subnet-1>,<public-subnet-1> --hosted-cp -y --mode manual

## Expect

Create command should work

## Step

Apply given commands

## Expect

Commands should work

## Step

Wait for cluster & machinepool ready

## Expect

Checklist:
- Cluster ready
- Machinepool ready
- Cluster Operators ready

## Step

Delete the Hypershift cluster by `rosa delete cluster`

## Expect

- The cluster can be deleted
- All resource on AWS should be deleted.

## Step

Delete operator roles

## Expect

- The operator roles are deleted from AWS
- There are readable message shown about the role deletion

## Step

Delete oidc provider

## Expect

- The oidc-provider are deleted from AWS
- There are readable message shown about the oidc-provider deletion
