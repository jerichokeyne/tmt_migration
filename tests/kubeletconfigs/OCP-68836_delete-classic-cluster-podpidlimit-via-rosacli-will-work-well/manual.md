# Test

## Step
1. Prepare a ROSA cluster.

## Expect

## Step
2. Check the `rosa delete` help message.

```bash
rosa delete -h
```

## Expect
The output includes `kubeletconfig Delete a kubeletconfig from a cluster`.

```
Delete a specific resource

Usage:
  rosa delete [command]

Aliases:
  delete, remove

Available Commands:
  account-roles          Delete account roles
  admin                  Deletes the admin user
  autoscaler             Delete autoscaler for cluster
  cluster                Delete cluster
  dns-domain             Delete DNS domain
  external-auth-provider Delete external authentication provider
  iamserviceaccount      Delete IAM role for Kubernetes service account
  idp                    Delete cluster identity providers (IDPs)
  image-mirror           Delete image mirror from a cluster
  ingress                Delete cluster ingress
  kubeletconfig          Delete a kubeletconfig from a cluster
  log-forwarder          Delete log forwarder
  machinepool            Delete machine pool
  ocm-role               Delete the Red Hat Hybrid Cloud Console role
  oidc-config            Delete an OpenID Connect (OIDC) configuration
  oidc-provider          Delete OpenID Connect (OIDC) provider
  operator-roles         Delete Operator Roles
  tuning-configs         Delete tuning config
  upgrade                Cancel cluster upgrade
  user-role              Delete user role

Flags:
  -h, --help             help for delete
      --profile string   Use a specific AWS profile from your credential file.
      --region string    Use a specific AWS region, overriding the AWS_REGION environment variable.
  -y, --yes              Automatically answer yes to confirm operation.

Global Flags:
      --color string   Surround certain characters with escape sequences to display them in color on the terminal. Allowed options are [auto never always] (default "auto")
      --debug          Enable debug mode.

Use "rosa delete [command] --help" for more information about a command.
```

## Step
3. Check the `rosa delete kubeletconfig` help message.

```bash
rosa delete kubeletconfig -h
```

## Expect
There are no typos and all descriptions are clear.

```
Delete a kubeletconfig from a cluster

Usage:
  rosa delete kubeletconfig [flags]

Aliases:
  kubeletconfig, kubelet-config

Examples:
  # Delete the KubeletConfig for ROSA Classic cluster 'foo'
  rosa delete kubeletconfig --cluster foo
  # Delete the KubeletConfig named 'bar' from cluster 'foo'
  rosa delete kubeletconfig --cluster foo --name bar

Flags:
  -c, --cluster string   Name or ID of the cluster.
  -y, --yes              Automatically answer yes to confirm operation.
      --name string      Name of the KubeletConfig (required for Hosted Control Plane clusters)
  -h, --help             help for kubeletconfig

Global Flags:
      --color string     Surround certain characters with escape sequences to display them in color on the terminal. Allowed options are [auto never always] (default "auto")
      --debug            Enable debug mode.
      --profile string   Use a specific AWS profile from your credential file.
      --region string    Use a specific AWS region, overriding the AWS_REGION environment variable. (DEPRECATED: Region flag will be removed from this command in future versions)
```

## Step
4. Delete the kubeletconfig before it is created.

```bash
rosa delete kubeletconfig -c sdq-ci-longname-xcvmk
```

## Expect
An error is returned.

```
? Deleting the custom KubeletConfig for cluster '27dpunj8rqemiknurji3i4md2jqqos5b' will cause all non-Control Plane nodes to reboot. This may cause outages to your applications. Do you wish to continue? Yes
E: Failed to delete custom KubeletConfig for cluster '27dpunj8rqemiknurji3i4md2jqqos5b': 'KubeletConfig for cluster with ID '27dpunj8rqemiknurji3i4md2jqqos5b' is not found'
```

## Step
5. Create a kubeletconfig for the cluster.

## Expect

## Step
6. Delete the kubeletconfig.

```bash
rosa edit kubeletconfig -c trad-class --pod-pids-limit 12345
rosa delete kubeletconfig -c sdq-ci-longname-xcvmk
```

## Expect
A warning explains the impact to the customer.

```
? Deleting the custom KubeletConfig for cluster '27dpunj8rqemiknurji3i4md2jqqos5b' will cause all non-Control Plane nodes to reboot. This may cause outages to your applications. Do you wish to continue? Yes
I: Successfully deleted custom KubeletConfig for cluster '27dpunj8rqemiknurji3i4md2jqqos5b'
```

## Step
7. Delete the kubeletconfig without the warning prompt.

```bash
rosa delete kubeletconfig -c sdq-ci-longname-xcvmk -y
```

## Expect
The kubeletconfig is deleted.

```
I: Successfully deleted custom KubeletConfig for cluster '27dpunj8rqemiknurji3i4md2jqqos5b'
```

## Step
8. Describe the kubeletconfig again.

```bash
rosa describe kubeletconfig -c 27dpunj8rqemiknurji3i4md2jqqos5b
```

## Expect

```
I: No custom KubeletConfig exists for cluster '27dpunj8rqemiknurji3i4md2jqqos5b'
```

## Step
9. Delete the kubeletconfig from a hosted cluster.

```bash
rosa delete kubeletconfig -c sdq-ci-wanze
```

## Expect
An error is returned.

```
E: Hosted Control Plane clusters do not support KubeletConfig configuration
```
