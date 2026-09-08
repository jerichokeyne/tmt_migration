# Setup
Account worker role is required to have policy 'arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly' attached  
  
Clone terraform file from: https://github.com/dustman9000/rosa-hcp-zero-egress-terraform.git

# Test

## Step
1. Use terraform file to setup vpc   
terraform init  
terraform apply

## Expect
Output will include private subnet IDs and vpc_id  
private_subnet_ids = "[\"subnet-04601c71dd4bcd966\",\"subnet-0ca2b2373af87c24d\",\"subnet-01ac219ffc5660c64\"]"  
vpc_id = "vpc-0e3e1fede9a5e2e9c"

## Step
2. Create an HCP cluster with zero-egress properties enabled   
  
rosa create cluster --cluster-name my-hcp-cluster --mode auto --role-arn arn:aws:iam::301721915996:role/$installer-role --support-role-arn arn:aws:iam::301721915996:role/$support-role --worker-iam-role arn:aws:iam::301721915996:role/$worker-role --operator-roles-prefix $prefix --oidc-config-id $oidc --region us-west-2 --replicas 3 --compute-machine-type m5.xlarge --machine-cidr 10.0.0.0/16 --service-cidr 172.30.0.0/16 --pod-cidr 10.128.0.0/14 --host-prefix 23 --subnet-ids $subnet_ids --hosted-cp --billing-account 301721915996 --properties zero_egress:true --private

## Expect
Cluster is created

## Step
3. Once cluster is created, verify that the cluster is set to zero_egress true  
  
ocm get /api/clusters_mgmt/v1/clusters/$cluster_id

## Expect
"properties": {  
"rosa_cli_version":"1.2.45",  
"rosa_creator_arn":"arn:aws:iam::301721915996:user/$user",  
"zero_egress":"true"  
}

## Step
4. Create a new machinepool on the cluster  
  
rosa create machinepool --name=$name -c $cluster

## Expect
I: Checking available instance types for machine pool 'mp-1'  
I: Machine pool 'mp-1' created successfully on hosted cluster 'my-hcp-cluster'

## Step
5. List machinepools associated with the cluster  
  
rosa list machinepools -c $cluster

## Expect
ID AUTOSCALING REPLICAS INSTANCE TYPE LABELS TAINTS AVAILABILITY ZONE SUBNET DISK SIZE VERSION AUTOREPAIR  
mp-1 Yes 0/5-20 m5.xlarge us-west-2a subnet-04601c71dd4bcd966 300 GiB 4.14.35 Yes  
workers-0 No 1/1 m5.xlarge us-west-2c subnet-01ac219ffc5660c64 300 GiB 4.14.35 Yes  
workers-1 No 1/1 m5.xlarge us-west-2a subnet-04601c71dd4bcd966 300 GiB 4.14.35 Yes  
workers-2 No 1/1 m5.xlarge us-west-2b subnet-0ca2b2373af87c24d 300 GiB 4.14.35 Yes

## Step
6. Create cluster admin  
  
rosa create admin -c $cluster

## Expect
Admin is created with login command

## Step
7. Create bastion host using this guide (requires a special config compared to normal bastion creation)  
<https://docs.google.com/document/d/1L_DiggdYDE4bWiFh7dyfDj-2_Y-9sf2twkJr0--i31g/edit#heading=h.t200wyeqawjk>

## Expect
Bastion host is created

## Step
8. SSH into bastion host  
  
ssh -i "jf-ze-keypair.pem" ec2-user@ec2-34-209-64-40.us-west-2.compute.amazonaws.com

## Expect
Able to ssh

## Step
9. Login to cluster  
  
oc login https://api.my-hcp-cluster.tnv2.s3.devshift.org:443 --username cluster-admin --password mUNKF-qfYgh-q2SrX-QewxU

## Expect
Able to login to cluster

## Step
10. Follow steps in this guide to install OC on cluster  
<https://docs.google.com/document/d/1QJphA-7bam0D9T2DtKpmOMV1bE8h-2o9f8Cd7b5g25g/edit>

## Expect
Able to install OC

## Step
11. Verify operators are up and available  
  
oc get co

