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
Create HTPasswd IDP via ROSA CLI command.

```bash
rosa create idp --name cidph --type htpasswd -c 1quu0ukmeffe30h0dvslrkhf9g60hhek --username chtpidpwy1 --password chtpi#qs$1
```

## Expect
- The IDP with the user is created and the cluster console can be logged into with the username and password.
- Query the htpasswd idp by OCM API, the result should contain the added users

## Step
Try to create admin via `rosa create admin`

## Expect
- There should be one more item in the response of retrieving HTPasswd idp by OCM API
- There is a cluster-admin user in the cluster-admins group, it can be retrieved by OCM API
- The cluster console can be logged with the username and password created by `rosa create admin`

## Step
Try to create another HTPasswd idp.

## Expect
It should fail with the error message `E: Cluster '1quu0ukmeffe30h0dvslrkhf9g60hhek' already has an HTPasswd IDP`.

## Step
Delete the idp

## Expect
- The IDP with all users, including the `cluster-admin` user, is deleted.

## Step
Create admin firstly via `rosa create admin`

## Expect
- There should be one item in the response of retrieving HTPasswd idp by OCM API
- There is a cluster-admin user in the cluster-admins group, it can be retrieved by OCM API
- The cluster console can be logged into with the username and password created by `rosa create admin`.

## Step
Repeat step2 to create one HTPasswd idp via command

## Expect
- Query the idp by OCM API, the result should be shown correctly
- The cluster console can be logged into with the username and password.

```bash
rosa create idp -c 1quu94mia05n8s7c6p7gua18095ul82b --type htpasswd
```

## Step
Create an HTPasswd IDP with `--users`.

- Set one user.
- Set multiple users.

```bash
./rosa create idp -c 246trjsjleo601cvtd6u0jmsu4s2npjo --type htpasswd --name yuwanhpdidp2 --users 'test3:456FGHtgsd%$^gasd678hja3,test4:asd-HFJ3-4234-dsfnHFsdf'
./rosa create idp -c 246trjsjleo601cvtd6u0jmsu4s2npjo --type htpasswd --name yuwanhpdidp7 --users 'test33:asd-HFJ3-4234-dsfnHFsdf'
```

## Expect
- Query the idp by OCM API, the result should be shown correctly
- The cluster console can be logged with the username and password

## Step
Create an HTPasswd IDP with `--from-file`.

```bash
rosa create idp -c 24qlf9ne2kemjt1g2vnc73pd0ret0ntt --type htpasswd --from-file /Users/yuwan/workplace/rosa/yw0707htpasswdfile2
```

Note: The htpasswd file can be generated with the `htpasswd` command.

## Expect
- Query the idp by OCM API, the result should be shown correctly
- The cluster console can be logged with the username and password(decrypt password)

## Step
Then create admin

## Expect
- There should be one more item in the response of retrieving HTPasswd idp by OCM API
- There is a cluster-admin user in the cluster-admins group, it can be retrieved by OCM API
- The cluster console can be logged with the username and password created by `rosa create admin`

## Step
Delete idp then create admin then create idp with --user setting

## Expect
The result should be same

## Step
Check the validation for username and password:

- Username must not contain `/`, `:`, or `%`.
- Password must be at least 14 ASCII-standard characters without whitespace, include lowercase and uppercase letters, and include numbers or symbols (ASCII-standard characters only).
- Set two or three of `--users`, `--username`, `--password`, and `--from-file` at the same time.

## Expect
1. There should be validation for them.
2. It should fail with an error or warning message.

```
yuwan1-mac:rosa yuwan$ ./rosa create idp -c 24qlf9ne2kemjt1g2vnc73pd0ret0ntt --type htpasswd --users 'test33:asd-HFJ3-4234-dsfnHFsdf' --username and --password 'fghjFGHJ4567#$%^fghs'
E: Only one of 'users', 'from-file' or 'username/password' may be specified.
Choose the option 'users' to add one or more users to the IDP.
Choose the option 'from-file' to load users from a htpassword file
```

## Step
Repeat the steps on Windows/MacOS/Linux

## Expect
- The function should work well.
- The output should display well
