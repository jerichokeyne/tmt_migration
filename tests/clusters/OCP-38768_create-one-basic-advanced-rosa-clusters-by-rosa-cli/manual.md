# Setup
Prepare the one AWS account which has access to the aws-marketplace.
NOTE: This needs DEV help ask aws people to add the account into the allow-list, and finish the subscription by visiting <https://aws.amazon.com/marketplace/pp?sku=4x332jmtisy0ah995jum4cvva> (See SDA-3011 comments)

# Test

## Step

Log in with t the rosa cli

## Expect

## Step

Try to create a basic single-az rosa cluster in the interactive mode.
```bash
rosa create cluster
```
\#rosa create cluster -i

## Expect

1. All parameter should be prompted correctly
2. All optional fields should be with "(optional)"
3. The interactive mode should work well
4. All the parameter should be with [? for help], the help message should be correct
5. All the default vaule for the parameter should work well
6. The 'invisible characters' in cluster name,like 'tab,space' will be stripped. For example," testcluster " will be treated as 'testcluster'. And the 'invisible characters' in the middle of the cluster name will lead error message
7. It should show the non-interactive command after the interactive mode quits. And all the parameters in the command should be same with the one in the interactive mode
8. The machinetype should be listed with the order of ("category asc"),'https://api.stage.openshift.com/api/clusters_mgmt/v1/machine_types?order=category+asc&page=1&search=cloud_provider.id+%3D+%27aws%27&size=100'" and set m5.xlarge as default one
9. The subnet should contains the subnet_name vpc_id and az info.If the subnet name is empty , it will show as ''
10. (OCM-2118 OCM-3377) If the select version is EOL version and the timestamp is not nil(!ocmVersion.EndOfLifeTimestamp().IsZero() &&
ocmVersion.EndOfLifeTimestamp().Compare(
now.Add(time.Duration(daysAwayToCheck)*OneDayHourDuration*time.Hour)) <= 0
), there will be warning message "W: The version of Red Hat OpenShift Service on AWS that you are installing will no longer be supported after '2023-09-10'. Red Hat recommends selecting a newer version. For more information, see https://docs.openshift.com/rosa/rosa_policy/rosa-life-cycle.html". If the no '-y' confirmation flag is set, there will be question option "? Are you sure you want to continue with version '4.10.63'?" to ask for confirmaion.

11. OCM-22351: There is a question to choose channel,"? OpenShift Channel (optional, choose 'Skip' to skip selection; ): stable-4.21", the prompted list should contain all available channel based on the cluster version

