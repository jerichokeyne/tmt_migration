# Test

## Step
Prepare 12 custom policies on aws as prerequisite

## Expect

## Step
Attach policy to IAM role which is tagged with red-hat-managed=true  
- use '--mode auto'  
- dont setting --mode flag in the command  
- there are duplicated arns exists

## Expect
auto mode:  
- the policy is attached successfully  
- The INFO message "I: Attached policy ....."  
  
~~manual mode: - INFO message shows "I: Run the following command to attach the policy:" - the aws command used for attaching policies shows - The policies can be attached by the prompted command.~~  
  
dont setting --mode flag:  
- Will call out the interactive mode to ask to choose the mode  
? Attach policy mode: auto  
- After choose the mode, the result shoud be as above  
  
there are duplicated arns exists:  
Only one of duplicated policy is attached

## Step
Detach policy from   
IAM role which is tagged with red-hat-managed=true  
- use '--mode auto'  
- dont setting --mode flag in the command  
- there are duplicated arns exists  
- One existing policy but not attached to the role

## Expect
auto mode:  
- the policy is detached successfully  
- The INFO message "I: Detached policy ....."  
  
~~manual mode: - INFO message shows "I: Run the following command to detach the policy:" - the aws command used for detaching policies shows - The policies can be detached by the prompted command.~~  
  
dont setting --mode flag:  
- Will call out the interactive mode to ask to choose the mode  
? Detach policy mode: auto  
- After choose the mode, the result shoud be as above  
  
there are duplicated arns exists:  
Only one of duplicated policy is detached  
  
  
One existing policy but not attached to the role:  
I: The policy 'arn:aws:iam::301721915996:policy/aa/cc/yuwan-testp9' is currently not attached to role 'yw0428accr1-Installer-Role'

## Step
Attach multiple policies to IAM role which is not tagged with red-hat-managed=true  
- use '--mode auto'  
- dont setting --mode flag in the command

## Expect
auto mode:  
- the policies attached successfully  
- The INFO message "I: Attached policy ....."  
  
~~manual mode: - INFO message shows "I: Run the following command to attach the policy:" - the aws command used for attaching policies shows - The policies can be attached by the prompted command.~~  
  
dont setting --mode flag:  
- Will call out the interactive mode to ask to choose the mode  
? Attach policy mode: auto  
- After choose the mode, the result shoud be as above  
  
there are duplicated arns exists:  
Only one of duplicated policy is attached

## Step
Detach multiple policies to IAM role which is tagged with red-hat-managed=true  
- use '--mode auto'  
- dont setting --mode flag in the command  
- there are duplicated arns exists

## Expect
auto mode:  
- the policies detached successfully  
- The INFO message "I: Detached policy ....."  
  
~~manual mode: - INFO message shows "I: Run the following command to detach the policy:" - the aws command used for detaching policies shows - The policies can be detached by the prompted command.~~  
  
dont setting --mode flag:  
- Will call out the interactive mode to ask to choose the mode  
? Detach policy mode: auto  
- After choose the mode, the result shoud be as above  
  
there are duplicated arns exists:  
Only one of duplicated policy is detached

## Step
Validations for the attch command:  
1. policy arn with invalid format  
2. not-existed policy arn  
3. not-existed role-name  
4. multiple policies arns and some of them are with invalid format or not existed  
5. The number of the attaching policies exceed the quote (L-0DA4ABF3)  
6. The role has no red-hat-managed=true tag  
7. There is empry string in the policy-arn

## Expect
1. E: Failed to find the policy 'aaaaa': operation error IAM: GetPolicy, https response error StatusCode: 400, RequestID: 83f82595-e3fa-465a-9d50-c7a6c444defe, api error ValidationError: 1 validation error detected: Value 'aaaaa' at 'policyArn' failed to satisfy constraint: Member must have length greater than or equal to 20  
  
2. E: Failed to find the policy 'arn:aws:iam::301721915996:policy/yuwan-testp999': operation error IAM: GetPolicy, https response error StatusCode: 404, RequestID: cccd5e7c-ff3e-4999-88ee-549f3681ed71, NoSuchEntity: Policy arn:aws:iam::301721915996:policy/yuwan-testp999 was not found.  
  
3. E: Failed to find the role 'yw0426accr999-Installer-Role': operation error IAM: GetRole, https response error StatusCode: 404, RequestID: 5bb239ba-cfdd-4d6b-b524-f3070f26ed46, NoSuchEntity: The role with name yw0426accr999-Installer-Role cannot be found.  
  
4. If should fail with the above message, and other policies should NOT be attached.  
  
5. E: Failed to attach policies due to quota limitations (total limit: 10, expected: 11)  
The total limit and expected number should be correct.  
  
6. E: Cannot attach/detach policies to non-ROSA roles  
  
7. E: Invalid policy arn '', expected a valid policy arn matching ^arn:aws[\w-]*:iam::(\d{12}|aws):policy(?:\/+[\w+=,.@-]+)+$

## Step
Validations for the detach command:  
1. policy arn with invalid format  
2. not-existed policy arn  
3. not-existed role-name  
4. multiple policies arns and some of them are with invalid format or not existed  
5. The role has no red-hat-managed=true tag  
6. There is empry string in the policy-arn

## Expect
1.E: Invalid policy arn 'arnaa', expected a valid policy arn matching ^arn:aws[\w-]*:iam::(\d{12}|aws):policy(?:\/+[\w+=,.@-]+)+$  
  
2. E: Failed to find the policy 'arn:aws:iam::301721915996:policy/aa/cc/yuwan-testp15': operation error IAM: GetPolicy, https response error StatusCode: 404, RequestID: 631b4655-4284-46dc-a835-aaf6b3f05982, NoSuchEntity: Policy arn:aws:iam::301721915996:policy/aa/cc/yuwan-testp15 was not found.  
  
3.E: Failed to find the role 'yw0428accr22-Installer-Role': operation error IAM: GetRole, https response error StatusCode: 404, RequestID: 1016545e-dd51-41e8-b24d-92a4fce0b182, NoSuchEntity: The role with name yw0428accr22-Installer-Role cannot be found.  
  
4. If should fail with the above message, and other policies should NOT be attached.  
  
5. E: Cannot attach/detach policies to non-ROSA roles  
  
6. E: Invalid policy arn '', expected a valid policy arn matching ^arn:aws[\w-]*:iam::(\d{12}|aws):policy(?:\/+[\w+=,.@-]+)+$

## Step
Attach multiple policies on account-roles and operator-roles then delete the roles

## Expect
- The roles deletion should work well  
- The arbitrary polcies should NOT be deleted by the command in auto mode. In manual mode, there should NOT be the commands to delete the arbitrary policies

## Step
decribe cluster with --get-role-policy-bindings flag

## Expect
The arbitrary polcies should be shown under the roles too.  
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

## Step
detach some arbitrary policy then repeat describe cluster step

## Expect
The policies should be updated accordingly

## Step
Check '--debug' flag of `rosa attach/detach policy ....`

## Expect
--debug flag works well
