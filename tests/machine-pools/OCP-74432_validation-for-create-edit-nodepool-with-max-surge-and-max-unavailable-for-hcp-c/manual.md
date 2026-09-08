# Test

## Step
Prepare a hcp cluster

## Expect

## Step
Try to create a nodepool to the cluster with both max-surge and max-unavailable set as zero  
$ rosa create machinepool -c aaraj-hcp-1 --interactive  
? Machine pool name: new-mp  
? OpenShift version (default = '4.15.16'): 4.15.16  
? Select subnet for a hosted machine pool: No  
? AWS availability zone (default = 'us-west-2a'): us-west-2a  
? Enable autoscaling: No  
? Replicas: 3  
? Labels (optional):   
? Taints (optional):   
? Tags (optional):   
I: Checking available instance types for machine pool 'new-mp'  
? Instance type (default = 'm5.xlarge'): m5.xlarge  
? Autorepair: Yes  
W: No kubelet configs available for cluster '2bvauk3nol6kpabpgu1ujvr4ov8j4h3r'. Any kubelet config in input will be ignored  
? Node drain grace period (optional):   
? Max surge: 0  
? Max unavailable: 0

## Expect
E: Failed to add machine pool to hosted cluster 'aaraj-hcp-1': The value of only one attribute, 'management_upgrade.max_unavailable' or 'management_upgrade.max_surge', could be zero, not both

## Step
Try to create a nodepool to the cluster with both max-surge and max-unavailable set as 0%  
$ rosa create machinepool -c aaraj-hcp-1 --interactive  
? Machine pool name: new-mp  
? OpenShift version (default = '4.15.16'): 4.15.16  
? Select subnet for a hosted machine pool: No  
? AWS availability zone (default = 'us-west-2a'): us-west-2a  
? Enable autoscaling: No  
? Replicas: 3  
? Labels (optional):   
? Taints (optional):   
? Tags (optional):   
I: Checking available instance types for machine pool 'new-mp'  
? Instance type (default = 'm5.xlarge'): m5.xlarge  
? Autorepair: Yes  
W: No kubelet configs available for cluster '2bvauk3nol6kpabpgu1ujvr4ov8j4h3r'. Any kubelet config in input will be ignored  
? Node drain grace period (optional):   
? Max surge: 0%  
? Max unavailable: 0%

## Expect
E: Failed to add machine pool to hosted cluster 'aaraj-hcp-1': The value of only one attribute, 'management_upgrade.max_unavailable' or 'management_upgrade.max_surge', could be zero, not both

## Step
Try to create a nodepool to the cluster with one set as absolute and another as percentage value.  
$ rosa create machinepool -c aaraj-hcp-1 --interactive  
? Machine pool name: new-mp  
? OpenShift version (default = '4.15.16'): 4.15.16  
? Select subnet for a hosted machine pool: No  
? AWS availability zone (default = 'us-west-2a'): us-west-2a  
? Enable autoscaling: No  
? Replicas: 3  
? Labels (optional):   
? Taints (optional):   
? Tags (optional):   
I: Checking available instance types for machine pool 'new-mp'  
? Instance type (default = 'm5.xlarge'): m5.xlarge  
? Autorepair: Yes  
W: No kubelet configs available for cluster '2bvauk3nol6kpabpgu1ujvr4ov8j4h3r'. Any kubelet config in input will be ignored  
? Node drain grace period (optional):   
? Max surge: 1  
? Max unavailable: 0%

## Expect
E: Failed to add machine pool to hosted cluster 'aaraj-hcp-1': Attribute 'management_upgrade.max_unavailable' and 'management_upgrade.max_surge' must both use the same units (absolute value or percentage)

## Step
Try to create a nodepool to the cluster with set max-surge/max-unavailable as negative value  
$ rosa create machinepool -c aaraj-hcp-1 --interactive  
? Machine pool name: new-mp  
? OpenShift version (default = '4.15.16'): 4.15.16  
? Select subnet for a hosted machine pool: No  
? AWS availability zone (default = 'us-west-2a'): us-west-2a  
? Enable autoscaling: No  
? Replicas: 3  
? Labels (optional):   
? Taints (optional):   
? Tags (optional):   
I: Checking available instance types for machine pool 'new-mp'  
? Instance type (default = 'm5.xlarge'): m5.xlarge  
? Autorepair: Yes  
W: No kubelet configs available for cluster '2bvauk3nol6kpabpgu1ujvr4ov8j4h3r'. Any kubelet config in input will be ignored  
? Node drain grace period (optional):   
X Sorry, your reply was invalid: Value -1 cannot be negative  
? Max surge: [? for help] (-1)   
X Sorry, your reply was invalid: Value -1 cannot be negative  
? Max unavailable: [? for help] (1) -1

