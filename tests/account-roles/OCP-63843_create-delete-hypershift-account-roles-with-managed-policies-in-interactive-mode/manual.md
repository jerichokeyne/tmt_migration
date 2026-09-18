# Test

## Step
Create account roles in interactive mode.

## Expect
- The Hosted CP option is prompted.
- Other options are shown as for classic STS account roles.

## Step
Repeat step 1 with a different channel group.

## Expect
The result should be the same.

## Step
Create multiple managed account roles.

## Expect
The result should be the same.

## Step
List the account roles and check the `AWS Managed` column.

## Expect
The output of `rosa list account-roles` includes `AWS Managed`. Account roles with managed policies show `Yes`; others show `No`.

## Step
Create a HyperShift cluster in manual mode.

## Expect
- AWS commands are prompted.
- Commands only create roles and attach managed policies; none create policies.
- Three account roles with the `-HCP-` infix are created with managed policies.

## Step
Delete the HyperShift account roles in manual mode.

```bash
rosa delete account-roles --prefix <prefix> --hosted-cp --mode manual
```

## Expect
- AWS commands detach the policies and delete the roles.
- No AWS commands delete the managed policies.

## Step
Try to delete account roles with `--hosted-cp` when the prefix is not for HyperShift account roles.

## Expect
```
E: There are no hosted CP account roles to be deleted
```
