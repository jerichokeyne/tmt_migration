# Test

## Step

Prepare kms key by aws client.
```bash
aws kms create-key --tags TagKey=Purpose,TagValue=Test --description "BYOK Test Key"
```

## Expect

## Step

Check the help message of 'rosa create cluster -h'

## Expect

--enable-customer-managed-key Enable to specific your KMS Key to encrypt EBS instance volumes. By default account’s default KMS key for that particular region is used.
--kms-key-arn string The key ARN is the Amazon Resource Name (ARN) of a CMK. It is a unique, fully qualified identifier for the CMK. A key ARN includes the AWS account, Region, and the key ID.

## Step

Create one cluster with the BYOK encryption by command.
```bash
rosa create cluster -c <cluster_name> --enable-customer-managed-key --kms-key-arn <arn>
```

## Expect

1. The cluster should be created successfully.
2. If only set --kms-key-arn flag but without --enable-customer-managed-key, it should work
3. If only set --enable-customer-managed-key flag but without --kms-key-arn, the interactive mode should be prompted.
4. Check the instance ebs is encrypted

## Step

Create one cluster the BYOK encryption via the interactive mode.
```bash
rosa create cluster -i
```

## Expect

1. There should be bellow items prompted in the interactive mode.
```
? Enable Customer Managed key (optional): Yes
? KMS Key ARN: arn:aws:kms:us-east-1:301721915996:key/3ead7012-a878-4bc5-a14e-7962d8d5d540
```

2. The cluster should be created successfully.
3. Check the instances ebs is encrypted

## Step

Login the cluster.
```bash
oc get co
```

## Expect

- All cluster operators are working well, in the active status
