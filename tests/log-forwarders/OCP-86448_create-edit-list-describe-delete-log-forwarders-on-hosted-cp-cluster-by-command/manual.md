# Test

## Step
1. Prepare S3 and CloudWatch on AWS and an IAM role for testing.

<https://access.redhat.com/solutions/7002219>

## Expect

## Step
2. Create a hosted-cp cluster with S3 and CloudWatch `log-fwd-config`.

## Expect
- The cluster should be created successfully.

## Step
3. List log forwarders.

```bash
rosa list log-forwarders -c 2n7af4dqcl4974cfi0ihv1v2juhvdu98
```

## Expect
```
ID                            TYPE        STATUS
2n7af5bhorhlrguqh5hovtnen0l6p9pr  S3          ready
2n7af59a8kv3m3btfh64vbl5198lh4tk  CloudWatch  ready
```

```bash
rosa list log-forwarders -h
```

```
List log forwarders configured on a cluster, given a cluster ID

Usage:
  rosa list log-forwarders -c <cluster-id> [flags]

Aliases:
  log-forwarders, logforwarders, log-forwarder, logforwarder

Examples:
  # List all log forwarders on a cluster named "mycluster": rosa list log-forwarders --cluster=mycluster

Flags:
  -c, --cluster string   Name or ID of the cluster.
  -h, --help             help for log-forwarders
  -o, --output string    Output format. Allowed formats are [json yaml]

Global Flags:
      --color string     Surround certain characters with escape sequences to display them in color on the terminal. Allowed options are [auto never always] (default "auto")
      --debug            Enable debug mode.
      --profile string   Use a specific AWS profile from your credential file.
      --region string    Use a specific AWS region, overriding the AWS_REGION environment variable. (DEPRECATED: Region flag will be removed from this command in future versions)
```

- Both S3 and CloudWatch log forwarders are listed with the above fields.
- If there is no log forwarder, reports `I: There are no log forwarders configured for cluster '2n7ccjndd7p7dvdmu787f600m4gv6hte'`.

## Step
4. Describe a log forwarder.

```bash
rosa describe log-forwarder -h
```

## Expect
```
Show details of a specific log forwarder used by a cluster

Usage:
  rosa describe log-forwarder [flags]

Examples:
rosa describe log-forwarder <log_fwd_id> -c mycluster-hcp

Flags:
  -c, --cluster string         Name or ID of the cluster.
  -h, --help                   help for log-forwarder
      --log-forwarder string   Log forwarder ID of the cluster to target
  -o, --output string          Output format. Allowed formats are [json yaml]

Global Flags:
      --color string     Surround certain characters with escape sequences to display them in color on the terminal. Allowed options are [auto never always] (default "auto")
      --debug            Enable debug mode.
      --profile string   Use a specific AWS profile from your credential file.
      --region string    Use a specific AWS region, overriding the AWS_REGION environment variable.
```

- For CloudWatch log forwarder, the following fields have correct values:

```bash
rosa describe log-forwarder 2n6ifmg0i5h5l67pp1ceqnr832rd4hgu -c 2n6ifln475lv578p11fhcr4jjd9s1cp7
```

```
Cloudwatch Log Group Name: yuwan1215cwlp
Cloudwatch Log Distribution Role Arn: arn:aws:iam::090777400063:role/yuwan1215lgr
Applications: kube-scheduler certified-operators-catalog
Groups: (api,v1.0) (authentication,v1.0)
Status Message: Log forwarding configuration has been applied successfully
Resolved Applications: audit-webhook certified-operators-catalog ignition-server konnectivity-agent kube-apiserver kube-scheduler oauth-openshift openshift-apiserver openshift-oauth-apiserver packageserver validation-webhook
```

- For S3 log forwarder, the following fields have correct values:

```bash
rosa describe log-forwarder 2n6ifmj56i1dqek6i4skutveevqvips8 -c 2n6ifln475lv578p11fhcr4jjd9s1cp7
```

```
S3 Bucket Prefix: rosa/test/logforwarder
S3 Bucket Name: yuwan1215s3b
Applications: kube-scheduler certified-operators-catalog
Groups: (api,v1.0)
Status Message: Log forwarding configuration has been applied successfully
Resolved Applications: audit-webhook certified-operators-catalog kube-apiserver
```

- If the log forwarder ID does not exist, reports `E: failed to get log forwarder '2n7af59a8kv3m3btfh64vbl5198lh4tkaa'`.

## Step
5. Edit log forwarders with the `--log-fwd-config` flag.

- Update applications and groups.
- Update `cloudwatch_log_role_arn`, `cloudwatch_log_group_name`, `s3_config_bucket_name`, and `s3_config_bucket_prefix`.

YAML example:

```yaml
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
```

## Expect
- It should update successfully.
- Check the result with `rosa describe log-forwarder`; the result should be expected.

## Step
6. Check validations for editing.

