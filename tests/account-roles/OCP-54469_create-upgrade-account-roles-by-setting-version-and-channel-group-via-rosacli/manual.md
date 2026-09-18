# Test

## Step
Log in with `rosa login`.

It is recommended to use the SDQE ROSA account because personal accounts might not have channel groups enabled.

## Expect
```
$ rosa login
To login to your Red Hat account, get an offline access token at https://console.redhat.com/openshift/token/rosa
I: Logged in as 'sdqe-rosa' on 'https://api.openshift.com'
```

## Step
Create account roles with different versions and channel groups.

```bash
rosa create account-roles --prefix <prefix> --mode auto --version <specific_version> --channel-group <channel_group>
```

Supported versions are currently `4.11`, `4.10`, `4.9`, `4.8`, and `4.7`. Potential channel groups are [listed in the documentation](https://docs.openshift.com/container-platform/4.13/updating/understanding-upgrade-channels-release.html).

## Expect
- Account roles with the specified version are created, and roles and policies are tagged with the version.
- The channel group works if a new version is released in that channel.

```
$ rosa create account-roles --prefix oaharoni --mode auto --channel-group fast
I: Logged in as 'sdqe-rosa' on 'https://api.openshift.com'
I: Validating AWS credentials...
I: AWS credentials are valid!
I: Validating AWS quota...
I: AWS quota ok. If cluster installation fails, validate actual AWS resource usage against https://docs.openshift.com/rosa/rosa_getting_started/rosa-required-aws-service-quotas.html
I: Verifying whether OpenShift command-line tool is available...
I: Current OpenShift Client Version: 4.14.6
I: Creating account roles
I: By default, the create account-roles command creates two sets of account roles, one for classic ROSA clusters, and one for Hosted Control Plane clusters.
In order to create a single set, please set one of the following flags: --classic or --hosted-cp
I: Creating classic account roles using 'arn:aws:iam::301721915996:user/oaharoni'
I: Created role 'oaharoni-Support-Role' with ARN 'arn:aws:iam::301721915996:role/oaharoni-Support-Role'
I: Created role 'oaharoni-Installer-Role' with ARN 'arn:aws:iam::301721915996:role/oaharoni-Installer-Role'
I: Created role 'oaharoni-ControlPlane-Role' with ARN 'arn:aws:iam::301721915996:role/oaharoni-ControlPlane-Role'
I: Created role 'oaharoni-Worker-Role' with ARN 'arn:aws:iam::301721915996:role/oaharoni-Worker-Role'
I: Creating hosted CP account roles using 'arn:aws:iam::301721915996:user/oaharoni'
I: Created role 'oaharoni-HCP-ROSA-Installer-Role' with ARN 'arn:aws:iam::301721915996:role/oaharoni-HCP-ROSA-Installer-Role'
I: Created role 'oaharoni-HCP-ROSA-Support-Role' with ARN 'arn:aws:iam::301721915996:role/oaharoni-HCP-ROSA-Support-Role'
I: Created role 'oaharoni-HCP-ROSA-Worker-Role' with ARN 'arn:aws:iam::301721915996:role/oaharoni-HCP-ROSA-Worker-Role'
```

## Step
Upgrade account roles from a lower version to a higher version using `--version` and `--channel-group`.

## Expect
- Account roles with the specified version are upgraded, and roles and policies are tagged with the version.
- The channel group works if a new version is released in that channel.

## Step
Repeat steps 2-3 in manual mode.

```bash
rosa create account-roles --prefix <prefix> --path <path> --mode manual --version <specific_version> --channel-group <channel_group>
```

## Expect
The results should be the same as above.
