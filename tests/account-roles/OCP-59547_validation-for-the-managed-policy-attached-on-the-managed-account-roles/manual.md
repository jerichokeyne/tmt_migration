# Test

## Step
Create managed account roles and make sure some do not have the managed policies attached.

## Expect

## Step
Create the STS cluster in manual mode with the account roles from step 1 in the STAGE environment.

## Expect
It fails with an error such as:

```
E: Failed while validating account roles: role 'yw0203acc1manp1-Worker-Role' is missing the attached managed policy 'arn:aws:iam::301721915996:policy/ROSAWorkerPolicy'
```

## Step
Attach the managed policy to the role in the error message, then repeat step 2.

## Expect
It fails with an error for another account role missing its policy.

## Step
Repeat step 2 in auto mode.

## Expect
The result should be the same.

## Step
Repeat steps 2 and 4 during HyperShift cluster creation.

## Expect
The result should be the same.

## Step
Repeat step 2 in the production environment.

## Expect
An error message reports that managed account roles are not supported in the production environment.
