# Setup
```bash
./rosa version
```
    1. 2.36
    I: Your ROSA CLI is up to date.

# Test

## Step

**Positive test cases :-**
1. Check the new '--domain-prefix' flag in rosacli --help message, the flag exists.

```bash
./rosa create cluster -h | grep "domain-prefix"
```

## Expect

The '--domain-prefix' flag should be present in help message

--domain-prefix string An optional unique domain prefix of the cluster. This will be used when genera

## Step

2. Create the rosa classic cluster in interactive mode with "Cluster name" of length <=54 and
"domain_prefix" of length <=15.

```bash
./rosa create cluster -i
```
I: Interactive mode enabled.
Any optional fields can be left empty and a default will be selected.
? Cluster name: akanni-abcliexmrynxwkkbthqedjpdhtwssamexwmow-very-long
? Domain prefix (optional): domprefix-1
? Deploy cluster with Hosted Control Plane: No
? Create cluster admin user: No

## Expect

The cluster should be created successfully.



```bash
./rosa list cluster
```
......
29ri2d283ods1idf6k8qugms0ep9l85e akanni-abcliexmrynxwkkbthqedjpdhtwssamexwmow-very-long ready Classic (STS)

## Step

3. Create the rosa classic cluster in interactive mode by only passing "Cluster name" and did not
supplied anything for "domain_prefix".

```bash
./rosa create cluster -i
```
I: Interactive mode enabled.
Any optional fields can be left empty and a default will be selected.
? Cluster name: akanni-abcliexmrynxwkkbthqedjpdhtwssamexwmow-very-l234
? Domain prefix (optional):
? Deploy cluster with Hosted Control Plane: No
? Create cluster admin user: No
......

## Expect

The cluster should be created successfully.



```bash
./rosa list cluster
```
.......
29rj10qj700b1u9qnrp3lp72p9vipi46 akanni-abcliexmrynxwkkbthqedjpdhtwssamexwmow-very-l234 ready Classic (STS)

## Step

4. Create rosa HCP cluster by using '--domain-prefix' flag.

```bash
./rosa create cluster --cluster-name akanni-abcliexmrynxwkkbthqedjpdhtwssamexwmow --domain-prefix akanni-d323
```
^BW: In a future release STS will be the default mode.
W: --sts flag won't be necessary if you wish to use STS.
W: --non-sts/--mint-mode flag will be necessary if you do not wish to use STS.
I: Creating cluster 'akanni-abcliexmrynxwkkbthqedjpdhtwssamexwmow'
I: To view a list of clusters and their status, run 'rosa list clusters'

## Expect

The cluster should be created successfully.


```
I: Cluster 'akanni-abcliexmrynxwkkbthqedjpdhtwssamexwmow' has been created.
```

## Step

**Negative test cases :-

** 1. Create a cluster of name length more than 54 characters.

```bash
./rosa create cluster --cluster-name akanni-abcliexmrynxwkkbthqedjpdhtwssamexwmow-very-lon3-1
```

## Expect

The cluster will not be created, an error message will be shown.

```
E: Cluster name must consist of no more than 54 lowercase alphanumeric characters or '-', start with a letter, and end with an alphanumeric character.
```

## Step

2. Create a cluster of domain_prefix length more than 15 characters.

```bash
./rosa create cluster --domain-prefix akash-domain-prefix
```
I: Enabling interactive mode
? Cluster name: akanni-rosa-cluster-with-long-name

## Expect

The cluster will not be created, an error message will be shown.

X Sorry, your reply was invalid: Cluster domain prefix must consist of no more than 15 lowercase alphanumeric characters or '-', start with a letter, and end with an alphanumeric character.

## Step

3. Try supplying invalid characters for 'cluster name' and 'doamin prefix'.

3. 1 'domain_prefix' which conatins '$' symbol.
```bash
./rosa create cluster --domain-prefix akanni$
```
I: Enabling interactive mode


3. 2 'name' which contains '@' symbol
```bash
./rosa create cluster --cluster-name akanni-abcliexmrynxwkkbthqedjpdhtwssamexwmow-very@lon3
```

## Expect

The cluster will not be created, an error message will be shown.

X Sorry, your reply was invalid: Cluster domain prefix must consist of no more than 15 lowercase alphanumeric characters or '-', start with a letter, and end with an alphanumeric character.
```
? Domain prefix: [? for help] (akanni$)
E: Expected a valid domain prefix: interrupt
```


```
E: Cluster name must consist of no more than 54 lowercase alphanumeric characters or '-', start with a letter, and end with an alphanumeric character.
```

## Step

4. Create a cluster with duplicate “domain_prefix”
Create ‘cluster-1’ with “domain_prefix”=’akanni-d345’ once it is in ready state,
Try creating ‘cluster-2’ with the same "domain_prefix"=’akanni-d345’.

## Expect

The cluster will not be created, an error message will be shown.

```
E: Failed to create cluster: Duplicate cluster domain prefix. There is already a cluster with the domain prefix 'akanni-d345' in the organization '1jlfDskrR39egznAq3T18Ul0Xxv'
```

## Step

5. Try creating a cluster with duplicate name.

when cluster with name "akanni-abcliexmrynxwkkbthqedjpdhtwssamex-rosa-hcp-api" already exists in same organization and run below command to create a new cluster with same name.
```bash
./rosa create cluster -c akanni-abcliexmrynxwkkbthqedjpdhtwssamex-rosa-hcp-api
```

## Expect

The cluster will not be created, an error message will be shown.

```
E: Failed to create cluster: Duplicate cluster name. There is already a cluster with the name 'akanni-abcliexmrynxwkkbthqedjpdhtwssamex-rosa-hcp-api' in the organization '1jlfDskrR39egznAq3T18Ul0Xxv'
```
