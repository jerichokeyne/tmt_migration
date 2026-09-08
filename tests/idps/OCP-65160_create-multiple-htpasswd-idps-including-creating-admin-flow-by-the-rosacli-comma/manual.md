# Test

## Step
Prepare one ready rosa classic cluster

## Expect

## Step
Test the scenario:  
create admin --> create htpasswd idp with --users (htpasswdidp1) --> create htpasswd idp with --from-file (htpasswdidp2)--> ~~create htpasswd idp in the interactive mode (htpasswdidp3)~~

## Expect
- All idps are created without error

## Step
List idps

## Expect
- All created idps are shown correctly in the outout

## Step
Delete the idps with the name cluster-admin-> htpasswdidp3 --> htpasswdidp1 --> htpasswdidp2

## Expect
- All idps are deleted.

## Step
Test the scenario:  
create htpasswd idp with --from-file (htpasswdidp1)-->~~create htpasswd idp in the interactive mode (htpasswdidp2)~~ --> create htpasswd idp with (htpasswdidp3) --> create admin

## Expect
- All idps are created without error

## Step
List idps

## Expect
- All created idps are shown correctly in the outout

## Step
Delete the idps with the name cluster-admin-> htpasswdidp3 --> htpasswdidp1 --> htpasswdidp2

## Expect
-- All idps are deleted.

## Step
Check the validations  
  
- Create multiple idp with duplicated name which is not named 'cluster-admin'  
- Create idp with duplicated name 'cluster-admin'  
- Create admin after one htpasswd idp created with the name 'cluster-admin'

## Expect
- E: Failed to add IDP to cluster '24tb37r7sjpigede7q0jjg0mm1t8ueft': Identity Provider Name customhtpidp1 already exists.  
- for item3, (TBD) Currently it returns E: Failed to add 'cluster-admin' identity provider to cluster '24tb37r7sjpigede7q0jjg0mm1t8ueft' as part of admin flow. Please try again: Identity Provider Name cluster-admin already exists. , but the expected result is to forbid the cluster-admin name idp OCM-2741

## Step
Repeat all steps on hosted-cp cluster

## Expect

## Step
Repeat the steps on Windows/MacOS/Linux

## Expect
- The function should work well  
- The output should display well
