# Test

## Step

Login rosacli then create one hypershift cluster with an upgrade path

## Expect

## Step

Upgrade cluster with one automatic upgrade policy:

```bash
rosa upgrade cluster -c 2484t2b0f4sjdkdrqamn4beurpvp5uu8 --mode auto --schedule '20 20 * * *' -y --control-plane
```

~~`--allow-minor-version-updates -y`~~

## Expect

- The upgrade is schedule
- The info of `rosa describe upgrade` should show correct value
- Check the upgrade via backend API; `enable_minor_version_upgrades`, `schedule_type` (automatic or manual), and schedule should be with correct value as the rosacli flag set
- The cluster upgrade should be scheduled successfully
- If `--allow-minor-version-updates` is not set, the default value should be false.
- The default version

## Step

~~Check validation for this commnad: -- > OCP-73814 - set '--schedule' and '--version' at the same time - set --schedule with value not match the cron expression - set '--schedule-date' and '--schedule-time' and '--schedule' at the same time~~

## Expect

- E: The '--schedule' option is mutually exclusive with '--version'
- E: Schedule 'asd' is not a valid cron expression
- E: The '--schedule-date' and '--schedule-time' options are mutually exclusive with '--schedule'

## Step

Describe upgrade:

```bash
rosa describe upgrade -c <id>
```

## Expect

```bash
rosa describe upgrade -c 24aqdlpthh2k0skovm5on7ef2s9fhu6n
```

```
ID: 5394808a-09bd-11ee-89a1-0a580a831b78
Cluster ID: 24aqdlpthh2k0skovm5on7ef2s9fhu6n
Schedule Type: automatic
Next Run: 2023-06-13 23:23:00 +0000 UTC
Upgrade State: pending
Schedule At: 23 23 * * *
Enable minor version upgrades: false
Version: 4.12.19
```

- For hosted-cp clusters, `Schedule Type:` should be automatic; `Schedule At` and `Enable minor version upgrades` should be same with the values of the input.

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

Repeat all above step on different OS

## Expect

result should be same
