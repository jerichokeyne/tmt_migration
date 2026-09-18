# Test

## Step

```bash
rosa upgrade cluster -h
```

## Expect

## Step

Login rosacli then create one hypershift cluster with an upgrade path

## Expect

`enable_minor_version_upgrades` and `--schedule` help message should be there.

## Step

Upgrade cluster with one automatic upgrade policy in the interactive mode:

```bash
rosa upgrade cluster -c 2484t2b0f4sjdkdrqamn4beurpvp5uu8 --control-plane -i
```

## Expect

```bash
rosa upgrade cluster -c 2484t2b0f4sjdkdrqamn4beurpvp5uu8 -i
```

```
I: Interactive mode enabled.
Any optional fields can be left empty and a default will be selected.
? IAM Roles/Policies upgrade mode: [Use arrows to move, type to filter, ? for more help]

> auto
> manual
> ? IAM Roles/Policies upgrade mode: auto
> ? Enable automatic upgrades: Yes
> ? Allow minor upgrades (optional): Yes
> ? Please input desired automatic schedule with a cron expression: [? for help] ?
> ? cron expression in UTC which will be the time when an upgrade to the latest release will be automatically scheduled and repeated at each occurrence. Mutually exclusive with --schedule-date and --schedule-time. This is currently supported only for Hosted Control Planes.
> ? Please input desired automatic schedule with a cron expression: 1 2 * * *
> ? Please input desired automatic schedule with a cron expression: 1 2 * * *
> I: Ensuring account and operator role policies for cluster '2484t2b0f4sjdkdrqamn4beurpvp5uu8' are compatible with upgrade.
> ......
> I: Upgrade successfully scheduled for cluster '2484t2b0f4sjdkdrqamn4beurpvp5uu8'
```

- The upgrade is schedule
- The info of `rosa describe upgrade` should show correct value
- Check the upgrade via backend API; `enable_minor_version_upgrades`, `schedule_type` (automatic or manual), and schedule should be with correct value as the rosacli flag set
- The cluster upgrade should be scheduled successfully

## Step

Upgrade cluster with one automatic upgrade policy for cluster and describe it (OCM-3478).
Precondition: there is no available upgrade version for the cluster

## Expect

- The automatic upgrade policy should create successfully.
- The version is empty in policy.

```bash
rosa describe upgrade -c ying-hp1
```

```
ID: 3a2ddc8e-488e-11ee-aaa2-0a580a8011d7
Cluster ID: 25uv4t993p7tbqg1f727jgvf1shrnsnc
Schedule Type: automatic
Next Run: 2023-09-02 05:20 UTC
Upgrade State: pending

Schedule At: 20 5 * * *

Enable minor version upgrades: false
```

## Step

Set `Enable automatic upgrades` is false and do the manual upgrade to cluster.

## Expect

```bash
rosa upgrade cluster -c ying-hcp-1 --control-plane -i
```

```
I: Interactive mode enabled.
Any optional fields can be left empty and a default will be selected.
? IAM Roles/Policies upgrade mode (default = 'auto'): auto
? Enable automatic upgrades: No
? Please input desired date in format yyyy-mm-dd: 2024-02-04
? Please input desired UTC time in format HH:mm: 13:20
? Version (default = '4.14.10'): 4.14.10
I: Ensuring account and operator role policies for cluster '296jhraoqli8g8904k9gerq6bvn1tnpt' are compatible with upgrade.
I: Account roles with the prefix 'sdq-ci-itjlo' have attached managed policies.
I: Cluster 'ying-hcp-1' operator roles have attached managed policies. An upgrade isn't needed
I: Account and operator roles for cluster 'ying-hcp-1' are compatible with upgrade
? Are you sure you want to upgrade cluster to version '4.14.10'? Yes
I: Upgrade successfully scheduled for cluster 'ying-hcp-1'
```

## Step

Repeat all above step on different OS

## Expect

result should be same
