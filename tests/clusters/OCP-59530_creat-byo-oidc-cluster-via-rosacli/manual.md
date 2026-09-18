# Test

## Step

Create account-roles

## Expect

The account-role should be created successfully

```bash
./rosa create account-roles
```
```
I: Logged in as 'ocmqe-akanni' on 'https://api.stage.openshift.com/'
I: Validating AWS credentials...
I: AWS credentials are valid!
I: Validating AWS quota...
I: AWS quota ok. If cluster installation fails, validate actual AWS resource usage against https://docs.openshift.com/rosa/rosa_getting_started/rosa-required-aws-service-quotas.html
I: Verifying whether OpenShift command-line tool is available...
I: Current OpenShift Client Version: 4.14.7
I: Creating account roles
? Role prefix: akanni
? Permissions boundary ARN (optional):
? Path (optional):
? Role creation mode: auto
? Create Classic account roles: Yes
? Create Hosted CP account roles: Yes
I: By default, the create account-roles command creates two sets of account roles, one for classic ROSA clusters, and one for Hosted Control Plane clusters.
In order to create a single set, please set one of the following flags: --classic or --hosted-cp
I: Creating classic account roles using 'arn:aws:iam::301721915996:user/akanni'
I: Created role 'akanni-Installer-Role' with ARN 'arn:aws:iam::301721915996:role/akanni-Installer-Role'
I: Created role 'akanni-ControlPlane-Role' with ARN 'arn:aws:iam::301721915996:role/akanni-ControlPlane-Role'
I: Created role 'akanni-Worker-Role' with ARN 'arn:aws:iam::301721915996:role/akanni-Worker-Role'
I: Created role 'akanni-Support-Role' with ARN 'arn:aws:iam::301721915996:role/akanni-Support-Role'
I: Creating hosted CP account roles using 'arn:aws:iam::301721915996:user/akanni'
I: Created role 'akanni-HCP-ROSA-Installer-Role' with ARN 'arn:aws:iam::301721915996:role/akanni-HCP-ROSA-Installer-Role'
I: Created role 'akanni-HCP-ROSA-Support-Role' with ARN 'arn:aws:iam::301721915996:role/akanni-HCP-ROSA-Support-Role'
I: Created role 'akanni-HCP-ROSA-Worker-Role' with ARN 'arn:aws:iam::301721915996:role/akanni-HCP-ROSA-Worker-Role'
```

## Step

Prepare the byo oidc config via `rosa create oidc-config --mode auto` command

## Expect

There should be bellow message to guide user to create operator roles with the oidc-config-id:
```
I: Setting up managed OIDC configuration
I: To create Operator Roles for this OIDC Configuration, run the following command and remember to replace <user-defined> with a prefix of your choice:
rosa create operator-roles --prefix <user-defined> --oidc-config-id 23h5cjr4sc4ob7tqe6n8i4oiur9fg6i3
```

## Step

~~Create STS cluster by setting 'oidc-private-key-secret-arn' and 'oidc-endpoint-url' with the available value NOTE: it needs to cover both manual mode and auto mode~~

## Expect

The cluster will be created with the byo oidc.

## Step

Create STS cluster by setting '--oidc-config-id' --mode auto
NOTE:
- this step should cover to use managed and unmanaged oidc config
- this step should cover to use the pre-created operator roles too

## Expect

- The cluster will be created with the byo oidc config
- There is no oidc provider created, will use the one of the oidc config
- If the operator role prefix is used with the exsting operator roles, there is no new operator roles created
- the oidc proider in the cluster spec should use the one of the oidc config
- In the interactive mode, there is a list to select the oidc config id at 'OIDC Configuration ID', all the oidc config of the same org will be listed.
- In the interactive mode for the non-hypershift sts cluster, there is option '? Deploy cluster using pre registered OIDC Configuration ID'. And if choose yes, '? OIDC Configuration ID' is prompted; If choose no, no '? OIDC Configuration ID' option to use the classic flow
- There should be bellow message to hint that creating operator-roles/oidc-provider is not required if reusing the resources.
```
I: When using reusable OIDC Config and resources have been created prior to cluster specification, this step is not required.
- SDA-9001 : if the cluster creation using un-managed oidc config, the cluster spec will add byo_oidc:{enable: true}, it will fail with error if not.A regression test is needed.
```

## Step

Create another STS cluster with the same setting and different account-roles with the ones in step2

## Expect

The cluster will be created.

## Step

Validation testing.
- Use the oidc-config-id which issue url is not in the existing operator roles
~~- Use the existing operator roles but without setting oidc-config-id(covered by 45742)~~
- Create hosted-cp without setting oidc-config-id neither classic-oidc-config（it will promte to ask for the oidc config）

## Expect

- E: Operator role 'arn:aws:iam::301721915996:role/yw0329shareopr12-openshift-cluster-csi-drivers-ebs-cloud-credent' does not have trusted relationship to 'd3gt1gce2zmg3d.cloudfront.net' issuer URL
~~- E: A role named 'yw0330shareopr1-openshift-cloud-network-config-controller-cloud-' already exists. Please delete the existing role, or provide a different prefix. If you'd like to reuse the operator roles, please provide a OIDC Configuration ID which has Issuer URL linked as the trusted relationship of the chosen operator roles prefix.~~
\-
```
E: Hosted Control Plane requires an OIDC Configuration ID
Please run `rosa create oidc-config -h` and create one.
```

## Step

~~Create third STS cluster with the same setting but in not the same region with the secret~~

## Expect

~~The cluster will be created.~~

## Step

Delete the cluster then delete the operator-roles and oidc-provider

## Expect

- The cluster will be deleted
- The operator roles will be deleted
- The oidc provider will be deleted (TBD:SDA-7992)

## Step

Repeat step1~5 with the commands of `rosa create cluster --mode manual` .

## Expect

- There should be not oidc provider aws command shown
- If the operator roles are existed already, there is no aws commands of creating operator roles shown
- other result should be same

## Step

~~Repeat step1~5 with the files to create the oidc config then use the config NOTE: this step will be covered in the OCP-57570 too.~~

## Expect

~~The result should be same~~

## Step

~~Repeat step 1~7 with the prefix setting for oidc config~~

## Expect

~~The result should be same~~

## Step

Repeat step 1~7 to create hypershift cluster
NOTE: It should contain the checkpoint both with the byo oidc created with hypershift installer role and non-hypershift account-role(as a regression test for SDA-8507)

## Expect

The result should be same

## Step

Test other flags of this command:
--color
--debug
--profile
-y

## Expect

They should work well
