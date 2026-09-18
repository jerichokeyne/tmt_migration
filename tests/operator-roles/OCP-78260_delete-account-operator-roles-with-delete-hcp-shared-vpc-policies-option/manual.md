# Test

## Step
Run:

```bash
```bash
rosa delete account-roles --help
```
```

## Expect
```
--delete-hcp-shared-vpc-policies   Deletes the Hosted Control Plane shared vpc policies
```

## Step
Run:

```bash
```bash
rosa delete operator-roles --help
```
```

## Expect
```
--delete-hcp-shared-vpc-policies   Deletes the Hosted Control Plane shared vpc policies
```

## Step
Delete account roles with `--delete-hcp-shared-vpc-policies=true`.

## Expect
Should **not** prompt `? Attempt to delete Hosted CP shared VPC policies? (y/N)`.

It should delete the policies:
```
time=2024-12-11T16:08:52-05:00 level=info msg=Deleting policy 'arn:aws:iam::301721915996:policy/jkeyne-1211-01-shared-route53-role-assume-role'
time=2024-12-11T16:08:52-05:00 level=info msg=Deleting policy 'arn:aws:iam::301721915996:policy/jkeyne-1211-01-shared-vpce-role-assume-role'
```

## Step
Delete account roles with `--delete-hcp-shared-vpc-policies=true` and `--mode=manual`.

## Expect
Should **not** prompt `? Attempt to delete Hosted CP shared VPC policies? (y/N)`.

Should contain these commands:
```bash
aws iam delete-policy \
  --policy-arn arn:aws:iam::301721915996:policy/jkeyne-1211-01-shared-route53-role-assume-role

aws iam delete-policy \
--policy-arn arn:aws:iam::301721915996:policy/jkeyne-1211-01-shared-vpce-role-assume-role
```

## Step
Delete account roles with `--delete-hcp-shared-vpc-policies=false`.

## Expect
Should **not** prompt `? Attempt to delete Hosted CP shared VPC policies? (y/N)`.

It should **not** delete the assume role policies

## Step
Delete account roles with `--delete-hcp-shared-vpc-policies=false` and `--mode=manual`.

## Expect
Should **not** prompt `? Attempt to delete Hosted CP shared VPC policies? (y/N)`.

Should **not** contain these commands:
```bash
aws iam delete-policy \
  --policy-arn arn:aws:iam::301721915996:policy/jkeyne-1211-01-shared-route53-role-assume-role

aws iam delete-policy \
--policy-arn arn:aws:iam::301721915996:policy/jkeyne-1211-01-shared-vpce-role-assume-role
```

## Step
Delete operator roles with `--delete-hcp-shared-vpc-policies=true`.

## Expect
Should **not** prompt `? Attempt to delete Hosted CP shared VPC policies? (y/N)`.

It should at least attempt to delete the policies:
```
time=2024-12-11T16:13:10-05:00 level=warning msg=Unable to delete policy arn:aws:iam::301721915996:policy/jkeyne-1211-01-shared-vpce-role-assume-role: Policy still attached to other resources
time=2024-12-11T16:13:10-05:00 level=warning msg=Unable to delete policy arn:aws:iam::301721915996:policy/jkeyne-1211-01-shared-route53-role-assume-role: Policy still attached to other resources
```

If not actually delete them:
```
time=2024-12-11T16:21:43-05:00 level=info msg=Deleting policy 'arn:aws:iam::301721915996:policy/jkeyne-1211-01-shared-vpce-role-assume-role'
time=2024-12-11T16:21:52-05:00 level=info msg=Deleting policy 'arn:aws:iam::301721915996:policy/jkeyne-1211-01-shared-route53-role-assume-role'
```

## Step
Delete operator roles with `--delete-hcp-shared-vpc-policies=true` and `--mode=manual`.

## Expect
Should **not** prompt `? Attempt to delete Hosted CP shared VPC policies? (y/N)`.

Should contain these commands:
```bash
aws iam delete-policy \
  --policy-arn arn:aws:iam::301721915996:policy/jkeyne-1211-01-shared-route53-role-assume-role

aws iam delete-policy \
--policy-arn arn:aws:iam::301721915996:policy/jkeyne-1211-01-shared-vpce-role-assume-role
```

## Step
Delete operator roles with `--delete-hcp-shared-vpc-policies=false`.

## Expect
Should **not** prompt `? Attempt to delete Hosted CP shared VPC policies? (y/N)`.

Should **not** attempt to delete the policies

## Step
Delete operator roles with `--delete-hcp-shared-vpc-policies=false` and `--mode=manual`.

## Expect
Should **not** prompt `? Attempt to delete Hosted CP shared VPC policies? (y/N)`.

Should **not** contain these commands:
```bash
aws iam delete-policy \
  --policy-arn arn:aws:iam::301721915996:policy/jkeyne-1211-01-shared-route53-role-assume-role

aws iam delete-policy \
--policy-arn arn:aws:iam::301721915996:policy/jkeyne-1211-01-shared-vpce-role-assume-role
```
