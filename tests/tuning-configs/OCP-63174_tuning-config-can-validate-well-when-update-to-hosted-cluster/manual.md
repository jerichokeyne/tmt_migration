# Test

## Step
Prepare a hosted cluster.

## Expect

## Step
Create a tuning config to the cluster.

```bash
rosa create tuning-configs -c am-hp0105 --name=tuned01 --spec-path spec.file
vi spec.file
```

```json
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
```

## Expect
```
: Tuning config 'tuned01' has been created on cluster 'am-hp0105'.
I: To view all tuning configs, run 'rosa list tuning-configs -c am-hp0105'
```

## Step
Update the tuning config with an incorrect name.

```bash
rosa edit tuning-configs -c am-hp0105 --name=tuned03 --spec-path spec.file
```

## Expect
```
E: Tuning config 'tuned0' does not exist on cluster '23el6sntvmglp4qi1picvel80cvqtni3'
```

## Step
Update the tuning config with an incorrect spec file.

```bash
rosa edit tuning-configs -c am-hp0105 --name=tuned01 --spec-path spec.fil
```

## Expect
```
E: Expected a valid spec file: open : no such file or directory
```

## Step
Update the tuning config with an invalid spec set in body.

```bash
rosa edit tuning-configs -c am-hp0105 --name=tuned01 --spec-path spec.file
```

## Expect
```
E: Expected a valid spec file
```
