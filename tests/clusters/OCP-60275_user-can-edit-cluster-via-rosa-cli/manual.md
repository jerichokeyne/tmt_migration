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
rosa edit cluster -c mycluster --private
```

\# Edit all options interactively
```bash
rosa edit cluster -c mycluster --interactive
```

```
Flags:
-c, --cluster string Name or ID of the cluster.
--private Restrict master API endpoint to direct, private connectivity.
--disable-workload-monitoring [DEPRECATED FOR ROSA HCP] Enables you to monitor your own projects in isolation from Red Hat Site Reliability Engineer (SRE) platform metrics.
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

Note: For STS cluster, we cannot edit its "--private" and will get following error:
```
E: Failed to update cluster: Cannot update listening mode of cluster's API on an AWS STS cluster
```

## Step

Edit the cluster with '--private=false' and '--disable-workload-monitoring' flags, then check the `rosa describe cluster` output

## Expect

- The result of 'Private' is changed from Yes to No and the api response api.listening=external
- Since OCM-17719, the disable-workload-monitoring flag is deprecated, there is warning message "Flag --disable-workload-monitoring has been deprecated, Disable user workload monitoring (--disable-workload-monitoring) is deprecated and will be discontinued in a future version of ROSA CLI."

- In M1 of deprecating UWM, the option of UWM still works functionally with rosacli<=1.2.56. In future M2, rosacli 1.2.57, will disable it.

## Step

Edit the cluster with '--private' and '--disable-workload-monitoring=false' flags, then check the `rosa describe cluster` output

## Expect

- The result of 'Private' is changed from No to Yes and the api response api.listening=internal
~~- The result of 'User Workload Monitoring' is disappeared.~~
When edit hosted cluster, there will be an error message shown:

```
W: You are choosing to make your cluster API private. You will not be able to access your cluster until you edit network settings in your cloud provider. To also change the privacy setting of the application router endpoints, use the 'rosa edit ingress' command. OAuth visibility will be affected by cluster visibility change. Any application using OAuth behind a public ingress like the OpenShift Console will not be accessible anymore unless the user already has access to the private network. List of affected public ingresses: k1g3
```

When edit classic cluster to private, there will be error message shown:
```
W: You are choosing to make your cluster API private. You will not be able to access your cluster until you edit network settings in your cloud provider. To also change the privacy setting of the application router endpoints, use the 'rosa edit ingress' command.
```

- Since OCM-17719, the disable-workload-monitoring flag is deprecated, there is warning message "Flag --disable-workload-monitoring has been deprecated, Disable user workload monitoring (--disable-workload-monitoring) is deprecated and will be discontinued in a future version of ROSA CLI."

- In M1 of deprecating UWM, the option of UWM still works functionally with rosacli<=1.2.56. In future M2, rosacli 1.2.57, will disable it.
