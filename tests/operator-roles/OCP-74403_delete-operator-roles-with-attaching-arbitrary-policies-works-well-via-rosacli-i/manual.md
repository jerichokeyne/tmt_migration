# Test

## Step
Create low version account-roles then create operator-roles prio to cluster spec

## Expect

## Step
Detach and Delete some operator-roles polcies+ and also attach one arbitrary polcy on some operator-role to make sure some operator-roles attaching one arbitray policies and some attaching muiltiple arbitrary policies

## Expect

## Step
Delete the operator-roles in auto mode

## Expect
- All roles are deleted  
- All not-arbitrary policies are deleted from AWS  
- arbitrary policies are detached and not be deleted.
