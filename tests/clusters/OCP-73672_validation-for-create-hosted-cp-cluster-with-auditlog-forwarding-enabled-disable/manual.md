# Test

## Step
Check the validation of the audit-log-arn:  
- the role'd trust relationship is without the correct oidc provider url  
- the arn is not existed  
- the arn is in incorrect format  
- the role's trust relationship is not same with the one of the cluster  
- the cluster is not hosted-cp cluster

## Expect
There should be readable error message.  
E: Audit log forwarding to AWS CloudWatch is only supported for Hosted Control Plane clusters  
E: Expected a valid value for audit log arn matching ^arn:aws:iam::\d{12}:role/[a-zA-Z0-9_-]+$  
  
E: Failed to update cluster: The audit log IAM role provided 'arn:aws:iam::301721915996:role/yuwan-audit-r' failed to be verified  
E: Failed to create cluster: The audit log IAM role provided 'arn:aws:iam::301721915996:role/yuwan-audit-r2sad' failed to be verified
