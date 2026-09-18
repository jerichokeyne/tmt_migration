# Setup
NOTE: the proxy and bundle update will be covered in other TC

# Test

## Step

Log in via rosa-cli and check the help message of 'rosa edit cluster -h'

## Expect

yuwan1-mac:rosa yuwan$ ./rosa edit cluster -h
Edit cluster.

```
Usage:
rosa edit cluster [flags]
```

```
Examples:
\# Edit a cluster named "mycluster" to make it private
rosa edit cluster mycluster --private
```

\# Edit all options interactively
```bash
rosa edit cluster -c mycluster --interactive
```

```
Flags:
-c, --cluster string Name or ID of the cluster.
--private Restrict master API endpoint to direct, private connectivity.
~~--disable-workload-monitoring Enables you to monitor your own projects in isolation from Red Hat Site Reliability Engineer (SRE) platform metrics.~~
--http-proxy string A proxy URL to use for creating HTTP connections outside the cluster. The URL scheme must be http.
--https-proxy string A proxy URL to use for creating HTTPS connections outside the cluster.
--no-proxy strings A comma-separated list of destination domain names, domains, IP addresses or other network CIDRs to exclude proxying.
--additional-trust-bundle-file string A file contains a PEM-encoded X.509 certificate bundle that will be added to the nodes' trusted certificate store.
-h, --help help for cluster
```

```
Global Flags:
--color string Surround certain characters with escape sequences to display them in color on the terminal. Allowed options are [auto never always] (default "auto")
--debug Enable debug mode.
-i, --interactive Enable interactive mode.
--profile string Use a specific AWS profile from your credential file.
--region string Use a specific AWS region, overriding the AWS_REGION environment variable.
```

## Step

Prepare one ready private cluster.
NOTE:
- this case will cover NON-STS cluster, STS cluster, Hypershift cluster.
- Private cluster is also a private-link cluster as default

## Expect

```
? Private cluster (optional): No
? Disable Workload monitoring (optional): No
```

## Step

Edit cluster on BYO classic STS cluster and hosted-cp cluster

## Expect

- The result of 'Private' is changed from Yes to No and the api response api.listening=external
~~- The result of 'User Workload Monitoring' is set with 'disabled'~~
- The options for proxy settings works well.
.....
```
? Update cluster-wide proxy (optional): Yes
? To remove any existing cluster-wide proxy value or an existing additional-trust-bundle value, enter a set of double quotes ("")
? HTTP proxy (optional): http://test.com:8080
? HTTPS proxy (optional): https://test.com:8080
? No proxy (optional):
? Update additional trust bundle (optional): Yes
? Additional trust bundle file path (optional):
.....
```

## Step

Edit cluster on hosted-cp cluster

## Expect

- The result of 'Private' is changed from No to Yes and the api response api.listening=internal
- The result of 'User Workload Monitoring' is disappeared.
- The options for audit logs settings works well.
....
```
? Enable audit log forwarding to AWS CloudWatch: Yes
I: To configure the audit log forwarding role in your AWS account, please refer to steps 1 through 6: https://access.redhat.com/solutions/7002219
? Audit log forwarding role ARN: arn:aws:iam::301721915996:role/yw0825accr1-Installer-Role
......
```
