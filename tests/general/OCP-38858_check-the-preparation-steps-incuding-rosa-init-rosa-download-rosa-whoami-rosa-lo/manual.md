# Test

## Step
Prepare the ROSA tool and check the `rosa init -h` help message.

## Expect
```
Applies templates to support Red Hat OpenShift Service on AWS. If you are not
yet logged in to OCM, it will prompt you for credentials.

Usage:
  rosa init [flags]

Examples:
  # Configure your AWS account to allow IAM (non-STS) ROSA clusters
  rosa init

  # Configure a new AWS account using pre-existing OCM credentials
  rosa init --token=$OFFLINE_ACCESS_TOKEN

Flags:
      --delete                 Deletes stack template applied to your AWS account during the 'init' command.
      --disable-scp-checks     Indicates if cloud permission checks are disabled when attempting installation of the cluster.
      --client-id string       OpenID client identifier. The default value is 'cloud-services'.
      --client-secret string   OpenID client secret.
      --govcloud               Uses the FedRAMP High OpenShift Cluster Manager API for creating clusters in AWS GovCloud regions
      --insecure               Enables insecure communication with the server. This disables verification of TLS certificates and host names.
      --region string          Use a specific AWS region, overriding the AWS_REGION environment variable.
      --scope strings          OpenID scope. If this option is used it will completely replace the default scopes. Can be repeated multiple times to specify multiple scopes. (default [openid])
  -t, --token string           Access or refresh token generated from https://console.redhat.com/openshift/token/rosa.
      --token-url string       OpenID token URL. The default value is 'https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token'.
      --use-auth-code          Login using OAuth Authorization Code. This should be used for most cases where a browser is available. See --use-device-code for remote hosts and containers.
      --use-device-code        Login using OAuth Device Code. This should only be used for remote hosts and containers where browsers are not available. See --use-auth-code for all other scenarios.
      --profile string         Use a specific AWS profile from your credential file.
  -y, --yes                    Automatically answer yes to confirm operation.
  -h, --help                   help for init

Global Flags:
      --color string   Surround certain characters with escape sequences to display them in color on the terminal. Allowed options are [auto never always] (default "auto")
      --debug          Enable debug mode.
```

## Step
Run `rosa init`.

## Expect
```
I: Logged in as 'sdqe-regular02' on 'https://api.stage.openshift.com'
I: Validating AWS credentials...
I: AWS credentials are valid!
I: Validating SCP policies...
I: AWS SCP policies ok
I: Validating AWS quota...
I: AWS quota ok
I: Ensuring cluster administrator user 'osdCcsAdmin'...
I: Admin user 'osdCcsAdmin' already exists!
I: Validating SCP policies for 'osdCcsAdmin'...
I: AWS SCP policies ok
I: Validating cluster creation...
I: Cluster creation valid
I: Verifying whether OpenShift command-line tool is available...
W: OpenShift command-line tool is not installed.
```

- The init procedure adds the region tag on the `osdCcsAdmin` user. It uses the default AWS configuration region if `--region` is not specified.
- ![](screenshot-20210520-123954.png)
- If there is no CloudFormation stack, a new one is created in the region specified with `--region` or configuration.
- If init encounters an error, it prompts an error message.
- Init with a region different from the IAM user tag should succeed.
- Init with `--profile` should work well. The init process uses the configuration and credentials of the profile value.

## Step
Run `rosa version`.

## Expect
The version should be shown correctly.

## Step
Run `rosa init --delete-stack`.

## Expect
- The stack will be deleted successfully.
- If `--region` is used and matches the user tag, it deletes the stack in that region.
- If `--region` is used but does not match the user tag, it deletes the stack for the user tag.
- If `--region` is not used, it deletes the stack in the default `us-east-1` region.

## Step
Run `rosa init --disable-scp-checks`.

## Expect
```
I: Logged in as 'sdqe-regular01' on 'https://api.stage.openshift.com'
I: Validating AWS credentials...
I: AWS credentials are valid!
I: Skipping AWS SCP policies check
I: Validating AWS quota...
I: AWS quota ok
I: Ensuring cluster administrator user 'osdCcsAdmin'...
I: Admin user 'osdCcsAdmin' already exists!
I: Validating SCP policies for 'osdCcsAdmin'...
I: AWS SCP policies ok
I: Validating cluster creation...
I: Cluster creation valid
I: Verifying whether OpenShift command-line tool is available...
I: Current OpenShift Client Version: version.Info{Major:"4", Minor:"1+",
```

## Step
Init with the `--dry-run` flag.

## Expect
It should be created successfully. There is no quota occupied.

```bash
rosa create cluster --cluster-name dyr-test --dry-run
```

```
I: Creating cluster 'dyr-test' should succeed. Run without the '--dry-run' flag to create the cluster.
```

## Step
Download the OCM tool with ROSA.

```bash
rosa download openshift-client
```

## Expect
The `openshift-client` should be downloaded.

## Step
Check user information with `rosa whoami`.

## Expect
When users are not logged in:

```
$ ./rosa whoami
E: User is not logged in to OCM
```

After logging in:

