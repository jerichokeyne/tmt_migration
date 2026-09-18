# Test

## Step
Launch rosa cli

## Expect

## Step
Run command to list the versions

```bash
rosa list version --hosted-cp
```

## Expect
- The enabled && moa_enabled version ID will be listed
- The listed versions comes from stable channel
- The default version hosted_control_plane_default is true in API
- The current minimal version is 4.13.x

```bash
ocm get /api/clusters_mgmt/v1/versions/openshift-v4.14.10 | jq.hosted_control_plane_default
```

## Step
Run command to list another channel versions

```bash
rosa list version --channel-group candidate --hosted-cp
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
