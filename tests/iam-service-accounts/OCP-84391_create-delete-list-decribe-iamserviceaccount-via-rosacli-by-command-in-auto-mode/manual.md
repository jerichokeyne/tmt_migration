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
Create iamserviceaccount with `--attach-policy-arn`
- With one attaching policoe.
- With multiple attaching policoes.

## Expect
- It should succeed.
- The IAM role are created.
- The output includes the INFO message of "Attached trust policy to role...", "Created IAM role...", and "Attached policy..." like below:

```
rosa create iamserviceaccount -c 2l3pivkhljpenrod2lm1hcmp19vhq3ke --name test-iamsa1 --namespace testns --attach-policy-arn arn:aws:iam::090777400063:policy/yuwan-test-policy,arn:aws:iam::090777400063:policy/yuwan-test-policy2 --path /aa/cc/ --permissions-boundary arn:aws:iam::090777400063:policy/yuwan-test-permissions-boundary --mode manual
I: Attached trust policy to role 'jkeyne-0904-31-testns-test-iamsa1-role(https://console.aws.amazon.com/iam/home?#/roles/jkeyne-0904-31-testns-test-iamsa1-role)': {
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Federated": "arn:aws:iam::090777400063:oidc-provider/oidc.os1.devshift.org/2l3pibu1rbb82fobrvgo0fgup0okmqhn"
      },
      "Action": "sts:AssumeRoleWithWebIdentity",
      "Condition": {
        "StringEquals": {
          "oidc.os1.devshift.org/2l3pibu1rbb82fobrvgo0fgup0okmqhn:sub": "system:serviceaccount:testns:test-iamsa1"
        }
      }
    }
  ]
}
I: Created IAM role 'jkeyne-0904-31-testns-test-iamsa1-role' with ARN 'arn:aws:iam::090777400063:role/aa/cc/jkeyne-0904-31-testns-test-iamsa1-role' using OIDC 'arn:aws:iam::090777400063:oidc-provider/oidc.os1.devshift.org/2l3pibu1rbb82fobrvgo0fgup0okmqhn'
I: Attached policy 'arn:aws:iam::090777400063:policy/yuwan-test-policy' to role 'jkeyne-0904-31-testns-test-iamsa1-role(https://console.aws.amazon.com/iam/home?#/roles/jkeyne-0904-31-testns-test-iamsa1-role)'
I: Attached policy 'arn:aws:iam::090777400063:policy/yuwan-test-policy2' to role 'jkeyne-0904-31-testns-test-iamsa1-role(https://console.aws.amazon.com/iam/home?#/roles/jkeyne-0904-31-testns-test-iamsa1-role)'
```

## Step
Create iamserviceaccount with `--inline-policy` and `--attach-policy-arn` at the same time

## Expect
The result should be same with the step2~3.

## Step
Create iamserviceaccount with `--inline-policy`

## Expect

## Step
Create iamserviceaccount with/without `--role-name`

## Expect
- It should be succeed if specify the role-name.
- If no role-name specified, one auto-generated role name will be used and it should be with the format `<cluster_name>-<name-space>-<iam-service-account-name>-role`.

## Step
Create iamserviceaccount with `--path` and `--permissions-boundary` setting

## Expect
- It should be succeed to create the role with the path and permissions boundary.

## Step
Check the flag of `--name` and `--namespace` work well

## Expect
- The flags values can be passed to the role successfully, can be checked by `rosa list iamserviceaccount` command.
- They will be used for the role's trust relationship.
- If namespace is not specified, the default value `default` will be used.

## Step
Check the role is created correctly

