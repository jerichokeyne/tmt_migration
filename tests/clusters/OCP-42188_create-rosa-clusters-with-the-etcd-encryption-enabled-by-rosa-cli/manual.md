# Test

## Step

Log in with the rosa cli with the account which has no capability.account.allow_etcd_encryption label

## Expect

## Step

Check the 'rosa create cluster -h'

## Expect

The help message bellow is included.
.....
--etcd-encryption Enable etcd encryption for your cluster to provide an additional layer of data security
......

## Step

Try to create the etcd_encryption rosa cluster with the command.
```bash
rosa create cluster -c <cluster_name> --etcd-encryption
```

## Expect

It should create the cluster successfully.

## Step

~~Check the prompt for the etcd_encryption in the interactive mode and create the cluster with choosing etcd_encryption yes~~

## Expect

~~? Enable etcd encryption (optional): [? for help] (y/N) y~~
~~? Enable etcd encryption (optional): Yes .... It should fail with the error E: Failed to create cluster: 'allow_etcd_encryption' capability is not set for this account~~

## Step

Login with the account which has the capability.account.allow_etcd_encryption label

## Expect

## Step

Try to create the etcd_encryption rosa cluster with the command.

## Expect

It should be created successfully.
Wait for the cluster ready and go the the cluster console and check if it works.
```bash
oc get openshiftapiserver -o=jsonpath='{range .items[0].status.conditions[?(@.type=="Encrypted")]}{.reason}{"\n"}{.message}{"\n"}'
```
The output should contain bellow message:
EncryptionCompleted
All resources encrypted: routes.route.openshift.io, oauthaccesstokens.oauth.openshift.io, oauthauthorizetokens.oauth.openshift.io

## Step

~~Try to create the etcd_encryption rosa cluster with the interactive mode.~~
From SDA-4602, the etcd-encryption is not shown in the interactive mode.

## Expect

## Step

Repeat the steps on Windows/MacOS/Linux

## Expect

- The function should work well
- The output should displau well
