# Test

## Step
Prepare a hcp cluster

## Expect

## Step
Try to create a nodepool to the cluster with both max-surge and max-unavailable set as zero  
$rosa create machinepool -c aaraj-hcp --name new-m-1p --replicas 3 --max-surge 0 --max-unavailable 0

## Expect
I: Checking available instance types for machine pool 'new-m-1p'  
E: Failed to add machine pool to hosted cluster 'aaraj-hcp': The value of only one attribute, 'management_upgrade.max_unavailable' or 'management_upgrade.max_surge', could be zero, not both

## Step
Try to create a nodepool to the cluster with both max-surge and max-unavailable set as 0%  
$rosa create machinepool -c aaraj-hcp --name new-m-1p --replicas 3 --max-surge 0% --max-unavailable 0%

## Expect
I: Checking available instance types for machine pool 'new-m-1p'  
E: Failed to add machine pool to hosted cluster 'aaraj-hcp': The value of only one attribute, 'management_upgrade.max_unavailable' or 'management_upgrade.max_surge', could be zero, not both

## Step
Try to create a nodepool to the cluster with one set as absolute and another as percentage value.  
$ rosa create machinepool -c aaraj-hcp --name new-m-1p --replicas 3 --max-surge 0 --max-unavailable 1% --subnet subnet-037c1b72c1f86ea04

## Expect
I: Checking available instance types for machine pool 'new-m-1p'  
E: Failed to add machine pool to hosted cluster 'aaraj-hcp': Attribute 'management_upgrade.max_unavailable' and 'management_upgrade.max_surge' must both use the same units (absolute value or percentage)

## Step
Try to create a nodepool to the cluster with set max-surge as negative value  
$ rosa create machinepool -c aaraj-hcp --name new-m-1p --replicas 3 --max-surge -1 --max-unavailable 1 --subnet subnet-037c1b72c1f86ea04

## Expect
I: Checking available instance types for machine pool 'new-m-1p'  
E: Failed to add machine pool to hosted cluster 'aaraj-hcp': The value of attribute 'management_upgrade.max_surge' cannot be a negative integer

## Step
Try to create a nodepool to the cluster with set max-unavailable as negative value  
$ rosa create machinepool -c aaraj-hcp --name new-m-1p --replicas 3 --max-surge 1 --max-unavailable -1 --subnet subnet-037c1b72c1f86ea04

## Expect
I: Checking available instance types for machine pool 'new-m-1p'  
E: Failed to add machine pool to hosted cluster 'aaraj-hcp': The value of attribute 'management_upgrade.max_unavailable' cannot be a negative integer

## Step
Try to create a nodepool to the cluster with max-unavailable set as negative percentage  
$ rosa create machinepool -c aaraj-hcp-1 --name test2 --version 4.15.2 --replicas 3 --max-surge 0% --max-unavailable -1%

## Expect
I: Checking available instance types for machine pool 'test2'  
E: Failed to add machine pool to hosted cluster 'aaraj-hcp-1': Failed to parse percentage value for attribute 'management_upgrade.max_unavailable': Value -1 must be between 0 and 100

## Step
Try to create a nodepool to the cluster with max-surge set as negative percentage  
$ rosa create machinepool -c aaraj-hcp-1 --name test2 --version 4.15.2 --replicas 3 --max-surge -1% --max-unavailable 0%

## Expect
I: Checking available instance types for machine pool 'test2'  
E: Failed to add machine pool to hosted cluster 'aaraj-hcp-1': Failed to parse percentage value for attribute 'management_upgrade.max_surge': Value -1 must be between 0 and 100

## Step
Try to create a nodepool to the cluster with max-unavailable set as greater than 100%  
$ rosa create machinepool -c aaraj-hcp-1 --name test2 --version 4.15.2 --replicas 3 --max-surge 0% --max-unavailable 101%

