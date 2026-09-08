# Test

## Step
Log in with the rosa tool

## Expect

## Step
Run below command to check the list regions help message
```bash
rosa list regions --help
```

## Expect
- All of the description is clear and correct
```
List regions that are available for the current AWS account.

Usage:
  rosa list regions [flags]

Aliases:
  regions, region

Examples:
  # List all available regions
  rosa list regions

Flags:
      --external-id string   A unique identifier that might be required when you assume a role in another account
  -h, --help                 help for regions
      --hosted-cp            List only regions with support for Hosted Control Planes
      --multi-az             List only regions with support for multiple availability zones
  -o, --output string        Output format. Allowed formats are [json yaml]
      --role-arn string      The Amazon Resource Name of the role that the API will assume to fetch available regions.

Global Flags:
      --color string     Surround certain characters with escape sequences to display them in color on the terminal. Allowed options are [auto never always] (default "auto")
      --debug            Enable debug mode.
      --profile string   Use a specific AWS profile from your credential file.
      --region string    Use a specific AWS region, overriding the AWS_REGION environment variable. (DEPRECATED: Region flag will be removed from this command in future versions)
```

## Step
Run below command to list the available regions
```bash
rosa list regions
```

## Expect
- The available regions will be listed
- 4 columns `ID`, `NAME`, `MULTI-AZ SUPPORT`, `HOSTED-CP SUPPORT` and its values should be correct
```
ID                NAME                         MULTI-AZ SUPPORT    HOSTED-CP SUPPORT
ap-northeast-1    Asia Pacific, Tokyo          true                false
ap-northeast-2    Asia Pacific, Seoul          true                false
ap-northeast-3    Asia Pacific (Osaka)         true                false
ap-south-1        Asia Pacific, Mumbai         true                false
ap-south-2        Asia Pacific, Hyderabad      true                false
ap-southeast-1    Asia Pacific, Singapore      true                false
ap-southeast-2    Asia Pacific, Sydney         true                false
ap-southeast-3    Asia Pacific, Jakarta        true                false
ap-southeast-4    Asia Pacific, Melbourne      true                false
ap-southeast-5    Asia Pacific, Malaysia       true                false
ap-southeast-6    Asia Pacific, New Zealand    true                false
ap-southeast-7    Asia Pacific, Thailand       true                false
ca-central-1      Canada, Central              true                false
ca-west-1         Canada, West                 true                false
eu-central-1      EU, Frankfurt                true                false
eu-central-2      Europe, Zurich               true                false
eu-north-1        EU, Stockholm                true                false
eu-south-1        Europe (Milan)               true                false
eu-south-2        Europe, Spain                true                false
eu-west-1         EU, Ireland                  true                false
eu-west-2         EU, London                   true                false
eu-west-3         EU, Paris                    true                false
il-central-1      Tel Aviv, Israel             true                false
me-central-1      Middle East, UAE             true                false
me-south-1        Middle East, Bahrain         true                false
mx-central-1      Mexico, Central              true                false
us-east-1         US East, N. Virginia         true                false
us-east-2         US East, Ohio                true                true
us-west-1         US West, N. California       false               false
us-west-2         US West, Oregon              true                true
```

## Step
Mark a region to unavailable on AWS(Cannot simulate for QE now)

## Expect

## Step
- Run below command to list the available regions
```bash
rosa list regions
```
- since QE cannot simulate the above step, we need to check it via command
```bash
rosa list regions --debug
```

