# Test

## Step

Create hosted-cp cluster in the interactive mode

## Expect

## Step

In the interactive questionaire, there should be bellow options to ask customer to choose
? Private API:
? Private ingress:

## Expect

- There is NO option for private link anymore
- the help message of "Private API:" is "? Restrict master API endpoint and application routes to direct, private connectivity. STS clusters can only be private if AWS PrivateLink is used. Once the cluster is created, this option cannot be changed. "
- the help message of "? Private ingress:" is "? Private ingress allows you to change the default level of ingress visibility
"

## Step

Choose Private API: Yes and Private ingress: Yes, then finish all interactive options

## Expect

- In the 'Subnet IDs' list, the public subnets should be excluded
- The cluster is created successfully
- Describe cluster with `rosa describe cluster -o json`, the api.listening should be 'internal'
- Check the ingress `rosa list ingress`, the 'PRIVATE' column should be 'Yes'

## Step

Choose Private API: Yes and Private ingress: No, then finish all interactive options

## Expect

- In the 'Subnet IDs' list, the public subnets should be NOT excluded
- If the public subnets are not picked, it will prompt error, "The number of public subnets for a public hosted cluster should be at least one"
- The cluster is created successfully
- Describe cluster with `rosa describe cluster -o json`, the api.listening should be 'internal'
- Check the ingress `rosa list ingress`, the 'PRIVATE' column should be 'No'

## Step

Choose Private API: No and Private ingress: Yes, then finish all interactive options

## Expect

- In the 'Subnet IDs' list, the public subnets should be NOT excluded
- If the public subnets are not picked, it will prompt error, "The number of public subnets for a public hosted cluster should be at least one"
- The cluster is created successfully
- Describe cluster with `rosa describe cluster -o json`, the api.listening should be 'external'
- Check the ingress `rosa list ingress`, the 'PRIVATE' column should be 'Yes'
