# Test

## Step
Prepare on-demand Capacity Reservation on specific az and with specifc instance type

## Expect

## Step
Make sure the Redhat organization has bellow capability label
```json
{ "created_at":"2025-08-26T02:34:40.751358Z", "href":"/api/accounts_mgmt/v1/organizations/2wLZWMFZgGEBkd1MBfJPtHTFSJZ/labels/capability.organization.hcp_enable_aws_capacity_reservations", "id":"31o1bF7bH79Voly9ANwE6a32Nxm", "internal":true, "key":"capability.organization.hcp_enable_aws_capacity_reservations", "kind":"Label", "organization_id":"2wLZWMFZgGEBkd1MBfJPtHTFSJZ", "updated_at":"2025-08-26T02:34:40.751358Z", "value":"true" }
```

## Expect
Or there will be error,"E: Failed to add machine pool to hosted cluster '2ksr019hemiuksa0q6qfb88v3mhtg7d4': status is 400, identifier is '400', code is 'CLUSTERS-MGMT-400', at '2025-08-25T09:45:31Z' and operation identifier is 'c6b46028-705e-4776-94e6-89f72af91cd5': AWS Capacity Reservations are not enabled for this organization
"

## Step
Prepare a ready hosted-cp cluster

## Expect

## Step
Create machinepool via rosacli command with flags "--instance-type" ,"--availability-zone"/"--subnet","--replicas" and "--capacity-reservation-id", and "--capacity-reservation-preference capacity-reservations-only"

## Expect
The machinepool should be created successfully.

## Step
Describe the created machinepool

## Expect
There should be Capacity Reservation field with ID and Type and Preference information.
Capacity Reservation:
- ID: cr-04f99ce73ad1d8afb
- Type: OnDemand
- Preference: capacity-reservations-only
\===============

Capacity Reservation:
- Preference: open
\=================

Capacity Reservation:
- ID: cr-04f99ce73ad1d8afb
- Type: OnDemand
~~- Preference:~~ ---- TBD: there should be NO '--Preference' field if the config don't contain preference value.

## Step
Check validations:
- setting "--capacity-reservation-id" and with the "--capacity-reservation-preference" value not capacity-reservations-only
- without setting "--capacity-reservation-id" and with invalid "--capacity-reservation-preference" value

## Expect
- E: expected a valid value for Capacity Reservation Preference: invalid Capacity Reservation Preference: 'none'. When specifying a capacity reservation id ('cr-0dc276a2524cc3da9'), you may only provide the 'capacity-reservations-only' preference
- E: expected a valid value for Capacity Reservation Preference: invalid Capacity Reservation Preference: 'aaaa'. When specifying a capacity reservation id ('cr-0dc276a2524cc3da9'), you may only provide the 'capacity-reservations-only' preference

## Step
Repeat above step with Capacity Block for ML ID.
NOTE: this kind of reservation will have a huge cost, be cautious about it!

## Expect
The result should be same with above.
