# Test

## Step
Prepare s3 and cloudwatch on AWS and IAM role for testing.  
<https://access.redhat.com/solutions/7002219>

## Expect

## Step
Create hosted-cp cluster with --log-fwd-config flag.  
- yaml config only contains cloudwatch  
- yaml config only contains s3  
- yaml config contains both cloudwatch and s3  
  
- for each log forwarders, use one group  
- for each log forwarders, use multiple groups  
- for each log forwarders, use one application  
- for each log forwarders, use multiple applications  
  
yaml example:  
cloudwatch:  
cloudwatch_log_role_arn: "arn:aws:iam::090777400063:role/yuwan1211cwr"  
cloudwatch_log_group_name: "yuwan1211cwlp"  
applications: ["kube-scheduler", "certified-operators-catalog"]  
groups: ["authentication", "api"]  
s3:  
s3_config_bucket_name: "yuwan1211s3buw2"  
s3_config_bucket_prefix: "test/logf/yuwan1211h2"  
applications: ["kube-scheduler", "certified-operators-catalog"]  
groups: ["authentication", "api"]

## Expect
- The cluster should be created successfully  
- the log forwarding can check by `rosa list/describe log-forwarding` command, the result should be same as the config  
\-

## Step
Check validations:  
- invalid field in the yaml file  
- invalid format of the elements in the yaml file  
- not-supported applications or group   
  
- without cloudwatch_log_role_arn  
- without cloudwatch_log_group_name  
- without s3_config_bucket_name  
- without groups  
  
- use not-existed s3_config_bucket_name

## Expect
- E: error parsing log forwarder config '/Users/yuwan/workplace/temp/s3cloudwatch1.yaml': yaml: unmarshal errors  
  
- E: error parsing log forwarder config '/Users/yuwan/workplace/temp/s3cloudwatch1.yaml': yaml: unmarshal errors  
  
- E: Failed to create cluster: status is 400, identifier is '400', code is 'CLUSTERS-MGMT-400', at '2025-12-11T08:10:37Z' and operation identifier is '67e0713c-8dc2-4e36-b606-a8e3baba3ae3': Validation failed for log forwarder 0: Invalid group provided in log forwarder configuration: 'authentication,api'  
  
- E: Failed to create cluster: status is 400, identifier is '400', code is 'CLUSTERS-MGMT-400', at '2025-12-11T09:01:15Z' and operation identifier is 'bc6ea573-eede-4997-8514-503ffe17b7ff': Validation failed for log forwarder 0: CloudWatch log distribution role ARN is required  
- E: Failed to create cluster: status is 400, identifier is '400', code is 'CLUSTERS-MGMT-400', at '2025-12-11T09:03:36Z' and operation identifier is '2f63c7c0-f3a4-4940-af80-e5c4269bdf76': Validation failed for log forwarder 0: CloudWatch log group name is required  
- E: Failed to create cluster: status is 400, identifier is '400', code is 'CLUSTERS-MGMT-400', at '2025-12-11T09:07:43Z' and operation identifier is '3192b0eb-17ba-4427-9f58-5160d26d1f2c': Validation failed for log forwarder 0: S3 bucket name is required  
  
  
  
- E: Failed to create cluster: status is 400, identifier is '400', code is 'CLUSTERS-MGMT-400', at '2025-12-11T09:05:25Z' and operation identifier is '84de57d0-7f1f-4ede-974b-0b3e907322ce': Validation failed for log forwarder 0: Invalid group provided in log forwarder configuration: ''  
  
- E: Failed to create cluster: status is 400, identifier is '400', code is 'CLUSTERS-MGMT-400', at '2025-12-12T06:55:34Z' and operation identifier is '0465f68a-94ec-4e13-abd9-2a9190ca5396': Validation failed for log forwarder 0: S3 bucket 'yuwan1211s3buw2' does not exist or is not accessible: Failed to reach bucket 'yuwan1211s3buw2'
