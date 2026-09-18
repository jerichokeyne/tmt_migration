# Setup

Refer to OCP-53857 setup.

# Test

## Step

Prepare a ROSA cluster.

## Expect

## Step

List the addons by command.

```bash
rosa list addons
```

## Expect

- The addons are listed correctly.

```
ID NAME AVAILABILITY
!@# sdqe-testing available
ocm-addon-test-operator OCM Add-On Test Operator available
reference-addon Reference Addon available
managed-api-service-internal Red Hat Openshift API Management (internal) unavailable
managed-odh Red Hat OpenShift AI available
managed-api-service Red Hat Openshift API Management available
```

## Step

Pick one of the addons and describe it.

```bash
rosa describe addon managed-odh
```

## Expect

- The addon details are shown correctly.

```
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
```

## Step

List the addons based on cluster.

```bash
rosa list addon -c 2djct75d5qkgrjm34je02m0atr9kd453
```

## Expect

- Only available addons are listed.

```
ID NAME STATE
ocm-addon-test-operator OCM Add-On Test Operator not installed
managed-odh Red Hat OpenShift AI not installed
managed-api-service Red Hat Openshift API Management not installed
```

## Step

Install an addon to the cluster.

```bash
rosa install addon managed-odh -c 2diu6kfhntnbo8alslltjdsakjmrl50f
```

## Expect

- The command runs successfully.

```
? Are you sure you want to install add-on 'managed-odh' on cluster '2diu6kfhntnbo8alslltjdsakjmrl50f'? Yes
? Notification email: xueli@redhat.com
? Billing Model (default = 'standard'): standard
I: Add-on 'managed-odh' is now installing. To check the status run 'rosa list addons -c 2diu6kfhntnbo8alslltjdsakjmrl50f'
I: To install this addOn again in the future, you can run:
rosa install addon --cluster rosa45745 managed-odh -y --notification-email xueli@redhat.com --billing-model standard
```

## Step

List the addon of the cluster.

```bash
rosa list addons -c <cluster name>
```

## Expect

- The addon status is `installing`.

```
ID NAME STATE
ocm-addon-test-operator OCM Add-On Test Operator not installed
managed-odh Red Hat OpenShift AI installing
managed-api-service Red Hat Openshift API Management not installed
```

## Step

Describe the addon installation.

```bash
rosa describe addon-installation -c 2diu6kfhntnbo8alslltjdsakjmrl50f --addon managed-odh
```

## Expect

- All detailed information, including the parameter set, is shown.

```
Id: managed-odh
Href: /api/addons_mgmt/v1/clusters/2diu6kfhntnbo8alslltjdsakjmrl50f/addons/managed-odh
Addon state: installing
Parameters:
"notification-email" : "xueli@redhat.com"
```

## Step

Wait for the addon installation to finish.

## Expect

## Step

Edit the addon parameter.

```bash
rosa edit addon -c 2diu6kfhntnbo8alslltjdsakjmrl50f managed-odh
```

## Expect

- The parameter is updated.

```
? Notification email: xueli2@redhat.com
I: Add-on 'managed-odh' is now updating. To check the status run 'rosa list addons -c 2diu6kfhntnbo8alslltjdsakjmrl50f'
```

## Step

Describe the addon installation again.

```bash
rosa describe addon-installation -c 2diu6kfhntnbo8alslltjdsakjmrl50f --addon managed-odh
```

## Expect

- The parameter is updated.

```
Id: managed-odh
Href: /api/addons_mgmt/v1/clusters/2diu6kfhntnbo8alslltjdsakjmrl50f/addons/managed-odh
Addon state: installing
Parameters:
"notification-email" : "xueli2@redhat.com"
```

## Step

Delete the addon.

```bash
rosa uninstall addon managed-odh -c 2diu6kfhntnbo8alslltjdsakjmrl50f
```

## Expect

- The command runs successfully.

```
? Are you sure you want to uninstall add-on 'managed-odh' from cluster '2diu6kfhntnbo8alslltjdsakjmrl50f'? Yes
I: Add-on 'managed-odh' is now uninstalling. To check the status run 'rosa list addons -c 2diu6kfhntnbo8alslltjdsakjmrl50f'
```

## Step

Describe the addon installation again.

```bash
rosa describe addon-installation -c 2diu6kfhntnbo8alslltjdsakjmrl50f --addon managed-odh
```

## Expect

- The status becomes `deleting`.

```
Id: managed-odh
Href: /api/addons_mgmt/v1/clusters/2diu6kfhntnbo8alslltjdsakjmrl50f/addons/managed-odh
Addon state: deleting
Parameters:
"notification-email" : "xueli2@redhat.com"
```

## Step

Wait for deletion to finish.

## Expect

## Step

List the addon again.

```bash
rosa list addon -c 2diu6kfhntnbo8alslltjdsakjmrl50f
```

## Expect

- It is shown as not installed again.

```
ID NAME STATE
ocm-addon-test-operator OCM Add-On Test Operator not installed
managed-odh Red Hat OpenShift AI not installed
managed-api-service Red Hat Openshift API Management not installed
```

## Step

Repeat the above steps with different billing models: `marketplace-rhm`, `marketplace-azure`, and `marketplace`.

Note: we do not have real quota for the above billing models. Only the `marketplace-aws` billing model can be used.

## Expect