## Expect
- The unavailable region cannot be listed
- If checking through `--debug`, check that the regions should comes from API `/api/cluster_mgmt/v1/cloud_providers/aws/available_regions`
```
...
time=2026-09-03T17:07:29-04:00 level=debug msg=Request method is POST
time=2026-09-03T17:07:29-04:00 level=debug msg=Request URL is 'https://api.stage.openshift.com/api/clusters_mgmt/v1/cloud_providers/aws/available_regions?page=1&size=100'
time=2026-09-03T17:07:29-04:00 level=debug msg=Request header 'Accept' is 'application/json'
time=2026-09-03T17:07:29-04:00 level=debug msg=Request header 'Authorization' is omitted
time=2026-09-03T17:07:29-04:00 level=debug msg=Request header 'Content-Type' is 'application/json'
time=2026-09-03T17:07:29-04:00 level=debug msg=Request header 'User-Agent' is 'ROSACLI/1.2.64 OCM-SDK/0.1.509'
time=2026-09-03T17:07:29-04:00 level=debug msg=Request body follows
time=2026-09-03T17:07:29-04:00 level=debug msg={
  "access_key_id": "***",
  "secret_access_key": "***"
}
time=2026-09-03T17:07:29-04:00 level=debug msg=Response protocol is 'HTTP/2.0'
time=2026-09-03T17:07:29-04:00 level=debug msg=Response status is '200 OK'
time=2026-09-03T17:07:29-04:00 level=debug msg=Response header 'Content-Type' is 'application/json'
time=2026-09-03T17:07:29-04:00 level=debug msg=Response header 'Date' is 'Thu, 03 Sep 2026 21:07:29 GMT'
time=2026-09-03T17:07:29-04:00 level=debug msg=Response header 'Server' is 'envoy'
time=2026-09-03T17:07:29-04:00 level=debug msg=Response header 'X-Envoy-Upstream-Service-Time' is '138'
time=2026-09-03T17:07:29-04:00 level=debug msg=Response header 'X-Ocm-Environment' is 'staging'
time=2026-09-03T17:07:29-04:00 level=debug msg=Response header 'X-Ocm-Server-Version' is 'eb9a82f'
time=2026-09-03T17:07:29-04:00 level=debug msg=Response header 'X-Operation-Id' is 'a8437428-1e5e-4e43-b3b6-0ceab5b4a53f'
time=2026-09-03T17:07:29-04:00 level=debug msg=Response body follows
time=2026-09-03T17:07:29-04:00 level=debug msg={
  "kind": "CloudRegionList",
  "page": 1,
  "size": 30,
  "total": 30,
  "items": [
...
```

## Step
Run command to list the multi_az regions
```bash
rosa list regions --multi-az # optionally --debug
```

## Expect
Compare with the response body, all of the regions listed should support multi az

```
ID                NAME                         MULTI-AZ SUPPORT    HOSTED-CP SUPPORT
ap-northeast-1    Asia Pacific, Tokyo          true                false
ap-northeast-2    Asia Pacific, Seoul          true                false
ap-northeast-3    Asia Pacific (Osaka)         true                false
ap-south-1        Asia Pacific, Mumbai         true                false
ap-south-2        Asia Pacific, Hyderabad      true                false
ap-southeast-1    Asia Pacific, Singapore      true                false
ap-southeast-2    Asia Pacific, Sydney         true                false
ap-southeast-3    Asia Pacific, Jakarta        true                false
ap-southeast-4    Asia Pacific, Melbourne      true                false
ap-southeast-5    Asia Pacific, Malaysia       true                false
ap-southeast-6    Asia Pacific, New Zealand    true                false
ap-southeast-7    Asia Pacific, Thailand       true                false
ca-central-1      Canada, Central              true                false
ca-west-1         Canada, West                 true                false
eu-central-1      EU, Frankfurt                true                false
eu-central-2      Europe, Zurich               true                false
eu-north-1        EU, Stockholm                true                false
eu-south-1        Europe (Milan)               true                false
eu-south-2        Europe, Spain                true                false
eu-west-1         EU, Ireland                  true                false
eu-west-2         EU, London                   true                false
eu-west-3         EU, Paris                    true                false
il-central-1      Tel Aviv, Israel             true                false
me-central-1      Middle East, UAE             true                false
me-south-1        Middle East, Bahrain         true                false
mx-central-1      Mexico, Central              true                false
us-east-1         US East, N. Virginia         true                false
us-east-2         US East, Ohio                true                true
us-west-2         US West, Oregon              true                true
```

## Step
List hosted-cp supported ones,

```bash
rosa list regions --hosted-cp
```

## Expect
- Only regions which are supported on hosted-cp cluster are shown.
```
ID           NAME               MULTI-AZ SUPPORT    HOSTED-CP SUPPORT
us-east-2    US East, Ohio      true                true
us-west-2    US West, Oregon    true                true
```

## Step
Check all of the flags should work for the list regions command
- `--profile`
- `--V` # TODO: Find out what this was supposed to be

## Expect

## Step
Check the unsupported flag
```bash
rosa list regions --interactive
```

## Expect
unknown flag Error with <usage> returned

```
Failed to execute root command: unknown flag: --interactive
```
