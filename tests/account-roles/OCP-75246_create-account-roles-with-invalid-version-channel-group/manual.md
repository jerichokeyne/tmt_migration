# Test

## Step
Log in with `rosa login`.

It is recommended to use the SDQE ROSA account because personal accounts might not have channel groups enabled.

## Expect
```
$ rosa login
To login to your Red Hat account, get an offline access token at https://console.redhat.com/openshift/token/rosa
I: Logged in as 'sdqe-rosa' on 'https://api.openshift.com'
```

## Step
Check validation for the version flag when creating account roles:
- Invalid version `4.20`.
- Invalid channel group `fakecg`.
- Invalid version format `4.11.1` (only `x.y` is supported).

## Expect
The commands fail with errors such as:

```
E: Error getting version: a valid version number must be specified
Valid versions: [4.8, 4.7, 4.11, 4.10, 4.9]

E: Error getting version: could not find versions for the provided channel-group: 'fakecg'

E: Error getting version: A valid policy version number must be specified
Valid versions: [4.10, 4.11, 4.12, 4.13, 4.14]
```
