# Test

## Step
Log in with the `rosa` tool.

## Expect

## Step
Run the following commands to check the help message.

```bash
rosa list -h
rosa list instance-types --help
```

## Expect
```
List Instance types that are available for use with ROSA.

Usage:
  rosa list instance-types [flags]

Aliases:
  instance-types, instancetypes

Examples:
  # List all instance types
	rosa list instance-types

Flags:
      --external-id string     An optional unique identifier that might be required when you assume a role in another account.
  -h, --help                   help for instance-types
      --hosted-cp              Enable the use of Hosted Control Planes
  -o, --output string          Output format. Allowed formats are [json yaml]
      --region string          Use a specific AWS region, overriding the AWS_REGION environment variable.
      --role-arn string        STS Role ARN with get secrets permission.
      --with-feature strings   Filter instance types by enabled features (e.g., '--with-feature win_li'). Can be specified multiple times.
                                Run 'rosa list instancetypes -ojson | "jq .[0].features | keys"' for a full list of instance type features.
  -y, --yes                    Automatically answer yes to confirm operation.

Global Flags:
      --color string     Surround certain characters with escape sequences to display them in color on the terminal. Allowed options are [auto never always] (default "auto")
      --debug            Enable debug mode.
      --profile string   Use a specific AWS profile from your credential file.
```

## Step
Run the following command to list the available instance types.

```bash
rosa list instance-types
```

## Expect
- The available instance types are listed.