\# ./rosa create cluster
```
I: Enabling interactive mode
? Cluster name: [? for help] foo
? Cluster name: foo
? Domain prefix (optional): [? for help]
? Deploy cluster with Hosted Control Plane: [? for help] (y/N)
? Deploy cluster with Hosted Control Plane: No
? Create cluster admin user: (y/N)
? Create cluster admin user: No
? Deploy cluster using AWS STS: [? for help] (Y/n)
? Deploy cluster using AWS STS: Yes
W: In a future release STS will be the default mode.
W: --sts flag won't be necessary if you wish to use STS.
W: --non-sts/--mint-mode flag will be necessary if you do not wish to use STS.
? OpenShift version (default = '4.13.34'): [Use arrows to move, type to filter, ? for more help]
> 4.13.34
4.15.0
4.14.13
4.14.12
4.14.11
4.14.10
4.14.9
? OpenShift Channel (optional, choose 'Skip' to skip selection; ): stable-4.21
? Configure the use of IMDSv2 for ec2 instances (default = 'optional'): [Use arrows to move, type to filter, ? for more help]
> optional
required
W: More than one Installer role found
? Installer role ARN (default = 'arn:aws:iam::301721915996:role/ManagedOpenShift-Installer-Role'): [Use arrows to move, type to filter, ? for more help]
arn:aws:iam::301721915996:role/aaraj1-Installer-Role
arn:aws:iam::301721915996:role/akanni-Installer-Role
> arn:aws:iam::301721915996:role/ManagedOpenShift-Installer-Role
arn:aws:iam::301721915996:role/osde2e-88k5a-Installer-Role
arn:aws:iam::301721915996:role/QEAuto-OCP-43070-ipno-Installer-Role
arn:aws:iam::301721915996:role/QEAuto-OCP-43070-zhvb-Installer-Role
arn:aws:iam::301721915996:role/QEAuto-OCP-43070auto-krtj-Installer-Role
? External ID (optional): [? for help]
? Operator roles prefix: [? for help] (foo-d9a9)
? Operator roles prefix: foo-d9a9
? Deploy cluster using pre registered OIDC Configuration ID: (Y/n)
? Deploy cluster using pre registered OIDC Configuration ID: Yes
? OIDC Configuration ID (default = '27h3ibknqa225c3n5m871814fq2acf2j | https://ci-op-x7mm5ymk-oidc-v5n3.s3.us-west-2.amazonaws.com'): [Use arrows to move, type to filter, ? for more help]
> 27h3ibknqa225c3n5m871814fq2acf2j | https://ci-op-x7mm5ymk-oidc-v5n3.s3.us-west-2.amazonaws.com
27e0hanfc48269q83ikbdnph2jhv8gkh | https://dvbwgdztaeq9o.cloudfront.net/27e0hanfc48269q83ikbdnph2jhv8gkh
27i2mshnp8qhdjbvqllrbl6vjkgtd7hk | https://dvbwgdztaeq9o.cloudfront.net/27i2mshnp8qhdjbvqllrbl6vjkgtd7hk
27kdvggg46sq0p6o0qh3aqog1q5nc0er | https://dvbwgdztaeq9o.cloudfront.net/27kdvggg46sq0p6o0qh3aqog1q5nc0er
25bigghjl0jcs26gtlvr7j8s7firrmk0 | https://dvbwgdztaeq9o.cloudfront.net/25bigghjl0jcs26gtlvr7j8s7firrmk0
25bigg6c7vdsr7ui9jmb47mt8t7ojjqm | https://dvbwgdztaeq9o.cloudfront.net/25bigg6c7vdsr7ui9jmb47mt8t7ojjqm
27i2oajo5hfo8n6eqocncdp1vffsn65s | https://dvbwgdztaeq9o.cloudfront.net/27i2oajo5hfo8n6eqocncdp1vffsn65s
? Tags (optional): [? for help]
? Multiple availability zones (optional): [? for help] (y/N)
? Multiple availability zones (optional): No
? AWS region: [Use arrows to move, type to filter, ? for more help]
eu-west-3
me-south-1
sa-east-1
us-east-1
> us-east-2
us-west-1
us-west-2
? AWS region: us-east-2
? PrivateLink cluster: [? for help] (y/N)
? PrivateLink cluster: No
? Machine CIDR: [? for help] (10.0.0.0/16)
? Machine CIDR: 10.0.0.0/16
? Service CIDR: [? for help] (172.30.0.0/16)
? Service CIDR: 172.30.0.0/16
? Pod CIDR: [? for help] (10.128.0.0/14)
? Pod CIDR: 10.128.0.0/14
? Install into an existing VPC (optional): [? for help] (y/N) y
? Install into an existing VPC (optional): Yes
? Subnet IDs (optional): [Use arrows to move, space to select, <right> to all, <left> to none, type to filter, ? for more help]
> [ ] subnet-02cb3bbb9a1b2d0b4 ('vprashar-224236-tgzdr-private-us-east-2b','vpc-004c4567177cfd7c2','us-east-2b')
[ ] subnet-07c35fcef49e2395a ('vprashar-224236-tgzdr-public-us-east-2a','vpc-004c4567177cfd7c2','us-east-2a')
[ ] subnet-0e5aa5f9e03862164 ('vprashar-224236-tgzdr-private-us-east-2c','vpc-004c4567177cfd7c2','us-east-2c')
[ ] subnet-0f219e1850ea41ad2 ('vprashar-224236-tgzdr-private-us-east-2a','vpc-004c4567177cfd7c2','us-east-2a')
[ ] subnet-0fe0364ff819f4f1e ('vprashar-224236-tgzdr-public-us-east-2b','vpc-004c4567177cfd7c2','us-east-2b')
[ ] subnet-0fd46e9f50b4feb0e ('vprashar-224236-tgzdr-public-us-east-2c','vpc-004c4567177cfd7c2','us-east-2c')
[ ] subnet-0376ed93e368f81a2 ('minl-aws0809-b6sxq-private-us-east-2b','vpc-0116f969f68f5a12f','us-east-2b')
```

