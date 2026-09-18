# Test

## Step
Log in with rosacil and prepare some set of prefixed operator-roles as bellow:
- Hypershift/STS operator roles attaching managed policies
- Hypershift/STS operator-roles with un-managed policies
- operator-roles in different supported version

## Expect

## Step
List the operator roles without --prefix and --version set
```bash
rosa list operator-roles
```

## Expect
- All the prefixed operator-roles are listed with 'ROLE PREFIX' and 'AMOUNT IN BUNDLE' columns.The values of them are correct.
-~~Question "Would you like to detail a specific prefix" shown,if choose 'N', it exists; If choose Y, it prompts 'Operator Role Prefix'~~
~~- After input existing prefix, the details shows as bellow, the value should be correct~~
```
OPERATOR NAME OPERATOR NAMESPACE ROLE NAME ROLE ARN CLUSTER ID VERSION POLICIES AWS Managed IN USE
cloud-credential-operator-iam-ro-creds yuwan-ashp1-r9x8-openshift-cloud-credential-operator-cloud-crede arn:aws:iam::301721915996:role/yuwan-ashp1-r9x8-openshift-cloud-credential-operator-cloud-crede 25f5f7fv8dohdm6r352d2ut6kqqh4ev8 4.13 [yw0807accr-openshift-cloud-credential-operator-cloud-credential-] No Yes
cloud-credentials openshift-cloud-network-config-controller yuwan-ashp1-r9x8-openshift-cloud-network-config-controller-cloud arn:aws:iam::301721915996:role/yuwan-ashp1-r9x8-openshift-cloud-network-config-controller-cloud 25f5f7fv8dohdm6r352d2ut6kqqh4ev8 4.13 [yw0807accr-openshift-cloud-network-config-controller-cloud-crede] No Yes
ebs-cloud-credentials openshift-cluster-csi-drivers yuwan-ashp1-r9x8-openshift-cluster-csi-drivers-ebs-cloud-credent arn:aws:iam::301721915996:role/yuwan-ashp1-r9x8-openshift-cluster-csi-drivers-ebs-cloud-credent 25f5f7fv8dohdm6r352d2ut6kqqh4ev8 4.13 [yw0807accr-openshift-cluster-csi-drivers-ebs-cloud-credentials] No Yes
installer-cloud-credentials openshift-image-registry yuwan-ashp1-r9x8-openshift-image-registry-installer-cloud-creden arn:aws:iam::301721915996:role/yuwan-ashp1-r9x8-openshift-image-registry-installer-cloud-creden 25f5f7fv8dohdm6r352d2ut6kqqh4ev8 4.13 [yw0807accr-openshift-image-registry-installer-cloud-credentials] No Yes
cloud-credentials openshift-ingress-operator yuwan-ashp1-r9x8-openshift-ingress-operator-cloud-credentials arn:aws:iam::301721915996:role/yuwan-ashp1-r9x8-openshift-ingress-operator-cloud-credentials 25f5f7fv8dohdm6r352d2ut6kqqh4ev8 4.13 [yw0807accr-openshift-ingress-operator-cloud-credentials] No Yes
aws-cloud-credentials openshift-machine-api yuwan-ashp1-r9x8-openshift-machine-api-aws-cloud-credentials arn:aws:iam::301721915996:role/yuwan-ashp1-r9x8-openshift-machine-api-aws-cloud-credentials 25f5f7fv8d
```

NOTE:
- If the role is not attached policies, it will not be listed(TBD)
- If the roles are "managed", the version should be empty(As the managed policies are without version tag(TBD))

## Step
List operator-roles with the --prefix

## Expect
- If there is no operator-roles with the prefix existed, there will be some Info message
- If the operator-roles with the prefix are found, they will be listed with detail as above step
NOTE: If the role is not attached policies, it will not be listed(TBD)

## Step
List the operator-roles with the --version

## Expect
- Question "Would you like to detail a specific prefix" shown ,if choose 'N', it exists; If choose Y, it prompts 'Operator Role Prefix'
- All the operator roles with the version will be listed with detail
- The managed roles will be shown with any specific version as the managed policies are without version tag

## Step
List operator-roles with both --prefix and --version set

## Expect
- The matched operator roles will be shown with detail.
- If no matched operator roles are found, there will be readable INFO message.

## Step
List operator-roles with cluster id

## Expect
- If cluster/operator-roles are created with byo-oidc config flow, there is INFO "I: No operator roles available"
- all operator-roles will be shown with name, arn, cluster id, version, the value should be correct.
```
OPERATOR NAME OPERATOR NAMESPACE ROLE NAME ROLE ARN CLUSTER ID VERSION POLICIES AWS Managed IN USE
cloud-credential-operator-iam-ro-creds yuwan-ashp1-r9x8-openshift-cloud-credential-operator-cloud-crede arn:aws:iam::301721915996:role/yuwan-ashp1-r9x8-openshift-cloud-credential-operator-cloud-crede 25f5f7fv8dohdm6r352d2ut6kqqh4ev8 4.13 [yw0807accr-openshift-cloud-credential-operator-cloud-credential-] No Yes
cloud-credentials openshift-cloud-network-config-controller yuwan-ashp1-r9x8-openshift-cloud-network-config-controller-cloud arn:aws:iam::301721915996:role/yuwan-ashp1-r9x8-openshift-cloud-network-config-controller-cloud 25f5f7fv8dohdm6r352d2ut6kqqh4ev8 4.13 [yw0807accr-openshift-cloud-network-config-controller-cloud-crede] No Yes
ebs-cloud-credentials openshift-cluster-csi-drivers yuwan-ashp1-r9x8-openshift-cluster-csi-drivers-ebs-cloud-credent arn:aws:iam::301721915996:role/yuwan-ashp1-r9x8-openshift-cluster-csi-drivers-ebs-cloud-credent 25f5f7fv8dohdm6r352d2ut6kqqh4ev8 4.13 [yw0807accr-openshift-cluster-csi-drivers-ebs-cloud-credentials] No Yes
installer-cloud-credentials openshift-image-registry yuwan-ashp1-r9x8-openshift-image-registry-installer-cloud-creden arn:aws:iam::301721915996:role/yuwan-ashp1-r9x8-openshift-image-registry-installer-cloud-creden 25f5f7fv8dohdm6r352d2ut6kqqh4ev8 4.13 [yw0807accr-openshift-image-registry-installer-cloud-credentials] No Yes
cloud-credentials openshift-ingress-operator yuwan-ashp1-r9x8-openshift-ingress-operator-cloud-credentials arn:aws:iam::301721915996:role/yuwan-ashp1-r9x8-openshift-ingress-operator-cloud-credentials 25f5f7fv8dohdm6r352d2ut6kqqh4ev8 4.13 [yw0807accr-openshift-ingress-operator-cloud-credentials] No Yes
aws-cloud-credentials openshift-machine-api yuwan-ashp1-r9x8-openshift-machine-api-aws-cloud-credentials arn:aws:iam::301721915996:role/yuwan-ashp1-r9x8-openshift-machine-api-aws-cloud-credentials 25f5f7fv8d
```

## Step
Some validation check:
- invalid version

## Expect
```
E: E: Version '4.20' is invalid
```
