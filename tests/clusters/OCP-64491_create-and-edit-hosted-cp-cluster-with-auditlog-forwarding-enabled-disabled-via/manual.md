# Test

## Step

Create a BYO OIDC config

## Expect

## Step

Prepare a role on aws for audit feature <https://access.redhat.com/solutions/7002219>

## Expect

## Step

Create hosted-cp cluster with setting --audit-log-arn

## Expect

- The cluster is created
- The spec of the cluster on CS should contain bellow configure.
- The function should work well
.....
"aws": {
"audit_log": {
"role_arn": <role arn>
}
.....

```bash
aws logs describe-log-streams --log-group-name ocm-staging-24bju1p8cglgo8rli1ugbjadj81jntua-yuwan-uaud1 --region us-west-2
```
\------------------------------------------------------------------------------------------------------------------------------------------------------
| DescribeLogStreams |
+----------------------------------------------------------------------------------------------------------------------------------------------------+
|| logStreams ||
|+---------------------+----------------------------------------------------------------------------------------------------------------------------+|
|| arn | arn:aws:logs:us-west-2:301721915996:log-group:ocm-staging-24bju1p8cglgo8rli1ugbjadj81jntua-yuwan-uaud1:log-stream:audit ||
|| creationTime | 1686736585784 ||
|| firstEventTimestamp| 1686736591893 ||
|| lastEventTimestamp | 1686745133857 ||
|| lastIngestionTime | 1686745133903 ||
|| logStreamName | audit ||
|| storedBytes | 0 ||
|| uploadSequenceToken| 49039859549777297205311419662350586510140788730328589164 ||
|+---------------------+----------------------------------------------------------------------------------------------------------------------------+|

## Step

Describe cluster

## Expect

there is one field to show the audit log enable/disable and the audit role.
.....
Audit Log Forwarding: enabled
Audit Log Role ARN: arn:aws:iam::301721915996:role/yw0705audit1role
.....

## Step

Edit the cluster to disable audit log forwarding
```bash
rosa edit cluster -c 24bju1p8cglgo8rli1ugbjadj81jntua --audit-log-arn ""
```

## Expect

- There is confirmation question "Are you sure you want to disable audit log forwarding for cluster?"
- Choose yes, then the audit log forwarding is disabled, checking the cluster spec, it should be like bellow:
.....
"aws": {
"audit_log": {
"role_arn": ""
}
.....
- There is no related fields in the output of `rosa describe cluster`

## Step

Edit the cluster to enable audit log forwarding with setting arn value
```bash
rosa edit cluster -c 24bju1p8cglgo8rli1ugbjadj81jntua --audit-log-arn <arn>
```

## Expect

- There is confirmation question "Are you sure you want to enable audit log forwarding for cluster with the provided role arn 'arn:aws:iam::301721915996:role/yuwan-audit-r'?"
- It succeeds to edit cluster, the cluster spec should contin aws.audit_log.role_arn with the correct value
- The function works well
