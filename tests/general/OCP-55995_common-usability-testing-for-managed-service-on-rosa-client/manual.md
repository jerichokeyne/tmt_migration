# Test

## Step
All deletion command need a confirmation.

## Expect

## Step
For the commands which need many parameters in the interactive mode, eg, `rosa cluster service`, it's better prompt the related command if the request is failed as last.

## Expect

## Step
For any operation , rosacli should contain all commands for a whole workflow including creation,deletion/list/describe/edit if no design is indicated specifically.

## Expect

## Step
There should a message returning the result for all operations

## Expect

## Step
It should retry if it meets network issue during the request

## Expect

## Step
There should be some wait time and retry steps when it meets condition race, for example, multi users send request at the same time

## Expect

## Step
Different version account-roles used to create managed service can be updated

## Expect

## Step
~~It should prompt the parameter input again if the invalid para is input in the interactive mode~~

## Expect
