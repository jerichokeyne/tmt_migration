# Test

## Step
Create the user role with the manual mode by command  
\# rosa create user-role --permision-boundary <pb>--mode manual -y

## Expect
The commands for creating/linking user-role are generated.

## Step
Run the commands generated in step1

## Expect
- Run commands successfully.  
- The user-role is created and linked.

## Step
Delete user-role with the manual mode by command.

## Expect
The commands for creating/linking user-role are generated. If the role is not linked, the commands don't have the unlink role command.

## Step
Run the commands generated in step3

## Expect
- Run commands successfully.  
- The user-role is unlinked and deleted.
