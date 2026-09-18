# Test

## Step
Create Hosted CP and classic account roles with the same prefix.

```bash
rosa create account-roles --prefix ywtest1 --mode auto -y --classic
rosa create account-roles --prefix ywtest1 --mode auto -y --hosted-cp
rosa create account-roles --prefix ywtest2 --mode auto -y --classic
rosa create account-roles --prefix ywtest2 --mode auto -y --hosted-cp
rosa create account-roles --prefix ywtest3 --mode auto -y --classic
rosa create account-roles --prefix ywtest4 --mode auto -y --hosted-cp
```

## Expect
All account roles are created.

## Step
Delete all account roles with the prefix in auto and manual modes.

```bash
rosa delete account-role --prefix ywtest1
```

## Expect
- In manual mode, prompted AWS commands delete all classic and HyperShift account roles.
- All classic and HyperShift account roles are deleted, with messages such as:

```
I: Deleting classic account roles
I: Deleting account role 'ywtest1-Installer-Role'
I: Deleting account role 'ywtest1-ControlPlane-Role'
I: Deleting account role 'ywtest1-Worker-Role'
I: Deleting account role 'ywtest1-Support-Role'
I: Successfully deleted the classic account roles
I: Deleting hosted CP account roles
I: Deleting account role 'ywtest1-HCP-Worker-Role'
I: Deleting account role 'ywtest1-HCP-Installer-Role'
I: Deleting account role 'ywtest1-HCP-Support-Role'
I: Successfully deleted the hosted CP account roles
```

## Step
Delete classic account roles in auto and manual modes.

```bash
rosa delete account-role --prefix ywtest2 --classic
```

## Expect
- In manual mode, prompted AWS commands delete all classic account roles.
- All classic account roles are deleted, with messages such as:

```
I: Deleting classic account roles
I: Deleting account role 'ywtest11-Support-Role'
I: Deleting account role 'ywtest11-Installer-Role'
I: Deleting account role 'ywtest11-ControlPlane-Role'
I: Deleting account role 'ywtest11-Worker-Role'
I: Successfully deleted the classic account roles
```

## Step
Delete HyperShift account roles in auto and manual modes.

```bash
rosa delete account-role --prefix ywtest2 --hosted-cp
```

## Expect
- In manual mode, prompted AWS commands delete all HyperShift account roles.
- All HyperShift account roles are deleted, with messages such as:

```
I: Deleting hosted CP account roles
I: Deleting account role 'ywtest11-HCP-Installer-Role'
I: Deleting account role 'ywtest11-HCP-Support-Role'
I: Deleting account role 'ywtest11-HCP-Worker-Role'
I: Successfully deleted the hosted CP account roles
```

## Step
Delete classic account roles with the `ywtest4` prefix.

## Expect
```
W: There are no hosted CP account roles to be deleted
```

## Step
Delete HyperShift account roles with the `ywtest3` prefix.

## Expect
```
W: There are no classic account roles to be deleted
```

## Step
Delete account roles without `--hosted-cp` or `--classic` using the `yuwantest3` prefix.

## Expect
- Only classic account roles are deleted.
- A message reports that no HyperShift account roles were deleted.

```
$ rosa delete account-roles --prefix ywtest2 --mode auto -y
I: Deleting classic account roles
I: Deleting account role 'ywtest2-Installer-Role'
I: Deleting account role 'ywtest2-ControlPlane-Role'
I: Deleting account role 'ywtest2-Worker-Role'
I: Deleting account role 'ywtest2-Support-Role'
I: Successfully deleted the classic account roles
W: There are no hosted CP account roles to be deleted
```

## Step
Delete account roles without `--hosted-cp` or `--classic` using the `yuwantest4` prefix.

## Expect
- Only HyperShift account roles are deleted.
- A message reports that no classic account roles were deleted.

```
W: There are no classic account roles to be deleted
I: Deleting hosted CP account roles
I: Deleting account role 'ywtest3-HCP-Installer-Role'
I: Deleting account role 'ywtest3-HCP-Support-Role'
I: Deleting account role 'ywtest3-HCP-Worker-Role'
I: Successfully deleted the hosted CP account roles
```
