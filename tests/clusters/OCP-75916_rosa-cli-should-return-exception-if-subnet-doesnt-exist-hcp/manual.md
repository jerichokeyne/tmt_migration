# Test

## Step

1. Create HCP cluster with invalid subnets using ROSA CLI cmd:
```bash
rosa create cluster --subnet-ids subnet-0899b733d44427777, subnet-0899b733d44429127
```

## Expect

```
E: Failed to get the list of subnets: InvalidSubnetID.NotFound: The subnet ID '' does not exist
status code: 400, request id: 802db770-d40f-4a4b-8b67-50f74f63dc9c
```
