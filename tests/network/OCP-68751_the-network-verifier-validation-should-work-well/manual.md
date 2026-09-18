# Test

## Step

1. Check these validations:
   - No non-BYO VPC cluster.
   - No `--role-arn` is set.
   - The cluster ID does not exist.

## Expect

- `E: No subnets on cluster`
- `E: role-arn is required`
- `E: Error verifying subnets: The subnet ID 'subnet-03046a9b92b5014fb' does not exist`
- `E: Failed to get cluster 'yuwan-j5hp2-j6r5': There is no cluster with identifier or name 'yuwan-j5hp2-j6r5'`

## Step

1. Check the network for a cluster with invalid tags.

```bash
rosa verify network -c sdq-ci-ngdrb --tags aa=bb
```

## Expect

The command returns an error message.

```
I: Verifying the following subnet IDs are configured correctly: [subnet-0829f6ddbab53bc0c subnet-005a1e3e4d3586893 subnet-052827033925f9f91 subnet-04b1e06f6f3cf0da7 subnet-018dbeca35a828d07 subnet-01acf1800fcef659a]
E: invalid tag format for tag '[aa=bb]'. Expected tag format: 'key:value'
```

## Step

1. Check the network for a cluster with `--hosted-cp`.

```bash
rosa verify network -c sdq-ci-fjfer --hosted-cp
```

## Expect

The command returns an error message.

```
I: Verifying the following subnet IDs are configured correctly: [subnet-0461e28d37d13fa0f subnet-08d21d7b3efe40d6f subnet-0d0c82ce04b761d46 subnet-0045a2f7711cb6368 subnet-07b418826c7ea969b subnet-0473de62a7e215ffb]
E: '--hosted-cp' flag is not required when running the network verifier with cluster
```

## Step

1. Check these validations:
   - The subnet IDs do not exist.
   - The role ARN does not exist.
   - The role ARN does not have sufficient permissions or a trust relationship.
   - The cluster is in `waiting`, `validating`, `pending`, or `uninstalling` state.

## Expect

- A readable error message is returned for each validation.
