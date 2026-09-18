# Test

## Step
Log in with the ROSA CLI and prepare one ready non-private cluster.

## Expect

## Step
Check the help message of `rosa edit cluster -h`.

## Expect
```
Edit cluster.

Usage:
  rosa edit cluster [flags]

Examples:
  # Edit a cluster named "mycluster" to make it private
  rosa edit cluster -c mycluster --private

  # Edit all options interactively
  rosa edit cluster -c mycluster --interactive

Flags:
  -c, --cluster string                                         Name or ID of the cluster.
  -y, --yes                                                    Automatically answer yes to confirm operation.
      --enable-delete-protection                               Enable or disable cluster delete protection against accidental deletion. Use '--enable-delete-protection=false' to disable.
      --private                                                Restrict master API endpoint to direct, private connectivity.
      --disable-workload-monitoring                            Enables you to monitor your own projects in isolation from Red Hat Site Reliability Engineer (SRE) platform metrics. Not supported for Hosted Control Plane clusters.
      --http-proxy string                                      A proxy URL to use for creating HTTP connections outside the cluster. The URL scheme must be http.
      --https-proxy string                                     A proxy URL to use for creating HTTPS connections outside the cluster. The URL scheme must be http or https.
      --no-proxy strings                                       A comma-separated list of destination domain names, domains, IP addresses or other network CIDRs to exclude proxying.
      --additional-trust-bundle-file string                    A file contains a PEM-encoded X.509 certificate bundle that will be added to the nodes' trusted certificate store.
      --audit-log-arn string                                   The ARN of the role that is used to forward audit logs to AWS CloudWatch.
      --spot-termination-queue-url string                      Optional SQS queue URL that enables graceful Spot interruption handling for Hosted Control Plane clusters.
      --autonode string                                        Configure AutoNode for the cluster. Valid values are: enabled
      --autonode-iam-role-arn string                           The AWS ARN of the IAM Role that has permissions for AutoNode
      --additional-allowed-principals strings                  A comma-separated list of additional allowed principal ARNs to be added to the Hosted Control Plane's VPC Endpoint Service to enable additional VPC Endpoint connection requests to be automatically accepted.
      --registry-config-allowed-registries strings             A comma-separated list of registries for which image pull and push actions are allowed.
      --registry-config-insecure-registries strings            A comma-separated list of registries which do not have a valid TLS certificate or only support HTTP connections.
      --registry-config-blocked-registries strings             A comma-separated list of registries for which image pull and push actions are denied.
      --registry-config-allowed-registries-for-import string   Limits the container image registries from which normal users can import images. The format should be a comma-separated list of 'domainName:insecure'. 'domainName' specifies a domain name for the registry. 'insecure' indicates whether the registry is secure or insecure.
      --registry-config-additional-trusted-ca string           A json file containing the registry hostname as the key, and the PEM-encoded certificate as the value, for each additional registry CA to trust.
      --billing-account string                                 Account ID used for billing subscriptions purchased through the AWS console for ROSA
      --network-type string                                    Migrate a cluster's network type from OpenShiftSDN to OVN-Kubernetes
      --ovn-internal-subnets string                            OVN-Kubernetes internal subnet configuration for migrating 'network-type' from OpenShiftSDN -> OVN-Kubernetes. Must be supplied as a string=value pair with any of 'join', 'transit', 'masquerade' followed by a CIDR.
                                                               Example: '--ovn-internal-subnets="join=192.168.255.0/24,transit=192.168.255.0/24,masquerade=192.168.255.0/24"'
      --channel-group string                                   Changes the channel group used for cluster versions. Channel group is the name of the channel where this image belongs, for example "stable" or "eus".
      --channel string                                         Changes the channel used for cluster versions. Channel is the name of the channel where this image belongs, for example "stable-4.20" or "eus-4.16".
  -h, --help                                                   help for cluster

Global Flags:
      --color string     Surround certain characters with escape sequences to display them in color on the terminal. Allowed options are [auto never always] (default "auto")
      --debug            Enable debug mode.
  -i, --interactive      Enable interactive mode.
      --profile string   Use a specific AWS profile from your credential file.
      --region string    Use a specific AWS region, overriding the AWS_REGION environment variable. (DEPRECATED: Region flag will be removed from this command in future versions)
```

## Step
Edit the cluster by command:

1. Edit with `--private`.
2. Edit without the cluster ID.
3. Edit with an incorrect cluster ID.

## Expect
1. The cluster is changed to `private`.
2. `E: Expected exactly one command line argument or flag containing the name or identifier of the cluster`
3. `E: Failed to get cluster '1iekajbm5j6ps8hh5ddjdpe64880c1q6aaaa': There is no cluster with identifier or name '1iekajbm5j6ps8hh5ddjdpe64880c1q6aaaa'`

## Step
Repeat the steps on Windows

## Expect
- There will be no color for the output.
![](1425503088.jpg)
