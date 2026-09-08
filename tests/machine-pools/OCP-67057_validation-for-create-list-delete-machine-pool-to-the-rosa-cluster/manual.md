# Setup
Create hosted cluster:  
rosa create cluster --cluster-name eld2 --sts --role-arn arn:aws:iam::425464789085:role/eld2-Installer-Role --support-role-arn arn:aws:iam::425464789085:role/eld2-Support-Role --controlplane-iam-role arn:aws:iam::425464789085:role/eld2-ControlPlane-Role --worker-iam-role arn:aws:iam::425464789085:role/eld2-Worker-Role --operator-roles-prefix eld2-label-13bg129-q0w0 --region ap-southeast-3 --compute-machine-type m5.xlarge --machine-cidr 10.0.0.0/16 --service-cidr 172.30.0.0/16 --subnet-ids subnet-0ef71fb42b20cc43c,subnet-0c28fe19063b652f1 --properties cert-manager:use --hosted-cp --version 4.12.23

# Test

## Step
Create hosted cluster

## Expect
it will succeed

## Step
Enter special value for machine pool name:  
Machine pool name: !!!!!!

## Expect
X Sorry, your reply was invalid: !!! does not match regular expression ^[a-z]([-a-z0-9]*[a-z0-9])?$

## Step
Enter special value for replicas:  
-1

## Expect
X Sorry, your reply was invalid: min-replicas must be greater than zero

## Step
Enter incorrect format for labels:  
Labels: x3561516!!

## Expect
X Sorry, your reply was invalid: Expected key=value format for labels

## Step
Enter incorrect format for Taints:  
Taints: x3561516!!

## Expect
X Sorry, your reply was invalid: Expected key=value:scheduleType format for taints. Got 'x3561516'

## Step
Enter any value for Y/N question, such as:  
Autorepair: 00110

## Expect
X Sorry, your reply was invalid: "0" is not a valid answer, please try again.
