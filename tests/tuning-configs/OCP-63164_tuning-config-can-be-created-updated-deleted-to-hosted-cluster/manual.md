# Test

## Step
Prepare a hosted cluster

## Expect

## Step
Create a tuning config (json) to the cluster  
~ > rosa create tuning-configs -c am-hp0105 --name=tuned01 --spec-path spec.file  
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
I: Tuning config 'tuned01' has been created on cluster 'am-hp0105'.  
I: To view all tuning configs, run 'rosa list tuning-configs -c am-hp0105'

## Step
Create another tuning config (yaml) to the cluster
    
    ~ > rosa create tuning-configs -c am-hp0105 --name=tuned02 --spec-path spec.file  
    vi spec.file<pre>{  
    profile:  
      - data: |-  
          [main]  
          summary=Custom OpenShift profile  
          include=openshift-node  
          [sysctl]  
          vm.dirty_ratio=\"25\"  
        name: tuned-3-profile  
    recommend  
      - priority: 10  
        profile: tuned-3-profile

## Expect
I: Tuning config 'tuned02' has been created on cluster 'am-hp0105'.  
I: To view all tuning configs, run 'rosa list tuning-configs -c am-hp0105'

## Step
List the tuning configs  
~ > rosa list tuning-configs -c am-hp0105

## Expect
27431487-e8ae-11ed-a846-0a580a810e4b tuned01  
7d97ac61-e8ae-11ed-ac0e-0a580a800c79 tuned02

## Step
Update tuning config to the cluster
    
    ~ > rosa update tuning-configs -c am-hp0105 tuned01 --spec-path spec.file  
    vi spec.file<pre>{  
        "profile": [  
          {  
            "data": "[main]\nsummary=Custom OpenShift profile\ninclude=openshift-node\n\n[sysctl]\nvm.dirty_ratio=\"25\"\n",  
            "name": "tuned-2-profile"  
          }  
        ],  
        "recommend": [  
          {  
            "priority": 10,  
            "profile": "tuned-2-profile"  
          }  
        ]  
     }

## Expect
I: Updated tuning config 'tuned01' for cluster 'am-hp0105'

## Step
Check the description of the tuning config  
`rosa describe tuning-config tuned01 -c ying-hp-kms`

## Expect
- The output should be updated ones.

## Step
Delete tuning config on the cluster
    
    ~ > rosa delete tuning-configs -c am-hp0105 tuned01

## Expect
I: Successfully deleted tuning config 'tuned01' from cluster 'am-hp0105'

## Step
List the tuning configs  
~ > rosa list tuning-configs -c am-hp0105

## Expect
- The deleted one is not in the output
