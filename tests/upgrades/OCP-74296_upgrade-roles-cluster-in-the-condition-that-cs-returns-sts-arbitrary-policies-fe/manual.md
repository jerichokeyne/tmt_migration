# Test

## Step
Prepare one STS cluster in the version which has upgrade path

## Expect

## Step
Make featre toggles, 'persist-role-policy-bindings-enabled: false' and 'return-error-for-deactivated-rpb-feature: true'.

## Expect

## Step
Upgrade roles in manual mode

## Expect
- There is a warning message "STS arbitrary policies feature is currently not available. Please ensure that the required policies are attached to the upgraded roles."  
- with '--debug' flag, there is an info message "I: STS arbitrary policies feature is currently not available for organization: 1jlfDskrR39egznAq3T18Ul0Xxv"  
- The aws commands for upgrading are prompted and can be executed successfully  
- The cluster upgrade action should succeed

## Step
Upgrade roles in auto mode

## Expect
- There is a warning message "STS arbitrary policies feature is currently not available. Please ensure that the required policies are attached to the upgraded roles."  
- with '--debug' flag, there is an info message "I: STS arbitrary policies feature is currently not available for organization: <org_id>"  
- The aws commands for upgrading are prompted and can be executed successfully  
- The cluster upgrade action should succeed

## Step
Upgrade cluster in manual mode

## Expect
Same as above

## Step
Upgrade cluster in auto mode

## Expect
Same as above

## Step
Repeat on hosted-cp cluster

## Expect
- I: Cluster 'yuwan-0611h1' operator roles have attached managed policies. An upgrade isn't needed  
- The cluster upgrade action should succeed
