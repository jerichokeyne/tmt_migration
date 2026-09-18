# Test

## Step

Prepare one MOA cluster

## Expect

## Step

Show the cluster description of the cluster by the rosa tool
```bash
rosa describe cluster -c <clusrer_id>
```

## Expect

1. Bellow info should be shown:
Name:
Display Name: --- from OCM-1405, this field is added, it gets the display_name from AMS
DNS：
ID:
External ID:
Control Plane: Customer Hosted
AWS Account:
API URL:
Console URL:
Nodes:
Region:
State:
Channel Group:
Created:
when staging environment
Details Page: https://console.dev.redhat.com/openshift/details/s/cluster_subscription_id (OCM-10532)
when production environment
Details Page: <https://console.redhat.com/openshift/details/s/>cluster_subscription_id
Infra_ID:
NOTE: The status should show different during the cluster creation, like bellow:
State: pending(Preparing Account)
State: Installing(DNS Setup in Progress)
State: Installing(Install is taking longer than expected) --> in case of provision failed and retrying.
State: Ready
Managed Policies:
2. Check the Node field, All the number of nodes across all machinepools should be shown correctly.
3. The status of pending will show the cluster status description, or it will show Preparing Account).
NOTE:It can be checked to create a sts cluster, it will be "pending (Waiting for OIDC configuration)"
4. If the cluster installation fails with error and the description of /clusters/<cluster_id>/status returns some message, the Status field will show the error+description, this case can be simulated by OCP-59987.
...
State: error (Route 53: NS record 'asbo.s3.devshift.org' already exists while creating 'rosa.yuwan-shp2.asbo.s3.devshift.org' on 's3.devshift.org.')
....
5. there is no "AWS Billing Account" attribute if not set
6. There is no "User Workload Monitoring" field in the output since OCM-17719 . - the field is still displayed , "[DEPRECATED] User Workload Monitoring: Enabled"

## Step

Describe one cluster with the incorrect cluster_id

## Expect

```
E: Failed to get cluster 'aaa': There is no cluster with identifier or name 'aaa'
```

## Step

Describe another cluster owned by the user in OCM but not moa

## Expect

It should show error that Failed to get cluster <id>: There is no cluster with identifier or name '<id>'

## Step

Repeat the steps on Windows/MacOS/Linux

## Expect

- The function should work well
- The output should displau well
