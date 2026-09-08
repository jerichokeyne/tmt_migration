# Test

## Step
Prepare a rosa non-sts byovpc multi-az cluster on the region which has local zone

## Expect

## Step
Create machinepool in the interactive mode and choose the subnet created in the local zone

## Expect
- The 'Instance type' only shows the supported one on the local zone   
- The machinepool can be created successfully  
- The instances should be created correctly on AWS.

## Step
Create machinepool by the rosacli command and choose the subnet created in the local zone

## Expect
The result should be same with the one in step2

## Step
Prepare a rosa non-sts byovpc single-az cluster on the region which has local zone

## Expect
- The 'Instance type' only shows the supported one on the local zone   
- The machinepool can be created successfully  
- The instances should be created correctly on AWS.

## Step
Create machinepool in the interactive mode and choose the subnet created in the local zone

## Expect
- The 'Instance type' only shows the supported one on the local zone   
- The machinepool can be created successfully  
- The instances should be created correctly on AWS.  
- There is no 'Use spot instances' option when choose local zone

## Step
Create machinepool by the rosacli command and choose the subnet created in the local zone

## Expect
- The 'Instance type' only shows the supported one on the local zone   
- The machinepool can be created successfully  
- The instances should be created correctly on AWS.  
- There is no 'Use spot instances' option when choose local zone

## Step
After craeted machinepool on local zone, list machinepool with flags '--all' and '--az-type'

## Expect
- The output will show 'AZ TYPE' colume and value is 'LocalZone'  
- If use '--all' flag, all columns should be shown even the empty ones; If use '--az-type', the 'AZ TYPE' should be shown and other empty column should be not displayed.  
\-
