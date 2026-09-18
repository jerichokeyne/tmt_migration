# Test

## Step

- In M1 of deprecating UWM, the option of UWM still works functionally with rosacli<=1.2.56. In future M2, rosacli 1.2.57, will disable it.
- There is warning message at the questionair in the interactive mode,
W: [DEPRECATED FOR ROSA HCP] User workload monitoring (--disable-workload-monitoring) has been deprecated for Hosted Control Plane clusters, and will be removed in a future version of ROSA CLI. Please remove from your workflows to avoid future issues

## Expect

## Step

Create classic cluster without setting '--sts'/'--non-sts'/'--mint-mode' flags and without the account-roles arns set.
```bash
rosa create cluster -c <cluster_name> -y
```

## Expect

- rosacli will prompt the STS cluster creation flow
- The STS cluster should be created

## Step

Create classic cluster without setting '--sts' flag in the interactive mode

## Expect

- rosacli will prompt the STS cluster creation flow
- The STS cluster should be created

## Step

Create classic cluster with setting '--non-sts'/'--mint-mode' flag in interactive mode.

## Expect

rosacli will prompt " Deploy cluster using AWS STS:" to allow users to choose if create STS cluster

## Step

Interactive mode, edit the cluster with '--private=false' and '--disable-workload-monitoring' flags, then check the `rosa describe cluster` output

## Expect

- The result of 'Private' is changed from Yes to No and the api response api.listening=external
- The result of 'Private' is changed from Yes to No and the api response api.listening=external

## Step

Interactive mode, edit the cluster with '--private' and '--disable-workload-monitoring=false' flags, then check the `rosa describe cluster` output

## Expect

- The result of 'Private' is changed from No to Yes and the api response api.listening=internal
- ~~The result of 'User Workload Monitoring' is disappeared. When edit hosted cluster, there will be an error message shown:~~

```
W: You are choosing to make your cluster API private. You will not be able to access your cluster until you edit network settings in your cloud provider. To also change the privacy setting of the application router endpoints, use the 'rosa edit ingress' command. OAuth visibility will be affected by cluster visibility change. Any application using OAuth behind a public ingress like the OpenShift Console will not be accessible anymore unless the user already has access to the private network. List of affected public ingresses: k1g3
```

When edit classic cluster to private, there will be error message shown:
```
W: You are choosing to make your cluster API private. You will not be able to access your cluster until you edit network settings in your cloud provider. To also change the privacy setting of the application router endpoints, use the 'rosa edit ingress' command.
```

- Since <https://issues.redhat.com/browse/OCM-17719> There is no prompted questionair "Disable Workload monitoring", that's deprecated.
