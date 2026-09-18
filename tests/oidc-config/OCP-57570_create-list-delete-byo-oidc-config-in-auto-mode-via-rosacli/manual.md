# Test

## Step
Create account-roles used in below steps

## Expect

## Step
Create managed=false oidc config in auto mode

```bash
rosa create oidc-config --mode auto -y --prefix <prefix> --installer-role-arn <role> -y
```

## Expect
- There is a message shown as bellow:

```
$ ./rosa create oidc-config --mode auto --region us-east-1 -y
I: This command will create a S3 bucket populating it with documents to be compliant with OIDC protocol. It will also create a Secret in Secrets Manager containing the private key.
I: Please run command below to create a cluster with this oidc config:
rosa create cluster --sts \
--oidc-endpoint-url https://oidc-q2t6.s3.us-east-1.amazonaws.com \
--oidc-private-key-secret-arn arn:aws:secretsmanager:us-east-1:301721915996:secret:rosa-private-key-oidc-q2t6-tef97i
```

- There is a s3 bucket creating on AWS
- The suffix is a random string of 4 charactors
- If the `prefix` is specified, the secret manager and the oidc endpoint url will be created named with the prefix like bellow:

```
$ ./rosa create oidc-config --prefix yw0207bcca1 --mode auto
I: This command will create a S3 bucket populating it with documents to be compliant with OIDC protocol. It will also create a Secret in Secrets Manager containing the private key.
I: Setting up OIDC configuration 'yw0207bcca1-oidc-l0h0'
I: Please run command below to create a cluster with this oidc config:
rosa create cluster --sts \
--oidc-endpoint-url https://yw0207bcca1-oidc-l0h0.s3.us-east-2.amazonaws.com \
--oidc-private-key-secret-arn arn:aws:secretsmanager:us-east-2:301721915996:secret:rosa-private-key-yw0207bcca1-oidc-l0h0-RDCIkP
$ ls -lrt
```

- All the created resources,including s3 bucket,openid-configuration, key, and secret manager should have the tag `red-hat-managed=true`

## Step
Check the validation of creating managed=false oidc config.

Validations for the prefix (for oidc-provider name/url and S3 bucket name and secret manager name):
- ~~special charators~~
- ~~dulplicated prefix~~
- the length (`maxLengthUserPrefix`)
- prefix and managed at the same time
- prefix and installer-role-arn at the same time

## Expect
- `W: --raw-files param is not supported alongside --managed paramv`

## Step
Validation for creating managed oidc config

- in manual mode
- existing one which is not used
- with `--installer-role-arn` flag
- with prefix flag
- with `raw-files` flag

## Expect
- `W: --managed=true param is not supported outside --mode auto flow`
- `E: There was a problem registering your managed OIDC Configuration: Your organization '1jlfDskrR39egznAq3T18Ul0Xxv' has an unused Managed OIDC Configuration '22os1ekqcem156vh5f2ar3bu09g76svn'`
- It should fail with readable error message
- `W: --prefix param is not supported for managed OIDC config`
- `W: --raw-files param is not supported alongside --managed param`

## Step
Create managed oidc config in auto mode

```bash
rosa create oidc-config --mode auto -y
```

NOTE: The managed=true is as default if no managed=false set

## Expect

## Step
Delete the byo config

## Expect
- It succeed deleted.

## Step
Check the validation of deleting byo config

- incorrect format of the ARN
- the not-existed arn

## Expect
There should be failed with readable error message
