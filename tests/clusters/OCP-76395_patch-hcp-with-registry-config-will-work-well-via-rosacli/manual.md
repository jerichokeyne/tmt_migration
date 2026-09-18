# Test

## Step

Check the edit help message
```bash
rosa edit cluster -h
```

## Expect

-The registry config related flag should be in it
...
--registry-config-allowed-registries strings A comma-separated list of registries for which image pull and push actions are allowed.
--registry-config-insecure-registries strings A comma-separated list of registries which do not have a valid TLS certificate or only support HTTP connections.
--registry-config-blocked-registries strings A comma-separated list of registries for which image pull and push actions are denied.
--registry-config-allowed-registries-for-import string Limits the container image registries from which normal users can import images. The format should be a comma-separated list of 'domainName:insecure'. 'domainName' specifies a domain name for the registry. 'insecure' indicates whether the registry is secure or insecure.
--registry-config-additional-trusted-ca string A json file containing the registry hostname as the key, and the PEM-encoded certificate as the value, for each additional registry CA to trust.
-h, --help help for cluster
...

## Step

Edit hcp cluster registry config with the below scenarios

  * delete the configured value
  * add the non-configured value
  * update the configured value

## Expect

-The parameters should be updated accordingly
-There will be question to remind users
$rosa edit cluster -c sdq-longname-yrqzz-dbkwdtkblpdwejcybjlpdrprlwuaennedfc --registry-config-blocked-registries "test.com"
```
? Changing any registry related parameter will trigger a rollout across all machinepools (all machinepool nodes will be recreated, following pod draining from each node). Do you want to proceed? Yes
I: Updated cluster 'sdq-longname-yrqzz-dbkwdtkblpdwejcybjlpdrprlwuaennedfc'
```

## Step

Describe the hcp cluster

## Expect

-The parameters value should be updated
