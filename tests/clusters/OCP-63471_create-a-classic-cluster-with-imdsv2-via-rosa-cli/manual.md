# Setup
<https://issues.redhat.com/browse/OCM-140>

# Test

## Step
Login with rosa cli, rosa token: https://console.redhat.com/openshift/token/rosa/show  
$ rosa login -env staging --token=

## Expect
Success

## Step
Create the account roles  
$ rosa create account-roles --mode auto -y --prefix zhsun-rosa1

## Expect
Success

## Step
Create cluster with httpTokens=Required and version>=4.11  
$ rosa create cluster --sts -c zhsun-rosa1 --mode auto --ec2-metadata-http-tokens=required

## Expect
Could set up cluster successful, all token are set to required.  
Bootstrap node is still optional, as bug <https://issues.redhat.com/browse/OCPBUGS-13086> hasn't backport to 4.12.  
\# aws ec2 describe-instances --instance-ids i-0eb91c952b3818521 --region us-east-2 --output json | jq .Reservations[].Instances[].MetadataOptions.HttpTokens  
"optional"  
  
$ oc get node   
NAME STATUS ROLES AGE VERSION  
ip-10-0-152-40.us-east-2.compute.internal Ready worker 46m v1.25.8+37a9a08  
ip-10-0-166-73.us-east-2.compute.internal Ready worker 46m v1.25.8+37a9a08  
ip-10-0-172-253.us-east-2.compute.internal Ready control-plane,master 54m v1.25.8+37a9a08  
ip-10-0-181-164.us-east-2.compute.internal Ready infra,worker 26m v1.25.8+37a9a08  
ip-10-0-186-101.us-east-2.compute.internal Ready infra,worker 26m v1.25.8+37a9a08  
ip-10-0-201-192.us-east-2.compute.internal Ready control-plane,master 54m v1.25.8+37a9a08  
ip-10-0-231-194.us-east-2.compute.internal Ready control-plane,master 54m v1.25.8+37a9a08  
  
$ instanceId=$(oc get machine -n openshift-machine-api -o jsonpath="{.items[*].status.providerStatus.instanceId}")  
$ arr=(${instanceId//,/})  
$ for i in "${arr[@]}"; do aws ec2 describe-instances --instance-ids $i --region us-east-2 --output json |jq .Reservations[].Instances[].MetadataOptions.HttpTokens; done  
"required"  
"required"  
"required"  
"required"  
"required"  
"required"  
"required"

## Step
Create cluster with httpTokens=Optional and version>=4.11  
$ rosa create cluster --sts -c zhsun-rosa1 --mode auto --ec2-metadata-http-tokens=optional

## Expect
Could set up cluster successful, all token are set to optional.  
$ instanceId=$(oc get machine -n openshift-machine-api -o jsonpath="{.items[*].status.providerStatus.instanceId}")  
$ arr=(${instanceId//,/})  
$ for i in "${arr[@]}"; do aws ec2 describe-instances --instance-ids $i --region us-east-2 --output json |jq .Reservations[].Instances[].MetadataOptions.HttpTokens; done  
"optional"  
"optional"  
"optional"  
"optional"  
"optional"  
"optional"  
"optional"

## Step
Create cluster with httpTokens=Optional and version<4.11  
$ rosa create cluster --sts -c zhsun-imdso10 --mode auto --ec2-metadata-http-tokens=optional --version=4.10

## Expect
Success  
$ ocm list cluster | grep zhsun   
23no2k3o1a8vk3fs9pbej1r6fq630lno zhsun-imdso10 https://api.zhsun-imdso10.kntp.s1.devshift.org:6443 4.10.59 rosa aws us-east-2 ready

## Step
Create cluster with no httpTokens specified  
$ rosa create cluster --sts -c zhsun-imdsr10 --mode auto --ec2-metadata-http-tokens="" --version=4.11.39

## Expect
Cluster should be created succeesful, token should be optional by default  
$ ocm list cluster | grep zhsun   
23no71ik0lpms5vobhlla6gq4v9tr4re zhsun-imdsr10 https://api.zhsun-imdsr10.9pep.s1.devshift.org:6443 4.11.39 rosa aws us-east-2 ready

## Step
Create day2 machinepool  
$ rosa create machinepool -c zhsun-imdsr

## Expect
Should match from the cluster  
$ oc get machine -n openshift-machine-api   
NAME PHASE TYPE REGION ZONE AGE  
zhsun-imdsr-pqf8j-infra-us-east-2a-6cxmr Running r5.xlarge us-east-2 us-east-2a 42m  
zhsun-imdsr-pqf8j-infra-us-east-2a-95pcc Running r5.xlarge us-east-2 us-east-2a 42m  
zhsun-imdsr-pqf8j-master-0 Running m5.2xlarge us-east-2 us-east-2a 68m  
zhsun-imdsr-pqf8j-master-1 Running m5.2xlarge us-east-2 us-east-2a 68m  
zhsun-imdsr-pqf8j-master-2 Running m5.2xlarge us-east-2 us-east-2a 68m  
zhsun-imdsr-pqf8j-worker-us-east-2a-98x28 Running m5.xlarge us-east-2 us-east-2a 64m  
zhsun-imdsr-pqf8j-worker-us-east-2a-qcq9q Running m5.xlarge us-east-2 us-east-2a 64m  
zhsun-imdsr-pqf8j-zhsun-imdsr1-us-east-2a-bljj4 Running m5.xlarge us-east-2 us-east-2a 4m33s  
$ oc get machine -n openshift-machine-api zhsun-imdsr-pqf8j-zhsun-imdsr1-us-east-2a-bljj4 -o yaml | grep instanceId   
instanceId: i-03081bfe8d004ccbe  
\# aws ec2 describe-instances --instance-ids i-03081bfe8d004ccbe --region us-east-2 --output json |jq .Reservations[].Instances[].MetadataOptions.HttpTokens  
"required"

## Step
Update machinepool/machineset?  
$ oc edit machineset zhsun-imdsr-pqf8j-zhsun-imdsr1-us-east-2a  
metadataServiceOptions:  
authentication: Optional

## Expect
Field should be immutable for day2  
cluster-admin:  
$ rosa create admin -c zhsun-imdsr  
$ oc login https://api.zhsun-imdsr.01sp.s1.devshift.org:6443 --username cluster-admin --password 4qAed-XXX  
$ oc edit machineset zhsun-imdsr-pqf8j-zhsun-imds2-us-east-2a   
error: machinesets.machine.openshift.io "zhsun-imdsr-pqf8j-zhsun-imds2-us-east-2a" could not be patched: admission webhook "regular-user-validation.managed.openshift.io" denied the request: Prevented from accessing Red Hat managed resources. This is in an effort to prevent harmful actions that may cause unintended consequences or affect the stability of the cluster. If you have any questions about this, please reach out to Red Hat support at https://access.redhat.com/support  
  
kubeadmin:  
\# aws ec2 describe-instances --instance-ids i-033ee004e0517c7ca --region us-east-2 --output json |jq .Reservations[].Instances[].MetadataOptions.HttpTokens  
"optional"
