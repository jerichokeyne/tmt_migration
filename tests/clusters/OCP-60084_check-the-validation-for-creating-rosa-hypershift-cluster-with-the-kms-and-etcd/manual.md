# Test

## Step

Prepare kms key by aws client.

```bash
aws kms create-key --tags TagKey=Purpose,TagValue=Test --description "yuwan BYOK Test Key 20230214usw2" --region us-west-2
```

## Expect

## Step

Try to create an ROSA Hypershift cluster only with --etcd-encryption (without --etcd-encryption-kms-arn flag)
```bash
rosa create cluster --cluster-name am-kms-v --sts --role-arn arn:aws:iam::425464789085:role/hp-test-Installer-Role --support-role-arn arn:aws:iam::425464789085:role/hp-test-Support-Role --controlplane-iam-role arn:aws:iam::425464789085:role/hp-test-ControlPlane-Role --worker-iam-role arn:aws:iam::425464789085:role/hp-test-Worker-Role --operator-roles-prefix am-kms-v-t6w5 --region us-west-2 --channel-group candidate --version 4.12.3 --replicas 2 --compute-machine-type m5.xlarge --machine-cidr 10.0.0.0/16 --service-cidr 172.30.0.0/16 --pod-cidr 10.128.0.0/14 --host-prefix 23 --subnet-ids subnet-0bd4e7b02a0f9ff07,subnet-0181c4dd03eb6e352 --hosted-cp --etcd-encryption
```

## Expect

Interactive mode is prompt and the user asked to add KMS ARN
```
? Etcd encryption KMS ARN: [? for help]
```

## Step

Try to create an ROSA Hypershift cluster with --etcd-encryption-kms-arn flag without value
```bash
rosa create cluster --cluster-name am-kms-v --sts --role-arn arn:aws:iam::425464789085:role/hp-test-Installer-Role --support-role-arn arn:aws:iam::425464789085:role/hp-test-Support-Role --controlplane-iam-role arn:aws:iam::425464789085:role/hp-test-ControlPlane-Role --worker-iam-role arn:aws:iam::425464789085:role/hp-test-Worker-Role --operator-roles-prefix am-kms-v-t6w5 --region us-west-2 --channel-group candidate --version 4.12.3 --replicas 2 --compute-machine-type m5.xlarge --machine-cidr 10.0.0.0/16 --service-cidr 172.30.0.0/16 --pod-cidr 10.128.0.0/14 --host-prefix 23 --subnet-ids subnet-0bd4e7b02a0f9ff07,subnet-0181c4dd03eb6e352 --hosted-cp --etcd-encryption --etcd-encryption-kms-arn
```

## Expect

IFailed to execute root command: flag needs an argument: --etcd-encryption-kms-arn

## Step

Try to create an ROSA Hypershift cluster with the invalid key arn by command
```bash
rosa create cluster --cluster-name am-kms-v --sts --role-arn arn:aws:iam::425464789085:role/hp-test-Installer-Role --support-role-arn arn:aws:iam::425464789085:role/hp-test-Support-Role --controlplane-iam-role arn:aws:iam::425464789085:role/hp-test-ControlPlane-Role --worker-iam-role arn:aws:iam::425464789085:role/hp-test-Worker-Role --operator-roles-prefix am-kms-v-t6w5 --region us-west-2 --channel-group candidate --version 4.12.3 --replicas 2 --compute-machine-type m5.xlarge --machine-cidr 10.0.0.0/16 --service-cidr 172.30.0.0/16 --pod-cidr 10.128.0.0/14 --host-prefix 23 --subnet-ids subnet-0bd4e7b02a0f9ff07,subnet-0181c4dd03eb6e352 --hosted-cp --etcd-encryption-kms-arn arn:aws:kms:us-west-2:425464789085:key/ffad33a8-ab67-412a-8759-4e3f6678af8d
```

## Expect

```
E: Failed to create cluster: KMS Key ARN 'arn:aws:kms:us-west-2:301721915996:key/9fdfaf2f-efb7-4db7-a5c3-0d047c52f094' not found in the region 'us-east-2'. Create a new one in the correct region, replace the ARN, and try again
```

## Step

Try to create ROSA Hypershift cluster with the valid key arn but the region is not matched.

## Expect

```
E: Failed to create cluster: Error when validating KMS Key ARN 'arn:aws:kms:us-east-1:301721915996:key/3ead7012-a878-4bc5-a14e-7962d8d5d540'. Check your key and try again
```

## Step

Try to create ROSA Hypershift cluster with the key arn which is not in the correct format.

## Expect

```
E: Expected a valid value for kms-key-arn. It should be in the format arn:aws:kms:<region>:<accountid>:key/<keyid>
```

## Step

Try to create ROSA Hypershift cluster with the wrong key arn

## Expect

`E: Failed to create cluster: KMS Key ARN 'XXX' not found in the region 'us-west-2'. Create a new one in the correct region, replace the ARN, and try again`

## Step

Try to create ROSA Hypershift cluster with the version <4.12.2

## Expect

The error is shown

## Step

Create classic rosa cluster with --etcd-encryption flag

## Expect

The cluster created successfully

## Step

Repeat step2~4 with the interactive mode.
1. the invalide key arn
2. the valid key arn but the region is not matched.
3. the key arn which is not in the correct format
4. empty arn

## Expect

- X Sorry, your reply was invalid: asd does not match regular expression ^arn:aws[\w-]*:kms:[\w-]+:\d{12}:key\/mrk-[0-9a-f]{32}$|[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$
-E: Failed to create cluster: KMS Key ARN 'arn:aws:kms:us-west-2:301721915996:key/9fdfaf2f-efb7-4db7-a5c3-0d047c52f094' not found in the region 'us-east-2'. Create a new one in the correct region, replace the ARN, and try again
-X Sorry, your reply was invalid: asd does not match regular expression ^arn:aws[\w-]*:kms:[\w-]+:\d{12}:key\/mrk-[0-9a-f]{32}$|[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$
- X Sorry, your reply was invalid: Value is required
