# Test

## Step
Verify that when editing a machine pool, the max replica values are correct and that validation is in place  
  
1. Verify that when you edit the replica count, the verification works  
rosa edit machinepool -c jkeyne-0116-01 workers --replicas 6000  
  
2. Verify that the verification works for minimum replicas  
rosa edit machinepool -c jkeyne-0116-01 mp0 --min-replicas 6000 --max-replicas 6000000  
  
3. Verify that the verification works for maximum replicas  
rosa edit machinepool -c jkeyne-0116-01 mp0 --min-replicas 1 --max-replicas 6000000

## Expect
Classic:**  
** If the version < 4.14.14 then the maximum should be 180 nodes  
If the version >= 4.14.14 then the maximum should be 249 nodes**  
**  
HCP:  
The maximum should be 500 nodes  
  
1.  
E: Failed to update machine pool 'workers' on hosted cluster 'jkeyne-0116-01': status is 400, identifier is '400', code is 'CLUSTERS-MGMT-400', at '2025-01-17T17:15:34Z' and operation identifier is 'c81e8eb4-94e6-4657-9594-3dbfc22757a5': Replicas+Autoscaling.Min: The total number of compute nodes for a single cluster '6001' exceeds the maximum allowed '500'. Reduce the total compute nodes requested to be within the maximum allowed.  
  
2.  
E: Failed to update machine pool 'mp0' on hosted cluster 'jkeyne-0116-01': status is 400, identifier is '400', code is 'CLUSTERS-MGMT-400', at '2025-01-17T17:16:52Z' and operation identifier is 'c008dc11-f10c-47ed-a46a-d25c8ccbd42f': Replicas+Autoscaling.Min: The total number of compute nodes for a single cluster '6002' exceeds the maximum allowed '500'. Reduce the total compute nodes requested to be within the maximum allowed.  
  
3.  
E: Failed to update machine pool 'mp0' on hosted cluster 'jkeyne-0116-01': status is 400, identifier is '400', code is 'CLUSTERS-MGMT-400', at '2025-01-17T17:17:02Z' and operation identifier is 'd76c32cd-40a4-45ef-a4f6-59b80030ea46': Replicas+Autoscaling.Max: The total number of compute nodes for a single cluster '6000002' exceeds the maximum allowed '500'. Reduce the total compute nodes requested to be within the maximum allowed.

## Step
Ensure that the verification works for creating machine pools  
  
1. Verify that when you create a machine pool and specify the replica count, the verification works  
rosa create machinepool -c jkeyne-0116-01 --name mp1 --replicas 60000  
  
2. Verify that the verification works for minimum replicas  
rosa create machinepool -c jkeyne-0116-01 --name mp1 --min-replicas 6000 --max-replicas 600000 --enable-autoscaling  
  
3. Verify that the verification works for maximum replicas  
rosa create machinepool -c jkeyne-0116-01 --name mp1 --min-replicas 1 --max-replicas 600000 --enable-autoscaling

## Expect
All should have this error (with the correct number):  
E: should provide an integer number less than or equal to '500'

## Step
Ensure that the verification works for creating clusters  
  
1. Verify that when you create a cluster and specify the replica count, the verification works  
rosa create cluster -c jkeyne-0117-01 --replicas 6000  
  
2. Verify that the verification works for minimum replicas  
rosa create cluster -c jkeyne-0117-01 --min-replicas 600 --max-replicas 60000 --enable-autoscaling  
  
3. Verify that the verification works for maximum replicas  
rosa create cluster -c jkeyne-0117-01 --min-replicas 2 --max-replicas 60000 --enable-autoscaling

## Expect
All should have this error (with the correct number):  
E: should provide an integer number less than or equal to '249'
