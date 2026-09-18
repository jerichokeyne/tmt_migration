# Test

## Step

Create account-roles

## Expect

## Step

Add condition in the account-roles (installer and worker roles) with the external id
```json
{
"Version": "2012-10-17",
"Statement": [
{
"Effect": "Allow",
"Principal": {
"AWS": "arn:aws:iam::644306948063:role/RH-Managed-OpenShift-Installer"
},
"Action": "sts:AssumeRole",
"Condition": {
"StringEquals": {
"sts:ExternalId": "223B9588-36A5-ECA4-BE8D-7C673B77CEC1"
}
}
}
]
}
```

## Expect

## Step

Create STS cluster with setting the external id with the value not same with the one in step2

## Expect

Failed with error:
```
E: Failed to retrieve AWS regions: status is 400, identifier is '400', code is 'CLUSTERS-MGMT-400' and operation identifier is 'f97a3a89-0d13-4c4d-8cce-c89462f18511': An error occurred while trying to create an AWS client: Failed to assume role with ARN 'arn:aws:iam::301721915996:role/yw0812accr3-HCP-ROSA-Installer-Role': operation error STS: AssumeRole, https response error StatusCode: 403, RequestID: 8e32e21b-cc36-4cd1-b508-a9d221418762, api error AccessDenied: User: arn:aws:sts::644306948063:assumed-role/RH-Managed-OpenShift-Installer/OCM is not authorized to perform: sts:AssumeRole on resource: arn:aws:iam::301721915996:role/yw0812accr3-HCP-ROSA-Installer-Role
```

## Step

Create STS cluster with setting the external id with the value same with the one in step2

## Expect

It should succeed

## Step

After the cluster is ready

## Expect

the machinepools should be created.

## Step

Create additional machinepool

## Expect

It should succeed

## Step

Repeat above steps with the installer without the external id condition

## Expect

It should succeed, including the step 3

## Step

Repeat all above step on the HCP cluster

## Expect

result should be same
