# Test

## Step
Log in with the rosa cli

## Expect

## Step
Check the validation for the common parameter by the command.

1. Invalid type.
2. Invalid mapping method (this validation is removed for HTPasswd IDPs).
3. ~~Invalid CA file path.~~

## Expect
1. `E: Expected a valid IDP type. Options are [github gitlab google ldap openid]`
2. `E: Failed to add IDP to cluster '1iekajbm5j6ps8hh5ddjdpe64880c1q6': Only claim/add/generate/lookup is supported in the 'mapping_method' field`
3. `E: Failed to create IDP for cluster '1iekajbm5j6ps8hh5ddjdpe64880c1q6': Expected a valid certificate bundle: open ssss: no such file or directory`

## Step
Check the validation for GitHub IDP creation in command mode.

1. Invalid format of teams.

## Expect
1. `E: Failed to add IDP to cluster '1iekajbm5j6ps8hh5ddjdpe64880c1q6': 'team' 'jojo' in not in format <org/team>`
2. If not all required parameters are provided, interactive mode is called and parameters already provided in the command are treated as default values.

## Step
Check the validation for GitLab IDP creation in command mode.

1. Invalid type.
2. Invalid mapping method.
3. Invalid CA file path.

## Expect
1. Same as step 3.
2. If not all required parameters are provided, interactive mode is called and parameters already provided in the command are treated as default values.

## Step
Check the validation for Google IDP creation in command mode.

1. Invalid type.
2. Invalid mapping method.
3. ~~Invalid CA file path.~~

## Expect
1. Same as step 3.
2. If not all required parameters are provided, interactive mode is called and parameters already provided in the command are treated as default values.

## Step
Check the validation for LDAP IDP creation in command mode.

1. `bind_dn` and `bind_password` must be provided together. If they are not provided, they are empty by default.
2. LDAP URL with an incorrect format.
3. LDAP attributes use default values if they are not provided.
4. `ca` and `insecure` cannot be set at the same time.

## Expect
1. If not all required parameters are provided, interactive mode is called and parameters already provided in the command are treated as default values.
2. `E: Failed to create IDP for cluster '1iekajbm5j6ps8hh5ddjdpe64880c1q6': Expected LDAP URL to have an ldap:// or ldaps:// scheme`
3. `E: Failed to create IDP for cluster '1iekajbm5j6ps8hh5ddjdpe64880c1q6': Cannot use certificate bundle with an insecure connection`

## Step
Check the validation for OpenID IDP creation in command mode.

1. Invalid type.
2. Invalid mapping method.
3. Invalid CA file path.
4. The groups item includes `dedicated-admins`, `cluster-admins`, or both.
5. Add an IDP with the groups claim on a cluster with a version lower than `4.10.0`.

## Expect
Same as step 3.

- `E: Failed to add IDP to cluster 'yuwan-sts4': Claim groups name cannot be one of 'dedicated-admins','cluster-admins'`
- `E: Failed to add IDP to cluster '1si79jfoflh9vn0rp0dhbd5nsbdlpj71': Cannot set OpenID identity provider groups claim for cluster version older than '4.10.0'`

## Step
Repeat the steps on Windows/MacOS/Linux

## Expect
- The function should work well.
- The output should display well
