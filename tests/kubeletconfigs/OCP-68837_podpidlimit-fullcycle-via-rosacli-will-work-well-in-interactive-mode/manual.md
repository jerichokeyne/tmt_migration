# Test

## Step
1. Prepare a ROSA cluster.

## Expect

## Step
2. Create a kubeletconfig without `--pod-pids-limit`.

```bash
rosa create kubeletconfig -c 27dpunj8rqemiknurji3i4md2jqqos5b
```

## Expect
Interactive mode requests input.

```
I: Enabling interactive mode
? Pod Pids Limit?: [? for help]
```

## Step
3. Enter `?` to check the help message.

## Expect
The help message is displayed correctly.

```
I: Enabling interactive mode
? Set the Pod Pids Limit field to a value between 4096 and 16,384
? Pod Pids Limit?:
```

## Step
4. Enter the invalid value `1`.

## Expect
An error message is displayed.

```
I: Enabling interactive mode
X Sorry, your reply was invalid: '1' is less than the permitted minimum of '4096'
? Set the Pod Pids Limit field to a value between 4096 and 16,384
? Pod Pids Limit?:
```

## Step
5. Enter an invalid value greater than `16,384`.

## Expect
The correct error message is displayed.

## Step
6. Enter a value between `4096` and `16,384`.

## Expect
The creation succeeds.

## Step
7. Edit the kubeletconfig in interactive mode.

## Expect

## Step
8. Repeat the preceding actions.

## Expect
The actions work as expected.
