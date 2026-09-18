# Test

## Step

Create non-sts cluster with the use-local-credentials flag

## Expect

- The cluster should be created
- The creation operation will use the default local credential
- osdCcsAdmin user credential will not be updated
- There is warning message W: Using local AWS access key for 'arn:aws:iam::301721915996:user/yuwan'
- The cluster spec should contain:
.....
"properties": {
.....
"use_local_credentials": "true"
},
.....

## Step

Create machinepool on the cluster

## Expect

- The machinepool should be created
- The creation operation will use the default local credential
- osdCcsAdmin user credential will not be updated
