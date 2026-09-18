# Test

## Step
Create account roles in interactive mode.

```bash
rosa create account-roles -i
```

## Expect
```
? Create Hosted CP account roles: Yes
? Use account roles for Hosted CP shared VPC?: Yes
? Set VPC endpoint role ARN (optional): arn:aws:iam::641733028092:role/yuwan-sharevpc-vpc-endpoint-role
? Set route53 role ARN (optional): arn:aws:iam::641733028092:role/yuwan-sharevpc-role
```

- When `Create Hosted CP account roles` is `Yes`, the three questions above are prompted; otherwise they are not.
- When `Use account roles for Hosted CP shared VPC` is `Yes`, the VPC endpoint and Route 53 role ARN questions are prompted and required.
- With auto mode, entered role ARNs create account roles; the Hosted CP installer role attaches one managed policy and two assume-role policies as in command mode.
- With manual mode, AWS commands create account roles, create and attach the two assume-role policies to the Hosted CP installer role, as in command mode.
- The two assume-role policies are tagged `hcp-shared-vpc=true` and `red-hat-managed=true`.

## Step
Create shared-VPC account roles with a command that omits required flags such as `--prefix` or `--mode`.

## Expect
- Interactive mode is prompted and follows the flow from step 1.
- Values set by flags are prefilled as defaults in questions.

## Step
Validate:
- `vpc-endpoint-role-arn` without `route53-role-arn`.
- Empty VPC endpoint and Route 53 role ARNs, passed with double quotation marks or the Enter key.
- Invalid ARN format.

## Expect
```
X Sorry, your reply was invalid: Value is required
X Sorry, your reply was invalid: Value is required
X Sorry, your reply was invalid: Invalid ARN: arn: invalid prefix
```

## Step
Check help for the three questions.

## Expect
```
? Whether or not to set route53/VPC endpoint role ARNs to be used for Hosted CP shared VPC (cross-account VPC)
? Role ARN associated with the shared VPC used for Hosted Control Plane clusters, this role contains policies to be used with the VPC endpoint
? Role ARN associated with the private hosted zone used for Hosted Control Plane cluster shared VPC, this role contains policies to be used with Route 53
```

## Step
Delete account roles without a mode flag to test interactive mode.

## Expect
- Interactive mode prompts for mode.
- In manual mode, it asks `Attempt to delete Hosted CP shared VPC policies`.
- In auto mode, choosing `N` does not attempt to delete the two shared-VPC assume-role policies; choosing `Y` tries to delete them.
- When no resource attaches the policies, they are deleted with messages such as:

```
time=2024-12-03T16:37:37+08:00 level=info msg=Deleting policy 'arn:aws:iam::301721915996:policy/yuwan-sharevpc-vpc-endpoint-role2-assume-role'
...
time=2024-12-03T16:38:00+08:00 level=info msg=Deleting policy 'arn:aws:iam::301721915996:policy/yuwan-sharevpc-role2-assume-role'
```

- If another resource attaches the policies, they are not deleted, and each policy gets one warning:

```
I: Deleting account role 'yw1203svpc1-HCP-ROSA-Installer-Role'
time=2024-12-03T17:14:01+08:00 level=warning msg=Unable to delete policy yuwan-sharevpc-role-assume-role: Policy still attached to 1 other resource(s)
time=2024-12-03T17:14:01+08:00 level=warning msg=Unable to delete policy yuwan-sharevpc-vpc-endpoint-role-assume-role: Policy still attached to 1 other resource(s)
```

- In manual mode, choosing `Y` at `Create commands to delete Hosted CP shared VPC policies?` includes commands for shared-VPC account roles and assume-role policies; choosing `N` excludes the assume-role-policy commands.

## Step
Check `--delete-hcp-shared-vpc-policies` and `? Attempt to delete Hosted CP shared VPC policies?` through interactive mode.

```bash
rosa delete account-roles --prefix <prefix> --delete-hcp-shared-vpc-policies
```

Test manual and auto modes with the flag, without the flag, and with `--delete-hcp-shared-vpc-policies=false`.

## Expect
- In manual mode, the flag produces assume-role-policy deletion commands; omitting it or setting it to `false` does not.
- In auto mode, the flag does not ask the question and tries to delete assume-role policies.

```
$ rosa delete account-roles --prefix yw1211svpc1 --delete-hcp-shared-vpc-policies
? Account role deletion mode: auto
W: There are no classic account roles to be deleted
I: Deleting hosted CP account roles
? Delete the account role 'yw1211svpc1-HCP-ROSA-Worker-Role'? Yes
I: Deleting account role 'yw1211svpc1-HCP-ROSA-Worker-Role'
? Delete the account role 'yw1211svpc1-HCP-ROSA-Installer-Role'? Yes
I: Deleting account role 'yw1211svpc1-HCP-ROSA-Installer-Role'
time=2024-12-12T11:27:38+08:00 level=info msg=Deleting policy 'arn:aws:iam::301721915996:policy/a/b/yuwan-sharevpc-role2-assume-role'
time=2024-12-12T11:27:38+08:00 level=info msg=Deleting policy 'arn:aws:iam::301721915996:policy/a/b/yuwan-sharevpc-vpc-endpoint-role2-assume-role'
? Delete the account role 'yw1211svpc1-HCP-ROSA-Support-Role'? Yes
I: Deleting account role 'yw1211svpc1-HCP-ROSA-Support-Role'
I: Successfully deleted the hosted CP account roles
```

- Without the flag, auto mode asks the question; `Y` attempts deletion and `N` does not.
- With `--delete-hcp-shared-vpc-policies=false`, auto mode neither asks the question nor deletes assume-role policies.
