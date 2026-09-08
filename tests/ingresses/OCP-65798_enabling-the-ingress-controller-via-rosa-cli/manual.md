# Test

## Step
(note: It is behind a feature toggle and now it is toggled on for all users on INT/STG env)  
  
1. create new cluster and specify ingress configurations  
$ rosa create cluster --cluster-name=hongli-414 --region=us-west-2 --multi-az --non-sts --version 4.14.0-rc0 --channel-group candidate \  
--default-ingress-route-selector app1=test1,app2=test2 \  
--default-ingress-excluded-namespaces test-ns1,test-ns2 \  
--default-ingress-wildcard-policy WildcardsDisallowed \  
--default-ingress-namespace-ownership-policy Strict

## Expect

## Step
2. waiting fro the cluster is ready, check the output of "rosa list ingress"  
$ rosa list ingress -c <cluster-id>

## Expect
ID APPLICATION ROUTER PRIVATE DEFAULT ROUTE SELECTORS LB-TYPE EXCLUDED NAMESPACE WILDCARD POLICY NAMESPACE OWNERSHIP HOSTNAME TLS SECRET REF  
b8g8 https://apps.hongli-414.1ev0.i1.devshift.org no yes app1=test1, app2=test2 nlb [test-ns1, test-ns2] WildcardsDisallowed Strict

## Step
3. then get kubeadmin credentials  
$ ocm get /api/clusters_mgmt/v1/clusters/<cluster_id>/credentials | jq -r .kubeconfig > rosa-414.kubeconfig  
  
(note: to get credential you need to switch to $SUPER_ADMIN_USER_TOKEN with command:  
$ ocm login --url staging --token $SUPER_ADMIN_USER_TOKEN  
and after get the kubeconfig please switch back to $ORG_MEMBER_TOKEN)

## Expect

## Step
4. login to the cluster with kubeconfig and check ingresscontroller settings.  
$ export KUBECONFIG=~/rosa-414.kubeconfig  
$ oc -n openshift-ingress-operator get ingresscontroller/default -oyaml

## Expect
spec:  
namespaceSelector:  
matchExpressions:  
- key: kubernetes.io/metadata.name  
operator: NotIn  
values:  
- test-ns1  
- test-ns2  
routeAdmission:  
namespaceOwnership: Strict  
wildcardPolicy: WildcardsDisallowed  
routeSelector:  
matchExpressions:  
- key: app1  
operator: NotIn  
values:  
- test1  
- key: app2  
operator: NotIn  
values:  
- test2

## Step
5. (optional) create new clusters with various ingress attributes, after cluster is ready check "rosa list ingresss" and ingresscontroller settings.

## Expect
the "rosa list ingress" and ingresscontroller's setting should be same to the flags

## Step
6. (negative) try to create cluster with ingress attributes on version<=4.13 cluster, e.g  
  
$ rosa create cluster --cluster-name=new-413 --region=us-west-2 --multi-az --non-sts --version=4.13.11 -**-default-ingress-excluded-namespaces=test-ns**

## Expect
E: Failed to create cluster: Cannot supply default ingress attributes on cluster creation for clusters that have legacy ingress

## Step
7. (negative) try to create cluster with ingress attributes on HCP cluster, e.g  
  
$ rosa create cluster -c new-hcp --subnet-ids subnet-0b1d8f65412725851,subnet-0bc5e03848e00d9bb,subnet-0a163a8340f05cd80,subnet-0530d62c9e744d846 --hosted-cp --mode auto --oidc-config-id 256e70rac3q62kik3let80lnrk5ome9t **--default-ingress-namespace-ownership-policy InterNamespaceAllowed**

## Expect
E: Updating Namespace Ownership Policy is not supported for Hosted Control Plane clusters

# Cleanup
*
