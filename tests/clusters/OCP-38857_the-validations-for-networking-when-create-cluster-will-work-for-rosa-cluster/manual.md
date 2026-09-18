# Test

## Step

Launch staging env with rosa cli

## Expect

## Step

Check the illegal machine cidr when create cluster
```bash
rosa create cluster -c xueli-rosa --machine-cidr 10111.0.0.0/16
```

## Expect

```
Error: invalid argument "10111.0.0.0/16" for "--machine-cidr" flag: invalid CIDR address: 10111.0.0.0/16
<usage> will show
```

## Step

Check the illegal service cidr when create cluster
```bash
rosa create cluster -c xueli-rosa --service-cidr 10111.0.0.0/16
```

## Expect

```
Error: invalid argument "10111.0.0.0/16" for "--service-cidr" flag: invalid CIDR address: 10111.0.0.0/16
<usage> will show
```

## Step

Check the illegal pod cidr when create cluster
```bash
rosa create cluster -c xueli-rosa --pod-cidr 10111.0.0.0/16
```

## Expect

```
Error: invalid argument "10111.0.0.0/16" for "--pod-cidr" flag: invalid CIDR address: 10111.0.0.0/16
<usage> will show
```

## Step

Check the overlapped CIDR block validation:
```bash
rosa create cluster -c xueli-rosa --service-cidr 1.0.0.0/16 --pod-cidr 1.0.0.0/16
```

## Expect

- It will met error
[xueli@xueli-work tmp]$ rosa create cluster -c xueli-rosa --service-cidr 1.0.0.0/16 --pod-cidr 1.0.0.0/16
```
I: Creating cluster 'xueli-rosa'
I: To view a list of clusters and their status, run 'rosa list clusters'
E: Failed to create cluster: Service CIDR '1.0.0.0/16' and pod CIDR '1.0.0.0/16' overlap
```

## Step

Check the invalid machine CIDR
```bash
rosa create cluster -c xueli-rosa --machine-cidr 2.0.0.0/8
```

## Expect

- It will met error
[xueli@xueli-work tmp]$ rosa create cluster -c xueli-rosa --machine-cidr 2.0.0.0/8 --pod-cidr 1.0.0.0/16
```
I: Creating cluster 'xueli-rosa'
I: To view a list of clusters and their status, run 'rosa list clusters'
E: Failed to create cluster: Validating Machine CIDR '2.0.0.0/8' failed: The allowed block size must be between a /16 netmask and /25
```

## Step

Check invalid service CIDR
```bash
rosa create cluster -c xueli-rosa --service-cidr 1.0.0.0/25
```

## Expect

-It will met error
[xueli@xueli-work tmp]$ rosa create cluster -c xueli-rosa --service-cidr 1.0.0.0/25
```
I: Creating cluster 'xueli-rosa'
I: To view a list of clusters and their status, run 'rosa list clusters'
E: Failed to create cluster: Validating Service CIDR '1.0.0.0/25' failed: Service CIDR value range is too small for correct provisioning. Netmask maximum allowed value is 24
```

## Step

Check invalid pod CIDR
```bash
rosa create cluster -c xueli-rosa --pod-cidr 1.0.0.0/28
```

## Expect

- It will met error
[xueli@xueli-work tmp]$ rosa create cluster -c xueli-rosa --pod-cidr 1.0.0.0/28
```
I: Creating cluster 'xueli-rosa'
I: To view a list of clusters and their status, run 'rosa list clusters'
E: Failed to create cluster: Validating Pod CIDR '1.0.0.0/28' failed: Pod CIDR value range is too small for correct provisioning. Netmask maximum allowed value is 21.
```

## Step

Check the invalid machine CIDR for multi az
```bash
rosa create cluster -c xueli-rosa --machine-cidr 2.0.0.0/25 --multi-az
```

## Expect

- It will meet error
[xueli@xueli-work tmp]$ rosa create cluster -c xueli-rosa --machine-cidr 2.0.0.0/25 --multi-az
```
I: Creating cluster 'xueli-rosa'
I: To view a list of clusters and their status, run 'rosa list clusters'
E: Failed to create cluster: Validating Machine CIDR '2.0.0.0/25' failed: The allowed block size must be between a /16 netmask and /24
```

## Step

Check illegal host prefix
```bash
rosa create cluster -c xueli-rosa --host-prefix aa
```

## Expect

```
Error: invalid argument "aa" for "--host-prefix" flag: strconv.ParseInt: parsing "aa": invalid syntax
<usage> will show
```

## Step

Check invalid host prefix
```bash
rosa create cluster -c xueli-rosa --machine-cidr 2.0.0.0/25 --host-prefix 28
```

## Expect

[xueli@xueli-work tmp]$ rosa create cluster -c xueli-rosa --machine-cidr 2.0.0.0/25 --host-prefix 28
```
I: Creating cluster 'xueli-rosa'
I: To view a list of clusters and their status, run 'rosa list clusters'
E: Failed to create cluster: Invalid Network Host Prefix '28': Subnet length should be between '23' and '26'.
```

## Step

Check invalid private
```bash
rosa create cluster -c xueli-rosa --private=aa
```

## Expect

```
Error: invalid argument "aa" for "--private" flag: strconv.ParseBool: parsing "aa": invalid syntax
<Usage> also show
```
