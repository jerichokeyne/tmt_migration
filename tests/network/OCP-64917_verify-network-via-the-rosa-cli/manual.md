# Test

## Step

1. Check the help message.

```bash
rosa verify -h
rosa verify network -h
```

## Expect

```
Verify resources are configured correctly for cluster install

Usage:
  rosa verify [command]

Available Commands:
  network          Verify Virtual Private Cloud (VPC) subnets are configured correctly
  openshift-client Verify OpenShift client tools
  permissions      Verify AWS permissions are ok for non-AWS Security Token Service (STS) cluster install
  quota            Verify AWS quota is ok for cluster install
  rosa-client      Verify ROSA client tools

Flags:
  -h, --help   help for verify

Global Flags:
      --color string   Surround certain characters with escape sequences to display them in color on the terminal. Allowed options are [auto never always] (default "auto")
      --debug          Enable debug mode.

Use "rosa verify [command] --help" for more information about a command.
```

```
Verify that the Virtual Private Cloud (VPC) subnets are configured correctly.

Usage:
  rosa verify network [flags]

Examples:
  # Verify two subnets
	rosa verify network --subnet-ids subnet-03046a9b92b5014fb,subnet-03046a9c92b5014fb

Flags:
  -c, --cluster string       Name or ID of the cluster.
  -h, --help                 help for network
      --hosted-cp            Run network verifier with hosted control plane platform configuration
  -o, --output string        Output format. Allowed formats are [json yaml]
      --profile string       Use a specific AWS profile from your credential file.
      --region string        Use a specific AWS region, overriding the AWS_REGION environment variable.
      --role-arn string      STS Role ARN with get secrets permission.
  -s, --status-only          Check status of previously submitted subnets.
      --subnet-ids strings   The Subnet IDs to verify. Format should be a comma-separated list.
      --tags strings         Supply custom tags to the network verifier. Tags will default to cluster tags if a cluster is supplied. Tags are comma separated, for example: 'key value, foo bar'
  -w, --watch                Watch network verification progress.

Global Flags:
      --color string   Surround certain characters with escape sequences to display them in color on the terminal. Allowed options are [auto never always] (default "auto")
      --debug          Enable debug mode.
```

## Step

1. Verify the network with subnet IDs.

   Test one subnet ID and multiple subnet IDs. ~~To prepare a subnet ID that fails verification: create a VPC, then add deny rules in VPC Network ACLs (for example, deny port 443) with a rule number less than 100. (Migrate this step to OCP-70370.)~~

```bash
rosa verify network --subnet-ids subnet-0ce53302e769cdc1d --role-arn arn:aws:iam::301721915996:role/as/sdf/yw0705accr1-Installer-Role --region us-west-2
rosa verify network --watch --status-only --subnet-ids subnet-0ce53302e769cdc1d
rosa verify network --watch --status-only --subnet-ids subnet-0d0b68279e57a0e07,subnet-0961ae61201ce0e59,subnet-0f0ac9fef60d8c2f7
```

## Expect

```
I: Verifying the following subnet IDs are configured correctly: [subnet-0ce53302e769cdc1d]
I: subnet-0ce53302e769cdc1d: pending
I: Run the following command to wait for verification to complete:
rosa verify network --watch --status-only --subnet-ids subnet-0ce53302e769cdc1d
I: Verifying the following subnet IDs are configured correctly: [subnet-0ce53302e769cdc1d]
I: subnet-0ce53302e769cdc1d: passed
```

- The information message is shown as above.
- The command to wait for verification is correct.
- The result is returned from CS correctly.
- The status is one of `pending`, `passed`, or `failed`.

