# Setup
Create HCP cluster

# Test

## Step
1. Create new machinepool with correct tags
```bash
rosa create machinepool -c jf-hcp --name=mp-1--tags "label:value,label2:value2"
```

## Expect
```
I: Checking available instance types for machine pool 'mp-1'
I: Machine pool 'mp-1' created successfully on hosted cluster 'jf-hcp2'
I: To view the machine pool details, run 'rosa describe machinepool --cluster jf-hcp2 --machinepool mp-1'
I: To view all machine pools, run 'rosa list machinepools --cluster jf-hcp2'
```

## Step
2. Describe new machinepool

## Expect
```
ID: mp-1
Cluster ID: 2b421k4rh3pbjaq1r5vfkbqpkvddr7n5
Autoscaling: No
Desired replicas: 2
Current replicas: 2
Instance type: m5.xlarge
Labels:
Tags: api.openshift.com/nodepool-hypershift=jf-hcp2-mp-1, api.openshift.com/nodepool-ocm=mp-1, red-hat-clustertype=rosa, api.openshift.com/name=jf-hcp2, label=value, label2=value2, cluster-tag=cluster-value, red-hat-managed=true, api.openshift.com/environment=staging, api.openshift.com/id=2b421k4rh3pbjaq1r5vfkbqpkvddr7n5, api.openshift.com/legal-entity-id=1jlfDskrR39egznAq3T18Ul0Xxv
Taints:
Availability zone: us-west-2a
Subnet: subnet-0309526054864f01b
Version: 4.15.6
Autorepair: Yes
Tuning configs:
Additional security group IDs:
Node drain grace period:
Message:
```

## Step
3. Attempt to create machinepool with too many tags
```bash
rosa create machinepool --name=mp-2 -c jf-hcp2 --replicas=2 --tags "foo:bar,foo1:bar1,foo2:bar,foo3:bar1,foo4:bar1,foo5:bar1,
```
foo6:bar1,foo7:bar1,foo8:bar1,foo9:bar1,foo10:bar1,foo11:bar1,foo12:bar1,foo13:bar1,foo14:bar1,foo15:bar1,foo16:bar1,
foo17:bar1,foo18:bar1,foo19:bar1,foo20:bar1,foo21:bar1,foo22:bar1,foo23:bar1,foo24:bar1foo25:bar1,foo26:bar1,foo27:bar1,
foo28:bar1,foo29:bar1,foo30:bar1,foo31:bar1,foo32:bar1,foo33:bar1,foo34:bar1,foo35:bar1,foo36:bar1,foo37:bar1,foo38:bar1,foo39:bar1,
foo40:bar1,foo41:bar1,foo42:bar1,foo43:bar1,foo44:bar1,foo45:bar1,foo46:bar1,foo47:bar1,foo48:bar1,foo49:bar1,foo50:bar1,foo51:bar1"

## Expect
```
I: Checking available instance types for machine pool 'mp-2'
E: Failed to add machine pool to hosted cluster 'jf-hcp2': Invalid Node Pool AWS tags: Resource has too many AWS tags (52). A resource may have a maximum of 25 AWS tags. Please reduce the number of tags and try again.
```

## Step
4. Attempt to create machinepool with too long of a key name
```bash
rosa create machinepool --name=mp-1 -c jf-hcp2 --replicas=2 --tags "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
```
fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff:bar"

## Expect
```
E: expected a valid user tag key 'fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff' matching ^[\pL\pZ\pN_.:/=+\-@]{1,128}$
```

## Step
5. Attempt to create machinepool with too long of a value name
```bash
rosa create machinepool --name=mp-1 -c jf-hcp2 --replicas=2 --tags "foo:ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
```
fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff"

## Expect
```
E: expected a valid user tag value 'ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
fffffffffffffffffffffffffffffffffffffffffffffffffffffffffff' matching ^[\pL\pZ\pN_.:/=+\-@]{0,256}$
```

## Step
6. Attempt to create machinepool with "aws:" as a prefix
```bash
rosa create machinepool --name=mp-1 -c jf-hcp2 --replicas=2 --tags "aws:foo:bar"
```

## Expect
```
E: invalid tag format for tag '[aws foo bar]'. Expected tag format: 'key value'
```

## Step
7. Attempt to create machinepool with invalid key tag
```bash
rosa create machinepool --name=mp-3 -c jf-hcp2 --replicas=2 --tags '#:bar'
```

## Expect
```
E: expected a valid user tag key '#' matching ^[\pL\pZ\pN_.:/=+\-@]{1,128}$
```

## Step
8. Attempt to create machinepool with invalid value tag
```bash
rosa create machinepool --name=mp-3 -c jf-hcp2 --replicas=2 --tags 'foo:#'
```

## Expect
```
E: expected a valid user tag value '#' matching ^[\pL\pZ\pN_.:/=+\-@]{0,256}$
```
