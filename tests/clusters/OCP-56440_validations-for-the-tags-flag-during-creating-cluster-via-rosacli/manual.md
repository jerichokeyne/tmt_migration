# Setup
$ rosa create cluster -c ${name}aa --region ${region} --version ${version}-${channel_group} --channel-group ${channel_group} --role-arn arn:aws:iam::${aws_account_id}:role/OSDCCSAdmin --tags cluster-name:${name},cluster-version:${version}-${channel_group} ${roles} --external-id "<external_id>"

# Test

## Step
Check the validation for the '--tags' flag during `rosa create cluster`  
- The key doesn't match `^[\pL\pZ\pN_.:/=+\-@]{1,128}$` , for example, --tags=~~~:cluster  
- The value doesn't match `^[\pL\pZ\pN_.:/=+\-@]{0,256}$`, for example, --tags=name:****  
- Duplicated key, for example, --tags=name:test1,op:clound,name:test2  
- The tag doesn't contain : character for example, --tags=test1,test2,test4  
- Empty key/value, i.e. --tags foo:  
- --tags=name:gender:age

## Expect
Should fail with readable error message:  
E: expected a valid user tag key '^^^' matching ^[\pL\pZ\pN_.:/=+\-@]{1,128}$  
E: expected a valid user tag value '***' matching ^[\pL\pZ\pN_.:/=+\-@]{0,256}$  
E: Invalid tags, user tag keys must be unique, duplicate key 'name' found  
E: invalid tag format, Tags are comma separated, for example: --tags=foo:bar,bar:baz  
E: Failed to create cluster: Attribute value of 'aws.tags.foo' invalid, expected a non-empty value  
E: invalid tag format. Expected tag format: --tags=key:value
