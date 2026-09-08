# Test

## Step
Check the help message   
$ rosa edit cluster -h

## Expect
--channel-group string Changes the channel group used for cluster versions. Channel group is the name of the channel where this image belongs, for example "stable" or "eus". (default "stable")

## Step
Create a cluster with the version which is enable on multiple channel-group.  
for example, 4.18.6, both enabled on stable and candidate channel group

## Expect

## Step
Edit the cluster with '--channel-group' flag

## Expect
- It succeeds  
- Describe cluster to check if the channel groud is updated

## Step
Edit cluster with some flag ,but no '--channel-group' flag

## Expect
- It succeeds  
- The channel group will not be updated.(OCM-15190)

## Step
Validations:  
- Update the channel-group if the current cluster version is not available on updating channel group  
- Use fake channel group value

## Expect
- E: Failed to update cluster: status is 400, identifier is '400', code is 'CLUSTERS-MGMT-400', at '2025-04-10T09:22:08Z' and operation identifier is 'de44307b-42ca-401b-96c2-98ea763626df': The current version '4.18.6' is not available for the desired channel group 'nightly'  
- Result should be same as above because no available versions returned using fake channel group

## Step
~~TODO: Edit the cluster in the interactive mode.~~

## Expect
~~TODO: There will be qestions to ask for input the channel group and finally works~~
