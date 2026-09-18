# Test

## Step

Create 'API private' and 'ingress private' hosted-cp cluster by command.
```bash
rosa create cluster --cluster-name yuwan0703h3 --sts --mode auto ... --subnet-ids subnet-0759fd582460289f5,subnet-08d22e0c8c0a0a767,subnet-0c40d7da459c3ea00 --hosted-cp --private --default-ingress-private
```

## Expect

- The cluster is created successfully
- Describe cluster with `rosa describe cluster -o json`, the api.listening should be 'internal'
- Check the ingress `rosa list ingress`, the 'PRIVATE' column should be 'Yes'

Validation for subnets:
- If '--subnet-ids' includes public sunbets, it will report error "Cluster is set as private, cannot use public 'subnet-0a2aaa94a3cf160a5'"

## Step

Create hosted-cp cluster of 'API private' only by command.
```bash
rosa create cluster --cluster-name yuwan0703h3 --sts --mode auto ... --subnet-ids subnet-0759fd582460289f5,subnet-08d22e0c8c0a0a767,subnet-0c40d7da459c3ea00 --hosted-cp --private
```

## Expect

- The cluster is created successfully
- Describe cluster with `rosa describe cluster -o json`, the api.listening should be 'internal'
- Check the ingress `rosa list ingress`, the 'PRIVATE' column should be 'No'

Validation for subnets:
- If '--subnet-ids' only has private sunbets, it will report error "The number of public subnets for a public hosted cluster should be at least one"

## Step

Create hosted-cp cluster of 'ingress private' only by command.
```bash
rosa create cluster --cluster-name yuwan0703h3 --sts --mode auto ... --subnet-ids subnet-0759fd582460289f5,subnet-08d22e0c8c0a0a767,subnet-0c40d7da459c3ea00 --hosted-cp --default-ingress-private
```

## Expect

- The cluster is created successfully
- Describe cluster with `rosa describe cluster -o json`, the api.listening should be 'external'
- Check the ingress `rosa list ingress`, the 'PRIVATE' column should be 'Yes'

Validation for subnets:
- If '--subnet-ids' only has private sunbets, it will report error "The number of public subnets for a public hosted cluster should be at least one"

## Step

Check the private-link flag should be deprecated for hosted-cp cluster

## Expect

It will report warning error message when set private-link flag when creating hosted-cp cluster
