# Test

## Step
Prepare a kms key for testing.  
\# aws kms create-key --tags TagKey=Purpose,TagValue=Test --description "BYOK Test Key"

## Expect
Keep the 'Arn'

## Step
Try to create an aws ccs cluster with the invalide key arn by command

## Expect
E: Expected a valid value forkms-key-arn matching ^arn:aws[\w-]*:kms:[\w-]+:\d{12}:key\/mrk-[0-9a-f]{32}$|[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$

## Step
Try to create an aws ccs cluster with the valid key arn but the region is not matched.

## Expect
E: Failed to create cluster: KMS Key ARN <ARN> not found in the region 'us-west-2'. Create a new one in the correct region, replace the ARN, and try again

## Step
Try to create an aws ccs cluster with the key arn which is not in the correct format.

## Expect
E: Expected a valid value forkms-key-arn matching ^arn:aws[\w-]*:kms:[\w-]+:\d{12}:key\/mrk-[0-9a-f]{32}$|[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$

## Step
Repeat step2~4 with the interactive mode.  
1.the invalide key arn  
2.the valid key arn but the region is not matched.  
3.the key arn which is not in the correct format  
4.empty arn

## Expect
- X Sorry, your reply was invalid: asd does not match regular expression ^arn:aws[\w-]*:kms:[\w-]+:\d{12}:key\/mrk-[0-9a-f]{32}$|[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$  
-E: Failed to create cluster: KMS Key ARN 'arn:aws:kms:us-west-2:301721915996:key/9fdfaf2f-efb7-4db7-a5c3-0d047c52f094' not found in the region 'us-east-2'. Create a new one in the correct region, replace the ARN, and try again  
-X Sorry, your reply was invalid: asd does not match regular expression ^arn:aws[\w-]*:kms:[\w-]+:\d{12}:key\/mrk-[0-9a-f]{32}$|[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$   
- X Sorry, your reply was invalid: Value is required

## Step
Repeat all above steps on ROSA cluster

## Expect
The result should be same
