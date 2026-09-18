# Test

## Step
Check help messages:

```bash
rosa -h
rosa attach -h
rosa attach policy -h
rosa detach -h
rosa detach policy -h
```

## Expect
```
Attach AWS resource

Usage:

Flags:
  -h, --help   help for attach

Global Flags:
      --color string   Surround certain characters with escape sequences to display them in color on the terminal. Allowed options are [auto never always] (default "auto")
      --debug          Enable debug mode.
```

```
Attach existing AWS IAM Policies to an AWS IAM Role in the authenticated AWS Account

Usage:
  rosa attach policy [flags]

Examples:
  # Attach policy <policy_arn_1> and <policy_arn_2> to role <role_name>
  rosa attach policy --role-name=<role_name> --policy-arns=<policy_arn_1>,<policy_arn_2>

Flags:
  -h, --help                 help for policy
  -m, --mode string          How to perform the operation. Valid options are:
                             auto: Resource changes will be automatic applied using the current AWS account
                             manual: Commands necessary to modify AWS resources will be output to be run manually
  -p, --policy-arns string   Policy arn of the policies to be attached to the specified role. Format should be a comma-separated list. (required).
  -r, --role-name string     Role name of the role to attach the specified policy (required).

Global Flags:
      --color string   Surround certain characters with escape sequences to display them in color on the terminal. Allowed options are [auto never always] (default "auto")
      --debug          Enable debug mode.
```

```
Detach AWS resource

Usage:

Flags:
  -h, --help   help for detach

Global Flags:
      --color string   Surround certain characters with escape sequences to display them in color on the terminal. Allowed options are [auto never always] (default "auto")
      --debug          Enable debug mode.
```

```
Detach AWS IAM Policies from an AWS IAM Role in the authenticated AWS Account

Usage:
  rosa detach policy [flags]

Examples:
  # Detach policy <policy_arn_1> and <policy_arn_2> from role <role_name>
  rosa detach policy --role-name=<role_name> --policy-arns=<policy_arn_1>,<policy_arn_2>

Flags:
  -h, --help                 help for policy
  -m, --mode string          How to perform the operation. Valid options are:
                             auto: Resource changes will be automatic applied using the current AWS account
                             manual: Commands necessary to modify AWS resources will be output to be run manually
  -p, --policy-arns string   Policy arn of the policies to be detached from the specified role. Format should be a comma-separated list. (required).
  -r, --role-name string     Role name of the role to detach the specified policy (required).

Global Flags:
      --color string   Surround certain characters with escape sequences to display them in color on the terminal. Allowed options are [auto never always] (default "auto")
      --debug          Enable debug mode.
```

## Step
Prepare 12 custom policies on AWS as a prerequisite.

## Expect

## Step
Attach a policy to an IAM role tagged with `red-hat-managed=true`:

- Use `--mode manual`.
- Do not set the `--mode` flag in the command.
- Use duplicate ARNs.

## Expect
Manual mode:
- The `I: Run the following command to attach the policy:` info message is shown.
- The AWS command to attach policies is shown.
- The policies can be attached with the prompted command.

When `--mode` is not set:
- Interactive mode prompts to choose a mode.
- ```
  ? Attach policy mode: auto
  ```
- After selecting the mode, the result is as above.

With duplicate ARNs, only one duplicate policy is attached.

## Step
Detach a policy from an IAM role tagged with `red-hat-managed=true`:

- Use `--mode manual`.
- Do not set the `--mode` flag in the command.
- Use duplicate ARNs.
- Use one existing policy that is not attached to the role.

## Expect
Manual mode:
- The `I: Run the following command to detach the policy:` info message is shown.
- The AWS command to detach policies is shown.
- The policies can be detached with the prompted command.

When `--mode` is not set:
- Interactive mode prompts to choose a mode.
- ```
  ? Detach policy mode: auto
  ```
- After selecting the mode, the result is as above.

With duplicate ARNs, only one duplicate policy is detached.

For an existing policy that is not attached to the role:

```
I: The policy 'arn:aws:iam::301721915996:policy/aa/cc/yuwan-testp9' is currently not attached to role 'yw0428accr1-Installer-Role'
```

## Step
Attach multiple policies to an IAM role tagged with `red-hat-managed=true`:

- Use `--mode manual`.
- Do not set the `--mode` flag in the command.

## Expect
Manual mode:
- The `I: Run the following command to attach the policy:` info message is shown.
- The AWS command to attach policies is shown.
- The policies can be attached with the prompted command.

When `--mode` is not set:
- Interactive mode prompts to choose a mode.
- ```
  ? Attach policy mode: auto
  ```
- After selecting the mode, the result is as above.

With duplicate ARNs, only one duplicate policy is attached.

## Step
Detach multiple policies from an IAM role tagged with `red-hat-managed=true`:

- Use `--mode manual`.
- Do not set the `--mode` flag in the command.
- Use duplicate ARNs.