## Expect
NAME VERSION AVAILABLE PROGRESSING DEGRADED SINCE MESSAGE  
console 4.14.35 True False False 15m  
csi-snapshot-controller 4.14.35 True False False 24m  
dns 4.14.35 True False False 16m  
image-registry 4.14.35 True False False 15m  
ingress 4.14.35 True False False 15m  
insights 4.14.35 True False False 17m  
kube-apiserver 4.14.35 True False False 24m  
kube-controller-manager 4.14.35 True False False 24m  
kube-scheduler 4.14.35 True False False 24m  
kube-storage-version-migrator 4.14.35 True False False 6m53s  
monitoring 4.14.35 True False False 14m  
network 4.14.35 True False False 24m  
node-tuning 4.14.35 True False False 18m  
openshift-apiserver 4.14.35 True False False 24m  
openshift-controller-manager 4.14.35 True False False 24m  
openshift-samples 4.14.35 True False False 5m42s  
operator-lifecycle-manager 4.14.35 True False False 24m  
operator-lifecycle-manager-catalog 4.14.35 True False False 24m  
operator-lifecycle-manager-packageserver 4.14.35 True False False 24m  
service-ca 4.14.35 True False False 17m  
storage 4.14.35 True False False 18m

## Step
12. Verify nodes are up and available  
  
oc get nodes

## Expect
NAME STATUS ROLES AGE VERSION  
ip-10-0-0-28.us-west-2.compute.internal Ready worker 11m v1.27.16+e826056  
ip-10-0-1-145.us-west-2.compute.internal Ready worker 19m v1.27.16+e826056  
ip-10-0-2-241.us-west-2.compute.internal Ready worker 16m v1.27.16+e826056

## Step
13. Get the containers  
  
oc get po -owide -A

## Expect
NAMESPACE NAME READY STATUS RESTARTS AGE IP NODE NOMINATED NODE READINESS GATES  
kube-system konnectivity-agent-czbrd 1/1 Running 0 17m 10.0.2.241 ip-10-0-2-241.us-west-2.compute.internal <none> <none>  
kube-system konnectivity-agent-rn2qt 1/1 Running 0 20m 10.0.1.145 ip-10-0-1-145.us-west-2.compute.internal <none> <none>  
kube-system konnectivity-agent-xbssn 1/1 Running 0 11m 10.0.0.28 ip-10-0-0-28.us-west-2.compute.internal <none> <none>  
kube-system kube-apiserver-proxy-ip-10-0-0-28.us-west-2.compute.internal 1/1 Running 0 11m 10.0.0.28 ip-10-0-0-28.us-west-2.compute.internal <none> <none>  
kube-system kube-apiserver-proxy-ip-10-0-1-145.us-west-2.compute.internal 1/1 Running 0 20m 10.0.1.145 ip-10-0-1-145.us-west-2.compute.internal <none> <none>  
kube-system kube-apiserver-proxy-ip-10-0-2-241.us-west-2.compute.internal 1/1 Running 0 16m 10.0.2.241 ip-10-0-2-241.us-west-2.compute.internal <none> <none>

## Step
14. Verify that a pod cannot connect to quay.io mirror  
  
Swap to a pod project  
oc project openshift-network-diagnostics  
  
Log into container  
oc exec -it network-check-source-5649b59557-kmhh6 /bin/bash  
  
Check that quay.io is inaccessible

## Expect
Now using project "openshift-network-diagnostics" on server "https://api.jf-hcp-ze.73fd.s3.devshift.org:443".  
  
bash-4.4$ curl quay.io -v  
* Rebuilt URL to: quay.io/  
* Trying 54.85.105.227...  
* TCP_NODELAY set  
* Trying 2600:1f18:483:cf01:2fb9:340b:43cd:957...  
* TCP_NODELAY set  
* Immediate connect fail for 2600:1f18:483:cf01:2fb9:340b:43cd:957: Network is unreachable  
* Trying 2600:1f18:483:cf01:dafc:d2:315f:6064...  
* TCP_NODELAY set  
* Immediate connect fail for 2600:1f18:483:cf01:dafc:d2:315f:6064: Network is unreachable  
* Trying 2600:1f18:483:cf02:312d:8bd3:220f:671f...

## Step
15. Delete cluster

## Expect
