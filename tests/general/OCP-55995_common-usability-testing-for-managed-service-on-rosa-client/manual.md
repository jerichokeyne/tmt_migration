# Test

## Step
All deletion commands need a confirmation.

## Expect

## Step
For commands requiring many parameters in interactive mode, for example `rosa cluster service`, prompt the related command last if the request fails.

## Expect

## Step
For any operation, ROSA CLI should contain all commands for a whole workflow, including create, delete, list, describe, and edit, if no design is indicated specifically.

## Expect

## Step
There should be a message returning the result for all operations.

## Expect

## Step
It should retry if it encounters a network issue during the request.

## Expect

## Step
There should be a wait time and retry steps when it encounters a race condition, for example, multiple users sending requests at the same time.

## Expect

## Step
Different-version account roles used to create the managed service can be updated.

## Expect

## Step
~~It should prompt for parameter input again if an invalid parameter is entered in interactive mode.~~

## Expect