```
? Subnet IDs (optional): [Use arrows to move, space to select, <right> to all, <left> to none, type to filter, ? for more help]
[ ] subnet-051d36c378cd6c6c1 (us-east-2c)
> [ ] subnet-04b778ad42da2bfb2 (us-east-2a)
[ ] subnet-03c68085617dc51a3 (us-east-2c)
[ ] subnet-0d68a86fbfbb6569c (us-east-2c)
[ ] subnet-0bdf42f510c7a454d (us-east-2b)
[ ] subnet-0cff510b670bb3d64 (us-east-2a)
[ ] subnet-06d444960a32709d5 (us-east-2c)
? Subnet IDs (optional):
? Compute nodes instance type (optional): [Use arrows to move, type to filter, ? for more help]
> m5.xlarge
r5.xlarge
m5.2xlarge
c5.2xlarge
r5.2xlarge
m5.4xlarge
c5.4xlarge
? Compute nodes instance type (optional): [Use arrows to move, type to filter, ? for more help]
m5.xlarge
> r5.xlarge
m5.2xlarge
c5.2xlarge
r5.2xlarge
m5.4xlarge
c5.4xlarge
? Compute nodes instance type (optional): [Use arrows to move, type to filter, ? for more help]
> m5.xlarge
r5.xlarge
m5.2xlarge
c5.2xlarge
r5.2xlarge
m5.4xlarge
c5.4xlarge
? Compute nodes instance type (optional): [Use arrows to move, type to filter, ? for more help]
> m5.xlarge
r5.xlarge
m5.2xlarge
c5.2xlarge
r5.2xlarge
m5.4xlarge
c5.4xlarge
? Compute nodes instance type (optional): [Use arrows to move, type to filter, ? for more help]
> m5.xlarge
r5.xlarge
m5.2xlarge
c5.2xlarge
r5.2xlarge
m5.4xlarge
c5.4xlarge
? Compute nodes instance type (optional): m5.xlarge
? Enable autoscaling (optional): [? for help] (y/N)
? Enable autoscaling (optional): No
? Compute nodes: [? for help] (2)
? Compute nodes: 2
? Host prefix: [? for help] (23)
? Host prefix: 23
I: Creating cluster 'foo'
I: To create this cluster again in the future, you can run:
rosa create cluster --cluster-name foo --region us-east-2 --version 4.6.16 --compute-nodes 2 --compute-machine-type m5.xlarge --machine-cidr 10.0.0.0/16 --service-cidr 172.30.0.0/16 --pod-cidr 10.128.0.0/14 --host-prefix 23
I: To view a list of clusters and their status, run 'rosa list clusters'
^C^Z
[12]+ Stopped ./rosa create cluster
[root@yuwan moactl]# ./rosa create cluster
I: Enabling interactive mode
? Cluster name: [? for help] bay
? Cluster name: bay
? Multiple availability zones (optional): [? for help] (y/N)
? Multiple availability zones (optional): No
? AWS region: [Use arrows to move, type to filter, ? for more help]
eu-west-3
me-south-1
sa-east-1
us-east-1
> us-east-2
us-west-1
us-west-2
? AWS region: us-east-2
? OpenShift version: [Use arrows to move, type to filter, ? for more help]
> 4.6.16
4.5.11
4.5.16
4.6.1
4.6.12
4.6.13
4.6.15
? OpenShift version: 4.6.16
? Install into an existing VPC (optional): [? for help] (y/N) y
? Install into an existing VPC (optional): Yes
? Subnet IDs (optional): [Use arrows to move, space to select, <right> to all, <left> to none, type to filter, ? for more help]
> [ ] subnet-051d36c378cd6c6c1 (us-east-2c)
[ ] subnet-04b778ad42da2bfb2 (us-east-2a)
[ ] subnet-03c68085617dc51a3 (us-east-2c)
[ ] subnet-0d68a86fbfbb6569c (us-east-2c)
[ ] subnet-0bdf42f510c7a454d (us-east-2b)
[ ] subnet-0cff510b670bb3d64 (us-east-2a)
[ ] subnet-06d444960a32709d5 (us-east-2c)
? Subnet IDs (optional): [Use arrows to move, space to select, <right> to all, <left> to none, type to filter, ? for more help]
[ ] subnet-051d36c378cd6c6c1 (us-east-2c)
> [ ] subnet-04b778ad42da2bfb2 (us-east-2a)
[ ] subnet-03c68085617dc51a3 (us-east-2c)
[ ] subnet-0d68a86fbfbb6569c (us-east-2c)
[ ] subnet-0bdf42f510c7a454d (us-east-2b)
[ ] subnet-0cff510b670bb3d64 (us-east-2a)
[ ] subnet-06d444960a32709d5 (us-east-2c)
? Subnet IDs (optional): [Use arrows to move, space to select, <right> to all, <left> to none, type to filter, ? for more help]
[ ] subnet-051d36c378cd6c6c1 (us-east-2c)
> [x] subnet-04b778ad42da2bfb2 (us-east-2a)
[ ] subnet-03c68085617dc51a3 (us-east-2c)
[ ] subnet-0d68a86fbfbb6569c (us-east-2c)
[ ] subnet-0bdf42f510c7a454d (us-east-2b)
[ ] subnet-0cff510b670bb3d64 (us-east-2a)
[ ] subnet-06d444960a32709d5 (us-east-2c)
? Subnet IDs (optional): [Use arrows to move, space to select, <right> to all, <left> to none, type to filter, ? for more help]
[ ] subnet-051d36c378cd6c6c1 (us-east-2c)
[x] subnet-04b778ad42da2bfb2 (us-east-2a)
> [ ] subnet-03c68085617dc51a3 (us-east-2c)
[ ] subnet-0d68a86fbfbb6569c (us-east-2c)
[ ] subnet-0bdf42f510c7a454d (us-east-2b)
[ ] subnet-0cff510b670bb3d64 (us-east-2a)
[ ] subnet-06d444960a32709d5 (us-east-2c)
? Subnet IDs (optional): [Use arrows to move, space to select, <right> to all, <left> to none, type to filter, ? for more help]
[ ] subnet-051d36c378cd6c6c1 (us-east-2c)
[x] subnet-04b778ad42da2bfb2 (us-east-2a)
> [x] subnet-03c68085617dc51a3 (us-east-2c)
[ ] subnet-0d68a86fbfbb6569c (us-east-2c)
[ ] subnet-0bdf42f510c7a454d (us-east-2b)
[ ] subnet-0cff510b670bb3d64 (us-east-2a)
[ ] subnet-06d444960a32709d5 (us-east-2c)
? Subnet IDs (optional): subnet-04b778ad42da2bfb2 (us-east-2a), subnet-03c68085617dc51a3 (us-east-2c)
? Compute nodes instance type (optional): [Use arrows to move, type to filter, ? for more help]
> m5.xlarge
r5.xlarge
m5.2xlarge
c5.2xlarge
r5.2xlarge
m5.4xlarge
c5.4xlarge
? Compute nodes instance type (optional):
? Enable autoscaling (optional): [? for help] (y/N)
? Enable autoscaling (optional): No
? Compute nodes: [? for help] (2)
? Compute nodes: 2
? Machine CIDR: [? for help] (10.0.0.0/16)
? Machine CIDR: 10.0.0.0/16
? Service CIDR: [? for help] (172.30.0.0/16)
? Service CIDR: 172.30.0.0/16
? Pod CIDR: [? for help] (10.128.0.0/14)
? Pod CIDR: 10.128.0.0/14
? Host prefix: [? for help] (23)
? Host prefix: 23
I: Creating cluster 'bay'
I: To create this cluster again in the future, you can run:
rosa create cluster --cluster-name bay --region us-east-2 --version 4.6.16 --compute-nodes 2 --machine-cidr 10.0.0.0/16 --service-cidr 172.30.0.0/16 --pod-cidr 10.128.0.0/14 --host-prefix 23 --subnet-ids subnet-04b778ad42da2bfb2,subnet-03c68085617dc51a3
I: To view a list of clusters and their status, run 'rosa list clusters'
^Z
[13]+ Stopped ./rosa create cluster
[root@yuwan moactl]# ./rosa create cluster -c yuwan-012345678901234567890
E: Cluster name must consist of no more than 15 lowercase alphanumeric characters or '-', start with a letter, and end with an alphanumeric character.
[root@yuwan moactl]# ./rosa create cluster -c yuwan aa
I: Creating cluster 'yuwan'
I: To view a list of clusters and their status, run 'rosa list clusters'
^C^Z
[14]+ Stopped ./rosa create cluster -c yuwan aa
[root@yuwan moactl]# ./rosa create cluster
I: Enabling interactive mode
? Cluster name: [? for help] hihi aaa
? Cluster name: hihi aaa
E: Cluster name must consist of no more than 15 lowercase alphanumeric characters or '-', start with a letter, and end with an alphanumeric character.
[root@yuwan moactl]# ./rosa create cluster
I: Enabling interactive mode
? Cluster name: [? for help] ejbdfajejfw
? Cluster name: ejbdfajejfw
? Multiple availability zones (optional): [? for help] (y/N)
? Multiple availability zones (optional): No
? AWS region: [Use arrows to move, type to filter, ? for more help]
eu-west-3
me-south-1
sa-east-1
us-east-1
> us-east-2
us-west-1
us-west-2
? AWS region: us-east-2
? OpenShift version: [Use arrows to move, type to filter, ? for more help]
> 4.6.16
4.5.11
4.5.16
4.6.1
4.6.12
4.6.13
4.6.15
? OpenShift version: 4.6.16
? Install into an existing VPC (optional): [? for help] (y/N)
? Install into an existing VPC (optional): No
? Compute nodes instance type (optional): [Use arrows to move, type to filter, ? for more help]
> m5.xlarge
r5.xlarge
m5.2xlarge
c5.2xlarge
r5.2xlarge
m5.4xlarge
c5.4xlarge
? Compute nodes instance type (optional):
? Enable autoscaling (optional): [? for help] (y/N)
? Enable autoscaling (optional): No
? Compute nodes: [? for help] (2)
? Compute nodes: 2
? Machine CIDR: [? for help] (10.0.0.0/16)
? Machine CIDR: 10.0.0.0/16
? Service CIDR: [? for help] (172.30.0.0/16)
? Service CIDR: 172.30.0.0/16
? Pod CIDR: [? for help] (10.128.0.0/14)
? Pod CIDR: 10.128.0.0/14
? Host prefix: [? for help] (23)
? Host prefix: 23
I: Creating cluster 'ejbdfajejfw'
I: To create this cluster again in the future, you can run:
rosa create cluster --cluster-name ejbdfajejfw --region us-east-2 --version 4.6.16 --compute-nodes 2 --machine-cidr 10.0.0.0/16 --service-cidr 172.30.0.0/16 --pod-cidr 10.128.0.0/14 --host-prefix 23
I: To view a list of clusters and their status, run 'rosa list clusters'
```