## Expect
Manual mode:
- The `I: Run the following command to detach the policy:` info message is shown.
- The AWS command to detach policies is shown.
- The policies can be detached with the prompted command.

When `--mode` is not set:
- Interactive mode prompts to choose a mode.
- ```
  ? Detach policy mode: auto
  ```
- After selecting the mode, the result is as above.

With duplicate ARNs, only one duplicate policy is detached.

## Step
Validations for the attach command:

1. Policy ARN with invalid format.
2. Nonexistent policy ARN.
3. Nonexistent role name.
4. Multiple policy ARNs, some with invalid format or nonexistent.
5. The number of policies to attach exceeds the quota (`L-0DA4ABF3`).
6. The role has no `red-hat-managed=true` tag.
7. There is an empty string in `policy-arn`.

## Expect
1. ```
   E: Failed to find the policy 'aaaaa': operation error IAM: GetPolicy, https response error StatusCode: 400, RequestID: 83f82595-e3fa-465a-9d50-c7a6c444defe, api error ValidationError: 1 validation error detected: Value 'aaaaa' at 'policyArn' failed to satisfy constraint: Member must have length greater than or equal to 20
   ```
2. ```
   E: Failed to find the policy 'arn:aws:iam::301721915996:policy/yuwan-testp999': operation error IAM: GetPolicy, https response error StatusCode: 404, RequestID: cccd5e7c-ff3e-4999-88ee-549f3681ed71, NoSuchEntity: Policy arn:aws:iam::301721915996:policy/yuwan-testp999 was not found.
   ```
3. ```
   E: Failed to find the role 'yw0426accr999-Installer-Role': operation error IAM: GetRole, https response error StatusCode: 404, RequestID: 5bb239ba-cfdd-4d6b-b524-f3070f26ed46, NoSuchEntity: The role with name yw0426accr999-Installer-Role cannot be found.
   ```
4. It should fail with the above message, and the other policies should not be attached.
5. ```
   E: Failed to attach policies due to quota limitations (total limit: 10, expected: 11)
   ```
   The total limit and expected number should be correct.
6. ```
   E: Cannot attach/detach policies to non-ROSA roles
   ```
7. ```
   E: Invalid policy arn '', expected a valid policy arn matching ^arn:aws[\w-]*:iam::(\d{12}|aws):policy(?:\/+[\w+=,.@-]+)+$
   ```

## Step
Validations for the detach command:

1. Policy ARN with invalid format.
2. Nonexistent policy ARN.
3. Nonexistent role name.
4. Multiple policy ARNs, some with invalid format or nonexistent.
5. The role has no `red-hat-managed=true` tag.
6. There is an empty string in `policy-arn`.

## Expect
1. ```
   E: Invalid policy arn 'arnaa', expected a valid policy arn matching ^arn:aws[\w-]*:iam::(\d{12}|aws):policy(?:\/+[\w+=,.@-]+)+$
   ```
2. ```
   E: Failed to find the policy 'arn:aws:iam::301721915996:policy/aa/cc/yuwan-testp15': operation error IAM: GetPolicy, https response error StatusCode: 404, RequestID: 631b4655-4284-46dc-a835-aaf6b3f05982, NoSuchEntity: Policy arn:aws:iam::301721915996:policy/aa/cc/yuwan-testp15 was not found.
   ```
3. ```
   E: Failed to find the role 'yw0428accr22-Installer-Role': operation error IAM: GetRole, https response error StatusCode: 404, RequestID: 1016545e-dd51-41e8-b24d-92a4fce0b182, NoSuchEntity: The role with name yw0428accr22-Installer-Role cannot be found.
   ```
4. It should fail with the above message, and the other policies should not be attached.
5. ```
   E: Cannot attach/detach policies to non-ROSA roles
   ```
6. ```
   E: Invalid policy arn '', expected a valid policy arn matching ^arn:aws[\w-]*:iam::(\d{12}|aws):policy(?:\/+[\w+=,.@-]+)+$
   ```

## Step
Attach multiple policies to account roles and operator roles, then delete the roles.

## Expect
- Role deletion succeeds.
- Arbitrary policies are not deleted by the command in auto mode. In manual mode, no commands delete arbitrary policies.

## Step
Check the `--debug` flag of `rosa attach/detach policy ....`.

## Expect
The `--debug` flag works correctly.

## Step
Delete the installer role from AWS, then repeat describe cluster with `--get-role-policy-bindings`.

## Expect
```
E: Failed to get rolePolicyBinding: Failed to assume role with ARN 'arn:aws:iam::301721915996:role/aa/bb/yw0529accrv142-HCP-ROSA-Installer-Role': operation error STS: AssumeRole, https response error StatusCode: 403, RequestID: 9749829f-32af-413a-8024-ca43cf6f10b8, api error AccessDenied: User: arn:aws:sts::644306948063:assumed-role/RH-Managed-OpenShift-Installer/OCM is not authorized to perform: sts:AssumeRole on resource: arn:aws:iam::301721915996:role/aa/bb/yw0529accrv142-HCP-ROSA-Installer-Role
```
