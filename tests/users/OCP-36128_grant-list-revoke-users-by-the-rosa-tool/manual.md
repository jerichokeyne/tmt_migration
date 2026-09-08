# Test

## Step
Login the rosa tool and prepare one ROSA cluster

## Expect

## Step
Try to list the user when there is no one.  
\#rosa list user -c <cluster_id>  
Check the exit code of the last command  
echo $?

## Expect
~~W: There are no users configured for cluster '<cluster_id>' ~~I: There are no users configured for cluster 'aaraj-hcp' (OCM-4806)  
The exit code must be  
$ echo $?  
0

## Step
Check the help message for the 'grant' and 'revoke' command.  
\# rosa -h

## Expect
.....  
grant Grant role to a specific resource  
.....  
revoke Revoke role from a specific resource

## Step
Check the grant help message.  
\#rosa grant -h  
\#rosa grant user -h

## Expect
\# ./rosa grant -h  
Grant role to a specific resource  
  
Usage:  
rosa grant [command]  
  
Available Commands:  
user Grant user access to cluster  
  
Flags:  
-h, --help help for grant  
-i, --interactive Enable interactive mode.  
  
Global Flags:  
--debug Enable debug mode.  
--profile string Use a specific AWS profile from your credential file.  
-v, --v Level log level for V logs  
  
Use "rosa grant [command] --help" for more information about a command.  
\#./rosa grant user -h  
Grant user access to cluster under a specific role  
  
Usage:  
rosa grant user ROLE [flags]  
  
Aliases:  
user, role  
  
Examples:  
\# Add cluster-admin role to a user  
rosa grant user cluster-admin --user=myusername --cluster=mycluster  
  
\# Grant dedicated-admins role to a user  
rosa grant user dedicated-admin --user=myusername --cluster=mycluster  
  
Flags:  
-c, --cluster string Name or ID of the cluster to add the IdP to (required).  
-h, --help help for user  
-u, --user string Username to grant the role to (required).  
  
Global Flags:  
--debug Enable debug mode.  
-i, --interactive Enable interactive mode.  
--profile string Use a specific AWS profile from your credential file.  
-v, --v Level log level for V logs

## Step
Try to grant user access to cluster with illegal parameters.  
1. grant with the incorrect role  
2. grant with the not-existed cluster id  
3. grant with the name of 'cluster-admin'  
4. grant with the existed user name

## Expect
1.  
E: Expected at least one of [cluster-admins dedicated-admins]  
E: Failed to grant 'haha' to user 'tuser' to cluster '1gnbgde6b1vpbg7tf4nbjsipesi0ulu7': Group 'haha' does not exist on cluster '1gnbgde6b1vpbg7tf4nbjsipesi0ulu7'  
2.  
E: Failed to get cluster '1gnbgde6b1vpbg7tf4nbjsipesi0ulu711': There is no cluster with identifier or name '1gnbgde6b1vpbg7tf4nbjsipesi0ulu711'  
3.E: username 'cluster-admin' isn't valid  
4.E: Failed to grant 'cluster-admins' to user 'ca1' to cluster '1gnbgde6b1vpbg7tf4nbjsipesi0ulu7': User 'ca1' already exists on group 'cluster-admins' for cluster '1gnbgde6b1vpbg7tf4nbjsipesi0ulu7'

## Step
Try to grant user access with the correct parameter.  
\#rosa grant user cluster-admin --user=myusername --cluster=mycluster  
\#rosa grant user dedicated-admin --user=myusername --cluster=mycluster

## Expect
The user access should be added.  
Login the cluster console, the users are added under the groups.

## Step
List the users with a not-existed cluster_id.

## Expect
\# ./rosa list user -c 1111  
E: Failed to get cluster '1111': There is no cluster with identifier or name '1111'

## Step
List the users.

## Expect
\# ./rosa list user -c 1gnbgde6b1vpbg7tf4nbjsipesi0ulu7  
ID GROUPS  
yuwan-test cluster-admins  
ca1 cluster-admins  
dt1 dedicated-admins

## Step
Try to revoke the user access with illegal parameters.  
1. revoke with the incorrect role  
2. revoke with the not-existed cluster id  
3. revoke with the no-existed user

## Expect
1.  
\# ./rosa revoke user haha -u ca1 -c 1gnbgde6b1vpbg7tf4nbjsipesi0ulu7  
E: Expected at least one of [cluster-admins dedicated-admins]  
? Are you sure you want to revoke role haha from user ca1 in cluster 1gnbgde6b1vpbg7tf4nbjsipesi0ulu7? (y/N) y  
? Are you sure you want to revoke role haha from user ca1 in cluster 1gnbgde6b1vpbg7tf4nbjsipesi0ulu7? Yes  
E: Failed to revoke 'haha' from user 'ca1' in cluster '1gnbgde6b1vpbg7tf4nbjsipesi0ulu7': Failed to delete user 'ca1' from group 'haha' on cluster '1gnbgde6b1vpbg7tf4nbjsipesi0ulu7': Group 'haha' does not exist on cluster '1gnbgde6b1vpbg7tf4nbjsipesi0ulu7'  
2.  
\# ./rosa revoke user cluster-admins -u ca1 -c 1gnbgde6b1vpbg7tf4nbjsipesi0ul   
E: Failed to get cluster '1gnbgde6b1vpbg7tf4nbjsipesi0ul': There is no cluster with identifier or name '1gnbgde6b1vpbg7tf4nbjsipesi0ul'  
  
3.  
\# ./rosa revoke user cluster-admins -u cano -c 1gnbgde6b1vpbg7tf4nbjsipesi0ulu7  
? Are you sure you want to revoke role cluster-admins from user cano in cluster 1gnbgde6b1vpbg7tf4nbjsipesi0ulu7? (y/N) y  
? Are you sure you want to revoke role cluster-admins from user cano in cluster 1gnbgde6b1vpbg7tf4nbjsipesi0ulu7? Yes  
E: Failed to revoke 'cluster-admins' from user 'cano' in cluster '1gnbgde6b1vpbg7tf4nbjsipesi0ulu7': Failed to delete user 'cano' from group 'cluster-admins' on cluster '1gnbgde6b1vpbg7tf4nbjsipesi0ulu7': User 'cano' does not exist on group 'cluster-admins' for cluster '1gnbgde6b1vpbg7tf4nbjsipesi0ulu7'

## Step
Revoke the user access with correct parameters.

## Expect
The user access is revoked successfully.  
The user is not in the users list.  
Login the cluster console, the user is not under the group.