```
I: Verifying the following subnet IDs are configured correctly: [subnet-0d0b68279e57a0e07 subnet-0961ae61201ce0e59 subnet-0f0ac9fef60d8c2f7]
I: subnet-0d0b68279e57a0e07: failed Unable to verify egress to: [pull.q1w2.quay.rhcloud.com:443 cart-rhcos-ci.s3.amazonaws.com:443 openshift.org:443 quay.io:443 events.us-west-2.amazonaws.com:443 cloud.redhat.com:443 infogw.api.openshift.com:443 api.openshift.com:443 api.access.redhat.com:443 registry.access.redhat.com:443 sso.redhat.com:443 api.deadmanssnitch.com:443 observatorium.api.openshift.com:443 registry.redhat.io:443 ec2.amazonaws.com:443 route53.amazonaws.com:443 sts.amazonaws.com:443 sts.us-west-2.amazonaws.com:443 http-inputs-osdsecuritylogs.splunkcloud.com:443 elasticloadbalancing.us-west-2.amazonaws.com:443 nosnch.in:443 events.pagerduty.com:443 inputs1.osdsecuritylogs.splunkcloud.com:9997 ocm-quay-production-s3.s3.amazonaws.com:443 iam.amazonaws.com:443 quayio-production-s3.s3.amazonaws.com:443 console.redhat.com:80 tagging.us-east-1.amazonaws.com:443 quay-registry.s3.amazonaws.com:443 mirror.openshift.com:443 ec2.us-west-2.amazonaws.com:443 sso.redhat.com:80 console.redhat.com:443 cert-api.access.redhat.com:443]
```

## Step

1. Verify the network with a cluster ID.

```bash
rosa verify network --cluster ying-hcp-a
```

## Expect

```
I: Verifying the following subnet IDs are configured correctly: [subnet-03399d0847258e86e subnet-0a07b4eaceca39405 subnet-03e7db0cafd0e1f61 subnet-05eae08c0cfbd1e3f subnet-02394f7afd63b20f5 subnet-0be58182739fcb9dd]
I: subnet-03399d0847258e86e: pending
I: subnet-0a07b4eaceca39405: passed
I: subnet-03e7db0cafd0e1f61: pending
I: subnet-05eae08c0cfbd1e3f: passed
I: subnet-02394f7afd63b20f5: pending
I: subnet-0be58182739fcb9dd: passed
I: Run the following command to wait for verification to all subnets to complete:
rosa verify network --watch --status-only --region us-west-2 --subnet-ids subnet-03399d0847258e86e,subnet-0a07b4eaceca39405,subnet-03e7db0cafd0e1f61,subnet-05eae08c0cfbd1e3f,subnet-02394f7afd63b20f5,subnet-0be58182739fcb9dd
```

- ROSA CLI selects the cluster subnets automatically.
- Other results are the same as the subnet-ID verification.
- For an HCP cluster, the platform type is `hostedcluster`.
- For a Classic cluster, the platform type is `AWS`.

## Step

1. Verify the network with subnet IDs and a tag.

```bash
rosa verify network --subnet-ids subnet-0ce53302e769cdc1d --role-arn <arn> --region us-west-2 --tags t2:v2
```

## Expect

- The tags are set in the response with the default tags.

```json
"tags": {
  "Name": "osd-network-verifier",
  "osd-network-verifier": "owned",
  "red-hat-managed": "true",
  "t2": "v2"
}
```

- The tags are set on the AWS verifier instance.

## Step

1. Verify the network with a cluster ID and a tag.

```bash
rosa verify network --cluster <> --tags t2:v2
```

## Expect

- The tags are set in the response with the default tags.
- Tags include the default tags, `cluster.aws.tags`, and custom tags added through OCM.
- The tags are set on the AWS verifier instance.

## Step

1. Verify network with subnet IDs with and without `--hosted-cp`.

## Expect

- With `--hosted-cp`, the platform type is `hostedcluster`: `"platform": "aws-hosted-cp"`.
- Without `--hosted-cp`, the platform type is `aws`: `"platform": "aws-classic"`.

## Step

1. Check `--status-only`, `--watch`, and `--region`.

## Expect

- `--status-only` returns the status of previously submitted subnets.
- If no query was previously submitted, it prints `I: subnet-0931cb67194a01f74: Network verification for subnet 'subnet-0931cb67194a01f74' not found`.
- The verifier checks subnet IDs in the `--region` or in the configured default region when the flag is not set.
- `--watch` waits for verification progress and returns the final status.

## Step

1. Repeat the steps on Windows, macOS, and Linux.

## Expect

- The function works correctly.
- The output displays correctly.
