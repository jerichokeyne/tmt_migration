# Test

## Step
Make sure that the migration block doesn't show up when there's no migration in progress  
  
**rosa describe cluster -c $CLUSTER_ID**

## Expect
When checking the describe output, make sure there's no Migrations block  
  
eg. **rosa describe cluster -c jkeyne-0123-01 | grep 'Migrations'** should fail/produce no output

## Step
Make sure that the migration block does show up when there is a migration scheduled  
  
**rosa describe cluster -c $CLUSTER_ID**

## Expect
There should be a migrations section in the output like:  
  
Migrations:  
- 2gipbnqh1ebfe8itgj5md247t5s0k74c  
- Type: sdnToOvn  
- State: scheduled  
- Description:

## Step
Once it's started it should say that the migration is in progress

## Expect
Migrations:  
- 2gipbnqh1ebfe8itgj5md247t5s0k74c  
- Type: sdnToOvn  
- State: in progress  
- Description: migration in progress  
  
Migrations:  
- 2gipbnqh1ebfe8itgj5md247t5s0k74c  
- Type: sdnToOvn  
- State: in progress  
- Description: migration in progress, OVNKubernetes is deployed in the cluster

## Step
Once the migration is done, there should be no migration block and the network type should show as OVNKubernetes

## Expect
The network section should show the type as "OVNKuberntes"  
Network:  
- Type: OVNKubernetes  
- Service CIDR: 172.30.0.0/16  
- Machine CIDR: 10.0.0.0/16  
- Pod CIDR: 10.128.0.0/14  
- Host Prefix: /23  
  
And there should not be a migrations section

## Step
Check that "-o json" and "-o yaml" show the migration status

## Expect
rosa describe cluster -c $CLUSTER_ID -o json | jq .migrations  
[  
{  
"id": "2gkltf2iav79v1k8a4p5egq7j0cdl6fd",  
"state": "scheduled",  
"type": "sdnToOvn"  
}  
]
