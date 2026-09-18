# Test

## Step
Prepare a classic cluster.

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
E: This command is only supported for Hosted Control Planes
```
