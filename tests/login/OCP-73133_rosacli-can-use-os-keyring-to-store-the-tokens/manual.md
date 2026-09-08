# Setup
To make sure there is no ocm/rosacli local config existed, ideally, `rosa logout` can ensure that.  
  
  
Current supported kering on different OS are as bellow  | wincred | keychain | secret-service | pass  
---|---|---|---|---  
Windows | ✔️ | ❌ | ❌ | ❌  
macOS | ❌ | ✔️ | ❌ | ✔️  
Linux | ❌ | ❌ | ✔️ | ✔️  
  
  
How to keyring tools , please refer to the officail documents of each tool, and Here is a simple guide for QE testing. <https://docs.google.com/document/d/1_o1HmnbYkN25pziTlKgnW6S6wLRPsNsLLKTdlvEUy6g/edit>

# Test

## Step
MacOS keychain testing: Export OCM_KEYRING=keychain env vairable

## Expect

## Step
Run `rosa login` and `rosa login --token ******`

## Expect
1. rosacli login succeed  
2. One password item named "RedHatSSO" is generated, can check in the 'Keychain Access' tool  
3. all commands of rosacli can works.

## Step
Check and set config  
`rosa config get`  
`rosa config set`

## Expect
1. All the config variables can be retrieved  
2. Set config variables should work. Results can be checked by `rosa config get` after `rosa config set`

## Step
Check the credential shared with ocmcli,  
Run `ocm whoami` without logging

## Expect
- `ocm whoami` should show the correct result

## Step
rosacli logout

## Expect
- rosacli loggout  
- The password item named "RedHatSSO" is deleted

## Step
Login again then Unset the OCM_KEYRING env vaiable, then run rosacli command, like `rosa whoami`

## Expect
E: Failed to create OCM connection: Not logged in, run the 'rosa login' command

## Step
Export OCM_KEYRING=keychain env vairable then login. Delete the password item named "RedHatSSO" in 'Keychain Access' tool, then run rosacli command, like `rosa whoami`

## Expect
E: Failed to create OCM connection: Not logged in, run the 'rosa login' command

## Step
Repeat step1, then login with invalid and expired tokens

## Expect
There are readable message returned.  
  
E: Failed to create OCM connection: error creating connection. Not able to get authentication token: access and refresh tokens are unavailable or expired, and there are no password or client secret to request new ones  
  
E: Failed to parse token: token contains an invalid number of segments

## Step
MacOS pass testing: Export OCM_KEYRING=pass env vairable

## Expect

## Step
Repeat step 2~7

## Expect
The results should be same

## Step
On Linux, pass testing: Export OCM_KEYRING=pass env vairable  
Repeat step 2~7

## Expect
The results should be same

## Step
On Linux, secret-service testing: Export OCM_KEYRING=secret-service env vairable  
Repeat step 2~7

## Expect
The results should be same.  
The tokens can be checked by `secret-tool lookup profile RedHatSSO`

## Step
On Windows, wincred testing, add OCM_KEYRING=wincred in the env variable,Repeat step 2~6

## Expect
The results should be same.  
The token will be checked by `cmdkey.exe /list` in PowerShell, the target of the item should be "LegacyGeneric:target=RedHatSSO:RedHatSSO:RedHatSSO"

## Step
Check the validation for invalid keyring tool,  
export OCM_KEYRING=invalidkeyring then `rosa login`.  
MacOS: export OCM_KEYRING=wincred then `rosa login`.

## Expect
yuwan1-mac:1.2.37rc8rc1 yuwan$ ./rosa login  
E: Error validating keyring: keyring is invalid, expected one of: [wincred, keychain, secret-service, pass]  
yuwan1-mac:1.2.37rc8rc1 yuwan$ export OCM_KEYRING=wincred  
yuwan1-mac:1.2.37rc8rc1 yuwan$ ./rosa login  
E: Error validating keyring: keyring is valid but is not available on the current OS
