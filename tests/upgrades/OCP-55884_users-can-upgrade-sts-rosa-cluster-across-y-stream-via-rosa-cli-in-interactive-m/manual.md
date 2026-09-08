# Test

## Step
Prepare 4.8.z rosa sts cluster with machinepool which has an upgrade path to 4.9.z using the latest version account-roles, then upgrade the cluster to 4.9.z in the interactive mode and choose manually

## Expect
- All the printed info in the interactive should be correct  
- The prompted aws commands are correct and can be executed successfully  
- The upgrade is scheduled successfully.It can be checked by 'rosa list upgrade'  
- Check the cluster with machinepool upgrade is finished successfully

## Step
Prepare 4.9.z rosa sts cluster  with machinepool  which has an upgrade path to 4.10.z using the latest version account-roles, then upgrade the cluster to 4.10.z in the interactive mode and choose manually  
NOTE: In this steps, the account-roles used for testing should be with the path setting

## Expect
- All the printed info in the interactive should be correct  
- The prompted aws commands are correct and can be executed successfully  
- The prompted aws command should contain the ones to create the new added operator-role and policies for 4.10.z cluster  
- The upgrade is scheduled successfully.It can be checked by 'rosa list upgrade'  
- Check the cluster with machinepool upgrade  is finished successfully

## Step
Prepare 4.10.z rosa sts cluster  with machinepool which has an upgrade path to 4.11.z using the latest version account-roles, then upgrade the cluster to 4.11.z in the manual mode

## Expect
- All the printed info in the interactive should be correct  
- The prompted aws commands are correct and can be executed successfully  
- The upgrade is scheduled successfully.It can be checked by 'rosa list upgrade'  
- Check the cluster with machinepool upgrade  is finished successfully

## Step
Any new version is ready in future, test the cluster  with machinepool upgrade from the latest version in Y-1 stream to the latest Y steam in the manual mode

## Expect
- All the printed info in the interactive should be correct  
- The prompted aws commands are correct and can be executed successfully  
- The upgrade is scheduled successfully.It can be checked by 'rosa list upgrade'  
- Check the cluster with machinepool upgrade is finished successfully
