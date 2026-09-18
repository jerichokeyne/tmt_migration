# Test

## Step
Log in the moactl and prepare one MOA cluster

## Expect

## Step
Try to create GitHub IDPs by the command.

Note: The command should contain all supported flags.

## Expect
- It is created successfully

## Step
Try to create Google IDPs by the command.

Note: The command should contain all supported flags.

## Expect
- It is created successfully

## Step
Try to create OpenID IDPs by the command.

Note: The command should contain all supported flags.

## Expect
- It is created successfully

## Step
Try to create LDAP IDPs by the command.

Note: The command should contain all supported flags.

## Expect
- It is created successfully

## Step
Try to create GitLab IDPs by the command.

Note: The command should contain all supported flags.

## Expect
- It is created successfully

## Step
List idps

## Expect
- The output should be correct.
- There is no `AUTH URL` value for the LDAP IDP item.

```
yuwan1-mac:rosa yuwan$ ./rosa list idp -c 255pr2qjcob6d59i2i8gbvsoj7dui3o9
NAME TYPE AUTH URL
ldap-1 LDAP
openid-1 OpenID https://oauth-openshift.apps.yuwan-jwfsts1.uvo1.s1.devshift.org/oauth2callback/openid-1
github-1 GitHub https://oauth-openshift.apps.yuwan-jwfsts1.uvo1.s1.devshift.org/oauth2callback/github-1
gitlab-1 GitLab https://oauth-openshift.apps.yuwan-jwfsts1.uvo1.s1.devshift.org/oauth2callback/gitlab-1
google-1 Google https://oauth-openshift.apps.yuwan-jwfsts1.uvo1.s1.devshift.org/oauth2callback/google-1
```

## Step
Delete the idps then list idps

## Expect
- All deletions are successful.
- All items are not in the output of `rosa list idps`