## Expect
I: Checking available instance types for machine pool 'test2'  
E: Failed to add machine pool to hosted cluster 'aaraj-hcp-1': Failed to parse percentage value for attribute 'management_upgrade.max_unavailable': Value 101 must be between 0 and 100

## Step
Try to create a nodepool to the cluster with max-surge set as greater than 100%  
$ rosa create machinepool -c aaraj-hcp-1 --name test2 --version 4.15.2 --replicas 3 --max-surge 101% --max-unavailable 1%

## Expect
I: Checking available instance types for machine pool 'test2'  
E: Failed to add machine pool to hosted cluster 'aaraj-hcp-1': Failed to parse percentage value for attribute 'management_upgrade.max_surge': Value 101 must be between 0 and 100

## Step
Try to create a nodepool to the cluster with max-unavailable set as non-integer percentage.  
$ rosa create machinepool -c aaraj-hcp-1 --name test2 --version 4.15.2 --replicas 3 --max-surge 0% --max-unavailable 1.1%

## Expect
I: Checking available instance types for machine pool 'test2'  
E: Failed to add machine pool to hosted cluster 'aaraj-hcp-1': Failed to parse percentage value for attribute 'management_upgrade.max_unavailable': Error converting '1.1' to integer

## Step
Try to create a nodepool to the cluster with max-surge set as non-integer percentage.  
$ rosa create machinepool -c aaraj-hcp-1 --name test2 --version 4.15.2 --replicas 3 --max-surge 1.1% --max-unavailable 0%

## Expect
I: Checking available instance types for machine pool 'test2'  
E: Failed to add machine pool to hosted cluster 'aaraj-hcp-1': Failed to parse percentage value for attribute 'management_upgrade.max_surge': Error converting '1.1' to integer

## Step
Try to create a nodepool to the cluster with max-unavailable set as non-integer value  
$ rosa create machinepool -c aaraj-hcp-1 --name test2 --version 4.15.2 --replicas 3 --max-surge 0 --max-unavailable 1.1

## Expect
I: Checking available instance types for machine pool 'test2'  
E: Failed to add machine pool to hosted cluster 'aaraj-hcp-1': The value of attribute 'management_upgrade.max_unavailable' must be an integer

## Step
Try to create a nodepool to the cluster with max-surge set as non-integer value  
$ rosa create machinepool -c aaraj-hcp-1 --name test2 --version 4.15.2 --replicas 3 --max-surge 1.1 --max-unavailable 0

## Expect
: Checking available instance types for machine pool 'test2'  
E: Failed to add machine pool to hosted cluster 'aaraj-hcp-1': The value of attribute 'management_upgrade.max_surge' must be an integer

## Step
Try to edit a nodepool to the cluster with both max-surge and max-unavailable set as zero  
$ rosa edit machinepool -c aaraj-hcp-1 test2 --max-surge 0 --max-unavailable 0  
? Enable autoscaling: No  
? Replicas: 3  
? Labels (optional):   
? Taints (optional):   
? Autorepair: Yes  
? Node drain grace period (optional):   
? Max surge: 0  
? Max unavailable: 0

## Expect
E: Failed to update machine pool 'test2' on hosted cluster 'aaraj-hcp-1': The value of only one attribute, 'management_upgrade.max_unavailable' or 'management_upgrade.max_surge', could be zero, not both

## Step
Try to edit a nodepool to the cluster with both max-surge and max-unavailable set as 0%  
$ rosa edit machinepool -c aaraj-hcp-1 test2 --max-surge 0% --max-unavailable 0%  
? Enable autoscaling: No  
? Replicas: 3  
? Labels (optional):   
? Taints (optional):   
? Autorepair: Yes  
? Node drain grace period (optional):   
? Max surge: 0%  
? Max unavailable: 0%

## Expect
E: Failed to update machine pool 'test2' on hosted cluster 'aaraj-hcp-1': The value of only one attribute, 'management_upgrade.max_unavailable' or 'management_upgrade.max_surge', could be zero, not both

