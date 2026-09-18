# Test

## Step

Login via rosacli prepare one BYO-VPC rosa cluster

## Expect

It will return error with message
`Cluster-wide proxy is only supported for BYO-VPC clusters`

## Step

Edit cluster with invalid http_proxy set
```bash
rosa edit cluster --cluster-name yw-1029-t1 --additional-trust-bundle-file /root/workplace/rosa/additional_trust_bundle.ca --http_proxy "aaavvv"
```

## Expect

It will return error with message
`E: Invalid http-proxy value 'aaaaxxxx'`

## Step

Edit cluster with invalid http_proxy not started with http
```bash
rosa edit cluster --cluster-name yw-1029-t1 --additional-trust-bundle-file /root/workplace/rosa/additional_trust_bundle.ca --http-proxy "https://aaavvv.test.nohttp.com"
```

## Expect

It will return error with message
`E: Expected http-proxy to have an http:// scheme`

## Step

Edit cluster with invalid https_proxy set
```bash
rosa edit cluster --additional-trust-bundle-file /root/workplace/rosa/additional_trust_bundle.ca --https-proxy="aaavvv"
```

## Expect

It will return error with message
`E: parse "aaaaa": invalid URI for request`

## Step

Edit cluster with invalid additional_trust_bundle set

## Expect

It will return error with message
`Failed to parse additional_trust_bundle`

## Step

Edit wide-proxy cluster with invalid additional_trust_bundle set path

## Expect

It should fail with some error message, like 'no such file or directory'

## Step

Edit cluster which is set https-proxy with the command
```bash
rosa edit cluster --https-proxy "" --no-proxy "test.com"
```

## Expect

It should fail with some error message
Either 'proxy.http_proxy' or 'proxy.https_proxy' attributes is needed to set 'proxy.no_proxy' 'test.com'

## Step

Edit cluster which is set http-proxy with the command
```bash
rosa edit cluster --http-proxy "" --no-proxy "test.com"
```

## Expect

It should fail with some error message,
Either 'proxy.http_proxy' or 'proxy.https_proxy' attributes is needed to set 'proxy.no_proxy' 'test.com'

## Step

Edit cluster which is set http-proxy and http-proxy with the command
```bash
rosa edit cluster --http-proxy "" --https-proxy "" --no-proxy "test.com"
```

## Expect

It should fail with some error message
Cannot set 'proxy.no_proxy' attribute 'test.com' while removing 'proxy.http_proxy' and 'proxy.https_proxy' attributes

## Step

Edit cluster which is not set http-proxy and http-proxy with the command
```bash
rosa edit cluster --http-proxy "" --https-proxy "" --no-proxy "test.com"
```

## Expect

## Step

Edit cluster with invalid no_proxy "*"

## Expect

## Step

Repeat all above steps in the interactive mode

## Expect

the result should be same with the above ones

## Step

Try to edit the proxy on not-BYO-VPC cluster

## Expect

```
E: Cluster-wide proxy is not supported on clusters using the default VPC
```

## Step

Try to edit the proxy on not-BYO-VPC cluster in the interactive mode

## Expect

There is no proxy setting option prompted
