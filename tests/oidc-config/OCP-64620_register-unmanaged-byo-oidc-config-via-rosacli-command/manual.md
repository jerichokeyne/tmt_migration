# Test

## Step
Create unmanaged oidc config in manaul mode

```bash
rosa create oidc-config --manged=false -i
```

## Expect

## Step
Register oidc config by rosacli command in auto mode

```bash
./rosa register oidc-config --issuer-url https://yw0620byooc2-oidc-x1n5.s3.us-east-2.amazonaws.com --installer-role-arn arn:aws:iam::301721915996:role/sdfg/dfg/yw0620accrt1-Installer-Role --secret-arn arn:aws:secretsmanager:us-east-2:301721915996:secret:rosa-private-key-yw0620byooc2-oidc-x1n5-yqxQj8 --mode auto -y
```

## Expect
- The oidc config should be registered successfully, check by `rosa list oidc-config`
- Check the info message as bellow. "OIDC provider already exists" if oidc provider is existed
- Check the 'Please try again' message when any error during the registration, it should contain the correct command for re-try

```
I: Using arn:aws:iam::301721915996:role/sdfg/dfg/yw0620accrt1-Installer-Role for the installer role
I: To create Operator Roles for this OIDC Configuration, run the following command and remember to replace <user-defined> with a prefix of your choice:
rosa create operator-roles --prefix <user-defined> --oidc-config-id 24fh5ac0u0voutpdr7g73gmetdq77847
If you are going to create a Hosted Control Plane cluster please include '--hosted-cp'
I: OIDC provider already exists.

E: There was a problem building your unmanaged OIDC Configuration: Cannot create Unmanaged OIDC Config with duplicated Issuer URL 'https://yw0620byooc2-oidc-n3y3.s3.us-east-2.amazonaws.com'. Please try again:
rosa register oidc-config --issuer-url https://yw0620byooc2-oidc-n3y3.s3.us-east-2.amazonaws.com --secret-arn arn:aws:secretsmanager:us-east-2:301721915996:secret:rosa-private-key-yw0620byooc2-oidc-n3y3-DoAgbj --installer-role-arn arn:aws:iam::301721915996:role/sdfg/dfg/yw0620accrt1-Installer-Role
```

- It will prompt the interactive mode if `--mode`/`--secret-arn`/`--issuer-url` is not set

## Step
Register oidc config by rosacli command in manual mode

## Expect
- There should be the command for creating oidc provider
- others are same as the one in step2

```
I: Run the following commands to create the OIDC provider:
aws iam create-open-id-connect-provider \
--client-id-list openshift sts.amazonaws.com \
--tags Key=red-hat-managed,Value=true \
--thumbprint-list 9e99a48a9960b14926bb7f3b02e22da2b0ab7280 \
--url https://yw0620byooc2-oidc-n3y3.s3.us-east-2.amazonaws.com
```

## Step
Validation for creating managed oidc config

- invalid installer arn --- use default
- invalid secret arn
- invalid url
- duplicated secret arn/issue url

## Expect
There should be readable error message
