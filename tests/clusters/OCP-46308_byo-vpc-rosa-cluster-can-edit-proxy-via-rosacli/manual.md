# Test

## Step

**Log in via rosacli and check the help message of 'rosa edit cluster -h'**

## Expect

.......
--http-proxy string A proxy URL to use for creating HTTP connections outside the cluster. The URL scheme must be http.
--https-proxy string A proxy URL to use for creating HTTPS connections outside the cluster.
--no-proxy strings A comma-separated list of destination domain names, domains, IP addresses or other network CIDRs to exclude proxying.
--additional-trust-bundle-file string A file contains a PEM-encoded X.509 certificate bundle that will be added to the nodes' trusted certificate store.
.......

## Step

**Prepare one BYO -VPC rosa cluster without setting proxy**

## Expect

## Step

**Edit cluster with https_proxy, http_proxy, no_proxy and trust-bundle-file**
```bash
rosa edit cluster -c xxx --http-proxy **http** ://10.0.0.229:8080 --https-proxy **https** ://10.0.0.229:8080 **--no-proxy** editexample.com **--additional-trust-bundle-file** /Users/xxx/proxy/classic/ca-file.pem
```

## Expect

The cluster-wide proxy is set on the cluster.
The cluster description should show the proxy info

## Step

~~**Check the proxy is works.~~
NOTE:Follow the steps of OCP-45502
**

## Expect

~~The proxy is working.~~

## Step

**Edit cluster for removing cluster-wide proxy**`
`rosa edit cluster -c dawang-cls-43-rc3 --http-proxy "" --https-proxy "" --no-proxy ""

## Expect

It should empty the cluster-wide proxy, which it return non proxy information when `rosa describe cluster -c xxx`

## Step

**Edit cluster with https_proxy and no_proxy with different valid value
** no_proxy value format :hosts, IP addresses, or IP ranges in CIDR ,or a wildcard domain
Example:domain.example.com 10.0.0.12 10.0.0.0/24,.example.com

```bash
rosa edit cluster -c xxx --https-proxy **https** ://10.0.0.229:8080 --additional-trust-bundle-file /Users/xxx/proxy/classic/ca-file.ca --no-proxy "10.0.0.0/24,.example.com" --region us-west-2
```

## Expect

The cluster description through `rosa describe cluster -c <cluster id>` should show the correct proxy info

## Step

**Edit cluster with only http_proxy
** rosa edit cluster -c dawang-cls-43-rc3 --http-proxy "http://10.0.0.229:8080" --https-proxy "" --no-proxy ""**
**

## Expect

The cluster description through `rosa describe cluster -c <cluster id>` should show the correct proxy info

## Step

~~Edit cluster with proxy flags to update some proxy setting command~~

## Expect

~~The cluster proxy setting is updated.~~

## Step

~~Repeat above steps on sts BYO-VPC rosa cluster~~

## Expect

~~The cluster should be created successfully~~

## Step

~~Repeat above steps on different clusters(multi-az, private cluster....)~~

## Expect

## Step

~~Repeat all above steps via the interactive mode~~

## Expect

~~The proxy options are prompted. The clusters should be updated successfully. # ./rosa edit cluster -c 1omvtrv71ir13i1idugj5el76b8cliac -i I: Interactive mode enabled. Any optional fields can be ignored and will not be updated. ? Private cluster (optional): No ? Disable Workload monitoring (optional): No ? Update cluster-wide proxy (optional): Yes ? To remove any existing cluster-wide proxy value or an existing additional-trust-bundle value, enter a set of double quotes ( "") ? HTTP proxy: http://x1x.com ? HTTPS proxy: https://y2y.com ?No proxy:test.com ? Update additional trust bundle (optional): No I: Updated cluster '1omvtrv71ir13i1idugj5el76b8cliac'~~
