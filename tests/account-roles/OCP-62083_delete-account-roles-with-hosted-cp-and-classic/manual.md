# Test

## Step
Create hosted-cp account-roles and classic account-roles with same prefix   
\# rosa create account-roles --prefix ywtest1 --mode auto -y --classic  
\# rosa create account-roles --prefix ywtest1 --mode auto -y --hosted-cp  
  
\# rosa create account-roles --prefix ywtest2 --mode auto -y --classic  
\# rosa create account-roles --prefix ywtest2 --mode auto -y --hosted-cp  
  
\# rosa create account-roles --prefix ywtest3 --mode auto -y --classic  
  
\# rosa create account-roles --prefix ywtest4 --mode auto -y --hosted-cp

## Expect
All account roles are created.

## Step
Delete all account-roles with the prefix  
\# rosa delete account-role --prefix ywtest1  
NOTE:both auto mode and manual mode

## Expect
- The prompted aws commands includes the ones to delete all classic and hypershift account-roles in manual mode  
- All the classic and hypershift account-roles are deleted, and there are message showing the deleted account-roles  
  
I: Deleting classic account roles  
I: Deleting account role 'ywtest1-Installer-Role'  
I: Deleting account role 'ywtest1-ControlPlane-Role'  
I: Deleting account role 'ywtest1-Worker-Role'  
I: Deleting account role 'ywtest1-Support-Role'  
I: Successfully deleted the classic account roles  
I: Deleting hosted CP account roles  
I: Deleting account role 'ywtest1-HCP-Worker-Role'  
I: Deleting account role 'ywtest1-HCP-Installer-Role'  
I: Deleting account role 'ywtest1-HCP-Support-Role'  
I: Successfully deleted the hosted CP account roles

## Step
Delete the classic account-roles  
\# rosa delete account-role --prefix ywtest2 --classic  
NOTE:both auto mode and manual mode

## Expect
- The prompted aws commands includes the ones to delete all classic account-roles in manual mode  
- All the classic account-roles are deleted, and there are message showing the deleted account-roles  
  
I: Deleting classic account roles  
I: Deleting account role 'ywtest11-Support-Role'  
I: Deleting account role 'ywtest11-Installer-Role'  
I: Deleting account role 'ywtest11-ControlPlane-Role'  
I: Deleting account role 'ywtest11-Worker-Role'  
I: Successfully deleted the classic account roles

## Step
Delete the hypershift account-roles  
\# rosa delete account-role --prefix ywtest2 --hosted-cp  
NOTE:both auto mode and manual mode

## Expect
- The prompted aws commands includes the ones to delete all hypershift account-roles in manual mode  
- All the hypershift account-roles are deleted, and there are message showing the deleted account-roles  
  
I: Deleting hosted CP account roles  
I: Deleting account role 'ywtest11-HCP-Installer-Role'  
I: Deleting account role 'ywtest11-HCP-Support-Role'  
I: Deleting account role 'ywtest11-HCP-Worker-Role'  
I: Successfully deleted the hosted CP account roles

## Step
Delete the classic account-roles with the prefix ywtest4

## Expect
W: There are no hosted CP account roles to be deleted

## Step
Delete the hypershift account-roles with the prefix ywtest3

## Expect
W: There are no classic account roles to be deleted

## Step
Delete accout-roles without setting --hosted-cp and --classic flags with the prefix yuwantest3

## Expect
- Only the classic account-roles are deleted  
- There is message to tell no hypershift account-roles deleted  
  
yuwan1-mac:rosa yuwan$ ./rosa delete account-roles --prefix ywtest2 --mode auto -y   
I: Deleting classic account roles  
I: Deleting account role 'ywtest2-Installer-Role'  
I: Deleting account role 'ywtest2-ControlPlane-Role'  
I: Deleting account role 'ywtest2-Worker-Role'  
I: Deleting account role 'ywtest2-Support-Role'  
I: Successfully deleted the classic account roles  
W: There are no hosted CP account roles to be deleted

## Step
Delete accout-roles without setting --hosted-cp and --classic flags with the prefix yuwantest4

## Expect
- Only the hypershift account-roles are deleted  
- There is message to tell no classic account-roles deleted  
W: There are no classic account roles to be deleted  
I: Deleting hosted CP account roles  
I: Deleting account role 'ywtest3-HCP-Installer-Role'  
I: Deleting account role 'ywtest3-HCP-Support-Role'  
I: Deleting account role 'ywtest3-HCP-Worker-Role'  
I: Successfully deleted the hosted CP account roles
