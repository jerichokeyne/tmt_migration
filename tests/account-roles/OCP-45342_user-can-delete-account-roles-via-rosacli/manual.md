# Test

## Step
Log in with ROSA CLI and create account roles.

## Expect
STS is supported from version `1.0.6`.

## Step
Check `rosa delete` and `rosa delete account-roles` help.

```bash
rosa delete --help
rosa delete account-roles --help
```

## Expect
```
Cleans up account roles from the current AWS account.

Usage:
  rosa delete account-roles [flags]

Aliases:
  account-roles, accountroles, accountrole, account-role

Examples:
  # Delete Account roles"
  rosa delete account-roles -p prefix

Flags:
      --classic                          Delete classic account roles
      --delete-hcp-shared-vpc-policies   Deletes the Hosted Control Plane shared vpc policies
  -h, --help                             help for account-roles
      --hosted-cp                        Delete Hosted Control Planes roles
  -m, --mode string                      How to perform the operation. Valid options are:
                                         auto: Resource changes will be automatic applied using the current AWS account
                                         manual: Commands necessary to modify AWS resources will be output to be run manually
  -p, --prefix string                    Prefix of the account roles to be deleted.
  -y, --yes                              Automatically answer yes to confirm operation.
```

## Step
Check validation when deleting account roles:
- Delete without `-p`.
- Delete with an invalid mode.
- ~~Delete with an invalid role-name format.~~

## Expect
```
$ ./rosa delete account-role
E: Option account role prefix '-p' or role name '-r' is mandatory

$ rosa delete account-role --mode xxx
E: Invalid mode. Allowed values are [auto manual]
```

Defaulting to interactive mode counts as a pass.

## Step
Delete account roles without the mode flag.

## Expect
After confirming `yes`, all resources are deleted from AWS.

## Step
Delete account roles used by a cluster.

## Expect
```
E: Role aaraj-HCP-ROSA-Installer-Role is associated with the cluster aaraj-hcp
```

## Step
Delete account roles with `--mode manual`.

## Expect
AWS commands are prompted and delete all resources.

## Step
Delete account roles without `--mode`.

## Expect
`auto` and `manual` are prompted. Other results are the same as steps 5-6.

## Step
Try to delete account roles used by an STS cluster.

## Expect
They are deleted successfully.
