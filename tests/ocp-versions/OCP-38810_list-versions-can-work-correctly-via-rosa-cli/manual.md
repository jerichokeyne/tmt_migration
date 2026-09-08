# Test

## Step
Launch rosa cli

## Expect

## Step
Run command to check the list versions usage  
$ rosa list version -h

## Expect
- Message show correctly and clearly and readable  
- No typo error  
[xueli@xueli-work tmp]$ rosa list versions -h  
List versions of OpenShift that are available for creating clusters.  
  
  
Usage:  
rosa list versions [flags]  
  
  
Aliases:  
versions, version  
  
  
Examples:  
\# List all OpenShift versions  
rosa list versions  
  
  
Flags:  
--channel-group string List only versions from the specified channel group (default "stable")  
-h, --help help for versions  
--hosted-cp Lists only versions that are hosted-cp enabled  
-o, --output string Output format. Allowed formats are [json yaml]  
  
  
Global Flags:  
--debug Enable debug mode.  
--profile string Use a specific AWS profile from your credential file.  
-v, --v Level log level for V logs

## Step
Run command to list the versions  
$ rosa list version

## Expect
- The enabled && moa_enabled version ID will be listed  
- The listed versions comes from stable channel

## Step
Run command to list another channel versions  
$ rosa list version --channel-group candidate

## Expect
- The enabled && moa_enabled version ID will be listed  
- The listed versions comes from candidate channel

## Step
Run command to list version with all of the flags  
--debug  
--profile  
-v

## Expect
All of the flags can work well

## Step
List versions with unsupported flag  
$ rosa list versions --interactive

## Expect
Error with unknown flag  
[xueli@xueli-work tmp]$ rosa list version --channel-group nightly --interactive  
Error: unknown flag: --interactive  
Usage:  
rosa list versions [flags]  
  
  
Aliases:  
versions, version  
  
  
Examples:  
\# List all OpenShift versions  
rosa list versions  
  
  
Flags:  
--channel-group string List only versions from the specified channel group (default "stable")  
-h, --help help for versions  
  
  
Global Flags:  
--debug Enable debug mode.  
--profile string Use a specific AWS profile from your credential file.  
-v, --v Level log level for V logs  
  
  
Failed to execute root command: unknown flag: --interactive
