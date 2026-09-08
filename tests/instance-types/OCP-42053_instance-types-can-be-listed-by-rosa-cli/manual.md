# Test

## Step
Log in with the rosa tool

## Expect

## Step
Run below command to check the help message  
$ rosa list -h   
$ rosa list instance-types --help

## Expect
\# ./rosa list instance-types -h  
List Instance types that are available for use with ROSA.  
  
Usage:  
rosa list instance-types [flags]  
  
Aliases:  
instance-types, instancetypes  
  
Examples:  
\# List all instance types  
rosa list instance-types  
  
Flags:  
-h, --help help for instance-types  
  
Global Flags:  
--debug Enable debug mode.  
--profile string Use a specific AWS profile from your credential file.  
[root@yuwan rosa]#

## Step
Run below command to list the available instance-types  
$ rosa list instance-types

## Expect
- The available instance-types will be listed