```
$ ./rosa whoami
AWS Account ID: 301721915996
AWS Default Region: us-east-2
AWS ARN: arn:aws:iam::301721915996:user/yuwan
OCM API: https://api.stage.openshift.com
OCM Account ID: 1Pg91NjVkaKuxDvnp9iXQa8MlC3
OCM Account Name: sdqe-regular01 Green
OCM Account Username: sdqe-regular01
OCM Account Email: yasun+regular01@redhat.com
OCM Organization ID: 1OAqHo0k19kyq7Xt7I1Zqb8Ok4K
OCM Organization Name: Red Hat-Service Delivery-tester
OCM Organization External ID: 12553207
```

## Step
Check `rosa login`.

## Expect
There is an event recorded in Pendo.

![](screenshot-20220110-022032.png)

The help message should be shown as follows:

```
Log in to your Red Hat account, saving the credentials to the configuration file or OS Keyring.
The supported mechanism is by using a token, which can be obtained at: https://console.redhat.com/openshift/token/rosa

The application looks for the token in the following order, stopping when it finds it:
	1. OS Keyring via Environment variable (OCM_KEYRING)
	2. Command-line flags
	3. Environment variable (ROSA_TOKEN)
	4. Environment variable (OCM_TOKEN)
	5. Configuration file
	6. Command-line prompt

Usage:
  rosa login [flags]

Examples:
  # Login to the OpenShift API with an existing token generated from https://console.redhat.com/openshift/token/rosa
  rosa login --token=$OFFLINE_ACCESS_TOKEN

Flags:
      --client-id string       OpenID client identifier. The default value is 'cloud-services'.
      --client-secret string   OpenID client secret.
      --govcloud               Uses the FedRAMP High OpenShift Cluster Manager API for creating clusters in AWS GovCloud regions
  -h, --help                   help for login
      --insecure               Enables insecure communication with the server. This disables verification of TLS certificates and host names.
      --region string          Use a specific AWS region, overriding the AWS_REGION environment variable.
      --scope strings          OpenID scope. If this option is used it will completely replace the default scopes. Can be repeated multiple times to specify multiple scopes. (default [openid])
  -t, --token string           Access or refresh token generated from https://console.redhat.com/openshift/token/rosa.
      --token-url string       OpenID token URL. The default value is 'https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token'.
      --use-auth-code          Login using OAuth Authorization Code. This should be used for most cases where a browser is available. See --use-device-code for remote hosts and containers.
      --use-device-code        Login using OAuth Device Code. This should only be used for remote hosts and containers where browsers are not available. See --use-auth-code for all other scenarios.

Global Flags:
      --color string   Surround certain characters with escape sequences to display them in color on the terminal. Allowed options are [auto never always] (default "auto")
      --debug          Enable debug mode.
```

Log in with the ROSA CLI using the following token sources:

1. Environment variable `ROSA_TOKEN`.
2. Environment variable `OCM_TOKEN`.
3. Command-line flags.
4. Configuration file.
5. Command-line prompt.

It should be successful to log in:

```
I: Logged in as 'sdqe-regular01' on 'https://api.stage.openshift.com'
```

The token should be stored in the `ocm.json` file at:

- Linux: `~/.config/ocm/ocm.json`
- Windows: `%APPDATA%/ocm/ocm.json`
- macOS: `~/Library/Application Support/ocm/ocm.json`

Note: The `--use-auth-code` flag is supported after 1.2.33 (not included). After using this flag, do not enter a token; a browser tab opens to log in with Red Hat SSO. The browser shows `Login successful! Please close this window and return back to CLI` after succeeding.

```
$ ./rosa login --use-auth-code --env=staging
You will now be redirected to Red Hat SSO login
Token received successfully
I: Logged in as 'tzhou5' on 'https://api.stage.openshift.com'
```

## Step
Check `rosa login --use-device-code`.

## Expect
This is a hidden flag not shown in the `--help` message, supported from OCM-5815. After using this flag, follow the response instructions: access <https://sso.redhat.com/device> and enter the code in a browser.

```
./rosa login --use-device-code
I: To login, navigate to https://sso.redhat.com/device on another device and enter code DCKY-MMCO
I: Checking status every 5 seconds...
I: Logged in as 'sdqe-rosa' on 'https://api.openshift.com'
I: To switch accounts, logout from https://sso.redhat.com and run `rosa logout` before attempting to login again
```

After a valid code is entered, the browser shows success. Close the browser; login then succeeds in the terminal.

If the code is not entered on the auth page for a long time, ROSA CLI returns the error `E: An error occurred while polling for token exchange: error exchanging for token: context deadline exceeded`.

- After login without error, execute commands to make sure it works well: `rosa whoami` and `rosa list cluster`.

## Step
Log out.

## Expect
```bash
rosa logout
```

There is no error. All other commands should fail with `E: User is not logged in to OCM`.

## Step
Repeat steps 1-2 with the following flags:

1. `--region`
2. `--token-url --client-id --client-secret --insecure --scope`
3. `--token`

## Expect
1. The region information overwrites the configuration value.
2. It should work well as in step 2.
3. It should overwrite the token input during login.
4. After login without error, execute commands to make sure it works well: `rosa whoami` and `rosa list cluster`.
