# Test

## Step
Launch rosa cli

## Expect

## Step
Run command to check the list versions usage

```bash
rosa list versions -h
```

## Expect
- Message show correctly and clearly and readable
- No typo error

```
List versions of OpenShift that are available for creating clusters.

NOTE: Available upgrades shown in this command are deprecated.

Usage:
  rosa list versions [flags]

Aliases:
  versions, version

Examples:
  # List all OpenShift versions
  rosa list versions

Flags:
      --channel-group string   List only versions from the specified channel group (default "stable")
  -h, --help                   help for versions
      --hosted-cp              Lists only versions that are hosted-cp enabled
  -o, --output string          Output format. Allowed formats are [json yaml]

Global Flags:
      --color string     Surround certain characters with escape sequences to display them in color on the terminal. Allowed options are [auto never always] (default "auto")
      --debug            Enable debug mode.
      --profile string   Use a specific AWS profile from your credential file.
      --region string    Use a specific AWS region, overriding the AWS_REGION environment variable. (DEPRECATED: Region flag will be removed from this command in future versions)
```

## Step
Run command to list the versions

```bash
rosa list version
```

## Expect
- The enabled && moa_enabled version ID will be listed
- The listed versions comes from stable channel

## Step
Run command to list another channel versions

```bash
rosa list version --channel-group candidate
```

## Expect
- The enabled && moa_enabled version ID will be listed
- The listed versions comes from candidate channel

## Step
Run command to list version with all of the flags

- `--debug`
- `--profile`
- `-v`

## Expect
All of the flags can work well

## Step
List versions with unsupported flag

```bash
rosa list versions --interactive
```

## Expect
Error with unknown flag

```
Error: unknown flag: --interactive
Usage:
  rosa list versions [flags]

Aliases:
  versions, version

Examples:
  # List all OpenShift versions
  rosa list versions

Flags:
      --channel-group string   List only versions from the specified channel group (default "stable")
  -h, --help                   help for versions

Global Flags:
      --debug            Enable debug mode.
      --profile string   Use a specific AWS profile from your credential file.
  -v, --v                Level log level for V logs

Failed to execute root command: unknown flag: --interactive
```