## Expect

## Step
Try to create a nodepool to the cluster with max-surge/max-unavailable set as negative percentage  
$ rosa create machinepool -c aaraj-hcp-1 --interactive  
? Machine pool name: new-mp  
? OpenShift version (default = '4.15.16'): 4.15.16  
? Select subnet for a hosted machine pool: No  
? AWS availability zone (default = 'us-west-2a'): us-west-2a  
? Enable autoscaling: No  
? Replicas: 3  
? Labels (optional):   
? Taints (optional):   
? Tags (optional):   
I: Checking available instance types for machine pool 'new-mp'  
? Instance type (default = 'm5.xlarge'): m5.xlarge  
? Autorepair: Yes  
W: No kubelet configs available for cluster '2bvauk3nol6kpabpgu1ujvr4ov8j4h3r'. Any kubelet config in input will be ignored  
? Node drain grace period (optional):   
X Sorry, your reply was invalid: Percentage value -1 must be between 0 and 100  
? Max surge: 1  
X Sorry, your reply was invalid: Percentage value -1 must be between 0 and 100  
? Max unavailable: [? for help] (1)

## Expect

## Step
Try to create a nodepool to the cluster with max-surge/max-unavailable set as greater than 100%  
$ rosa create machinepool -c aaraj-hcp-1 --interactive  
? Machine pool name: new-mp  
? OpenShift version (default = '4.15.16'): 4.15.16  
? Select subnet for a hosted machine pool: No  
? AWS availability zone (default = 'us-west-2a'): us-west-2a  
? Enable autoscaling: No  
? Replicas: 3  
? Labels (optional):   
? Taints (optional):   
? Tags (optional):   
I: Checking available instance types for machine pool 'new-mp'  
? Instance type (default = 'm5.xlarge'): m5.xlarge  
? Autorepair: Yes  
W: No kubelet configs available for cluster '2bvauk3nol6kpabpgu1ujvr4ov8j4h3r'. Any kubelet config in input will be ignored  
? Node drain grace period (optional):   
X Sorry, your reply was invalid: Percentage value 101 must be between 0 and 100  
? Max surge: 100%  
X Sorry, your reply was invalid: Percentage value 101 must be between 0 and 100  
? Max unavailable: [? for help] (101%)

## Expect

## Step
Try to create a nodepool to the cluster with max-surge/max-unavailable set as non-integer percentage.  
$ rosa create machinepool -c aaraj-hcp-1 --interactive  
? Machine pool name: new-mp  
? OpenShift version (default = '4.15.16'): 4.15.16  
? Select subnet for a hosted machine pool: No  
? AWS availability zone (default = 'us-west-2a'): us-west-2a  
? Enable autoscaling: No  
? Replicas: 3  
? Labels (optional):   
? Taints (optional):   
? Tags (optional):   
I: Checking available instance types for machine pool 'new-mp'  
? Instance type (default = 'm5.xlarge'): m5.xlarge  
? Autorepair: Yes  
W: No kubelet configs available for cluster '2bvauk3nol6kpabpgu1ujvr4ov8j4h3r'. Any kubelet config in input will be ignored  
? Node drain grace period (optional):   
X Sorry, your reply was invalid: Percentage value '-1.1%' must be an integer  
? Max surge: 1  
X Sorry, your reply was invalid: Percentage value '-1.1' must be an integer  
? Max unavailable: [? for help] (-1.1%)

## Expect

## Step
Try to create a nodepool to the cluster with max-surge/max-unavailable set as non-integer value  
$ rosa create machinepool -c aaraj-hcp-1 --interactive  
? Machine pool name: new-mp  
? OpenShift version (default = '4.15.16'): 4.15.16  
? Select subnet for a hosted machine pool: No  
? AWS availability zone (default = 'us-west-2a'): us-west-2a  
? Enable autoscaling: No  
? Replicas: 3  
? Labels (optional):   
? Taints (optional):   
? Tags (optional):   
I: Checking available instance types for machine pool 'new-mp'  
? Instance type (default = 'm5.xlarge'): m5.xlarge  
? Autorepair: Yes  
W: No kubelet configs available for cluster '2bvauk3nol6kpabpgu1ujvr4ov8j4h3r'. Any kubelet config in input will be ignored  
? Node drain grace period (optional):   
X Sorry, your reply was invalid: Value '1.1' must be an integer  
? Max surge: 1  
X Sorry, your reply was invalid: Value '1.1' must be an integer  
? Max unavailable: [? for help] (1.1)

