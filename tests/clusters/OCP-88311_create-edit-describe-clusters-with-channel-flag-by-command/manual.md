# Test

## Step
Create hosted-cp cluster without channel

## Expect
- The cluster should be created successfully  
- The channel should be set with stable-<cluster version X.Y> value

## Step
Create hosted-cp cluster with the channel same with the cluster version's X.Y.  
--version 4.20.14 --channel stable-4.20

## Expect
- The cluster should be created successfully

## Step
Describe cluster cluster

## Expect
- The 'Channel: stable-4.20' field should be correct,same with the value when creating cluster

## Step
Create hosted-cp cluster with the channel higher than the cluster version's X.Y. then describe it  
--version 4.20.14 --channel stable-4.21  
  
NOTE: the higher channel should be an available channel based on the cluster version

## Expect
The result should be same with step 2~3.   
NOTE: the higher channel should be an available channel based on the cluster version

## Step
Edit cluster channel to higher one. For example, stable-4.20 -> stable-4.21. Then describe cluster  
NOTE: the higher channel should be an available channel based on the cluster version  
  
\# rosa edit cluster -c <cid> --channel <higher channel>

## Expect
- It should succeed  
- 'Channel' field of the `rosa describe cluster` output should be correct

## Step
Validation for channel during creating cluster:  
- Use channel and channel-group at the same time  
- Lower channel (TBD)  
- not availabled channel based on the cluster version  
- Invalid channel, for example, --channel "aaa"

## Expect
- Failed to execute root command: if any flags in the group [channel channel-group] are set none of the others can be; [channel channel-group] were all set  
  
- It should fail with error  
- It should fail with error  
- E: Failed to create cluster: status is 400, identifier is '400', code is 'CLUSTERS-MGMT-400', at '2026-03-16T09:51:10Z' and operation identifier is 'f0282ab1-57df-4fde-b8a1-1b17d7f5751a': Invalid channel format: 'aaa'. Channel must follow Y-stream format (e.g., stable-4.16, eus-4.16)

## Step
Validation for channel during editing cluster:  
- Use channel and channel-group at the same time  
- Lower channel   
- not availabled channel based on the cluster version(TBD)  
- Invalid channel, for example, --channel "aaa"

## Expect
- Failed to execute root command: if any flags in the group [channel channel-group] are set none of the others can be; [channel channel-group] were all set   
- E: Failed to update cluster: status is 400, identifier is '400', code is 'CLUSTERS-MGMT-400', at '2026-03-16T09:55:21Z' and operation identifier is '752fc98d-721f-4823-bf27-9a8d7623b86a': Channel 'stable-4.19' (Y-stream 4.19) cannot be lower than cluster version '4.20.14' (Y-stream 4.20). Channel must be 4.20 or higher  
- It should report error from backend  
- E: Failed to update cluster: status is 400, identifier is '400', code is 'CLUSTERS-MGMT-400', at '2026-03-16T09:57:00Z' and operation identifier is '8162bfae-b6e1-4d59-9ef9-301e6611b66f': Invalid channel format: 'aaa-4.1'. Channel must follow Y-stream format (e.g., stable-4.16, eus-4.16)
