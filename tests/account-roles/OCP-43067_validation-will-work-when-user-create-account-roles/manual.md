# Setup

```bash
rosa create cluster -c ${name}aa --region ${region} --version ${version}-${channel_group} --channel-group ${channel_group} --role-arn arn:aws:iam::${aws_account_id}:role/OSDCCSAdmin --tags cluster-name:${name},cluster-version:${version}-${channel_group} ${roles} --external-id "<external_id>"
```

# Test

## Step
Get the latest version of ROSA CLI.

## Expect
STS is supported from version `1.0.6`.

## Step
Create account roles with an invalid prefix.

```bash
rosa create account-roles --prefix ^^^^ --mode auto -y
```

## Expect
```
$ rosa create account-roles --prefix ^^^^ --version 4.7 --mode auto -y
I: Creating roles using 'arn:aws:iam::301721915996:user/xueli'
E: There was an error creating the account roles: ValidationError: The specified value for roleName is invalid. It must contain only alphanumeric characters and/or the following: +=,.@_-
status code: 400, request id: 51a28ec8-39f0-490a-9f40-90a07548b584
```

## Step
Create account roles with a prefix longer than 32 characters.

```bash
rosa create account-roles --prefix iamlongerthan32charactersiamlongerthan32characters --mode auto -y
```

## Expect
```
$ rosa init account --prefix iamlongerthan32charactersiamlongerthan32characters --version 4.7 --mode auto -y
I: Logged in as 'sdqe-sre' on 'https://api.openshift.com'
I: Validating AWS credentials...
I: AWS credentials are valid!
I: Validating AWS quota...
I: AWS quota ok. If cluster installation fails, validate actual AWS resource usage against https://docs.openshift.com/rosa/rosa_getting_started/rosa-required-aws-service-quotas.html
I: Verifying whether OpenShift command-line tool is available...
I: Current OpenShift Client Version: 4.8.0-fc.2
E: Expected a prefix with no more than 32 characters
```

## Step
Create account roles with an invalid mode.

```bash
rosa create account-roles --prefix valid --mode invalid -y
```

## Expect
```
$ rosa create account-roles --prefix valid --version 4.7 --mode invalid -y
E: Invalid mode. Allowed values are [auto manual]
```

## Step
Create account roles in auto mode with an invalid permissions boundary.

```bash
rosa create account-roles --prefix valid --mode auto -y --permissions-boundary invalid
```

## Expect
```
$ rosa create account-roles --permissions-boundary non-existed --version 4.8 --mode auto -y
E: Expected a valid policy ARN: arn: invalid prefix
```

## Step
Create account roles with a non-existing permissions boundary.

```bash
rosa create account-roles --prefix valid --mode auto -y --permissions-boundary arn:aws:iam::301721915996:policy/non-existing
```

## Expect
```
$ rosa create account-roles --permissions-boundary arn:aws:iam::301721915996:policy/xueli-openshift-cloud-credential-operator-cloud-credential-operanon-existed --version 4.8 --mode auto -y
I: Creating roles using 'arn:aws:iam::301721915996:user/xueli'
E: There was an error creating the account roles: NoSuchEntity: Scope ARN: arn:aws:iam::301721915996:policy/xueli-openshift-cloud-credential-operator-cloud-credential-operanon-existed does not exist or is not attachable.
status code: 404, request id: 5ce042b3-868b-456c-b5ae-dea9b4cf903d
```

## Step
Create account roles with force-policy creation in manual mode.

```bash
rosa create account-roles -f --mode manual
```

## Expect
```
I: Logged in as 'hac-ecosystem' on 'https://api.stage.openshift.com'
I: Validating AWS credentials...
I: AWS credentials are valid!
I: Validating AWS quota...
I: AWS quota ok. If cluster installation fails, validate actual AWS resource usage against https://docs.openshift.com/rosa/rosa_getting_started/rosa-required-aws-service-quotas.html
I: Verifying whether OpenShift command-line tool is available...
I: Current OpenShift Client Version: 4.11.0
I: Creating account roles
W: Forcing creation of policies only works in auto mode
```
