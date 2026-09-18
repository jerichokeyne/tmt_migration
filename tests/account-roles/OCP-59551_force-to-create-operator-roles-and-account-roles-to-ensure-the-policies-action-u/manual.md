# Test

## Step
Create account roles, remove actions from role policies, and delete policies.

## Expect

## Step
Create account roles with the same prefix and the `-f` flag.

## Expect
- Missing action permissions are added back.
- Missing policies are added back.
- Roles include a link to their AWS Console page, and policies include their ARN.
- Trust policies also include their content; managed policies instead link to their public AWS documentation.

```
I: Created role 'oa-417-Installer-Role' with ARN 'arn:aws:iam::301721915996:role/oa-417-Installer-Role'
I: Attached policy 'arn:aws:iam::301721915996:policy/oa-417-Installer-Role-Policy' to role 'oa-417-Installer-Role(https://console.aws.amazon.com/iam/home?#/roles/oa-417-Installer-Role)'
I: Attached trust policy to role 'oa-417-HCP-ROSA-Worker-Role(https://console.aws.amazon.com/iam/home?#/roles/oa-417-HCP-ROSA-Worker-Role)': {"Version": "2012-10-17", "Statement": [{"Action": ["sts:AssumeRole"], "Effect": "Allow", "Principal": {"Service": ["ec2.amazonaws.com"]}}]}
I: Created role 'oa-417-HCP-ROSA-Worker-Role' with ARN 'arn:aws:iam::301721915996:role/oa-417-HCP-ROSA-Worker-Role'
I: Attached policy 'ROSAWorkerInstancePolicy(https://docs.aws.amazon.com/aws-managed-policy/latest/reference/ROSAWorkerInstancePolicy)' to role 'oa-417-HCP-ROSA-Worker-Role(https://console.aws.amazon.com/iam/home?#/roles/oa-417-HCP-ROSA-Worker-Role)'
```

## Step
Repeat steps 1-2 with account roles using the path setting.

## Expect
The result should be the same.

## Step
~~Create an STS cluster, then remove actions from operator-role policies.~~

## Expect

## Step
~~Create operator roles with the same prefix and the `-f` flag.~~

## Expect
~~Missing actions are added back.~~

## Step
Repeat steps 4-5 with operator roles using the path setting.

## Expect
The result should be the same.

## Step
Repeat steps 4-6 on a HyperShift cluster.

## Expect
The result should be the same.

## Step
Validation (TBD): run `rosa create account-roles` with `-f` and `--managed` together.

## Expect
There should be validation for this.

## Step
Validate `-f` with `--mode manual`.

## Expect
```
W: Forcing creation of policies only works in auto mode
```

## Step
Update operator roles created before the cluster specification.

## Expect
It succeeds, new versions of the operator policies are added, and the operator policies are updated.

## Step
Check whether the OIDC config URL is used as the trust relationship of the operator roles.

## Expect
If not, it fails with:

```
E: There was a problem retrieving OIDC Config 'https://yw0515byooc1-oidc-c2t2.s3.us-east-2.amazonaws.com': The requested resource '/api/clusters_mgmt/v1/oidc_configs/https:/yw0515byooc1-oidc-c2t2.s3.us-east-2.amazonaws.com' doesn't exist
```
