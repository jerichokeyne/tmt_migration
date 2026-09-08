# Test

## Step
Check the help message of `rosa describe -h` and `rosa describe upgrade -h`

## Expect
....  
upgrade Show details of an upgrade  
....  
$ ./rosa describe upgrade -h  
Show details of an upgrade  
  
Usage:  
rosa describe upgrade [flags]  
  
Aliases:  
upgrade, appliance, upgrade  
  
Examples:  
\# Describe an upgrade-policy"  
rosa describe upgrade  
  
Flags:  
-c, --cluster string Name or ID of the cluster.  
-h, --help help for upgrade  
  
Global Flags:  
--color string Surround certain characters with escape sequences to display them in color on the terminal. Allowed options are [auto never always] (default "auto")  
--debug Enable debug mode.  
--profile string Use a specific AWS profile from your credential file.  
--region string Use a specific AWS region, overriding the AWS_REGION environment variable.

## Step
Create NON-STS rosa cluster which has an upgrade path

## Expect

## Step
Run `rosa describe upgarde -c <id>`

## Expect
$ ./rosa describe upgrade -c 20oak9878aef084ltpgcfe3v7r7rgr07  
E: No available upgrades for cluster id '20oak9878aef084ltpgcfe3v7r7rgr07' (It's better use warning message rather than error)

## Step
Schedule a manual upgrade policy  
\# rosa upgrade cluster

## Expect

## Step
Run `rosa list upgarde -c <id>`

## Expect
The NOTEs colume in the correct version shows 'scheduled',  
.....  
4.11.3 scheduled for 2022-12-22 15:00 UTC  
.....

## Step
Run `rosa describe upgarde -c <id>`

## Expect
yuwan1-mac:rosa yuwan$ ./rosa describe upgrade -c 20ork9ug8fa7645kkp99h8cogt7ltsnc  
  
ID: 447e53c6-81d2-11ed-b127-0a580a8114ea  
Cluster ID: 20ork9ug8fa7645kkp99h8cogt7ltsnc  
Next Run: 2022-12-22 15:00:00 +0000 UTC  
Upgrade State: scheduled  
Version: 4.11.3  
  
The info in the output should be correct.

## Step
Delete the manual upgrade schedule

## Expect

## Step
Create a automatic upgrade via UI or API

## Expect

## Step
Run `rosa list upgarde -c <id>`

## Expect
Same as above

## Step
Run `rosa describe upgarde -c <id>`

## Expect
Same as above

## Step
Run `rosa upgrade cluster -c <id>` again

## Expect
There should be some warning message shown,  
W: There is already a scheduled upgrade to version 4.10.45 on 2022-12-25 08:00 UTC

## Step
Repeat the steps with Hypershift cluster

## Expect
Validate that only hypershift_enabled versions are available for Upgrade
