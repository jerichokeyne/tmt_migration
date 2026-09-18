# Test

## Step
Log in to `moactl`.

## Expect

## Step
Prepare the AWS configuration and credentials with AWS profiles.

## Expect

## Step
Run `rosa init`, delete the `osdCcsAdmin` user, then run `rosa init` again.

## Expect
It should fail while validating SCP policies for `osdCcsAdmin` with the following error message:

```
E: Failed to verify permissions for user 'osdCcsAdmin': iamClient.GetUser: osdCcsAdmin
To reset the 'NoSuchEntity: The user with name osdCcsAdmin cannot be found.
status code: 404, request id: aaffbba4-ef0b-4f1c-9a73-35264fc5b7ec' account, run 'rosa init --delete-stack' and try again
```

## Step
Cause a `getClientDetails` error during `rosa init`.

## Expect
It should fail with the following error message:

```
E:getClientDetails: %v\n"+"Run 'rosa init' and try again
```

## Step
Run `rosa init`, delete the `osdCcsAdmin` user, then try to create a cluster.

## Expect
It should fail with the following error message:

```
E:Failed to get access keys for user <aws.AdminUserName>: <err>\n"
```

## Step
Ensure no AWS credential is configured, then run `rosa init`.

## Expect
```bash
rosa init
```

```
E: Error creating AWS client: Failed to find credentials. Check your AWS configuration and try again
```

## Step
Try to run init with the following conditions:

1. No `oc` client.
2. No AWS client.
3. No credential.
4. No configuration.
5. Invalid credential.
6. Invalid configuration.
7. `oc` client version is too low.

## Expect
There should be an error message to provide a hint.
