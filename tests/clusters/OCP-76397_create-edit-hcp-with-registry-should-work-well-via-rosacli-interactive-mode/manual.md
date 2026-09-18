# Test

## Step

create hcp with registry config via interactive mode
```bash
rosa create cluster --hosted-cp -i
```

## Expect

-It will prompt
....
```
? Enable registries config: Yes
? Allowed Registries (optional): insecure1.io,insecure2.io,insecure3.io
? Blocked Registries (optional): insecure4.io,insecure5.io
? Insecure Registries (optional): insecure7.io,insecure6.io
X Sorry, your reply was invalid: invalid identifier ' test.com:true' for 'allowed registries for import.' Should be in a <registry>:<boolean> format. The boolean indicates whether the registry is secure or not.
? Allowed Registries For Import (optional): test.com:true,test2.com:false
? Registry Additional Trusted CA (optional):
...
```

## Step

Create hcp with registry config with invalid value

## Expect

-it will not exist and provide a readable message

## Step

Edit hcp cluster registry config via interactive mode
```bash
rosa edit cluster <> -i
```

  * delete the configured value
  * add the non-configured value
  * update the configured value

## Expect

-It will prompt
-The value should be updated successfully
```bash
rosa edit cluster -c sdq-longname-yrqzz-dbkwdtkblpdwejcybjlpdrprlwuaennedfc
```
```
I: Interactive mode enabled.
Any optional fields can be ignored and will not be updated.
? Private cluster, check this command's help for possible impacts: No
? Disable Workload monitoring: Yes
? Update cluster-wide proxy: No
? Update additional trust bundle: No
? Update additional allowed principals: No
? Update existing audit log forwarding role 'arn:aws:iam::301721915996:role/drprlwuaennedfc': No
? Disable Audit Log: No
? Allowed Registries: untrusted.com,docker.io
? Insecure Registries: test.io
? Allowed Registries For Import: test.com:true
? Registry Additional Trusted CA (optional):
? Changing any registry related parameter will trigger a rollout across all machinepools (all machinepool nodes will be recreated, following pod draining from each node). Do you want to proceed? (y/N)
```

## Step

Edit hcp with registry config with invalid value

## Expect

-It will not exist and provide a readable message
