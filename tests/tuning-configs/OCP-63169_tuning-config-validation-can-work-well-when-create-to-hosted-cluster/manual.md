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
I: Tuning config 'tuned01' has been created on cluster 'am-hp0105'.
I: To view all tuning configs, run 'rosa list tuning-configs -c am-hp0105'
```

## Step
Create another tuning config in same name.

## Expect
```
E: Failed to add tuning config to cluster 'am-hp0105': A tuning config with name 'tuned02' and id '7d97ac61-e8ae-11ed-ac0e-0a580a800c79' already exists for cluster '23el6sntvmglp4qi1picvel80cvqtni3'
```

## Step
Create tuning config with name set to nil.

## Expect
```
Failed to execute root command: flag needs an argument: --name
```

## Step
Create tuning config with spec set to nil.

## Expect
```
E: Expected a valid TuneD spec file
```

## Step
Create a tuning config with invalid name like `%^&*(`.

## Expect
```
E: Failed to add tuning config to cluster 'am-hp0105': Name 'E##' is not valid. The name must be a lowercase RFC 1123 subdomain.
```

## Step
Create a tuning with invalid spec like `$%^&*(`.

## Expect
```
E: Expected a valid TuneD spec file: open spec.fil: no such file or directory
```

## Step
Create more than 100 tuning config to the cluster.

## Expect
```
E: Failed to add tuning config to cluster '2d8qc292r7mhb91rk5l3g36sr79rm3ts': Maximum number of TuningConfigs per cluster reached. Maximum allowed is '100'. Current count is '100'. Please review existing TuningConfigs and consider clearing some, then try again(OCM-10123)
```
