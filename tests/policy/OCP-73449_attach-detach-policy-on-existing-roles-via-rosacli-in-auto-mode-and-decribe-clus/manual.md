# Test

## Step
Prepare 12 custom policies on AWS as a prerequisite.

## Expect

## Step
Attach a policy to an IAM role tagged with `red-hat-managed=true`:

- Use `--mode auto`.
- Do not set the `--mode` flag in the command.
- Use duplicate ARNs.

## Expect
Auto mode:
- The policy is attached successfully.
- The `I: Attached policy .....` info message is shown.

~~Manual mode: the `I: Run the following command to attach the policy:` info message and AWS command are shown, and the policies can be attached with the prompted command.~~

When `--mode` is not set:
- Interactive mode prompts for the mode.
- ```
  ? Attach policy mode: auto
  ```
- After selecting the mode, the result is as above.

With duplicate ARNs, only one duplicate policy is attached.

## Step
Detach a policy from an IAM role tagged with `red-hat-managed=true`:

- Use `--mode auto`.
- Do not set the `--mode` flag in the command.
- Use duplicate ARNs.
- Use one existing policy that is not attached to the role.

## Expect
Auto mode:
- The policy is detached successfully.
- The `I: Detached policy .....` info message is shown.

~~Manual mode: the `I: Run the following command to detach the policy:` info message and AWS command are shown, and the policies can be detached with the prompted command.~~

When `--mode` is not set:
- Interactive mode prompts for the mode.
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
Attach multiple policies to an IAM role not tagged with `red-hat-managed=true`:

- Use `--mode auto`.
- Do not set the `--mode` flag in the command.

## Expect
Auto mode:
- The policies are attached successfully.
- The `I: Attached policy .....` info message is shown.

~~Manual mode: the `I: Run the following command to attach the policy:` info message and AWS command are shown, and the policies can be attached with the prompted command.~~

When `--mode` is not set:
- Interactive mode prompts for the mode.
- ```
  ? Attach policy mode: auto
  ```
- After selecting the mode, the result is as above.

With duplicate ARNs, only one duplicate policy is attached.

## Step
Detach multiple policies from an IAM role tagged with `red-hat-managed=true`:

- Use `--mode auto`.
- Do not set the `--mode` flag in the command.
- Use duplicate ARNs.

## Expect
Auto mode:
- The policies are detached successfully.
- The `I: Detached policy .....` info message is shown.

~~Manual mode: the `I: Run the following command to detach the policy:` info message and AWS command are shown, and the policies can be detached with the prompted command.~~

When `--mode` is not set:
- Interactive mode prompts for the mode.
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
Describe the cluster with the `--get-role-policy-bindings` flag.

## Expect
Arbitrary policies are shown under the roles.

```
.......
Role (STS) ARN: arn:aws:iam::301721915996:role/yw0531acrv14-Installer-Role
- arn:aws:iam::301721915996:policy/yw0531acrv14-Installer-Role-Policy
Support Role ARN: arn:aws:iam::301721915996:role/yw0531acrv14-Support-Role
- arn:aws:iam::301721915996:policy/yw0531acrv14-Support-Role-Policy
Instance IAM Roles:
- Control plane: arn:aws:iam::301721915996:role/yw0531acrv14-ControlPlane-Role
- arn:aws:iam::301721915996:policy/yuwan-testp5
- arn:aws:iam::301721915996:policy/yuwan-testp4
- arn:aws:iam::301721915996:policy/yw0531acrv14-ControlPlane-Role-Policy
- Worker: arn:aws:iam::301721915996:role/yw0531acrv14-Worker-Role
- arn:aws:iam::301721915996:policy/yuwan-testp5
- arn:aws:iam::301721915996:policy/yw0531acrv14-Worker-Role-Policy
- arn:aws:iam::301721915996:policy/yuwan-testp3
Operator IAM Roles:
- arn:aws:iam::301721915996:role/yuwan-0531sm2-asdf-openshift-ingress-operator-cloud-credentials
- arn:aws:iam::301721915996:policy/yw0531acrv14-openshift-ingress-operator-cloud-credentials
- arn:aws:iam::301721915996:role/yuwan-0531sm2-asdf-openshift-cluster-csi-drivers-ebs-cloud-crede
- arn:aws:iam::301721915996:policy/yw0531acrv14-openshift-cluster-csi-drivers-ebs-cloud-credentials
- arn:aws:iam::301721915996:role/yuwan-0531sm2-asdf-openshift-cloud-network-config-controller-clo
- arn:aws:iam::301721915996:policy/yw0531acrv14-openshift-cloud-network-config-controller-cloud-cre
- arn:aws:iam::301721915996:role/yuwan-0531sm2-asdf-openshift-machine-api-aws-cloud-credentials
- arn:aws:iam::301721915996:policy/yuwan-testp2
- arn:aws:iam::301721915996:policy/yuwan-testp1
- arn:aws:iam::301721915996:policy/yw0531acrv14-openshift-machine-api-aws-cloud-credentials
- arn:aws:iam::301721915996:role/yuwan-0531sm2-asdf-openshift-cloud-credential-operator-cloud-cre
- arn:aws:iam::301721915996:policy/yw0531acrv14-openshift-cloud-credential-operator-cloud-credentia
- arn:aws:iam::301721915996:policy/yuwan-testp1
- arn:aws:iam::301721915996:policy/yuwan-testp3
- arn:aws:iam::301721915996:role/yuwan-0531sm2-asdf-openshift-image-registry-installer-cloud-cred
- arn:aws:iam::301721915996:policy/yw0531acrv14-openshift-image-registry-installer-cloud-credential
Managed Policies: No
```

## Step
Detach arbitrary policies, then repeat the describe-cluster step.

## Expect
The policies are updated accordingly.

## Step
Check the `--debug` flag of `rosa attach/detach policy ....`.

## Expect
The `--debug` flag works correctly.
