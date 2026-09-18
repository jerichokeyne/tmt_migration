# Test

## Step
Create account roles with the managed account-role policies in auto mode.

```bash
rosa create account-roles --managed-policies --mode auto
rosa create account-roles --mp --mode auto
```

## Expect
- The account roles are created on AWS and have the managed policies attached.
- The roles on AWS are tagged with `rosa_managed_policies=true`.
- ~~The installer role will have three policy files attached: `ROSAInstallerCorePolicy`, `ROSAInstallerVPCPolicy`, and `ROSAInstallerPrivateLinkPolicy` (SDA-7941).~~

## Step
Create account roles with the managed account-role policies in manual mode.

```bash
rosa create account-roles --managed-policies --mode manual
rosa create account-roles --mp --mode manual
```

## Expect
- The prompted AWS commands do not create policies; they create roles and attach the managed policies.
- The roles on AWS are tagged with `rosa_managed_policies=true`.
- After running the commands, the account roles are created on AWS and have the managed policies attached.
- ~~Three commands to attach `ROSAInstallerCorePolicy`, `ROSAInstallerVPCPolicy`, and `ROSAInstallerPrivateLinkPolicy` to installer roles are prompted (SDA-7941).~~

## Step
~~Repeat steps 1-2 with the old-version managed policies (a temporary check before managed policies can be created by CS/product).~~

## Expect
~~The result should be the same.~~

## Step
Repeat steps 1-2 with the path setting.

## Expect
The result should be the same.

## Step
Repeat steps 1-2 with a different account-role version.

## Expect
The result should be the same.

## Step
Repeat steps 1-2 with a different managed account-policy version.

## Expect
The result should be the same.

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
Delete the managed account roles in auto mode.

## Expect
- The account roles are detached and deleted.
- The managed policies are not deleted.

## Step
Delete the managed account roles in manual mode.

## Expect
- AWS commands detach the policies and delete the roles.
- No AWS commands delete the managed policies.
