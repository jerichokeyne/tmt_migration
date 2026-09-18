# Test

## Step
Prepare on-demand Capacity Reservation on specific az and with specifc instance type

## Expect

## Step
Prepare a ready hosted-cp cluster

## Expect

## Step
Create machinepool in the interactive mode

## Expect
- There is questionaire of "? Capacity Reservation Preference (optional, choose 'Skip' to skip selection; ):" and four options for it, 'Skip','none','open' and 'capacity-reservations-only'


? Capacity Reservation Preference (optional, choose 'Skip' to skip selection; ): [Use arrows to move, type to filter, ? for more help]
Skip
none
> capacity-reservations-only
open

## Step
~~Input capacity reservation id at "? Capacity Reservation ID ~~" then choose 'none' or 'open' at "Capacity Reservation Preference "

## Expect
~~return error, E: expected a valid value for Capacity Reservation Preference: invalid Capacity Reservation Preference: 'none'. When specifying a capacity reservation id ('cr-0dc276a2524cc3da9'), you may only provide the 'capacity-reservations-only' preference~~

## Step
Input capacity reservation id at "? Capacity Reservation ID " then choose 'capacity-reservations-only'

## Expect
Only options of 'capacity-reservations-only' and 'Skip' shows

## Step
Don't input capacity reservation id at "? Capacity Reservation ID " then check all options of "Capacity Reservation Preference ".

## Expect
All options should be allowed, and th input preference value should be take effect, checking the request with --debug flag.

TBD: In future, we should have some field to show the capa-res preference in the output of `rosa describe machinepool`

## Step
Repeat above step with Capacity Block for ML ID.
NOTE: this kind of reservation will have a huge cost, be cautious about it!

## Expect
The result should be same with above.
