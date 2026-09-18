# Test

## Step

Try to create a cluster in interactive mode, and say yes to 'Configure cluster-autoscaler'

## Expect

## Step

Check the default value for the 'Maximum amount of nodes in the cluster'

## Expect

**To calculate the CAS maxNodesTotal for CLASSIC ROSA clusters,**
it takes into account:
**number of worker nodes**
below v4.14.14 == 180 nodes limit OR
at or above v4.14.14 == 249 nodes limit
PLUS
**number of infra nodes**
single AZ == 2 infra nodes OR
multi AZ == 3 infra nodes
PLUS
**number of master nodes**
fixed at 3 master nodes based on default [OSD-4](<https://issues.redhat.com/browse/OSD-4> "R&D refactoring repos") (default flavour)

So, for example (for a 4.17.7 cluster in a single AZ):
```
? Maximum amount of nodes in the cluster: (254)
```

## Step

Repeat the previous step for both the "rosa create autoscaler" command and "rosa edit autoscaler" command

## Expect

Should show the same value as the previous step

## Step

Try to create a cluster and check that the fields have the correct maximum value by entering too large of a number

? Compute nodes: [? for help] (3)
? Min replicas: [? for help] (2)
? Max replicas: [? for help] (2)

## Expect

Classic:**
180 or 249 for Classic is determined by below logi** c:
**number of worker node** **limits** **allowable during create and edit MP**
below v4.14.14 == 180 nodes limit OR
at or above v4.14.14 == 249 nodes limit
X Sorry, your reply was invalid: should provide an integer number less than or equal to '249'

HCP:
Always 500 nodes limit
X Sorry, your reply was invalid: should provide an integer number less than or equal to '500'

## Step

Try to create and edit a machinepool for a cluster and check that the following fields have the same maximum value as the previous step

? Replicas: [? for help] (2)
? Min replicas: [? for help]
? Max replicas: [? for help]

## Expect
