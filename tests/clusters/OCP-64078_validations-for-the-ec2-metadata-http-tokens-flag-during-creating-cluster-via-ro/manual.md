# Test

## Step

Create cluster with invalid httpTokens
```bash
rosa create cluster --sts -c zhsun-imdsin --mode auto --ec2-metadata-http-tokens=invalid
```

## Expect

Fail
```bash
rosa create cluster --sts -c zhsun-imdsin --mode auto --ec2-metadata-http-tokens=invalid --version=4.11.39
```
```
W: In a future release STS will be the default mode.
W: --sts flag won't be necessary if you wish to use STS.
W: --non-sts/--mint-mode flag will be necessary if you do not wish to use STS.
E: Expected a valid http tokens value : http-tokens value should be one of 'required', 'optional'
```

## Step

Create HCP cluster set the value
```bash
rosa create cluster rosa create cluster --hosted-cp --subnet-ids subnet-069d06e0ea927268f subnet-00c84b557627001af --private -c zhsun-rosa --ec2-metadata-http-tokens=invalid
```

## Expect

```
I: Using '301721915996' as billing account
I: To use a different billing account, add --billing-account xxxxxxxxxx to previous command
E: Expected a valid http tokens value : http-tokens value should be one of 'required', 'optional'(OCM-9159)
```
