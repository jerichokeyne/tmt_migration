# Setup
Example commands:

```bash
rosa delete iamserviceaccount -c 2l3pia7089sh3g9411bad5a21uu1jghm --role-name jkeyne-0904-30-default-my-app-iamsa2-role --mode auto -y
rosa create iamserviceaccount -c 2l3pivkhljpenrod2lm1hcmp19vhq3ke --name iamsaname --namespace iamsanamespace --attach-policy-arn arn:aws:iam::090777400063:policy/yuwan-test-policy,arn:aws:iam::090777400063:policy/yuwan-test-policy2 --inline-policy file:///Users/yuwan/workplace/rosa_release/rosa-ocm-18278/custom-policy.json --path /aa/cc/ --permissions-boundary arn:aws:iam::090777400063:policy/yuwan-test-permissions-boundary --mode auto
```

# Test

## Step
Prepare one BYOC-OIDC STS/hosted-cp cluster

## Expect

## Step
Create iamserviceaccount in manual mode
- With one attaching policoe.
- With multiple attaching policoes.
- With `--inline-policy` and `--attach-policy-arn` at the same time.
- With a custom role name.
- With a role path.
- With a permissions boundary.

NOTE: this is not supported to create in manual mode now.

## Expect

## Step
Delete iamserviceaccount in manual mode
- Delete the iamserviceaccount with the custom name by specified role name.
- Delete the iamserviceaccount with the auto-generated name by specified by role name and name+namespace.

## Expect
- There will be aws commands to detach policy and delete the role shown.

```
...
I: Run the following AWS CLI commands to delete the IAM role manually:
I:
I: # Detach managed policies
aws iam detach-role-policy --role-name jkeyne-0904-31-iamsanamespace-iamsaname-role --policy-arn arn:aws:iam::090777400063:policy/yuwan-test-policy

# Delete inline policies
aws iam delete-role-policy --role-name jkeyne-0904-31-iamsanamespace-iamsaname-role --policy-name jkeyne-0904-31-iamsanamespace-iamsaname-role-inline-policy

# Delete the role
aws iam delete-role --role-name jkeyne-0904-31-iamsanamespace-iamsaname-role
...
```

- It should succeed to execute the promoted aws commands.

## Step
Prepare one CLASSIC-OIDC STS cluster then repeat above steps

## Expect
The result should be same.
