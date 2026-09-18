# Test

## Step
1. Ensure you're logged out of ROSA by running `rosa logout`.

## Expect
You've logged out of ROSA. Running `rosa whoami` returns `Failed to create OCM connection: Not logged in, run the 'rosa login' command`.

## Step
2. Get the version of the CLI by running `rosa version`.

## Expect
You should be able to see the correct version number.

```
1.2.38
I: Your ROSA CLI is up to date.
```

## Step
3. Get the version without checking if you're up to date by running `rosa version --client`.

## Expect
You should be able to see the correct version number.

```
1.2.38
```
