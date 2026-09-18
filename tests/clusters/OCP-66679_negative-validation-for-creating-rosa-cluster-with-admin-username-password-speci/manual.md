# Setup
[https://issues.redhat.com/browse/OCM-158 Hypershift is not supported. Requires oc and rosa cli tools.](<https://issues.redhat.com/browse/OCM-158    Hypershift is not supported. Requires oc and rosa cli tools.>)

# Test

## Step

~~Try creating classic non-STS cluster in interactive mod with username that does not meet requirements. rosa create cluster -i`enter a cluster name answer no to Hosted Control Plane answer yes to create cluster admin user entering "?" at username prompt displays what characters are not allowed in usernames. Try entering usernames with invalid characters.` Once you have confirmed it will not accept an invalid username press ctrl-c to terminate the rosa cli.~~

## Expect

`[m@fedora 17:21:04 /tmp]$ rosa create cluster -i`
```
I: Interactive mode enabled.
Any optional fields can be left empty and a default will be selected.
**?** **Cluster name:** mycluster
**?** **Deploy cluster with Hosted Control Plane (optional):** No
**?** **Create cluster admin user:** Yes
X Sorry, your reply was invalid: invalid username 'my/user': username must not contain /, :, or %
? Username of Cluster Admin.
Username must not contain /, :, or %%
```

Pressing ? at username prompt displays requirements for username field, entering any invalid username displays the prompt again.

## Step

~~Try creating STS cluster in interactive mode with username that does not meet requirements. rosa create cluster --sts -i `enter a cluster name answer no to Hosted Control Plane answer yes to create cluster admin user entering "?" at username prompt displays what characters are not allowed in usernames. Try entering usernames with invalid characters.` Once you have confirmed it will not accept an invalid username press ctrl-c to terminate the rosa cli.~~

## Expect

`[m@fedora 17:21:04 /tmp]$ rosa create cluster -i`
```
I: Interactive mode enabled.
Any optional fields can be left empty and a default will be selected.
**?** **Cluster name:** mycluster
**?** **Deploy cluster with Hosted Control Plane (optional):** No
**?** **Create cluster admin user:** Yes
X Sorry, your reply was invalid: invalid username 'my/user': username must not contain /, :, or %
? Username of Cluster Admin.
Username must not contain /, :, or %%
```

Pressing ? at username prompt displays requirements for username field, entering any invalid username displays the prompt again.

## Step

Try creating classic non-STS cluster in interactive mode with a password that does not meet requirements
```bash
rosa create cluster -i
```

answer N to hosted control plane
answer y to create cluster admin user
press ? at the password prompt (should display password requirements)
enter an invalid password (password rejected, prompt displayed again)
press ctrl-c to terminate rosa-cli process.

## Expect

`[m@fedora 15:25:48 /tmp]$ rosa create cluster -i`
```
I: Interactive mode enabled.
Any optional fields can be left empty and a default will be selected.
**?** **Cluster name:** mgcluster
**?** **Deploy cluster with Hosted Control Plane (optional):** No
**?** **Create cluster admin user:** Yes
~~**?~~ Username:** user
? Password of Cluster Admin.
The password must
- Be at least 14 characters (ASCII-standard) without whitespaces
- Include uppercase letters, lowercase letters, and numbers or symbols (ASCII-standard characters only)
```

```
? Password of Cluster Admin.
X Sorry, your reply was invalid: password must be at least 14 characters (ASCII-standard) without whitespaces
**?** **Password:** [? for help]
```

## Step

Try creating classic STS cluster in interactive mode with a password that does not meet requirements
```bash
rosa create cluster --sts -i
```

answer N to hosted control plane
answer y to create cluster admin user
~~enter a valid username~~
press ? at the password prompt (should display password requirements)
enter an invalid password (password rejected, prompt displayed again)
press ctrl-c to terminate rosa-cli process.

## Expect

`[m@fedora 15:25:48 /tmp]$ rosa create cluster -i`
```
I: Interactive mode enabled.
Any optional fields can be left empty and a default will be selected.
**?** **Cluster name:** mgcluster
**?** **Deploy cluster with Hosted Control Plane (optional):** No
**?** **Create cluster admin user:** Yes
~~**?~~ Username:** user
? Password of Cluster Admin.
The password must
- Be at least 14 characters (ASCII-standard) without whitespaces
- Include uppercase letters, lowercase letters, and numbers or symbols (ASCII-standard characters only)
```

```
? Password of Cluster Admin.
X Sorry, your reply was invalid: password must be at least 14 characters (ASCII-standard) without whitespaces
**?** **Password:** [? for help]
```

## Step

Try to create Hypershift cluster with valid username/password in interactive mode.
```bash
rosa create cluster -i
```

answer yes to Hosted Control Plane
~~Confirm the next prompt does not ask for admin user creation~~ prompt will be shown for creating admin user, select yes
for prompt "Create custom password for cluster admin" select yes
press ? at the password prompt (should display password requirements)
enter an invalid password (password rejected, prompt displayed again)
press ctrl-c to terminate the rosa cli.


admin user creation for HCP cluster is supported by this PR <https://github.com/openshift/rosa/pull/1863>

## Expect

```bash
./rosa create cluster -i
```
```
I: Interactive mode enabled.
Any optional fields can be left empty and a default will be selected.
? Cluster name: akanni-66679
? Domain prefix (optional):
? Deploy cluster with Hosted Control Plane: Yes
? Create cluster admin user: Yes
? Create custom password for cluster admin: Yes
? The password must
X Sorry, your reply was invalid: Password must be at least 14 characters (got 3)
? Password: [? for help]
E: Failed to create IDP for cluster '': Expected a valid password: interrupt
```

# Cleanup
none, no clusters should be created.