```
I: Cluster 'yuwan-0125-sr1' has been created.
I: Once the cluster is installed you will need to add an Identity Provider before you can login into the cluster. See 'rosa create idp --help' for more information.
I: To determine when your cluster is Ready, run 'rosa describe cluster -c yuwan-0125-sr1'.
I: To watch your cluster installation logs, run 'rosa logs install -c yuwan-0125-sr1 --watch'.
Name: yuwan-0125-sr1
OpenShift Version:
DNS: yuwan-0125-sr1.skel.s2.devshift.org
ID: 1ie2qe2q1sejk4e0anhhi7fa4hjuv6a6
External ID:
AWS Account: 301721915996
API URL:
Console URL:
Nodes: Master: 3, Infra: 2, Compute: 2
Region: us-east-2
Multi-AZ: false
State: pending (Preparing account)
Channel Group: stable
Private: No
Created: Jan 25 2021 08:03:06 UTC
Details Page: https://qaprodauth.cloud.redhat.com/openshift/details/1ie2qe2q1sejk4e0anhhi7fa4hjuv6a6
```

- Since OCM-17719, there is no "? Disable Workload monitoring:" option in the interactive mode.(- In M1 of deprecating UWM, the option of UWM still works functionally with rosacli<=1.2.56. In future M2, rosacli 1.2.57, will disable it. there is warning message W: [DEPRECATED FOR ROSA HCP] User workload monitoring (--disable-workload-monitoring) has been deprecated for Hosted Control Plane clusters, and will be removed in a future version of ROSA CLI. Please remove from your workflows to avoid future issues
)

