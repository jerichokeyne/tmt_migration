# Test

## Step
1. Prepare a ROSA cluster.

## Expect

## Step
2. Check the `rosa create` help message.

```bash
rosa create -h
```

## Expect
The output includes `kubeletconfig Create a custom kubeletconfig for a cluster`.

```
Create a resource from stdin

Usage:
  rosa create [command]

Aliases:
  create, add

Available Commands:
  account-roles          Create account-wide Identity and Access Management (IAM) roles before creating your cluster.
  admin                  Creates an admin user to login to the cluster
  autoscaler             Create an autoscaler for a cluster
  break-glass-credential Create a break glass credential for a cluster.
  cluster                Create cluster
  decision               Create a decision for an Access Request
  dns-domain             Create Domain Name System (DNS) domain.
  external-auth-provider Create an external authentication provider for a cluster.
  iamserviceaccount      Create IAM role for Kubernetes service account
  idp                    Add an identity provider (IDP) for a cluster
  image-mirror           Create image mirror for a cluster
  kubeletconfig          Create a custom kubeletconfig for a cluster
  log-forwarder          Create a log forwarder for a Hosted Control Plane cluster
  machinepool            Add machine pool to cluster
  network                Network AWS cloudformation stack
  ocm-role               Create role used by Red Hat Hybrid Cloud Console
  oidc-config            Create OpenID Connect (OIDC) config compliant with OIDC protocol.
  oidc-provider          Create OpenID Connect (OIDC) provider for an AWS Security Token Service (STS) cluster.
  operator-roles         Create Operator Identity and Access Management (IAM) roles for a cluster.
  spot-termination-queue Create Spot termination queue resources
  tuning-configs         Add tuning config
  user-role              Create user role to verify account association

Flags:
  -h, --help             help for create
      --profile string   Use a specific AWS profile from your credential file.
      --region string    Use a specific AWS region, overriding the AWS_REGION environment variable.
  -y, --yes              Automatically answer yes to confirm operation.

Global Flags:
      --color string   Surround certain characters with escape sequences to display them in color on the terminal. Allowed options are [auto never always] (default "auto")
      --debug          Enable debug mode.

Use "rosa create [command] --help" for more information about a command.
```

## Step
3. Check the `rosa create kubeletconfig` help message.

```bash
rosa create kubeletconfig -h
```

## Expect
There are no typos and all descriptions are clear.

```
Create a custom kubeletconfig for a cluster

Usage:
  rosa create kubeletconfig [flags]

Aliases:
  kubeletconfig, kubelet-config

Examples:
  # Create a custom kubeletconfig with a pod-pids-limit of 5000
  rosa create kubeletconfig --cluster=mycluster --pod-pids-limit=5000

Flags:
      --pod-pids-limit int   Sets the requested pod_pids_limit for this KubeletConfig.
      --name string          Name of the KubeletConfig (required for Hosted Control Plane clusters)
  -c, --cluster string       Name or ID of the cluster.
  -i, --interactive          Enable interactive mode.
  -h, --help                 help for kubeletconfig

Global Flags:
      --color string     Surround certain characters with escape sequences to display them in color on the terminal. Allowed options are [auto never always] (default "auto")
      --debug            Enable debug mode.
      --profile string   Use a specific AWS profile from your credential file.
      --region string    Use a specific AWS region, overriding the AWS_REGION environment variable. (DEPRECATED: Region flag will be removed from this command in future versions)
  -y, --yes              Automatically answer yes to confirm operation.
```

## Step
4. Create a kubeletconfig for the cluster.

```bash
rosa create kubeletconfig -c trad-class --pod-pids-limit 12345
```

## Expect
A warning explains the impact to the customer.

```
? Creating the custom KubeletConfig for cluster '27d9uge7mvjd9dhmjb7l9ed6mvcdf0kn' will cause all non-Control Plane nodes to reboot. This may cause outages to your applications. Do you wish to continue? (y/N)
I: Creation of custom KubeletConfig for cluster '27d9uge7mvjd9dhmjb7l9ed6mvcdf0kn' aborted.
```

## Step
5. Create the kubeletconfig without the warning prompt.

```bash
rosa create kubeletconfig -c trad-class --pod-pids-limit 12345 -y
```

## Expect
The kubeletconfig is created.

```
I: Successfully created custom KubeletConfig for cluster '27d9uge7mvjd9dhmjb7l9ed6mvcdf0kn'
```

## Step
6. Describe the kubeletconfig.

```bash
rosa describe kubeletconfig -c trad-class
```

## Expect
The configuration is displayed.

```
Pod Pids Limit: 12345
```

## Step
7. Create a kubeletconfig with `--name` again.

## Expect
An error reports that the kubeletconfig already exists.

## Step
8. Create a machinepool with `--kubelet-configs` set.

## Expect
An error reports that the setting is not supported for a classic cluster.
