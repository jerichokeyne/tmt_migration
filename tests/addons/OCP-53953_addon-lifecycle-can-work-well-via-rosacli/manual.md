# Setup
Refer OCP-53857 steup

# Test

## Step
Prepare an ROSA cluster

## Expect

## Step
List the addons by command  
$ rosa list addons

## Expect
The addons will be listed correctly  
  
lixue@Xue-Lis-MacBook-Pro Python 3.11 % rosa list addons   
ID NAME AVAILABILITY  
!@# sdqe-testing available  
ocm-addon-test-operator OCM Add-On Test Operator available  
reference-addon Reference Addon available  
managed-api-service-internal Red Hat Openshift API Management (internal) unavailable  
managed-odh Red Hat OpenShift AI available  
managed-api-service Red Hat Openshift API Management available

## Step
Pick one of the addon and describe it

## Expect
The addon details will show correctly  
  
lixue@Xue-Lis-MacBook-Pro Python 3.11 % rosa describe addon managed-odh   
ADD-ON  
ID: managed-odh  
Name: Red Hat OpenShift AI  
Description: Install and configure the Red Hat OpenShift AI service.  
Documentation: https://access.redhat.com/documentation/en-us/red_hat_openshift_data_science  
Operator: rhods-operator  
Target namespace: redhat-ods-operator  
Install mode: all_namespaces  
  
  
ADD-ON PARAMETERS  
- ID: notification-email  
Name: Notification email  
Description: Enter one or more email addresses, separated by a comma. The email addresses  
entered here will receive relevant alerts about the service.  
Type: string  
Required: yes  
Editable: yes  
Validation: /^(?:[a-z0-9!#$%&'*+=?^_`{|}~-]+(?:\\.[a-z0-9!#$%&'*+=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\\])(,\s*(?:[a-z0-9!#$%&'*+=?^_`{|}~-]+(?:\\.[a-z0-9!#$%&'*+=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\\])){0,}$/

## Step
List the addons based on cluster

## Expect
Only available addons listed  
  
lixue@Xue-Lis-MacBook-Pro Python 3.11 % rosa list addon -c 2djct75d5qkgrjm34je02m0atr9kd453  
ID NAME STATE  
ocm-addon-test-operator OCM Add-On Test Operator not installed  
managed-odh Red Hat OpenShift AI not installed  
managed-api-service Red Hat Openshift API Management not installed

## Step
Install an addon to the cluster

## Expect
The command will run successfully  
  
lixue@Xue-Lis-MacBook-Pro Python 3.11 % rosa install addon managed-odh -c 2diu6kfhntnbo8alslltjdsakjmrl50f  
? Are you sure you want to install add-on 'managed-odh' on cluster '2diu6kfhntnbo8alslltjdsakjmrl50f'? Yes  
? Notification email: xueli@redhat.com  
? Billing Model (default = 'standard'): standard  
I: Add-on 'managed-odh' is now installing. To check the status run 'rosa list addons -c 2diu6kfhntnbo8alslltjdsakjmrl50f'  
I: To install this addOn again in the future, you can run:  
rosa install addon --cluster rosa45745 managed-odh -y --notification-email xueli@redhat.com --billing-model standard

## Step
List the addon of the cluster  
$ rosa list addons -c <cluster name>

## Expect
The addon status is installing  
  
lixue@Xue-Lis-MacBook-Pro Python 3.11 % rosa list addons -c 2diu6kfhntnbo8alslltjdsakjmrl50f  
ID NAME STATE  
ocm-addon-test-operator OCM Add-On Test Operator not installed  
managed-odh Red Hat OpenShift AI installing  
managed-api-service Red Hat Openshift API Management not installed

## Step
Describe the addon installation

## Expect
It will show all detailed information include the parameter set  
  
lixue@Xue-Lis-MacBook-Pro Python 3.11 % rosa describe addon-installation -c 2diu6kfhntnbo8alslltjdsakjmrl50f --addon managed-odh  
Id: managed-odh  
Href: /api/addons_mgmt/v1/clusters/2diu6kfhntnbo8alslltjdsakjmrl50f/addons/managed-odh  
Addon state: installing  
Parameters:  
"notification-email" : "xueli@redhat.com"

## Step
Wait for the addon installation finished

## Expect

## Step
Edit the addon parameter

## Expect
The parameter will be updated  
  
lixue@Xue-Lis-MacBook-Pro Python 3.11 % rosa edit addon -c 2diu6kfhntnbo8alslltjdsakjmrl50f managed-odh  
? Notification email: xueli2@redhat.com  
I: Add-on 'managed-odh' is now updating. To check the status run 'rosa list addons -c 2diu6kfhntnbo8alslltjdsakjmrl50f'

## Step
Describe the addon installation again

## Expect
The parameter should be updated  
lixue@Xue-Lis-MacBook-Pro Python 3.11 % rosa describe addon-installation -c 2diu6kfhntnbo8alslltjdsakjmrl50f --addon managed-odh  
Id: managed-odh  
Href: /api/addons_mgmt/v1/clusters/2diu6kfhntnbo8alslltjdsakjmrl50f/addons/managed-odh  
Addon state: installing  
Parameters:  
"notification-email" : "xueli2@redhat.com"

## Step
Delete the addon

## Expect
The command will run successfully  
lixue@Xue-Lis-MacBook-Pro Python 3.11 % rosa uninstall addon managed-odh -c 2diu6kfhntnbo8alslltjdsakjmrl50f  
? Are you sure you want to uninstall add-on 'managed-odh' from cluster '2diu6kfhntnbo8alslltjdsakjmrl50f'? Yes  
I: Add-on 'managed-odh' is now uninstalling. To check the status run 'rosa list addons -c 2diu6kfhntnbo8alslltjdsakjmrl50f'

## Step
Describe the addon installation again

## Expect
The status will become deleting  
lixue@Xue-Lis-MacBook-Pro Python 3.11 % rosa describe addon-installation -c 2diu6kfhntnbo8alslltjdsakjmrl50f --addon managed-odh   
Id: managed-odh  
Href: /api/addons_mgmt/v1/clusters/2diu6kfhntnbo8alslltjdsakjmrl50f/addons/managed-odh  
Addon state: deleting  
Parameters:  
"notification-email" : "xueli2@redhat.com"

## Step
Wait for deletion finished

## Expect

## Step
List the addon again

## Expect
It will be show not installed again  
lixue@Xue-Lis-MacBook-Pro Python 3.11 % rosa list addon -c 2diu6kfhntnbo8alslltjdsakjmrl50f  
ID NAME STATE  
ocm-addon-test-operator OCM Add-On Test Operator not installed  
managed-odh Red Hat OpenShift AI not installed  
managed-api-service Red Hat Openshift API Management not installed

## Step
Repeat above steps with different billing model:  
marketplace-rhm/marketplace-azure/marketplace  
(Note:we don't have the real quota for above billing model.It can only use marketplace-aws billing model)

## Expect
