# Test

## Step
Create Hosted CP account roles with `--vpc-endpoint-role-arn` and `--route53-role-arn` in manual mode.

```bash
rosa create account-roles --prefix yw1126svpc1 --path /aa/bb/ --route53-role-arn arn:aws:iam::641733028092:role/yuwan-sharevpc-role --vpc-endpoint-role-arn arn:aws:iam::641733028092:role/yuwan-sharevpc-vpc-endpoint-role --mode manual -y
```

## Expect
- AWS commands are prompted, including two additional commands that create assume-role policies with `sts:AssumeRole` permission for the Route 53 and VPC endpoint roles.
- Commands attach the two assume-role policies to `HCP-ROSA-Installer-Role`.
- Commands that create the policies include `red-hat-managed=true`.
- After running the AWS commands:
- Eight operator roles are created.
- `HCP-ROSA-Installer-Role` has one managed policy and two assume-role policies attached.
- The two assume-role policies have tags `hcp-shared-vpc=true` and `red-hat-managed=true`.

## Step
If the two assume-role policies already exist, repeat step 1.

## Expect
- No commands create the assume-role policies.
- Other results are the same as in step 1.

## Step
Check the path setting:
- The role ARN has a path.
- `vpc-endpoint-role-arn` and `route53-role-arn` have path settings.

## Expect
- Assume-role-policy paths match the `vpc-endpoint-role-arn` and `route53-role-arn` path settings.
- The `role-arn` path does not affect assume-role-policy paths.

## Step
Create another set of account roles with the same settings except for the prefix.

## Expect
- No commands create assume-role policies if they already exist.
- It succeeds as above.

## Step
Delete the shared-VPC HCP account roles in manual mode.

## Expect
- Prompted commands delete all created roles successfully.
- All policies attached to classic account roles are deleted.
- Two commands delete the assume-role policies.
- After running the AWS commands, all classic account roles and policies and all HCP account roles are deleted successfully.

## Step
Check `--delete-hcp-shared-vpc-policies`:
- Without the flag in manual mode.
- With the flag in manual mode.
- With `--delete-hcp-shared-vpc-policies=false` in manual mode.

## Expect
- `rosa delete account -h` includes `--delete-hcp-shared-vpc-policies Deletes the Hosted Control Plane shared vpc policies`.
- Without the flag, no commands delete assume-role policies.
- With the flag, commands delete assume-role policies.
- With `--delete-hcp-shared-vpc-policies=false`, no commands delete assume-role policies.

## Step
Validate:
- `--vpc-endpoint-role-arn` without `--route53-role-arn` or `--hosted-cp`.
- `--route53-role-arn` without `--vpc-endpoint-role-arn`, with `--hosted-cp`.

## Expect
```
E: Setting the `vpc-endpoint-role-arn` flag is only supported for hosted clusters
E: Invalid configuration: Must supply 'route53-role-arn' flag when using the 'vpc-endpoint-role-arn' flag
```

## Step
As regression testing, repeat step 1, attach arbitrary policies to account roles, then delete operator roles in manual mode.

## Expect
It succeeds.
