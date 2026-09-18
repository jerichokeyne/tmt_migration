# Test

## Step
Check `rosa create account-roles` help.

## Expect
```
      --route53-role-arn string        Role ARN associated with the private hosted zone used for Hosted Control Plane cluster shared VPC, this role contains policies to be used with Route 53
      --vpc-endpoint-role-arn string   Role ARN associated with the shared VPC used for Hosted Control Plane clusters, this role contains policies to be used with the VPC endpoint
```

## Step
Create Hosted CP account roles with `--vpc-endpoint-role-arn` and `--route53-role-arn`.

```bash
rosa create account-roles --prefix yw1120svpc1 --path /aa/bb/ --permissions-boundary arn:aws:iam::301721915996:policy/aa/bb/yw1120accr2-Installer-Role-Policy --route53-role-arn arn:aws:iam::641733028092:role/yuwan-sharevpc-role --vpc-endpoint-role-arn arn:aws:iam::641733028092:role/yuwan-sharevpc-vpc-endpoint-role --hosted-cp --mode auto -y
```

## Expect
- Three account roles are created.
- The installer role has three policies: one managed HCP installer policy and two assume-role policies created by ROSA CLI.
- The assume-role policies are named `<shared_vpc_role_name>-assume-role` and tagged `hcp-shared-vpc=true` and `red-hat-managed=true`.
- Info messages report role creation and policy attachment.

## Step
Create a second set of HCP shared-VPC roles with the same settings and a new prefix.

## Expect
The result should be the same.

## Step
Delete the first roles from step 2, then the second roles from step 3, in auto mode.

## Expect
1. All roles are deleted. The two created assume-role policies are not deleted and warnings are reported:

```
I: Deleting account role 'yw1128svpc2-HCP-ROSA-Installer-Role'
time=2024-11-28T10:15:59+08:00 level=warning msg=Unable to delete policy yuwan-sharevpc-role-assume-role: Policy still attached to 1 other resource(s)
time=2024-11-28T10:15:59+08:00 level=warning msg=Unable to delete policy yuwan-sharevpc-vpc-endpoint-role-assume-role: Policy still attached to 1 other resource(s)
```

2. All roles and policies, including the two assume-role policies, are deleted from AWS.

## Step
TBD: Create with the two role-ARN flags without `--hosted-cp` or `--classic`.

## Expect
All roles are created; the Hosted CP roles are as above.

## Step
Validate:
- Invalid ARNs for the two flags.
- Creating classic roles with the two flags.
- Creating with only one of the two flags.

## Expect
```
E: Setting the `route53-role-arn` flag is only supported for hosted clusters
E: Setting the `vpc-endpoint-role-arn` flag is only supported for hosted clusters
E: Must supply 'vpc-endpoint-role-arn' flag when using the 'route53-role-arn' flag
E: Must supply 'route53-role-arn' flag when using the 'vpc-endpoint-role-arn' flag
```

## Step
Create multiple times with the same shared-VPC ARNs.

## Expect
It succeeds.

## Step
Check `--delete-hcp-shared-vpc-policies` in auto mode:
- Without the flag.
- With the flag.
- With `--delete-hcp-shared-vpc-policies=false`.

## Expect
- With and without the flag as documented, ROSA CLI tries to delete assume-role policies; if no other resource is attached, they are deleted.

```
time=2024-12-11T16:08:52-05:00 level=info msg=Deleting policy 'arn:aws:iam::301721915996:policy/jkeyne-1211-01-shared-route53-role-assume-role'
time=2024-12-11T16:08:52-05:00 level=info msg=Deleting policy 'arn:aws:iam::301721915996:policy/jkeyne-1211-01-shared-vpce-role-assume-role'
```

- With `--delete-hcp-shared-vpc-policies=false`, ROSA CLI does not try to delete the assume-role policies and they remain.
