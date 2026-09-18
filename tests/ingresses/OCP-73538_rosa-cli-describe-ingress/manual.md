# Setup

Create one classic and one HCP cluster.

# Test

## Step

1. List the usage of `rosa describe ingress`.

```bash
rosa describe ingress -h
```

## Expect

```
Show details of the specified ingress within cluster

Usage:
  rosa describe ingress [flags]

Examples:
rosa describe ingress <ingress_id> -c mycluster

Flags:
  -c, --cluster string   Name or ID of the cluster.
  -h, --help             help for ingress
      --ingress string   Ingress of the cluster to target
  -o, --output string    Output format. Allowed formats are [json yaml]

Global Flags:
      --color string     Surround certain characters with escape sequences to display them in color on the terminal. Allowed options are [auto never always] (default "auto")
      --debug            Enable debug mode.
      --profile string   Use a specific AWS profile from your credential file.
      --region string    Use a specific AWS region, overriding the AWS_REGION environment variable. (DEPRECATED: Region flag will be removed from this command in future versions)
```

## Step

2. Run `rosa list ingress` to get the ingress ID.

```bash
rosa list ingress -c $cluster
```

## Expect

```
ID APPLICATION ROUTER PRIVATE DEFAULT ROUTE SELECTORS LB-TYPE EXCLUDED NAMESPACE WILDCARD POLICY NAMESPACE OWNERSHIP
h6u3 https://apps.qe-rosa-xsfuq.5cbo.s1.devshift.org no yes nlb WildcardsDisallowed Strict
```

## Step

3. Run `rosa describe ingress` using the ingress ID.

```bash
rosa describe ingress $ingressID -c $cluster
```

## Expect

```
Cluster ID: 27fd1e14gi4pkct19qo1jgbsodv22n5i
Default: true
ID: h6u3
LB-Type: nlb
Namespace Ownership Policy: Strict
Private: false
Wildcard Policy: WildcardsDisallowed
```
