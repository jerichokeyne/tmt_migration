# Test

## Step
Prepare a hosted cluster

## Expect

## Step
Create a tuning config to the cluster  
~ > rosa create tuning-configs -c am-hp0105 -i  
? Name of the tuning config: am  
? Path of the file containing the spec of the tuning config: spec.file  
  
  
vi spec.file
    
    {  
        "profile": [  
          {  
            "data": "[main]\nsummary=Custom OpenShift profile\ninclude=openshift-node\n\n[sysctl]\nvm.dirty_ratio=\"65\"\n",  
            "name": "tuned-2-profile"  
          }  
        ],  
        "recommend": [  
          {  
            "priority": 20,  
            "profile": "tuned-2-profile"  
          }  
        ]  
     }

## Expect
II: Tuning config 'am' has been created on cluster 'am-hp0105'.  
I: To view all tuning configs, run 'rosa list tuning-configs -c am-hp0105'

## Step
Create another tuning config to the cluster
    
    ~ > rosa create tuning-configs -c am-hp0105 -i  
    ? Name of the tuning config: am2  
    ? Path of the file containing the spec of the tuning config: spec.file  
    vi spec.file<pre>{  
        "profile": [  
          {  
            "data": "[main]\nsummary=Custom OpenShift profile\ninclude=openshift-node\n\n[sysctl]\nvm.dirty_ratio=\"25\"\n",  
            "name": "tuned-3-profile"  
          }  
        ],  
        "recommend": [  
          {  
            "priority": 10,  
            "profile": "tuned-3-profile"  
          }  
        ]  
     }

## Expect
I: Tuning config 'am2' has been created on cluster 'am-hp0105'.  
I: To view all tuning configs, run 'rosa list tuning-configs -c am-hp0105'

## Step
List the tuning configs  
~ > rosa list tuning-configs -c am-hp0105

## Expect
27431487-e8ae-11ed-a846-0a580a810e4b am  
7d97ac61-e8ae-11ed-ac0e-0a580a800c79 am2

## Step
Update the tuning config in interactive mode  
> rosa edit tuning-config -c am-hp0105 am -i  
? Path of the file containing the spec of the tuning config: spec.file

## Expect
I: Updated tuning config 'am' for cluster 'am-hp0105'
