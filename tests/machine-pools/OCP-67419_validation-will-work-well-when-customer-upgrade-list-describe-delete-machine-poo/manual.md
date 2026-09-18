# Test

## Step
Prepare a hosted cluster with machine pool version that can be upgraded

## Expect

## Step
Create upgrade for a not-ready cluster

## Expect
- It will return readable error message

## Step
Create upgrade with invalid format value
invalid --schedule/--version/--schedule-date/--schedule-time

## Expect
- It will return readable error message

## Step
Create multi policies to a same machine pool

## Expect
- It will return warning message
```
./rosa upgrade machinepool mp-3 --cluster ying-up1 --schedule "5 2 * * *" -y
```
```
W: There is already a pending upgrade to version 4.12.31 on 2023-09-14 02:05 UTC
I: An upgrade already exists for machine pool 'mp-3' in cluster 'ying-up1'
```

## Step
Create a version with ‘schedule ’ and --version/--schedule-date/--schedule-time

## Expect
- Error message will return to tell
```
E: The '--schedule' option is mutually exclusive with '--version'
Or
E: The '--schedule-date' and '--schedule-time' options are mutually exclusive with '--schedule'
```

## Step
Create/List/escribe/Delete upgrade without machine pool id
```bash
./rosa delete upgrade --machinepool --cluster ying-up1
```

## Expect
- It will return readable error message

## Step
Create/List/escribe/Delete upgrade with not-exiting machine pool id

## Expect
- It will return readable error message
```
E: Failed to get scheduled upgrades for machine pool 'mp-5': Machine pool 'mp-5' does not exist for hosted cluster 'ying-up1'
```
