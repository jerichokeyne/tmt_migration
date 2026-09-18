# Test

## Step

1. Note that additional ingresses cannot be created in staging/INT because `managed-ingress-support` is enabled for all users (from 09/18). Edit and delete additional ingress if present. Editing the default ingress is unchanged. Launch the ROSA CLI in the staging environment.

## Expect

## Step

2. Prepare a ready ROSA cluster.

## Expect

## Step

3. Check the help message for editing an ingress.

```bash
rosa edit ingress --help
```

## Expect

The help message is displayed:

```
Edit a cluster ingress for a cluster.

Usage:
  rosa edit ingress ID [flags]

Aliases:
  ingress, route

Examples:
  # Make additional ingress with ID 'a1b2' private on a cluster named 'mycluster'
  rosa edit ingress --private --cluster=mycluster a1b2

  # Update the router selectors for the additional ingress with ID 'a1b2'
  rosa edit ingress --label-match=foo=bar --cluster=mycluster a1b2

  # Update the default ingress using the sub-domain identifier
  rosa edit ingress --private=false --cluster=mycluster apps

  # Update the load balancer type of the apps2 ingress
  rosa edit ingress --lb-type=nlb --cluster=mycluster apps2

Flags:
  -c, --cluster string                      Name or ID of the cluster.
      --component-routes string             Component route settings. Specify one or more routes to update; routes not specified remain unchanged. Available keys are [oauth, console, downloads] (HCP clusters support console and downloads only). Each route requires a hostname and tlsSecretRef. To clear a route, set both to empty values. Format: 'console: hostname=example-hostname;tlsSecretRef=example-secret-ref,downloads:...'
      --excluded-namespaces string          Excluded namespaces for ingress. Format should be a comma-separated list 'value1, value2...'. If no values are specified, all namespaces will be exposed.
  -h, --help                                help for ingress
      --label-match string                  Alias to 'route-selector' flag.
      --lb-type string                      Type of Load Balancer. Options are classic,nlb.
      --namespace-ownership-policy string   Namespace Ownership Policy for ingress. Options are Strict,InterNamespaceAllowed. Default is 'Strict'.
      --private                             Restrict application route to direct, private connectivity.
      --route-selector string               Route Selector for ingress. Format should be a comma-separated list of 'key=value'. If no label is specified, all routes will be exposed on both routers. For legacy ingress support these are inclusion labels, otherwise they are treated as exclusion label.
      --wildcard-policy string              Wildcard Policy for ingress. Options are WildcardsDisallowed,WildcardsAllowed. Default is 'WildcardsDisallowed'.

Global Flags:
      --color string     Surround certain characters with escape sequences to display them in color on the terminal. Allowed options are [auto never always] (default "auto")
      --debug            Enable debug mode.
  -i, --interactive      Enable interactive mode.
      --profile string   Use a specific AWS profile from your credential file.
      --region string    Use a specific AWS region, overriding the AWS_REGION environment variable. (DEPRECATED: Region flag will be removed from this command in future versions)
  -y, --yes              Automatically answer yes to confirm operation.
```

## Step

4. Edit a default ingress.

```bash
rosa edit ingress <ingress id> -c <cluster name> --private=true --label-match="aaa=bbb,ccc=ddd"
```

## Expect

- No error is returned.

## Step

5. Repeat the step for an additional ingress.

## Expect

- No error is returned.
- The output shows the update succeeded.

## Step

6. List the ingress.

```bash
rosa list ingress -c <cluster name>
```

## Expect

- The updated ingress is listed.
- The updated route selectors are displayed.

```
[xueli@xueli-work tmp]$ rosa list ingress -c xueli-rosa
ID APPLICATION ROUTER PRIVATE DEFAULT ROUTE SELECTORS
u6x8 https://apps.xueli-rosa.r2th.s1.devshift.org yes yes
p3s7 https://apps2.xueli-rosa.r2th.s1.devshift.org yes no aaa=bbb, ccc=ddd
```
