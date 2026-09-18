# Setup
<https://docs.google.com/document/d/1HaEaQKzzQqNMiPxovnYWasLB2yVjHnsfSIs1q8BWD2Q/edit#heading=h.c1k2r73eamsh>

[OCP-71561](</polarion/#/project/OSE/workitem?id=OCP-71561>)

# Test

## Step
Check if the capability is enabled for the test organization

```bash
echo '{"feature": "capability.organization.hcp_allow_external_authentication"}' | ocm post /api/authorizations/v1/self_feature_review
```

## Expect

## Step
Prepare an HCP cluster with `--external-auth-providers-enabled`

## Expect

## Step
Check help information for `rosa create`, `rosa list`, `rosa describe`, and `rosa delete` external authentication providers

## Expect
The information should be readable and clear.

```bash
rosa create external-auth-provider -h
```

```
Configure a cluster to use an external authentication provider instead of an internal OpenID Connect (OIDC) provider.

Usage:
  rosa create external-auth-provider [flags]

Aliases:
  external-auth-provider, externalauthproviders, externalauthprovider, external-auth-providers

Examples:
  # Interactively create an external authentication provider to a cluster named "mycluster"
  rosa create external-auth-provider --cluster=mycluster --interactive

Flags:
      --claim-mapping-groups-claim string     Describes rules on how to transform information from an ID token into a cluster identity.
      --claim-mapping-username-claim string   The name of the claim that should be used to construct usernames for the cluster identity.
      --claim-validation-rule strings         ClaimValidationRules are rules that are applied to validate token claims to authenticate users. The input will be in a <claim>:<required_value> format. To have multiple claim validation rules, you could separate the values by ','. The input could be in a <claim>:<required_value>,<claim>:<required_value> format.
  -c, --cluster string                        Name or ID of the cluster.
      --console-client-id string              The application or client id for your app registration that is used for console.
      --console-client-secret string          The value of the client secret that is associated with your console app registration.
  -h, --help                                  help for external-auth-provider
  -i, --interactive                           Enable interactive mode.
      --issuer-audiences strings              A comma-separated list of audiences that the token was issued for.
      --issuer-ca-file string                 Path to certificate file to use when making requests to the issuer server.
      --issuer-url string                     The serving url of the token issuer.
      --name string                           Name for the external authentication provider.

Global Flags:
      --color string     Surround certain characters with escape sequences to display them in color on the terminal. Allowed options are [auto never always] (default "auto")
      --debug            Enable debug mode.
      --profile string   Use a specific AWS profile from your credential file.
      --region string    Use a specific AWS region, overriding the AWS_REGION environment variable. (DEPRECATED: Region flag will be removed from this command in future versions)
  -y, --yes              Automatically answer yes to confirm operation.
```

```bash
rosa list external-auth-provider -h
```

```
List external authentication provider for a cluster.

Usage:
  rosa list external-auth-providers [flags]

Aliases:
  external-auth-providers, externalauthproviders, externalauthprovider, external-auth-provider

Examples:
  # List all external authentication providers for a cluster named 'mycluster'"
  rosa list external-auth-provider -c mycluster

Flags:
  -c, --cluster string   Name or ID of the cluster.
  -h, --help             help for external-auth-providers
  -o, --output string    Output format. Allowed formats are [json yaml]

Global Flags:
      --color string     Surround certain characters with escape sequences to display them in color on the terminal. Allowed options are [auto never always] (default "auto")
      --debug            Enable debug mode.
      --profile string   Use a specific AWS profile from your credential file.
      --region string    Use a specific AWS region, overriding the AWS_REGION environment variable. (DEPRECATED: Region flag will be removed from this command in future versions)
```

```bash
rosa describe external-auth-provider -h
```

```
Show details of an external authentication provider on a cluster.

Usage:
  rosa describe external-auth-provider [flags]

Aliases:
  external-auth-provider, externalauthproviders, externalauthprovider, external-auth-providers

Examples:
  # Show details of an external authentication provider named "exauth" on a cluster named "mycluster"
  rosa describe external-auth-provider exauth --cluster=mycluster

Flags:
  -c, --cluster string   Name or ID of the cluster.
  -o, --output string    Output format. Allowed formats are [json yaml]
      --name string      Name for the external authentication provider of the cluster to target
  -h, --help             help for external-auth-provider

Global Flags:
      --color string     Surround certain characters with escape sequences to display them in color on the terminal. Allowed options are [auto never always] (default "auto")
      --debug            Enable debug mode.
      --profile string   Use a specific AWS profile from your credential file.
      --region string    Use a specific AWS region, overriding the AWS_REGION environment variable. (DEPRECATED: Region flag will be removed from this command in future versions)
```

```bash
rosa delete external-auth-provider -h
```

```
Delete an external authentication provider from a cluster.

Usage:
  rosa delete external-auth-provider [flags]

Aliases:
  external-auth-provider, externalauthproviders, externalauthprovider, external-auth-providers

Examples:
  # Delete an external authentication provider named exauth-1
  rosa delete external-auth-provider exauth-1  --cluster=mycluster

Flags:
  -c, --cluster string   Name or ID of the cluster.
  -h, --help             help for external-auth-provider

Global Flags:
      --color string     Surround certain characters with escape sequences to display them in color on the terminal. Allowed options are [auto never always] (default "auto")
      --debug            Enable debug mode.
      --profile string   Use a specific AWS profile from your credential file.
      --region string    Use a specific AWS region, overriding the AWS_REGION environment variable. (DEPRECATED: Region flag will be removed from this command in future versions)
  -y, --yes              Automatically answer yes to confirm operation.
```

## Step
Create external authentication provider for the cluster

```bash
rosa create external-auth-provider \
  --cluster=lponce-local-01 \
  --name=microsoft-entra-id \
  --issuer-url=https://login.microsoftonline.com/fa5d3dd8-b8ec-4407-a55c-ced639f1c8c5/v2.0 \
  --issuer-audiences=a9464024-b142-4bdf-86c0-a153109cdb14 \
  --claim-mapping-username-claim=email \
  --claim-mapping-groups-claim=groups \
  --claim-validation-rule claim1:rule1
```

## Expect
- It can create successfully.

```
I: Successfully created an external authentication provider for cluster '2a2qh276107ljep597jmjrd7f6kn2ol1'
```

- It will give a message like this: `It may take several minutes for this access to become active`.

## Step
List the external authentication provider for the cluster

```bash
./rosa list external-auth-provider -c sdq-ci-ylgck
```

## Expect
- It can get the created external auth provider.

```
./rosa list external-auth-provider -c sdq-ci-ylgck
NAME ISSUER URL
microsoft-entra-id https://login.microsoftonline.com/fa5d3dd8-b8ec-4407-a55c-ced639f1c8c5/v2.0
```

## Step
Describe external authentication provider for the cluster

## Expect
```
./rosa describe external-auth-provider --name microsoft-entra-id -c sdq-ci-ylgck
ID: microsoft-entra-id
Cluster ID: 2a2qh276107ljep597jmjrd7f6kn2ol1
Issuer audiences:
- a9464024-b142-4bdf-86c0-a153109cdb14
Issuer Url: https://login.microsoftonline.com/fa5d3dd8-b8ec-4407-a55c-ced639f1c8c5/v2.0
Claim mappings group: groups
Claim mappings username: email
```

## Step
Delete the external authentication provider for the cluster

## Expect
- It can be deleted successfully.

```
./rosa delete external-auth-provider microsoft-entra-id -c sdq-ci-ylgck -y
I: Successfully deleted external authentication provider 'microsoft-entra-id' from cluster 'sdq-ci-ylgck'

/rosa list external-auth-provider -c sdq-ci-ylgck
E: there are no external authentication providers for this cluster
```

## Step
Create a new external authentication provider with a CA for a cluster with external authentication configuration using the CLI

```bash
./rosa create external-auth-provider -c sdq-ci-ylgck --name=microsoft-entra-id --issuer-url=https://login.microsoftonline.com/fa5d3dd8-b8ec-4407-a55c-ced639f1c8c5/v2.0 --issuer-audiences=a9464024-b142-4bdf-86c0-a153109cdb14 --issuer-ca-file=/home/yingzhan/mytest/rosa/mitm-ca.pem --claim-mapping-username-claim=email --claim-mapping-groups-claim=groups
```

- Describe the external authentication configuration.

## Expect
- It can create successfully.
- It should contain CA related information.

```
./rosa describe external-auth-provider --name microsoft-entra-id -c sdq-ci-ylgck

ID: microsoft-entra-id
Cluster ID: 2a2qh276107ljep597jmjrd7f6kn2ol1
Issuer audiences:
- a9464024-b142-4bdf-86c0-a153109cdb14
Issuer Url: https://login.microsoftonline.com/fa5d3dd8-b8ec-4407-a55c-ced639f1c8c5/v2.0
Claim mappings group: groups
Claim mappings username: email
```

## Step
Create a new external authentication provider for a cluster with client parameters

```bash
rosa create external-auth-provider \
  --cluster=lponce-local-01 \
  --name=microsoft-entra-id \
  --issuer-url=https://login.microsoftonline.com/fa5d3dd8-b8ec-4407-a55c-ced639f1c8c5/v2.0 \
  --issuer-audiences=a9464024-b142-4bdf-86c0-a153109cdb14,8a769b34-13c9-4f5b-9933-ec439700ec6 \
  --claim-mapping-username-claim=email \
  --claim-mapping-groups-claim=groups \
  --console-client-id=8a769b34-13c9-4f5b-9933-ec439700ec6 \
  --console-client-secret=****************************************
```

- Describe the external authentication configuration.

## Expect
- It can create successfully.
- It should contain client ID.

```
./rosa describe external-auth-provider --name microsoft-entra-id-a -c sdq-ci-ylgck

ID: microsoft-entra-id-a
Cluster ID: 2a2qh276107ljep597jmjrd7f6kn2ol1
Issuer audiences:
- a9464024-b142-4bdf-86c0-a153109cdb14
- 8a769b34-13c9-4f5b-9933-ec439700ec6
Issuer Url: https://login.microsoftonline.com/fa5d3dd8-b8ec-4407-a55c-ced639f1c8c5/v2.0
Claim mappings group: groups
Claim mappings username: email
Console client id: 8a769b34-13c9-4f5b-9933-ec439700ec6
```
