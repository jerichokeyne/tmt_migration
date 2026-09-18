# Test

## Step

1. Check the help messages.

```bash
rosa create ocm-role -h
rosa create user-role -h
```

## Expect

The help output includes `--path`.

## Step

1. Create a user role in interactive mode, then choose manual mode when prompted.

## Expect

- An AWS command is prompted and includes `Key=red-hat-managed,Value=true` (SDA-6439).
- A ROSA CLI command to link the role is shown.
- The prompted AWS and ROSA CLI commands execute successfully.
- After the commands execute, the user role with the configured path is created successfully.
- The user role displays correctly in `rosa list user-role`.

## Step

1. Create another user role in interactive mode, then choose auto mode when prompted.

## Expect

- The user role with the configured path is created successfully.
- The user role displays correctly in `rosa list user-role`.

## Step

1. Unlink the user role created in step 2.

## Expect

It succeeds.

## Step

1. Delete the user role created in step 2.

## Expect

It succeeds.

## Step

1. Create an OCM role in interactive mode, then choose manual mode when prompted.

## Expect

- An AWS command is prompted and includes `Key=red-hat-managed,Value=true` (SDA-6439).
- A ROSA CLI command to link the role is shown.
- The prompted AWS and ROSA CLI commands execute successfully.
- After the commands execute, the OCM role with the configured path is created successfully.
- The OCM role displays correctly in `rosa list user-role`.

## Step

1. Create another OCM role in interactive mode, then choose auto mode when prompted.

## Expect

- The OCM role with the configured path is created successfully.
- The OCM role displays correctly in `rosa list user-role`.

## Step

1. Unlink the OCM role created in step 6.

## Expect

It succeeds.

## Step

1. Delete the OCM role created in step 6 by ARN.

## Expect

It succeeds.

## Step

1. Check `--path` validation in `rosa create ocm-role -i` and `rosa create user-role -i`.

## Expect

```
I: Creating User role
? Role prefix: a
? Permissions boundary ARN (optional):
X Sorry, your reply was invalid: invalid ARN Path. It must begin and end with / and contain only alphanumeric characters
? Role Path (optional): [? for help]
```