## Step

Try to create a basic single-az rosa cluster with some of parameters in the interactive mode.
\#rosa create cluster -c test-cluster-1 --multi-az --compute-nodes=5 -i

## Expect

The interactive mode should be called up.
All the parameters in the command should be shown as a default value in the interactive mode.
(OCM-2118 OCM-3377) If the select version is EOL version and the timestamp is not nil(!ocmVersion.EndOfLifeTimestamp().IsZero() &&
ocmVersion.EndOfLifeTimestamp().Compare(
now.Add(time.Duration(daysAwayToCheck)*OneDayHourDuration*time.Hour)) <= 0
), there will be warning message "W: The version of Red Hat OpenShift Service on AWS that you are installing will no longer be supported after '2023-09-10'. Red Hat recommends selecting a newer version. For more information, see https://docs.openshift.com/rosa/rosa_policy/rosa-life-cycle.html". If the no '-y' confirmation flag is set, there will be question option "? Are you sure you want to continue with version '4.10.63'?" to ask for confirmaion.
```
[root@yuwan moactl]# ./rosa create cluster -c test-cluster-1 --multi-az --compute-nodes=6 -i
```
I: Interactive mode enabled.
Any optional fields can be left empty and a default will be selected.
? Cluster name: [? for help] (test-cluster-1)
? Cluster name: test-cluster-1
? Multiple availability zones: [? for help] (Y/n)
? Multiple availability zones: Yes
? AWS region: [Use arrows to move, type to filter, ? for more help]
eu-west-3
me-south-1
sa-east-1
us-east-1
```
```bash
us-east-2
```
us-west-1
us-west-2
```
? AWS region: us-east-2
? OpenShift version: [Use arrows to move, type to filter, ? for more help]
```
```bash
4.6.12
```
4. 5.11
4. 5.12
4. 5.13
4. 5.14
4. 5.15
4. 5.16
```
? OpenShift version: 4.6.12
? Install into an existing VPC (optional): [? for help] (y/N)
? Install into an existing VPC (optional): No
? Compute nodes instance type (optional): [Use arrows to move, type to filter, ? for more help]
```
```bash
m5.xlarge
```
r5.xlarge
m5.2xlarge
c5.2xlarge
r5.2xlarge
m5.4xlarge
c5.4xlarge
```
? Compute nodes instance type (optional):
? Enable autoscaling (optional): [? for help] (y/N)
? Enable autoscaling (optional): No
? Compute nodes: [? for help] (6)
? Compute nodes: 6
? Machine CIDR: [? for help] (10.0.0.0/16)
? Machine CIDR: 10.0.0.0/16
? Service CIDR: [? for help] (172.30.0.0/16)
? Service CIDR: 172.30.0.0/16
? Pod CIDR: [? for help] (10.128.0.0/14)
? Pod CIDR: 10.128.0.0/14
.....
```
```