## Step
Try to edit a nodepool to the cluster with one set as absolute and another as percentage value.  
$ rosa edit machinepool -c aaraj-hcp-1 test2 --max-surge 0% --max-unavailable 1  
? Enable autoscaling: No  
? Replicas: 3  
? Labels (optional):   
? Taints (optional):   
? Autorepair: Yes  
? Node drain grace period (optional):   
? Max surge: 0%  
? Max unavailable: 1

## Expect
E: Failed to update machine pool 'test2' on hosted cluster 'aaraj-hcp-1': Attribute 'management_upgrade.max_unavailable' and 'management_upgrade.max_surge' must both use the same units (absolute value or percentage)

## Step
Try to edit a nodepool to the cluster with set max-surge/max-unavailable as negative value.  
$ rosa edit machinepool -c aaraj-hcp-1 test2 --max-surge -1 --max-unavailable -1  
? Enable autoscaling: No  
? Replicas: 3  
? Labels (optional):   
? Taints (optional):   
? Autorepair: Yes  
? Node drain grace period (optional):   
X Sorry, your reply was invalid: Value -1 cannot be negative  
? Max surge: -1  
X Sorry, your reply was invalid: Value -1 cannot be negative  
? Max unavailable: [? for help] (-1)

## Expect

## Step
Try to edit a nodepool to the cluster with max-surge/max-unavailable set as negative percentage  
$ rosa edit machinepool -c aaraj-hcp-1 test2 --max-surge -1% --max-unavailable -1%  
? Enable autoscaling: No  
? Replicas: 3  
? Labels (optional):   
? Taints (optional):   
? Autorepair: Yes  
? Node drain grace period (optional):   
X Sorry, your reply was invalid: Percentage value -1 must be between 0 and 100  
? Max surge: -1%  
X Sorry, your reply was invalid: Percentage value -1 must be between 0 and 100  
? Max unavailable: [? for help] (-1%)

## Expect

## Step
Try to edit a nodepool to the cluster with max-surge/max-unavailable set as greater than 100%  
$ rosa edit machinepool -c aaraj-hcp-1 test2 --max-surge 101% --max-unavailable 101%  
? Enable autoscaling: No  
? Replicas: 3  
? Labels (optional):   
? Taints (optional):   
? Autorepair: Yes  
? Node drain grace period (optional):   
X Sorry, your reply was invalid: Percentage value 101 must be between 0 and 100  
? Max surge: 101%  
X Sorry, your reply was invalid: Percentage value 101 must be between 0 and 100  
? Max unavailable: [? for help] (101%)

## Expect

## Step
Try to edit a nodepool to the cluster with max-surge/max-unavailable set as non-integer percentage.  
$ rosa edit machinepool -c aaraj-hcp-1 test2 --max-surge 1.1% --max-unavailable 1.1%  
? Enable autoscaling: No  
? Replicas: 3  
? Labels (optional):   
? Taints (optional):   
? Autorepair: Yes  
? Node drain grace period (optional):   
X Sorry, your reply was invalid: Percentage value '1.1' must be an integer  
? Max surge: 1.1%  
X Sorry, your reply was invalid: Percentage value '1.1' must be an integer  
? Max unavailable: [? for help] (1.1%)

## Expect

## Step
Try to edit a nodepool to the cluster with max-surge/max-unavailable set as non-integer value  
$ rosa edit machinepool -c aaraj-hcp-1 test2 --max-surge 1.1 --max-unavailable 1.1  
? Enable autoscaling: No  
? Replicas: 3  
? Labels (optional):   
? Taints (optional):   
? Autorepair: Yes  
? Node drain grace period (optional):   
X Sorry, your reply was invalid: Value '1.1' must be an integer  
? Max surge: 1.1  
X Sorry, your reply was invalid: Value '1.1' must be an integer  
? Max unavailable: [? for help] (1.1)

## Expect
