# Test

## Step
Log in with the ROSA CLI and check the help message for the HTPasswd IDP.

```bash
rosa create idp -h
```

## Expect
```
.......
-t, --type string Type of identity provider. Options are [github gitlab google htpasswd ldap openid].
....
--username string HTPasswd: Username to log into the cluster's console with.

--password string HTPasswd: Password for provided username, to log into the cluster's console with.
.......
```

## Step
Try to create another HTPasswd idp.

## Expect
The idp should be successfully created.

## Step
Delete the idp

## Expect
- The idp with all users including the cluster-admin user are deleted.

## Step
Check the validation for username and password:

- Username must not contain `/`, `:`, or `%`.
- Password must be at least 14 ASCII-standard characters without whitespace, include lowercase and uppercase letters, and include numbers or symbols (ASCII-standard characters only).

## Expect
There should be validation for them.(TBD)

## Step
Repeat the steps on Windows/MacOS/Linux

## Expect
- The function should work well.
- The output should display well
