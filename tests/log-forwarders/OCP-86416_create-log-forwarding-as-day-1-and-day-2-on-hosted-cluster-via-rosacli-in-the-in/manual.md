# Test

## Step
Prepare s3 and cloudwatch on AWS and IAM role for testing.  
<https://access.redhat.com/solutions/7002219>

## Expect

## Step
Check the help message of `rosa create cluster -h`

## Expect
--log-fwd-config string A path to a log forwarding config file. This should be a YAML file with the following structure:  
  
cloudwatch:  
cloudwatch_log_role_arn: "role_arn_here"  
cloudwatch_log_group_name: "group_name_here"  
applications: ["example_app_1", "example_app_2"]  
groups: "group-name"  
s3:  
s3_config_bucket_name: "bucket_name_here"  
s3_config_bucket_prefix: "bucket_prefix_here"  
applications: ["example_app_1", "example_app_2"]  
groups: "group-name"  
  
  
Please use interactive mode and enter '?' on the associated prompts to get the up to date lists for allowed Applications and allowed Groups

## Step
Create hosted-cp cluster in the interactive mode  
  
- Configure both or one of cloudwatch and s3  
- one or multiple groups for cloudwatch and s3  
- one or multiple or empty application for cloudwatch and s3

## Expect
- There is a question of "? Enabled log forwarding (optional, choose 'Skip' to skip selection; ):" and has bellow four options  
? Enabled log forwarding (optional, choose 'Skip' to skip selection; ): [Use arrows to move, type to filter]  
> Skip  
CloudWatch  
S3  
Both  
  
CloudWatch:  
- If choose "CloudWatch" or "Both", there will be "? CloudWatch Log forwarding role ARN:" and "? CloudWatch log group name: " questions to ask to input . and they are required inputs.  
- Then there will be a list of "? CloudWatch Log forwarding pod groups:" to ask to choose, at this option, none or **one or multiple** group can be selected.  
- If there is group selected, the "? CloudWatch Log forwarding applications " option should be required, or it should be optional  
? CloudWatch Log forwarding role ARN: arn:aws:iam::090777400063:role/yuwan1211cwr  
? CloudWatch log group name: yuwan1211cwlp  
? CloudWatch Log forwarding pod groups: [Use arrows to move, space to select, <right> to all, <left> to none, type to filter, ? for more help]  
> [ ] api  
[ ] authentication  
[ ] controller manager  
[ ] scheduler  
- Then a question of "? CloudWatch Log forwarding applications (optional): " comes, it is an optional field  
  
S3:  
- If choose "S3" or "Both", there will be "? CloudWatch Log forwarding applications (optional): " and required "? S3 Bucket name: " questions to ask to input.  
- then "? S3 Log forwarding pod groups:" is asked to select groups, at this option, none or **one or multiple** group can be selected.  
- then an optional question "? S3 Log forwarding applications (optional):" is asked to input  
- If there is group selected, the "? CloudWatch Log forwarding applications " option should be required, or it should be optional  
  
  
The cluster should be created successfully and the log forwarding configurations should work.

## Step
Create one hosted-cp cluster then create log forwarders as day-2 in the interactive mode

## Expect
- The prompted questions should be same with the one in step3  
- The S3 and cloudwatch log forwarders should be created successfully
