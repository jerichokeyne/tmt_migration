# Test

## Step
Prepare a HCP cluster

## Expect

## Step
List the kubeletconfig with not existing cluster

## Expect
It should return error

## Step
Create kubeletconfig with invalid name

## Expect
Error returns that the name is invalid

## Step
Create kubeletconfig with invalid pod pids limit value like 123456789

## Expect
It should return error that the pod pids limit value is invalid

## Step
Create a kubeletconfig

## Expect

## Step
Create another kubeletconfig with same name

## Expect
Got error for the creation

## Step
Edit the pod pids limit value of the kubelet config with invalid value

## Expect
It shows the error message that the pod pid limit is invalid

## Step
Describe the not existing kubeletconfig

## Expect
It shows the kubeletconfig not found

## Step
Delete the not existingkubeletconfig

## Expect
It shows the kubeletconfig not found

## Step
Describe the not existingkuebeletconfig again

## Expect
It shows the kubeletconfig not found