## Expect

## Step
Try to create a nodepool to the cluster with max-surge/max-unavailable set as neagtive non-integer value  
$ rosa create machinepool -c aaraj-hcp-1 --interactive  
? Machine pool name: new-mp  
? OpenShift version (default = '4.15.16'): 4.15.16  
? Select subnet for a hosted machine pool: No  
? AWS availability zone (default = 'us-west-2a'): us-west-2a  
? Enable autoscaling: No  
? Replicas: 3  
? Labels (optional):   
? Taints (optional):   
? Tags (optional):   
I: Checking available instance types for machine pool 'new-mp'  
? Instance type (default = 'm5.xlarge'): m5.xlarge  
? Autorepair: Yes  
W: No kubelet configs available for cluster '2bvauk3nol6kpabpgu1ujvr4ov8j4h3r'. Any kubelet config in input will be ignored  
? Node drain grace period (optional):   
X Sorry, your reply was invalid: Value '-1.1' must be an integer  
? Max surge: 1  
X Sorry, your reply was invalid: Value '-1.1' must be an integer  
? Max unavailable: [? for help] (-1.1)

## Expect

## Step
Try to edit a nodepool to the cluster with both max-surge and max-unavailable set as zero  
$ rosa edit machinepool -c aaraj-hcp-1 test2 --interactive  
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
$ rosa edit machinepool -c aaraj-hcp-1 test2 --interactive  
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
$ rosa edit machinepool -c aaraj-hcp-1 test2 --interactive  
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
$ rosa edit machinepool -c aaraj-hcp-1 test2 --interactive  
? Enable autoscaling: No  
? Replicas: 3  
? Labels (optional):   
? Taints (optional):   
? Autorepair: Yes  
? Node drain grace period (optional):   
? Max surge: 0  
X Sorry, your reply was invalid: Value -1 cannot be negative  
? Max unavailable: [? for help] (-1)

## Expect

## Step
Try to edit a nodepool to the cluster with max-surge/max-unavailable set as negative percentage  
$ rosa edit machinepool -c aaraj-hcp-1 test2 --interactive  
? Enable autoscaling: No  
? Replicas: 3  
? Labels (optional):   
? Taints (optional):   
? Autorepair: Yes  
? Node drain grace period (optional):   
? Max surge: 0%  
X Sorry, your reply was invalid: Percentage value -1 must be between 0 and 100  
? Max unavailable: [? for help] (-1%)

## Expect

## Step
Try to edit a nodepool to the cluster with max-surge/max-unavailable set as greater than 100%  
$ rosa edit machinepool -c aaraj-hcp-1 test2 --interactive  
? Enable autoscaling: No  
? Replicas: 3  
? Labels (optional):   
? Taints (optional):   
? Autorepair: Yes  
? Node drain grace period (optional):   
? Max surge: 0%  
X Sorry, your reply was invalid: Percentage value 101 must be between 0 and 100  
? Max unavailable: [? for help] (101%)

## Expect

## Step
Try to edit a nodepool to the cluster with max-surge/max-unavailable set as non-integer percentage.  
$ rosa edit machinepool -c aaraj-hcp-1 test2 --interactive  
? Enable autoscaling: No  
? Replicas: 3  
? Labels (optional):   
? Taints (optional):   
? Autorepair: Yes  
? Node drain grace period (optional):   
? Max surge: 0%  
X Sorry, your reply was invalid: Percentage value '1.1' must be an integer  
? Max unavailable: [? for help] (1.1%)

## Expect

## Step
Try to edit a nodepool to the cluster with max-surge/max-unavailable set as non-integer value  
$ rosa edit machinepool -c aaraj-hcp-1 test2 --interactive  
? Enable autoscaling: No  
? Replicas: 3  
? Labels (optional):   
? Taints (optional):   
? Autorepair: Yes  
? Node drain grace period (optional):   
? Max surge: 0  
X Sorry, your reply was invalid: Value '1.1' must be an integer  
? Max unavailable: [? for help] (1.1)

## Expect

## Step
Try to edit a nodepool to the cluster with max-surge/max-unavailable set as negative non-integer value  
$ rosa edit machinepool -c aaraj-hcp-1 test2 --interactive  
? Enable autoscaling: No  
? Replicas: 3  
? Labels (optional):   
? Taints (optional):   
? Autorepair: Yes  
? Node drain grace period (optional):   
? Max surge: 0  
X Sorry, your reply was invalid: Value '-1.1' must be an integer  
? Max unavailable: [? for help] (-1.1)

## Expect