- In the YAML file, omit required `cloudwatch_log_role_arn`, `cloudwatch_log_group_name`, or `s3_config_bucket_name`.
- Omit applications or groups.
- Use a different cloud forwarder type of struct to update.
- Use a role or S3 name that does not exist.

## Expect
```
E: failed to edit log forwarder '2n6ifmg0i5h5l67pp1ceqnr832rd4hgu' for cluster '2n6ifln475lv578p11fhcr4jjd9s1cp7': status is 400, identifier is '400', code is 'CLUSTERS-MGMT-400', at '2025-12-15T07:10:55Z' and operation identifier is '861308a2-ec4a-4efe-a397-862412aab58d': CloudWatch log distribution role ARN is required

E: failed to edit log forwarder '2n6ifmg0i5h5l67pp1ceqnr832rd4hgu' for cluster '2n6ifln475lv578p11fhcr4jjd9s1cp7': status is 400, identifier is '400', code is 'CLUSTERS-MGMT-400', at '2025-12-15T06:44:55Z' and operation identifier is '7a419376-9891-46d6-80f8-ed11bbdc8b4d': At least one application or group must be specified for log forwarding

E: failed to edit log forwarder '2n6ifmg0i5h5l67pp1ceqnr832rd4hgu' for cluster '2n6ifln475lv578p11fhcr4jjd9s1cp7': status is 400, identifier is '400', code is 'CLUSTERS-MGMT-400', at '2025-12-15T07:10:36Z' and operation identifier is '9576ebd7-5492-4d14-8b85-e1ec47f9d737': Cannot change log forwarder type. Please delete the existing log forwarder and create a new one.

E: failed to edit log forwarder '2n6ifmg0i5h5l67pp1ceqnr832rd4hgu' for cluster '2n6ifln475lv578p11fhcr4jjd9s1cp7': status is 400, identifier is '400', code is 'CLUSTERS-MGMT-400', at '2025-12-15T07:19:34Z' and operation identifier is 'd69ba401-545b-41f3-9416-e3b4c00b13d2': Log distribution role does not exist or is not accessible: Failed to find provided role
```

## Step
7. Delete a log forwarder.

```bash
rosa delete log-forwarder -h
```

## Expect
```
Delete a log forwarder from a cluster.

Usage:
  rosa delete log-forwarder -c <cluster-id> <log-forwarder-id> [flags]

Aliases:
  log-forwarder, log_forwarder, log-forwarder, logforwarder

Examples:
  # Delete log forwarder with ID 'example-id' from a cluster named 'mycluster-hcp'
  rosa delete log-forwarder --cluster=mycluster-hcp example-id

Flags:
  -c, --cluster string         Name or ID of the cluster.
  -h, --help                   help for log-forwarder
      --log-forwarder string   Log forwarder ID to delete
  -y, --yes                    Automatically answer yes to confirm operation.

Global Flags:
      --color string     Surround certain characters with escape sequences to display them in color on the terminal. Allowed options are [auto never always] (default "auto")
      --debug            Enable debug mode.
      --profile string   Use a specific AWS profile from your credential file.
      --region string    Use a specific AWS region, overriding the AWS_REGION environment variable. (DEPRECATED: Region flag will be removed from this command in future versions)
```

```bash
rosa delete log-forwarder -c 2n7af4dqcl4974cfi0ihv1v2juhvdu98 2n7af5bhorhlrguqh5hovtnen0l6p9pr
rosa delete log-forwarder -c 2n7af4dqcl4974cfi0ihv1v2juhvdu98 2n7af5bhorhlrguqh5hovtnen0l6p9pr -y
```

```
? Are you sure you want to delete log forwarder '2n7af5bhorhlrguqh5hovtnen0l6p9pr'?? (y/N)
I: Successfully deleted log forwarder '2n7af5bhorhlrguqh5hovtnen0l6p9pr' from cluster '2n7af4dqcl4974cfi0ihv1v2juhvdu98'
```

- The log forwarder should be deleted successfully.
- The deleted one will not display in the result of `rosa list/describe log-forwarder`.
- Deleting a non-existent one reports `E: log forwarder '2n7af5bhorhlrguqh5hovtnen0l6p9praa' not found`.

## Step
8. Delete all log forwarders, then create new ones.

- Create both S3 and CloudWatch log forwarders.
- Create one of S3 and CloudWatch log forwarder.
- Create a new one when a log forwarder already exists.

## Expect
- The new log forwarder should be created.

```bash
rosa create log-forwarder -c 2n7af4dqcl4974cfi0ihv1v2juhvdu98 --log-fwd-config ./s3cw.yaml
```

```
I: Successfully created log forwarder for HCP cluster '2n7af4dqcl4974cfi0ihv1v2juhvdu98'

E: failed to create log forwarder: status is 409, identifier is '409', code is 'CLUSTERS-MGMT-409', at '2025-12-16T09:07:18Z' and operation identifier is 'db6ee3dd-4171-420e-abad-12ddbde27eaa': A log forwarder of type 's3' already exists for this cluster. Only one log forwarder per type is allowed.
```
