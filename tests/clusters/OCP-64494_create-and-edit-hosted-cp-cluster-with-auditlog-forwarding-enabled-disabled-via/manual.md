# Test

## Step
Create a BYO OIDC config

## Expect

## Step
Prepare a role on aws for audit feature <https://access.redhat.com/solutions/7002219>

## Expect

## Step
Check the help message  
\# rosa create cluster -h  
\# rosa edit cluster -h

## Expect
-audit-log-arn string The ARN of the role that is used to forward audit logs to AWS CloudWatch.

## Step
Create hosted-cp cluster in the interactive mode

## Expect
- There is the question "? Audit log forwarding role ARN" to ask for the arn value and the ? help message is "? The ARN of the role that is used to forward audit logs to AWS CloudWatch."  
- The cluster is created  
- The spec of the cluster on CS should contain bellow configure.  
- The function should work well  
.....  
"aws": {  
"audit_log": {  
"role_arn": <role arn>  
}  
.....  
  
$ aws logs describe-log-streams --log-group-name ocm-staging-24bju1p8cglgo8rli1ugbjadj81jntua-yuwan-uaud1 --region us-west-2  
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
(TBD) there is one field to show the audit log enable/disable and the audit role.

## Step
Edit the cluster to disable audit log forwarding in the interactive mode  
\# rosa edit cluster -i

## Expect
- there is question "? Update existing audit log forwarding role 'arn:aws:iam::301721915996:role/yuwan-audit-r': (y/N) " and "? Audit log forwarding role ARN" to input the value  
- (TBD) input "" to disable the audit log forwarding  
- There is INFO "I: Updated cluster '24bju1p8cglgo8rli1ugbjadj81jntua'"  
- Choose yes, then the audit log forwarding is disabled, checking the cluster spec, it should be like bellow:  
.....  
"aws": {  
"audit_log": {  
"role_arn": ""  
}  
.....  
  
TO disable it:  
- There should be "Disable Audit Log (optional):" after input N at "Update existing audit log forwarding role 'arn:aws:iam::301721915996:role/yuwan-audit-r2"

## Step
Edit the cluster to enable audit log forwarding in the interactive mode  
\# rosa edit cluster -i

## Expect
- There is INFO "I: Updated cluster '24bju1p8cglgo8rli1ugbjadj81jntua'"  
- It succeeds to edit cluster, the cluster spec should contin aws.audit_log.role_arn with the correct value  
- The function works well

## Step
Check the validation of the audit-log-arn:  
- the role'd trust relationship is without the correct oidc provider url  
- the arn is not existed  
- the arn is in incorrect format  
- the role's trust relationship is not same with the one of the cluster  
- the cluster is not hosted-cp cluster

## Expect
There should be readable error message.  
X Sorry, your reply was invalid: "" does not match regular expression ^arn:aws:iam::\d{12}:role/[a-zA-Z0-9_-]+$  
  
E: Audit log forwarding to AWS CloudWatch is only supported for Hosted Control Plane clusters  
E: Expected a valid value for audit log arn matching ^arn:aws:iam::\d{12}:role/[a-zA-Z0-9_-]+$  
  
E: Failed to update cluster: The audit log IAM role provided 'arn:aws:iam::301721915996:role/yuwan-audit-r' failed to be verified  
E: Failed to create cluster: The audit log IAM role provided 'arn:aws:iam::301721915996:role/yuwan-audit-r2sad' failed to be verified
