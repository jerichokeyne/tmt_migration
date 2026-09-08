# Test

## Step
List region with `--hosted-cp` flag

## Expect
- Only support region shows in the region list  
- The output should contain bellow column, `ID`, `NAME`, `MULTI-AZ SUPPORT`, `HOSTED_CP SUPPORT`

## Step
List regions without `--hosted-cp` flag

## Expect
- All support region should be shown.  
- The output should contain bellow column, `ID`, `NAME`, `MULTI-AZ SUPPORT`, `HOSTED_CP SUPPORT`

## Step
Use the supported region, the hypershift cluster can be created successfully.

## Expect
