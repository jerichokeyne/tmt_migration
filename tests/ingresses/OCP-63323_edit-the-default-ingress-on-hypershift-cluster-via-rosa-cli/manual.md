# Test

## Step

1. Run the command and check the help message.

```bash
rosa edit ingress --help
```

## Expect

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

2. Edit a default ingress with `--label-match`.

```bash
rosa edit ingress <ingress id> -c <cluster name> --private=true --label-match="aaa=bbb,ccc=ddd"
```

## Expect

- `E: Updating route selectors is not supported for hosted cp clusters`

## Step

3. Edit a default ingress with `--private`.

```bash
rosa edit ingress <ingress id> -c <cluster name> --private=false
rosa edit ingress <ingress id> -c <cluster name> --private
```

Then list the ingress and check the `PRIVATE` column.

## Expect

- If there is no change: `W: No need to update ingress as there are no changes`.
- Otherwise: `I: Updated ingress 'j0j2' on cluster '23j0i3uboco0c12hddfmnknueblgnvpd'`.
- If `--private` works, `PRIVATE` is `yes`; if `--private=false` works, it is `no`.

## Step

4. Check interactive mode.

## Expect

- Only the `Private ingress` question is shown, and it works correctly.

```
yuwan1-mac:rosa yuwan$ ./rosa edit ingress j0j2 -c 23j0i3uboco0c12hddfmnknueblgnvpd -i
? Restrict application route to direct, private connectivity.
? Private ingress (optional): (y/N)
```
