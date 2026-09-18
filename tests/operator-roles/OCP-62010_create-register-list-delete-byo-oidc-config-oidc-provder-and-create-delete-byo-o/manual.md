# Test

## Step
Login via rosacli and check the help message of `rosa create oidc-config -h` and `rosa create -h` and `rosa delete oidc-config` and `rosa list oidc-config`

## Expect
The help message of them should be enough and clear.

## Step
Create managed oidc config in manual mode and interative mode
```bash
rosa create oidc-config --mode manual --managed -y
```
```bash
rosa create oidc-config --mode manual --managed -i
```

## Expect
- The oidc ocnfig registration on CS is removed, and the aws command to delete the oidc provider is prompted.
- Ask question about if create oidc-provider

## Step
Delete the managed oidc config in manual mode and interative mode
- rosa delete oidc-config -y
- rosa delete oidc-config -i

## Expect
- The oidc config is deleted, check the item is disappeared in `rosa list oidc-config`
- The oidc provider should be deleted too. and warning message if it is not existed on AWS
- In the interactive mode will ask for the mode and select the 'OIDC Configuration ID'
- If the deleting one is used by some cluster,E: There are clusters using OIDC config 'https://d3gt1gce2zmg3d.cloudfront.net/22pctrdhrs6n1jj84f38olocfbanrg49', can't delete the configuration
- There is some info message,I: Registered OIDC Config ID has been removed from OCM and can no longer be used. Remember to run given commands to clean up aws resources.

## Step
Create unmanaged oidc config in manual mode and interactive mode
```bash
rosa create oidc-config --mode manual --installer-role-arn <> --prefix <>
```
```bash
rosa create oidc-config -i
```

## Expect
Manual mode:
- the command to create the s3 and secret manager and remove the temp files will be shows
- there is message and document for register the config on OCM(CMS)
- The command for creating oidc-provider also shows

Interactive mode:
- All options for the oidc config creation will be prompted
- Ask if create oidc provider(TBD: needs t0 discuss if it should be removed )
- commands should be same with the manual mode above
- In the interactive mode, there is list to select installer role at '? Installer role ARN' option

## Step
Create managed and unmanaged oidc config when existing one which is not used.
NOTE: The toggle ValidateUnusedManagedOidcConfigs = "validate-unused-managed-oidc-configs" to control it

## Expect
It will fail with error when the toggle is enabled.
"Please use OIDC Configuration '%s' which is unused by your organization"

## Step
Register oidc config with manual mode and interactive mode
```bash
rosa register oidc-config -i
```
```bash
rosa register oidc-config --issuer-url https://yw0620byooc2-oidc-x1n5.s3.us-east-2.amazonaws.com --installer-role-arn arn:aws:iam::301721915996:role/sdfg/dfg/yw0620accrt1-Installer-Role --secret-arn arn:aws:secretsmanager:us-east-2:301721915996:secret:rosa-private-key-yw0620byooc2-oidc-x1n5-yqxQj8 --mode manual -y
```

## Expect
Manual mode:
- the command to create oidc-provider is propmted with INFO message
- The oidc config is registered successfully, check by `rosa list oidc-config`
- Interactive mode should be called out if --secret-arn or --issuer-url is missing
- If --installer-role-arn is not set, will use the first default one

Interactive mode:
- Ask questions to input fields
- the command to create oidc-provider is propmted with INFO message
- The oidc config is registered successfully, check by `rosa list oidc-config`

yuwan1-mac:rosa yuwan$ ./rosa register oidc-config -i
? OIDC Provider creation mode: manual
W: More than one Installer role found
? Installer role ARN: arn:aws:iam::301721915996:role/sdfg/dfg/yw0620accrt1-HCP-ROSA-Installer-Role
I: Using arn:aws:iam::301721915996:role/sdfg/dfg/yw0620accrt1-HCP-ROSA-Installer-Role for the installer role
? Issuer URL (please include 'https://'): https://yw0620byooc2-oidc-n3y3.s3.us-east-2.amazonaws.com
? Secret ARN: arn:aws:secretsmanager:us-east-2:301721915996:secret:rosa-private-key-yw0620byooc2-oidc-n3y3-DoAgbj
I: To create Operator Roles for this OIDC Configuration, run the following command and remember to replace <user-defined> with a prefix of your choice:
```bash
rosa create operator-roles --prefix <user-defined> --oidc-config-id 24fgtph7jfu287465f45bh0ldaebgq0s
```
If you are going to create a Hosted Control Plane cluster please include '--hosted-cp'
I: Run the following commands to create the OIDC provider:
aws iam create-open-id-connect-provider \
--client-id-list openshift sts.amazonaws.com \
--tags Key=red-hat-managed,Value=true \
--thumbprint-list 9e99a48a9960b14926bb7f3b02e22da2b0ab7280 \
--url https://yw0620byooc2-oidc-n3y3.s3.us-east-2.amazonaws.com
yuwan1-mac:rosa yuwan$

