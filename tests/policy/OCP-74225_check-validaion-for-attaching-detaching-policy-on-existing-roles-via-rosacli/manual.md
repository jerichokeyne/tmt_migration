# Test

## Step
Prepare 12 custom policies on AWS as a prerequisite.

## Expect

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
Attach some policies to an IAM role.

## Expect

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
