# Test

## Step

Prepare a hosted cluster with machinepool version that can be upgraded

## Expect

## Step

Prepare a machinepool with available upgrade

## Expect

## Step

Upgrade machine pool with one automatic upgrade policy in the interactive mode:

```bash
rosa upgrade machinepool <mp_id> -c <cluster_name/id> -i
```

## Expect

- It can create successuflly.

```bash
rosa upgrade machinepool mp-3 --cluster ying-up1 -i
```

```
I: Interactive mode enabled.
Any optional fields can be left empty and a default will be selected.
? Enable automatic upgrades: Yes
? Allow minor upgrades (optional): No
? Please input desired automatic schedule with a cron expression: 2 5 * * *
? Are you sure you want to schedule automatic upgrades for machine pool 'mp-3' at '2 5 * * *'? Yes
I: Upgrade successfully scheduled for the machine pool 'mp-3' on cluster 'ying-up1'
```

## Step

Describe the update:

```bash
rosa describe upgrade --machinepool mp-3 --cluster ying-up1
```

## Expect

- All the parameters value should be same with configuration.
- The Version will be empty if there is no Z stream available version.

```bash
rosa describe upgrade --machinepool mp-3 --cluster ying-up1
```

```
ID: d8682c50-51d4-11ee-b516-0a580a8114c3
Cluster ID: 266nc4ivhk6ekojofvc5mvucmchrmb6d
Schedule Type: automatic
Next Run: 2023-09-13 05:02 UTC
Upgrade State: scheduled
Schedule At: 2 5 * * *
Enable minor version upgrades: false
Version: 4.12.31
```

## Step

Upgrade machine pool with one manual upgrade policy in the interactive mode

## Expect

- All the parameters value should be same with configuration.
- The y stream available upgrade version will show in the options.
- All available versions will be listed (Use `rosa list version` to check available versions).
- There is no Enable minor version upgrades option.

```bash
rosa upgrade machinepool mp-3 --cluster ying-up1 -i
```

```
I: Interactive mode enabled.
Any optional fields can be left empty and a default will be selected.
? Enable automatic upgrades: No
? Please input desired date in format yyyy-mm-dd: 2023-09-13
? Please input desired UTC time in format HH:mm: 01:47
? Machine pool version: 4.13.10
? Are you sure you want to upgrade machine pool 'mp-3' to version '4.13.10'? Yes
I: Upgrade successfully scheduled for the machine pool 'mp-3' on cluster 'ying-up1'
```

## Step

Describe the update:

```bash
rosa describe upgrade --machinepool mp-3 --cluster ying-up1
```

## Expect

- All the attributes are matched to configuration.
  OCM-3492: Make sure attributes are left-aligned

```bash
rosa describe upgrade --machinepool mp-3 --cluster ying-up1
```

```
ID: 1edbd240-51d6-11ee-b516-0a580a8114c3
Cluster ID: 266nc4ivhk6ekojofvc5mvucmchrmb6d
Schedule Type: manual
Next Run: 2023-09-13 01:47 UTC
Upgrade State: scheduled

Version: 4.13.10
```
