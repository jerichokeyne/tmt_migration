# Test

## Step
Log in rosaa-cli with the account which org has NO "capability.organization.hibernate_cluster" label and and feature toggle "hibernation-ga" must be disabled,  
prepare a ready ROSA cluster

## Expect

## Step
Check the help message  
\#rosa -h  
\# rosa hibernate -h  
\# rosa resume -h

## Expect
There should be help message for hibernate/resume cluster.  
[root@yuwan rosa]# ./rosa hibernate -h  
Hibernate Ready cluster  
  
Usage:  
rosa hibernate [command]  
  
Available Commands:  
cluster Hibernate cluster  
  
Flags:  
-h, --help help for hibernate  
--profile string Use a specific AWS profile from your credential file.  
  
Global Flags:  
--debug Enable debug mode.  
  
Use "rosa hibernate [command] --help" for more information about a command.  
[root@yuwan rosa]# ./rosa resume -h  
Resume Hibernate cluster  
  
Usage:  
rosa resume [command]  
  
Available Commands:  
cluster Resume cluster  
  
Flags:  
-h, --help help for resume  
--profile string Use a specific AWS profile from your credential file.  
  
Global Flags:  
--debug Enable debug mode.  
  
Use "rosa resume [command] --help" for more information about a command.  
[root@yuwan rosa]#

## Step
Hibernate/resume the cluster.  
\# rosa hibernate cluster -c <cluster_id>  
\# rosa resume cluster -c <cluster_id>

## Expect
E: Failed to update cluster: The 'capability.organization.hibernate_cluster' capability is not set for org '1OAqHo0k19kyq7Xt7I1Zqb8Ok4K'  
E: Failed to update cluster: The 'capability.organization.hibernate_cluster' capability is not set for org '1OAqHo0k19kyq7Xt7I1Zqb8Ok4K'

## Step
Add the the "capability.organization.hibernate_cluster" label

## Expect

## Step
Hibernate the cluster.  
\# rosa hibernate cluster -c <cluster_id>

## Expect
1.It should succeed without any error.  
2.The cluster status should be changed to 'hibernating' both by API and UI  
3. Log in HIVE and check the ClusterDeployments.powerState field should be set "Hibernating"  
4.Bellow actions should be prohibited, and return some readable message.  
Delete/update cluster.  
Create/update/delete IDP.  
Create/update/delete addon.  
Create/update/delete an additional machinepool.  
Create/update/delete upgrade schedule policy.  
Create/delete dedicated admin and cluster admin.  
5. The cluster console cannot be logged in   
  
[root@yuwan rosa]# ./rosa hibernate cluster -c yunjiang-zy3  
I: Hibernation is a Technical Preview feature subject to the terms listed in https://access.redhat.com/articles/7012966  
? Do you want to proceed with hibernation by accepting to the Technical Preview terms? Yes  
I: You will be reminded to resume the cluster within next 60 days in order to avoid resume failures  
I: Cluster 'yunjiang-zy3' is hibernating. (OCM-2134)  
  
[root@yuwan rosa]# ./rosa describe cluster -c 1lvdag5reavir50prlpo16q52h18biqm  
Name: yuwan-0716-sr1  
ID: 1lvdag5reavir50prlpo16q52h18biqm  
External ID: bb296ef2-4d19-4b53-98d4-3ac8e38e97f6  
OpenShift Version: 4.7.19  
Channel Group: stable  
DNS: yuwan-0716-sr1.opsw.s2.devshift.org  
AWS Account: 301721915996  
API URL: https://api.yuwan-0716-sr1.opsw.s2.devshift.org:6443  
Console URL: https://console-openshift-console.apps.yuwan-0716-sr1.opsw.s2.devshift.org  
Region: us-east-1  
Multi-AZ: false  
Nodes:  
- Master: 3  
- Infra: 2  
- Compute: 2  
Network:  
- Service CIDR: 172.30.0.0/16  
- Machine CIDR: 10.0.0.0/16  
- Pod CIDR: 10.128.0.0/14  
- Host Prefix: /23  
State: powering_down  
Private: No  
Created: Jul 16 2021 06:12:20 UTC  
Details Page: https://qaprodauth.cloud.redhat.com/openshift/details/s/1vNwdCDkxUJLd4zBoOckOYWan86  
NOTE:The cluster status should be powering_down --> hibernating

## Step
During the cluster hibernating

## Expect

## Step
Reume the cluster.  
\# rosa resume cluster -c <cluster_id>

## Expect
1.It should succeed without any error.And the cluster should be back ready  
2.The cluster status should be changed to 'ready' both by API and UI  
3. Log in HIVE and check the ClusterDeployments.powerState field should be set "Running"  
4.Bellow actions should be allowed  
Delete/update cluster.  
Create/update/delete IDP.  
Create/update/delete addon.  
Create/update/delete an additional machinepool.  
Create/update/delete upgrade schedule policy.  
Create/delete dedicated admin and cluster admin.  
5. The cluster console can be logged in

## Step
Try to hibernate the cluster not in the status of 'ready'

## Expect
E: Hibernating a cluster is only supported for 'Ready' clusters. Cluster '1lvdag5reavir50prlpo16q52h18biqm' is in 'hibernating' state

## Step
To hibernate the cluster which has a schedule upgrade policy

## Expect
It should failed with error message like "Moving yuwan-stsui1111 cluster to Hibernating state is not possible while there is a scheduled cluster upgrade"

## Step
Try to resume the cluster not in the status of 'hibernating'

## Expect
E: Resuming a cluster from hibernation is only supported for clusters in 'Hibernating' state. Cluster '1lvdag5reavir50prlpo16q52h18biqm' is in 'ready' state

## Step
Create rosa clusters then install one addon with some external resource.  
“NOTE : hosted-cp doesn't support for addon installation as of now, skip this addon installation step for hosted-cp”  
Find an addon which "has_external_resources":true to install.  
classic and hosted-cp clusters when hosted-cp supports addon installation.

## Expect

## Step
Delete the clusters when it is in the status of 'hibernating/powering down/resuming'.

## Expect
It should failed

## Step
Delete the cluster with best-effort when they are in the status of 'hibernating/powering down/resuming'.  
\# rosa delete cluster -c <cluster_id> --best-effort

## Expect
clusters can be deleted immediately
