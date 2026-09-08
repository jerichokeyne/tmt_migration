# Test

## Step
Prepare the rosa tool

## Expect

## Step
Check all commands with --debug flag

## Expect
All commands should return the debug log for them

## Step
Check all commands with --debug --v flag

## Expect
The log should be shown with different levels

## Step
Run commands with --profile flag

## Expect
The command will be run with the config in the --profile flag

## Step
Check the request body of all commands which needs aws client in backend

## Expect
It should have ROSACLI vX.Y.Z in the user agent field.  
eg. # rosa create machinepool -c 1olbdku4tjd7u1pg6bcurmlh9q4ep3j6 --name=tp1 --replicas=2 --debug 2>&1 | grep -i user.agent | head -n1  
time="2021-11-24T16:40:52+08:00" level=debug msg="Request header 'User-Agent' is 'ROSACLI/1.1.6 aws-sdk-go/1.39.3 (go1.15.8; linux; amd64)'"

## Step
Repeat the steps on Windows/MacOS/Linux

## Expect
- The function should work well  
- The output should display well
