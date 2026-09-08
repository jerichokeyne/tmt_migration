# Test

## Step
Check the help message:  
\# rosa create ocm-role -h  
\# rosa create user-role -h

## Expect
There is the help info of '--path'

## Step
Create user-role in the interactive mode then choose manual in the promoted option

## Expect
- AWS command is prompted, and it includes "Key=red-hat-managed,Value=true"(SDA-6439)  
- There is the rosacli command for linking the role  
- The promoted AWS/ROSACLI commands can be executed successfully   
  
After the commands are executed:  
- The user-role with setting path is created successfully.  
- The user should show correctly by `rosa list user-role`

## Step
Create another user-role in the interactive mode then choose auto in the promoted option

## Expect
- The user-role with setting path is created successfully.  
- The user-role should show correctly by `rosa list user-role`

## Step
Unlink the user-role created in step2

## Expect
It should succeed

## Step
Delete the user-role created in step2

## Expect
It should succeed

## Step
Create ocm-role in the interactive mode then choose manual in the promoted option

## Expect
- AWS command is prompted, and it includes "Key=red-hat-managed,Value=true"(SDA-6439)  
- There is the rosacli command for linking the role  
- The promoted AWS/ROSACLI commands can be executed successfully   
  
After the commands are executed:  
- The ocm-role with setting path is created successfully.  
- The ocm-role should show correctly by `rosa list user-role`

## Step
Create another ocm-role in the interactive mode then choose auto in the promoted option

## Expect
- The ocm-role with setting path is created successfully.  
- The ocm-role should show correctly by `rosa list user-role`

## Step
Unlink the ocm-role created in step6

## Expect
It should succeed

## Step
Delete the ocm-role with the arn created in step6

## Expect
It should succeed

## Step
Check the validation for `rosa create ocm-role -i` and `rosa create user-role -i` for '--path'

## Expect
yuwan1-mac:rosa yuwan$ ./rosa create user-role -i  
I: Creating User role  
? Role prefix: a  
? Permissions boundary ARN (optional):   
X Sorry, your reply was invalid: invalid ARN Path. It must begin and end with / and contain only alphanumeric characters  
? Role Path (optional): [? for help]
