# Test

## Step
1. Prepare a HCP cluster.

## Expect

## Step
2. List kubeletconfigs for a nonexistent cluster.

## Expect
An error is returned.

## Step
3. Create a kubeletconfig with an invalid name.

## Expect
An error states that the name is invalid.

## Step
4. Create a kubeletconfig with an invalid pod PIDs limit, such as `123456789`.

## Expect
An error states that the pod PIDs limit is invalid.

## Step
5. Create a kubeletconfig.

## Expect

## Step
6. Create another kubeletconfig with the same name.

## Expect
An error is returned for the creation.

## Step
7. Edit the pod PIDs limit of the kubeletconfig with an invalid value.

## Expect
An error states that the pod PIDs limit is invalid.

## Step
8. Describe a nonexistent kubeletconfig.

## Expect
The kubeletconfig is reported as not found.

## Step
9. Delete a nonexistent kubeletconfig.

## Expect
The kubeletconfig is reported as not found.

## Step
10. Describe the nonexistent kubeletconfig again.

## Expect
The kubeletconfig is reported as not found.
