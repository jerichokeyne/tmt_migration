# Test

## Step
Check the validation for cmd  
\# rosa upgrade cluster -c <> --control-plane

## Expect

## Step
Check validation for the command:  
- without --control-plane   
- invalida cluster id  
- incorrect format of the date and time

## Expect
There should be error message shown.

## Step
Check validation for this commnad:  
- set '--schedule' and '--version' at the same time  
- set --schedule with value not match the cron expression  
- set '--schedule-date' and '--schedule-time' and '--schedule' at the same time

## Expect
- E: The '--schedule' option is mutually exclusive with '--version'  
- E: Schedule 'asd' is not a valid cron expression  
- E: The '--schedule-date' and '--schedule-time' options are mutually exclusive with '--schedule'

## Step
Try to upgrade the Control Plane and setting the `node_drain_grace_period`

## Expect
It should fail  
  
> rosa upgrade cluster -c $CLUSTER_NAME --control-plane --node-drain-grace-period 60  
? IAM Roles/Policies upgrade mode (default = 'auto'): auto  
? Version (default = '4.14.10'): 4.14.10  
I: Ensuring account and operator role policies for cluster '29bth8oogj4asqun523ba16klqsefcha' are compatible with upgrade.  
I: Account roles with the prefix 'tr-prev2' have attached managed policies.  
I: Cluster 'tr-prev2' operator roles have attached managed policies. An upgrade isn't needed  
I: Account and operator roles for cluster 'tr-prev2' are compatible with upgrade  
**E: node-drain-grace-period flag is not supported to hosted clusters**
