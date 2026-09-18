# Test

## Step
List regions with the `--hosted-cp` flag.

## Expect
- Only supported regions are shown in the region list.
- The output contains the `ID`, `NAME`, `MULTI-AZ SUPPORT`, and `HOSTED_CP SUPPORT` columns.

## Step
List regions without the `--hosted-cp` flag.

## Expect
- All supported regions are shown.
- The output contains the `ID`, `NAME`, `MULTI-AZ SUPPORT`, and `HOSTED_CP SUPPORT` columns.

## Step
Use a supported region to create a HyperShift cluster.

## Expect
