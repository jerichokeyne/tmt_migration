# Test

## Step

1. Create Classic and HCP cluster

## Expect

Clusters are created

## Step

2. Verify edit cluster -h flag
```bash
rosa edit cluster -h
```

## Expect

Edit cluster.

```
Usage:
rosa edit cluster [flags]
```

```
Examples:
\# Edit a cluster named "mycluster" to make it private
rosa edit cluster -c mycluster --private
```

\# Edit all options interactively
```bash
rosa edit cluster -c mycluster --interactive
```

```
Flags:
-c, --cluster string Name or ID of the cluster.
-y, --yes Automatically answer yes to confirm operation.
--enable-delete-protection Toggle cluster deletion protection against accidental cluster deletion.
--private Restrict master API endpoint to direct, private connectivity.
--disable-workload-monitoring Enables you to monitor your own projects in isolation from Red Hat Site Reliability Engineer (SRE) platform metrics.
--http-proxy string A proxy URL to use for creating HTTP connections outside the cluster. The URL scheme must be http.
--https-proxy string A proxy URL to use for creating HTTPS connections outside the cluster.
--no-proxy strings A comma-separated list of destination domain names, domains, IP addresses or other network CIDRs to exclude proxying.
--additional-trust-bundle-file string A file contains a PEM-encoded X.509 certificate bundle that will be added to the nodes' trusted certificate store.
--audit-log-arn string The ARN of the role that is used to forward audit logs to AWS CloudWatch.
-h, --help help for cluster
```

```
Global Flags:
--color string Surround certain characters with escape sequences to display them in color on the terminal. Allowed options are [auto never always] (default "auto")
--debug Enable debug mode.
-i, --interactive Enable interactive mode.
--profile string Use a specific AWS profile from your credential file.
--region string Use a specific AWS region, overriding the AWS_REGION environment variable. (DEPRECATED: Region flag will be removed from this command in future versions)
```

## Step

3. Verify enabling delete protection


```bash
rosa edit cluster -c $cluster --enable-delete-protection=true
rosa describe cluster -c $cluster
```

## Expect

Delete protection field should be marked as 'Enabled'

Delete Protection: Enabled

## Step

4. Verify disabling delete protection



```bash
rosa edit cluster -c $cluster --enable-delete-protection=false
rosa describe cluster -c $cluster
```

## Expect

Delete protection field should be marked as 'Enabled'

Delete Protection: Disabled

## Step

5. Verify delete protection works as expected
```bash
rosa delete cluster -c jf-hcp-57094
```

## Expect

```
E: Failed to delete cluster 2alktmdc18ncoirg8cn9k1odv2ao519a: Delete-protection has been activated on this cluster and it cannot be deleted until delete-protection is disabled
```

## Step

6. Disable the delete protection and delete the cluster

## Expect

Cluster is deleted as expected
