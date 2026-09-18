# Test

## Step
1. Prepare S3 and CloudWatch on AWS and an IAM role for testing.

<https://access.redhat.com/solutions/7002219>

## Expect

## Step
2. Check the help message of `rosa create cluster -h`.

```bash
rosa create cluster -h
```

## Expect
```
--log-fwd-config string                                  A path to a log forwarding config file. This should be a YAML file with the following structure:

                                                       cloudwatch:
                                                         cloudwatch_log_role_arn: "role_arn_here"
                                                         cloudwatch_log_group_name: "group_name_here"
                                                         applications: ["example_app_1", "example_app_2"]
                                                         groups: ["group-name", "group_name-2"]
                                                       s3:
                                                         s3_config_bucket_name: "bucket_name_here"
                                                         s3_config_bucket_prefix: "bucket_prefix_here"
                                                         applications: ["example_app_1", "example_app_2"]
                                                         groups: ["group-name"]
```

Please use interactive mode and enter `?` on the associated prompts to get the up-to-date lists for allowed Applications and allowed Groups.

## Step
3. Create a hosted-cp cluster in interactive mode.

- Configure both or one of CloudWatch and S3.
- Use one or multiple groups for CloudWatch and S3.
- Use one, multiple, or no applications for CloudWatch and S3.

## Expect
- There is an `? Enabled log forwarding (optional, choose 'Skip' to skip selection; ):` question with four options:

```
? Enabled log forwarding (optional, choose 'Skip' to skip selection; ): [Use arrows to move, type to filter]
> Skip
CloudWatch
S3
Both
```

- For CloudWatch or Both, there are required `? CloudWatch Log forwarding role ARN:` and `? CloudWatch log group name:` prompts.
- The `? CloudWatch Log forwarding pod groups:` prompt allows no, one, or multiple groups.
- If a group is selected, the `? CloudWatch Log forwarding applications` option should be required; otherwise it should be optional.

```
? CloudWatch Log forwarding role ARN: arn:aws:iam::090777400063:role/yuwan1211cwr
? CloudWatch log group name: yuwan1211cwlp
? CloudWatch Log forwarding pod groups: [Use arrows to move, space to select, <right> to all, <left> to none, type to filter, ? for more help]
> [ ] api
[ ] authentication
[ ] controller manager
[ ] scheduler
```

- Then an optional `? CloudWatch Log forwarding applications (optional):` question appears.
- For S3 or Both, there are `? CloudWatch Log forwarding applications (optional):` and required `? S3 Bucket name:` prompts.
- The `? S3 Log forwarding pod groups:` prompt allows no, one, or multiple groups.
- Then an optional `? S3 Log forwarding applications (optional):` prompt appears.
- If a group is selected, the `? CloudWatch Log forwarding applications` option should be required; otherwise it should be optional.
- The cluster should be created successfully and the log-forwarding configurations should work.

## Step
4. Create one hosted-cp cluster, then create log forwarders as day 2 in interactive mode.

## Expect
- The prompted questions should be the same as in step 3.
- The S3 and CloudWatch log forwarders should be created successfully.