## Step

Try to create a basic single-az rosa cluster by the command with all required parameter.
```bash
rosa create cluster -c <cluster_name>
```

## Expect

The cluster should be created with the default parameter values.

## Step

Try to create a basic single-az rosa cluster by the command with the required parameter(cluster_name) and some optional parameter.

## Expect

The cluster should be created with the input parameter values.

## Step

Try to create a single-az advanced cluster by the command, including bellow parameters:
--cluster-name
--channel-group --version(not the default one)
--compute-machine-type(not the default one)
--enable-autoscaling --min-replicas --max-replicas
--machine-cidr --service-cidr --pod-cidr --host-prefix --private
--disable-scp-checks
--subnet-ids
--tags key1:value1,key2:value2
Add checkpoint for tags OCM-2701: use tags value with space character between multiple tag like --tags="tag-k1:tag-v1, tag-k2:tag-v2" OR --tags="tag-k1 tag-v1, tag-k2 tag-v2"

## Expect

The cluster should be created successfully.
For the tags:
- The tags will be correct in the response.
- There should be tag red-hat-managed=true for all of the resources, including the temporary VPC and Subnet for verifying access to the correct AMI

## Step

Check the install log.

## Expect

Check the install log when cluster in pending/installing status before installation pod start in HIVE.

[xueli@xueli-work tmp]$ rosa logs install -c xueli-rosa3
```
I: Cluster 'xueli-rosa3' is in installing state waiting for installation to begin. Logs will show up within 5 minutes
Wait for 5 mins then check the install log again.
- Installation log will show
- last tail 2000 logs will show
- Logs will be wrapped by lines
Try to get the log from the end of log.
- It will show the last 5 line logs and kept waiting for new logs to show
- New logs will kept outputting when received
- The process won't exit until the cluster installation finished
NOTE:Logs won't show "export KUBECONFIG=/output/auth/kubeconfig" or "REDACTED LINE OF OUTPUT" by the end
Run command to check the ready cluster install log.
xueli@xueli-work tmp]$ rosa logs install -c xueli-rosa
I: Cluster 'xueli-rosa' has been successfully installed
Uninstall the cluster and check the install log of the uninstalling cluster
$ rosa logs install --cluster <cluster id>
I: Cluster 'xueli-rosa' is uninstalling
```

## Step

Repeat all above steps to create a multi-az cluster

## Expect

The result should be same with the above ones

## Step

Create the second cluster with the same user immediately after the first cluster is created:
Log in with the rosa tool with the user1 on env1 and Log in with the rosa tool with the user1 on another env2, then create one rosa cluster on env1 then create another cluster on env2 immediately

## Expect

Two clusters should be created successfully

## Step

Repeat the steps on Windows/MacOS/Linux

## Expect

- The function should work well
- The output should displau well

## Step

Add the capability "capability.organization.classic_rosa_disable" to your organization(OCM-5448)
With capability, Create Classic ROSA cluster
Without capability, Create Classic ROSA cluster

## Expect

It will be successful without capability, Create Classic ROSA cluster
It will be failed with capability, Create Classic ROSA cluster with error message
"E: Failed to create cluster: Creating Classic ROSA clusters capability is disabled"
