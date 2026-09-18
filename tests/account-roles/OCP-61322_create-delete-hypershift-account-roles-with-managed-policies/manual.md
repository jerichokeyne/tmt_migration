# Test

## Step
Create account roles with `--hosted-cp` in auto mode.

Test with:
- Only `--hosted-cp` and `--prefix`.
- `--path`, `--permissions-boundary`, `--force-policy-creation`, and `--version`.

## Expect
- Three roles are created: `<prefix>-HCP-Installer-Role`, `<prefix>-HCP-Support-Role`, and `<prefix>-HCP-Worker-Role`.
- The three roles have managed policies attached.
- `--path`, `--permissions-boundary`, `--force-policy-creation`, and `--version` work.
- Role names use the format `<prefix>-HCP-ROSA-<role type>`.
- Role types are `Installer-Role`, `Support-Role`, and `Worker-Role`.

## Step
Create account roles with `--hosted-cp` in manual mode.

Test with:
- Only `--hosted-cp` and `--prefix`.
- `--path`, `--permissions-boundary`, and `--version`.

## Expect
- Prompted AWS commands create the three roles from step 1 and attach the related managed policies.
- The roles on AWS are tagged with `rosa_managed_policies=true`.
- After running the commands, the account roles are created on AWS and have the managed policies attached.
- `--path`, `--permissions-boundary`, `--force-policy-creation`, and `--version` work; commands contain their related parameters.
- The following warning is shown:

```
W: Setting `version` flag for hosted CP managed policies has no effect, any supported ROSA version can be installed with managed policies
```

## Step
Repeat steps 1-2 with a different channel group.

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
Delete the HyperShift account roles in auto mode.

```bash
rosa delete account-roles --prefix <prefix> --hosted-cp --mode auto
```

## Expect
- Account roles are detached and deleted.
- Managed policies are not deleted.
- The version warning above is shown.

## Step
Delete the HyperShift account roles in manual mode.

```bash
rosa delete account-roles --prefix <prefix> --hosted-cp --mode manual
```

## Expect
- AWS commands detach the policies and delete the roles.
- No AWS commands delete managed policies.

## Step
Try to delete account roles with `--hosted-cp` when the prefix is not for HyperShift account roles.

## Expect
```
E: There are no hosted CP account roles to be deleted
```
