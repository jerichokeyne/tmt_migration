# Test

## Step
(note: It is behind a feature toggle so far, please ensure your org ID is '1jIMvDrxDv8pPUDJ71t7rLGRtLf' and test in integration env)  
  
1. ensure a ROSA/OSD cluster is ready (version >= 4.14)

## Expect

## Step
2. rosa list the default ingresscontroller attributes.  
$ rosa list ingress -c <cluster-id>

## Expect
ID APPLICATION ROUTER PRIVATE DEFAULT ROUTE SELECTORS LB-TYPE EXCLUDED NAMESPACE WILDCARD POLICY NAMESPACE OWNERSHIP HOSTNAME TLS SECRET REF  
b8g8 https://apps.hongli-413.1ev0.i1.devshift.org no yes nlb WildcardsDisallowed Strict

## Step
3. update the default ingress attributes via rosa CLI  
$ rosa edit ingress apps -c hongli-413 --excluded-namespaces test-ns1,test-ns2 --route-selector app1=test1,app2=test2 --namespace-ownership-policy Strict --wildcard-policy WildcardsDisallowed

## Expect
no error

## Step
Verify the updating of the configuration via rosacli  
$ rosa list ingress -c hongli-413

## Expect
Verify that  
The excluded namespaces had been changed to test-ns1,test-ns2  
The route-selector had been changed to app1=test1,app2=test2  
The namespace ownership policy had been changed to Strict  
The wildcard policy had been changed to WildcardsDisallowed

## Step
~~4. Get the kubeconfig and login the cluster~~

## Expect

## Step
~~5. Check the default ingressconroller 's setting~~

## Expect
~~spec: namespaceSelector: matchExpressions: - key: kubernetes.io/metadata.name operator: NotIn values: - test-ns1 - test-ns2 routeAdmission: namespaceOwnership: Strict wildcardPolicy: WildcardsDisallowed routeSelector: matchExpressions: - key: app1 operator: NotIn values: - test1 - key: app2 operator: NotIn values: - test2~~

## Step
6. change some ingress attributes via rosa CLI  
$ rosa edit ingress apps -c hongli-413 --excluded-namespaces test-ns1 --route-selector app1=test1 --namespace-ownership-policy InterNamespaceAllowed --wildcard-policy WildcardsAllowed

## Expect
no error

## Step
7. Describe the settings of the ingress via rosa CLI  
$ rosa list ingress -c hongli-413

## Expect
The settings had been updated to the value updated~~spec: namespaceSelector: matchExpressions: - key: kubernetes.io/metadata.name operator: NotIn values: - test-ns1 routeAdmission: namespaceOwnership: InterNamespaceAllowed wildcardPolicy: WildcardsAllowed routeSelector: matchExpressions: - key: app1 operator: NotIn values: - test1~~

## Step
8. (this part should be automated in backend) Check the service log to ensure all operations are logged properly.  
$ ocm get /api/service_logs/v1/cluster_logs -p search="cluster_id=<cluster id>"

## Expect

## Step
9. (negative)Try to edit the ingress attributes on version<=4.12 cluster  
  
$ rosa edit ingress apps -c hongli-412 --namespace-ownership-policy InterNamespaceAllowed  
  
$ rosa edit ingress apps -c hongli-412 --route-selector "foo=bar"

## Expect
E: Failed to update ingress 'y6l7' on cluster 'hongli-412': Can't update route namespace ownership policy on legacy supported ingress 'y6l7' in cluster '2571urk8nr36st5j68fs59al857eb79n'  
  
E: Failed to update ingress 'y6l7' on cluster 'hongli-412': Can't update route selectors to default ingress 'y6l7' in cluster '2571urk8nr36st5j68fs59al857eb79n'

## Step
10. (negative) Try to edit the ingress on HCP cluster, e.g  
  
$ rosa edit ingress apps -c hongli-hcp --wildcard-policy WildcardsAllowed  
  
$ rosa edit ingress apps -c hongli-hcp --excluded-namespaces test-ns

## Expect
E: Updating Wildcard Policy is not supported for Hosted Control Plane clusters  
  
E: Updating excluded namespace is not supported for Hosted Control Plane clusters  
  
...
