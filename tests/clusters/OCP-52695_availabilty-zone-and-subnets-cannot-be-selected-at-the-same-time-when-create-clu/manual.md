# Test

## Step
Create cluster with interactive mode  
$ rosa create cluster -i

## Expect
It will go into interactive mode

## Step
Fill in the required elements

## Expect

## Step
Fill yes for question  
? Install into an existing VPC (optional):

## Expect
Check that there will be subnets selections  
But  
There won't be zone questions

## Step
Repeat above step

## Expect

## Step
Fill "N" for question  
? Install into an existing VPC (optional):

## Expect
Check that there will be question Select availability zones (optional)  
[xueli@xueli-work rosa]$ rosa create cluster -i  
I: Interactive mode enabled.  
Any optional fields can be left empty and a default will be selected.  
? Cluster name: aaa  
? Deploy cluster using AWS STS: No  
? OpenShift version: 4.10.17  
? Multiple availability zones (optional): No  
? AWS region: us-west-2  
? PrivateLink cluster (optional): No  
? Private cluster (optional): No  
? Install into an existing VPC (optional): No  
? Select availability zones (optional): Yes  
? Availability zones: [Use arrows to move, space to select, <right> to all, <left> to none, type to filter, ? for more help]  
> [x] us-west-2a  
[ ] us-west-2b  
[ ] us-west-2c  
[ ] us-west-2d

## Step
Select "y"

## Expect
And it will show all of zones can be used for cluster deploy

## Step
Try on different regions

## Expect
The zone selection should be different based on the region

## Step
Select zone and create the cluster

## Expect
The cluster can be created successfully with the selected zone
