# Test

## Step

Create account-roles with latest(default) version with setting path,
\# rosa create account-roles --prefix <prefix> --path /accountrole/custom/path/ --mode auto -y

## Expect

## Step

Create STS clusters which has upgrade path the the latest Y stream version

## Expect

## Step

Upgrade the cluster created in step 2

## Expect

There is warning message "W: To check and acknowledge gates prior to scheduling an upgrade, run this command with '--dry-run'"

## Step

Upgrade the cluster with "--dry-run" flag

## Expect

There is info "I: Upgrading cluster '2koueoefaseah289bb7csu59fuu0pjmu' should succeed. Please wait 1 to 2 minutes, then rerun this command without the '--dry-run' flag, to allow time for the acknowledged agreements to be reflected."

## Step

Upgrade the cluster to the latest Y stream version

## Expect

- The new added operator role and policy are added during the upgrade if the upgrading version cluster has some
- The upgrade is scheduled successfully.It can be checked by 'rosa list upgrade'
