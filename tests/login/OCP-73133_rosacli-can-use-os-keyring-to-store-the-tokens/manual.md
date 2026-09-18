# Setup
To make sure there is no OCM/rosa CLI local config, ideally run `rosa logout`.

Current supported keyrings on different OSes are as follows:

| OS | wincred | keychain | secret-service | pass |
| --- | --- | --- | --- | --- |
| Windows | Yes | No | No | No |
| macOS | No | Yes | No | Yes |
| Linux | No | No | Yes | Yes |

For keyring tools, refer to the official documentation for each tool. Here is a simple guide for QE testing: <https://docs.google.com/document/d/1_o1HmnbYkN25pziTlKgnW6S6wLRPsNsLLKTdlvEUy6g/edit>

# Test

## Step
1. macOS Keychain testing: export the `OCM_KEYRING=keychain` environment variable.

```bash
export OCM_KEYRING=keychain
```

## Expect

## Step
2. Run `rosa login` and `rosa login --token ******`.

```bash
rosa login
rosa login --token ******
```

## Expect
1. rosa CLI login succeeds.
2. A password item named `RedHatSSO` is generated and can be checked in the Keychain Access tool.
3. All rosa CLI commands work.

## Step
3. Check and set config.

```bash
rosa config get
rosa config set
```

## Expect
1. All config variables can be retrieved.
2. Setting config variables should work. Results can be checked with `rosa config get` after `rosa config set`.

## Step
4. Check the credential shared with ocmcli. Run `ocm whoami` without logging in.

```bash
ocm whoami
```

## Expect
- `ocm whoami` should show the correct result.

## Step
5. Run rosa CLI logout.

```bash
rosa logout
```

## Expect
- rosa CLI logs out.
- The password item named `RedHatSSO` is deleted.

## Step
6. Log in again, unset the `OCM_KEYRING` environment variable, then run a rosa CLI command such as `rosa whoami`.

```bash
unset OCM_KEYRING
rosa whoami
```

## Expect
```
E: Failed to create OCM connection: Not logged in, run the 'rosa login' command
```

## Step
7. Export `OCM_KEYRING=keychain`, then log in. Delete the password item named `RedHatSSO` in the Keychain Access tool, then run a rosa CLI command such as `rosa whoami`.

```bash
export OCM_KEYRING=keychain
rosa whoami
```

## Expect
```
E: Failed to create OCM connection: Not logged in, run the 'rosa login' command
```

## Step
8. Repeat step 1, then log in with invalid and expired tokens.

## Expect
- Readable messages are returned.

```
E: Failed to create OCM connection: error creating connection. Not able to get authentication token: access and refresh tokens are unavailable or expired, and there are no password or client secret to request new ones

E: Failed to parse token: token contains an invalid number of segments
```

## Step
9. macOS pass testing: export the `OCM_KEYRING=pass` environment variable.

```bash
export OCM_KEYRING=pass
```

## Expect

## Step
10. Repeat steps 2-7.

## Expect
- The results should be the same.

## Step
11. On Linux, test pass: export the `OCM_KEYRING=pass` environment variable. Repeat steps 2-7.

```bash
export OCM_KEYRING=pass
```

## Expect
- The results should be the same.

## Step
12. On Linux, test secret-service: export the `OCM_KEYRING=secret-service` environment variable. Repeat steps 2-7.

```bash
export OCM_KEYRING=secret-service
```

## Expect
- The results should be the same.
- The tokens can be checked by `secret-tool lookup profile RedHatSSO`.

## Step
13. On Windows, test wincred: add `OCM_KEYRING=wincred` to the environment variable. Repeat steps 2-6.

```powershell
$env:OCM_KEYRING = "wincred"
```

## Expect
- The results should be the same.
- The token can be checked by `cmdkey.exe /list` in PowerShell. The target of the item should be `LegacyGeneric:target=RedHatSSO:RedHatSSO:RedHatSSO`.

## Step
14. Check validation for an invalid keyring tool: export `OCM_KEYRING=invalidkeyring`, then run `rosa login`. On macOS, export `OCM_KEYRING=wincred`, then run `rosa login`.

```bash
export OCM_KEYRING=invalidkeyring
rosa login
export OCM_KEYRING=wincred
rosa login
```

## Expect
```
yuwan1-mac:1.2.37rc8rc1 yuwan$ ./rosa login
E: Error validating keyring: keyring is invalid, expected one of: [wincred, keychain, secret-service, pass]
yuwan1-mac:1.2.37rc8rc1 yuwan$ export OCM_KEYRING=wincred
yuwan1-mac:1.2.37rc8rc1 yuwan$ ./rosa login
E: Error validating keyring: keyring is valid but is not available on the current OS
```
