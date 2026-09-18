# Test

## Step
The help message shows how to filter for Win-LI instance types

```bash
rosa list instance-types -h
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
You can list instance types that support Win-LI

```bash
rosa list instance-types --with-feature win_li
```

## Expect
It should match the list of machine types from the API:
```bash
ocm get /api/clusters_mgmt/v1/machine_types -p search="features.win_li = 'true'"
```

```
❯ rosa list instance-types --with-feature win_li
ID CATEGORY CPU_CORES MEMORY
g4dn.metal accelerated_computing 96 384.0 GiB
c5d.metal compute_optimized 96 192.0 GiB
c5.metal compute_optimized 96 192.0 GiB
c5n.metal compute_optimized 72 192.0 GiB
c6a.metal compute_optimized 192 384.0 GiB
c6id.metal compute_optimized 128 256.0 GiB
c6i.metal compute_optimized 128 256.0 GiB
m5d.metal general_purpose 96 384.0 GiB
m5dn.metal general_purpose 96 384.0 GiB
m5.metal general_purpose 96 384.0 GiB
m5n.metal general_purpose 96 384.0 GiB
m5zn.metal general_purpose 48 192.0 GiB
m6a.metal general_purpose 192 768.0 GiB
m6id.metal general_purpose 128 512.0 GiB
m6i.metal general_purpose 128 512.0 GiB
r5b.metal memory_optimized 96 768.0 GiB
r5d.metal memory_optimized 96 768.0 GiB
r5dn.metal memory_optimized 96 768.0 GiB
r5.metal memory_optimized 96 384.0 GiB
r5n.metal memory_optimized 96 384.0 GiB
r6a.metal memory_optimized 192 1.5 TiB
r6id.metal memory_optimized 128 1.0 TiB
r6i.metal memory_optimized 128 1.0 TiB
u-12tb1.metal memory_optimized 448 12.0 TiB
u-18tb1.metal memory_optimized 448 18.0 TiB
u-24tb1.metal memory_optimized 448 24.0 TiB
u-6tb1.metal memory_optimized 448 6.0 TiB
u-9tb1.metal memory_optimized 448 9.0 TiB
x2idn.metal memory_optimized 128 2.0 TiB
x2iedn.metal memory_optimized 128 4.0 TiB
x2iezn.metal memory_optimized 48 1.5 TiB
z1d.metal memory_optimized 48 384.0 GiB
i3en.metal storage_optimized 96 768.0 GiB
i3.metal storage_optimized 72 512.0 GiB
i4i.metal storage_optimized 128 1.0 TiB
```
## Step
ROSACLI can output the list in JSON format

```bash
rosa list instance-types --with-feature win_li -o json
```

## Expect
It should match the list of machine types from the API:
```bash
ocm get /api/clusters_mgmt/v1/machine_types -p search="features.win_li = 'true'"
```

```
❯ rosa list instance-types --with-feature win_li -o json
```
```json
[
{
"kind": "MachineType",
"id": "g4dn.metal",
"href": "/api/clusters_mgmt/v1/machine_types/g4dn.metal",
"ccs_only": true,
"cpu": {
"unit": "vCPU",
"value": 96
},
"architecture": "amd64",
"category": "accelerated_computing",
"cloud_provider": {
"kind": "CloudProviderLink",
"id": "aws",
"href": "/api/clusters_mgmt/v1/cloud_providers/aws"
},
"features": {
"win_li": true
},
"generic_name": "g4-gpu-metal",
"memory": {
"unit": "B",
"value": 412316860416
},
"name": "g4dn.metal - Accelerated Computing",
"size": "metal"
},
...
```
