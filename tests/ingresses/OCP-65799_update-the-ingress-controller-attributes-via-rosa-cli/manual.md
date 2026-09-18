# Test

## Step

1. Ensure a ROSA/OSD cluster is ready (version >= `4.14`). This test is behind a feature toggle; use organization ID `1jIMvDrxDv8pPUDJ71t7rLGRtLf` in the integration environment.

## Expect

## Step

2. List the default ingress controller attributes.

```bash
rosa list ingress -c <cluster-id>
```

## Expect

```
ID APPLICATION ROUTER PRIVATE DEFAULT ROUTE SELECTORS LB-TYPE EXCLUDED NAMESPACE WILDCARD POLICY NAMESPACE OWNERSHIP HOSTNAME TLS SECRET REF
b8g8 https://apps.hongli-413.1ev0.i1.devshift.org no yes nlb WildcardsDisallowed Strict
```

## Step

3. Update the default ingress attributes via the ROSA CLI.

```bash
rosa edit ingress apps -c hongli-413 --excluded-namespaces test-ns1,test-ns2 --route-selector app1=test1,app2=test2 --namespace-ownership-policy Strict --wildcard-policy WildcardsDisallowed
```

## Expect

No error.

## Step

4. Verify the updated configuration via the ROSA CLI.

```bash
rosa list ingress -c hongli-413
```

## Expect

- The excluded namespaces are `test-ns1,test-ns2`.
- The route selector is `app1=test1,app2=test2`.
- The namespace ownership policy is `Strict`.
- The wildcard policy is `WildcardsDisallowed`.

## Step

~~5. Get the kubeconfig and log in to the cluster.~~

## Expect

## Step

~~6. Check the default ingresscontroller setting.~~

## Expect

```yaml
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
```

## Step

7. Change ingress attributes via the ROSA CLI.

```bash
rosa edit ingress apps -c hongli-413 --excluded-namespaces test-ns1 --route-selector app1=test1 --namespace-ownership-policy InterNamespaceAllowed --wildcard-policy WildcardsAllowed
```

## Expect

No error.

## Step

8. Describe the ingress settings via the ROSA CLI.

```bash
rosa list ingress -c hongli-413
```

## Expect

The settings are updated to:

```yaml
spec:
  namespaceSelector:
    matchExpressions:
    - key: kubernetes.io/metadata.name
      operator: NotIn
      values:
      - test-ns1
  routeAdmission:
    namespaceOwnership: InterNamespaceAllowed
    wildcardPolicy: WildcardsAllowed
  routeSelector:
    matchExpressions:
    - key: app1
      operator: NotIn
      values:
      - test1
```

## Step

9. Check the service log to ensure all operations are logged properly. This part should be automated in the backend.

```bash
ocm get /api/service_logs/v1/cluster_logs -p search="cluster_id=<cluster id>"
```

## Expect

## Step

10. Try to edit ingress attributes on a version <= `4.12` cluster.

```bash
rosa edit ingress apps -c hongli-412 --namespace-ownership-policy InterNamespaceAllowed
rosa edit ingress apps -c hongli-412 --route-selector "foo=bar"
```

## Expect

```
E: Failed to update ingress 'y6l7' on cluster 'hongli-412': Can't update route namespace ownership policy on legacy supported ingress 'y6l7' in cluster '2571urk8nr36st5j68fs59al857eb79n'

E: Failed to update ingress 'y6l7' on cluster 'hongli-412': Can't update route selectors to default ingress 'y6l7' in cluster '2571urk8nr36st5j68fs59al857eb79n'
```

## Step

11. Try to edit ingress attributes on an HCP cluster.

```bash
rosa edit ingress apps -c hongli-hcp --wildcard-policy WildcardsAllowed
rosa edit ingress apps -c hongli-hcp --excluded-namespaces test-ns
```

## Expect

```
E: Updating Wildcard Policy is not supported for Hosted Control Plane clusters

E: Updating excluded namespace is not supported for Hosted Control Plane clusters

...
```
