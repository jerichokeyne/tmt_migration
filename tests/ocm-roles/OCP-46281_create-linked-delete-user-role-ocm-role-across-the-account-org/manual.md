# Setup
[SDA] Create/Linked/Delete user-role/ocm-role across the account/org

# Test

## Step
Login roascli with not-org-admin-RH-user1

## Expect

## Step
Create ocm-role with the auto mode.  
\# rosa create ocm-role --prefix <prefix> --mode auto -y

## Expect
- The ocm-role is created on AWS.  
- It should fail as the step of linking role with readable error message.

## Step
Link the ocm-role in step2

## Expect
It should fail with readable error message.

## Step
Login roascli with org-admin-RH-user1

## Expect

## Step
Link the ocm-role in step2

## Expect
It should succeed

## Step
Link second ocm-role under the same AWS account

## Expect
It should fail with readable error message.

## Step
Link second ocm-role under the different AWS account

## Expect
It should succeed

## Step
Login roascli with not-org-admin-RH-user1

## Expect

## Step
Create user-role but don't link

## Expect

## Step
Login roascli with not-org-admin-RH-user2 which is under the same org of not-org-admin-RH-user1

## Expect

## Step
Link the user-role in step9

## Expect
It should succeed

## Step
Login roascli with not-org-admin-RH-user3 which is NOT under the same org of not-org-admin-RH-user1

## Expect

## Step
Link the user-role in step9

## Expect
It should fail with readable error message.