## Expect
- The trust relationship should be added and the `Principal.Federated` is the oidc provider and `Condition` is the `system:serviceaccount:<name-space>:<service-account-name>`.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Federated": "arn:aws:iam::090777400063:oidc-provider/oidc.os1.devshift.org/2l3pibu1rbb82fobrvgo0fgup0okmqhn"
      },
      "Action": "sts:AssumeRoleWithWebIdentity",
      "Condition": {
        "StringEquals": {
          "oidc.os1.devshift.org/2l3pibu1rbb82fobrvgo0fgup0okmqhn:sub": "system:serviceaccount:iamsanamespace:iamsaname"
        }
      }
    }
  ]
}
```

- The role should be with bellow tags:

```
rosa.openshift.io/cluster:<cluster-name>
rosa.openshift.io/namespace:<namespace>
rosa.openshift.io/service-account:<service-account-name>
rosa_role_type:ServiceAccountRole
red-hat-managed:true
```

## Step
Check the validations of `rosa create iamserviceaccount`
- Without setting `--name`.
- Without setting `-c`.
- Without `--attach-policy-arn` or `--inline-policy`.
- Existing name.
- There is OIDC provider on the cluster.

## Expect
```
E: at least one service account name is required
Failed to execute root command: required flag(s) "cluster" not set
E: at least one policy ARN or inline policy must be specified
E: failed to create role: Role with same name but different path exists. Existing role ARN: arn:aws:iam::090777400063:role/jkeyne-0904-31-default-iamsaname-role
E: failed to get OIDC provider ARN: no OIDC provider found for cluster with ID '2koueoefaseah289bb7csu59fuu0pjmu'
```

## Step
List iamserviceaccount

## Expect
- Bellow fields should be shown with correct value:

```
rosa list iamserviceaccount -c 2l3pia7089sh3g9411bad5a21uu1jghm
NAME                                      ARN                                                                                     CLUSTER           NAMESPACE  SERVICE ACCOUNT  CREATED
jkeyne-0904-30-default-my-app-iamsa1-role arn:aws:iam::090777400063:role/jkeyne-0904-30-default-my-app-iamsa1-role              jkeyne-0904-30    default    my-app-iamsa1    2025-09-05 05:41:01
jkeyne-0904-30-default-my-app-iamsa2-role arn:aws:iam::090777400063:role/jkeyne-0904-30-default-my-app-iamsa2-role              jkeyne-0904-30    default    my-app-iamsa2    2025-09-04 20:33:33
jkeyne-0904-30-default-my-app-iamsa3-role arn:aws:iam::090777400063:role/jkeyne-0904-30-default-my-app-iamsa3-role              jkeyne-0904-30    default    my-app-iamsa3    2025-09-04 20:40:31
```

- If there is no service account role existed, `I: No IAM service account roles found`.

## Step
Describe the iamserviceaccount role by role name

## Expect
- Below information of the role should be displayed.

```
rosa describe iamserviceaccount -c 2l6hqoak4pi6udqsibr9er6ocq5nmkbu --role-name yuwan0909t1-2nyiirm1onmsd0mqq6xind-iamsanamespace-iamsaname-role
Name: yuwan0909t1-2nyiirm1onmsd0mqq6xind-iamsanamespace-iamsaname-role
ARN: arn:aws:iam::090777400063:role/aa/cc/yuwan0909t1-2nyiirm1onmsd0mqq6xind-iamsanamespace-iamsaname-role
Cluster: yuwan0909t1-2nyiirm1onmsd0mqq6xindpz7eu8k3q1xxiffnzxah
Namespace: iamsanamespace
Service Account: iamsaname
Created: 2025-09-09 08:32:46 UTC
Path: /aa/cc/
Permissions Boundary: arn:aws:iam::090777400063:policy/yuwan-test-permissions-boundary
Max Session Duration: 3600 seconds
OIDC Provider: yuwan0909t1-2ny-oidc-h5d3.s3.us-east-2.amazonaws.com

Attached Policies:
- yuwan-test-policy (arn:aws:iam::090777400063:policy/yuwan-test-policy)
- yuwan-test-policy2 (arn:aws:iam::090777400063:policy/yuwan-test-policy2)

Inline Policies:
- yuwan0909t1-2nyiirm1onmsd0mqq6xind-iamsanamespace-iamsaname-role-inline-policy

Tags:
rosa_role_type: ServiceAccountRole
red-hat-managed: true
rosa.openshift.io/cluster: yuwan0909t1-2nyiirm1onmsd0mqq6xindpz7eu8k3q1xxiffnzxah
rosa.openshift.io/namespace: iamsanamespace
rosa.openshift.io/service-account: iamsaname

Trust Policy:
{"Version":"2012-10-17","Statement":[{"Effect":"Allow","Principal":{"Federated":"arn:aws:iam::090777400063:oidc-provider/yuwan0909t1-2ny-oidc-h5d3.s3.us-east-2.amazonaws.com"},"Action":"sts:AssumeRoleWithWebIdentity","Condition":{"StringEquals":{"yuwan0909t1-2ny-oidc-h5d3.s3.us-east-2.amazonaws.com:sub":"system:serviceaccount:iamsanamespace:iamsaname"}}}]}
```

## Step
Delete iamserviceaccount in the auto mode
- Delete the iamserviceaccount with the custom name.
- Delete the iamserviceaccount with the auto-generated name.

## Expect
- If there is role-name flag setting, the role of the name will be deleted successfully.
- If there is no role-name flag, the role with the auto-generated name will be delete successfully.
- If no role-name is set, and not both `--name` and `--name-space` are set, the interactive mode will be prompted to ask for input.
- There should be INFO message of "Role details:" and "Successfully deleted IAM service account role.."

```
rosa delete iamserviceaccount -c 2l3pia7089sh3g9411bad5a21uu1jghm --role-name jkeyne-0904-30-default-my-app-iamsa2-role --mode auto -y
I: Role details:
Name: jkeyne-0904-30-default-my-app-iamsa2-role
ARN: arn:aws:iam::090777400063:role/jkeyne-0904-30-default-my-app-iamsa2-role
Service Account: default/my-app-iamsa2
Attached Policies: 1
- arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess
I: Successfully deleted IAM service account role 'jkeyne-0904-30-default-my-app-iamsa2-role'
```

## Step
Delete iamserviceaccount in manual mode

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
Check validation of `rosa delete iamserviceaccount`
- The auto-generated name using the `--name` and `--namespace` doesn't exist.
- The specified role-name doesn't exist.

## Expect
```
W: Role 'jkeyne-0904-40-default-aa-role' does not exist
W: Role 'aaa' does not exist
```

## Step
Prepare one CLASSIC-OIDC STS cluster then repeat above steps

## Expect
The result should be same.