Validation:
- invalid values should print error and ask for re-try in the interactive mode

## Step
Delete the unmanaged oidc config in manual mode and interactive mode

## Expect
- The commands to delete the s3 and secret manager and oidc provider will be shown
- In the interactive mode, will ask for the mode
- In the interactive mode, there is a list to select the oidc config id at 'OIDC Configuration ID', all the oidc config of the same org will be listed.

## Step
Create the oidc provider in the interactive

## Expect
- 'OIDC Configuration ID' will be prompted to ask to select the oidc config
- The oidc-provide should be created with the url of the selected oidc config.
yuwan1-mac:rosa yuwan$ ./rosa create oidc-provider -i
? OIDC provider creation mode: auto
? OIDC Configuration ID: 23h5b8idjlalt9401jvvjn0n7jcduj5j | https://ywa5byooc1-oidc-j1n5.s3.us-east-2.amazonaws.com
I: Creating OIDC provider using 'arn:aws:iam::301721915996:user/yuwan'
? Create the OIDC provider? Yes
I: Created OIDC provider with ARN 'arn:aws:iam::301721915996:oidc-provider/ywa5byooc1-oidc-j1n5.s3.us-east-2.amazonaws.com'
yuwan1-mac:rosa yuwan$

## Step
Create the oidc provider in the manual mode with setting oidc-config-id

## Expect
- The command will prompted to create the oidc provider
- The url in the command should be the one of the selected/inputed oidc config

## Step
List oidc-providers.
```bash
rosa list oidc-providers
```

-Check the help message.
-Check with filter oidc-config-id .

## Expect
- All "OIDC PROVIDER ARN","Cluster ID,"In Use" should be correct
- There will be no "Cluster ID" value if the oidc provider is BYO
yuwan1-mac:rosa yuwan$ ./rosa list oidc-providers
I: Fetching OIDC providers
OIDC PROVIDER ARN Cluster ID In Use
arn:aws:iam::301721915996:oidc-provider/d3gt1gce2zmg3d.cloudfront.net/23ius386mboolgsoluoqjpo3djohskdo No
arn:aws:iam::301721915996:oidc-provider/d3gt1gce2zmg3d.cloudfront.net/2465bk9dfnsugpni9ha7tu5ler1rrv96 2465cm0dmrrhi280c2a74l92rrs5fvi3 No
arn:aws:iam::301721915996:oidc-provider/d3gt1gce2zmg3d.cloudfront.net/246u8c0emqh7885t3drgmnd1h0lcjn0p 246u8c0emqh7885t3drgmnd1h0lcjn0p Yes
arn:aws:iam::301721915996:oidc-provider/d3gt1gce2zmg3d.cloudfront.net/246vj95pthr9pqrvkclnk0vuka61nb1a No
arn:aws:iam::301721915996:oidc-provider/rh-oidc.s3.us-east-1.amazonaws.com/246d5a6e4vner21fq8lc3ca660ostio1 246d5a6e4vner21fq8lc3ca660ostio1 No
arn:aws:iam::301721915996:oidc-provider/yw0607byooc1-oidc-y4m2.s3.us-east-2.amazonaws.com Yes
-It should contain the support flag infor
```bash
./rosa list oidc-providers -h
```
-It should only show the oidc-config matching provider
```bash
./rosa list oidc-providers --oidc-config-id <>
```
If there is no oidc provider for the config, it should return message : No OIDC providers available
If oidc config is not valid, it should return readable message: OIDC Configuration '29l5utp6mgt6i626n5jeq4go5d9b1f29' not found

## Step
Delete oidc-provider by oidc-config id

## Expect
- If one cluster created with the different aws account-role with the current aws account is using the oidc provider, it should allow to delete it. (
- Create two clusters with one same managed oidc-config but these two clusters including oidc-providers created with two aws accounts logged in rosacli
- Delete cluster then delete the oidc-provider with rosacli login with one aws account
- It should succeed to delete the oidc-provider
)
- If there is some cluster using the oidc provder and the aws account-roles using for creating the cluster is same with the current one, it should fail with error like "E: There are clusters using OIDC config 'https://d3gt1gce2zmg3d.cloudfront.net/24a66rofr6p4br8lgbh7ac4m8vmmgg6u', can't delete the provider"
- For scenarios not above two, the provider should be deleted.

## Step
Create cluster with BYO oidc-config and the prior-to-cluster operator-roles in manual mode

## Expect
- In manual mode: the commands to created the operator-roles and policies will be prompted, and the roles and polices will be created with the commands.

## Step
Delete cluster with BYO oidc-config and the prior-to-cluster operator-roles in manual mode

## Expect
- In manual mode: the commands to delete the operator-roles and policies will be prompted, and the roles and polices will be deleted with the commands.
