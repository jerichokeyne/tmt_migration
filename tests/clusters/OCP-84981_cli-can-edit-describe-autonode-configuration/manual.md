# Setup
You need a HCP cluster on at least OCP version 4.19. You also need the "capability.organization.rosa_hcp_allow_autonode" capability enabled on your organization

# Test

## Step
1. Run "rosa edit cluster -c $CLUSTER_NAME --autonode 'enabled' --autonode-iam-role-arn $IAM_ROLE_ARN" to enable the feature

## Expect
The command will succeed  
`**❯` ./rosa edit cluster -c jkeyne-0926-11 --autonode 'enabled' --autonode-iam-role-arn arn:aws:iam::090777400063:role/jkeyne-HCP-ROSA-Installer-Role**  
I: Updated cluster 'jkeyne-0926-11'

## Step
2. Describe the cluster: "rosa describe cluster -c $CLUSTER_NAME"

## Expect
The output will contain a section describing the auto node configuration  
  
`...`  
`AutoNode:`  
Mode: enabled  
IAM Role ARN: arn:aws:iam::090777400063:role/jkeyne-HCP-ROSA-Installer-Role  
...

## Step
3. Verify that after enabling the autonode feature, you can change the IAM role:  
rosa edit cluster -c $CLUSTER_NAME --autonode 'enabled' --autonode-iam-role-arn $NEW_IAM_ROLE_ARN

## Expect
The command will succeed  
`**❯` ./rosa edit cluster -c jkeyne-0926-11 --autonode 'enabled' --autonode-iam-role-arn arn:aws:iam::090777400063:role/jkeyne-HCP-ROSA-Support-Role**  
I: Updated cluster 'jkeyne-0926-11'

## Step
Validations check:  
- Verify that only "enabled" is supported for "--autonode"  
`rosa edit cluster -c jkeyne-0926-11 --autonode 'invalid'  
  
- Check that the IAM role format is validated non-interactively  
  
-Verify that you can't set the IAM role without enabling the feature  
rosa edit cluster -c $CLUSTER_NAME --autonode-iam-role-arn $IAM_ROLE_ARN  
  
- Verify that you can't enable the feature on classic clusters`

## Expect
`E:` Invalid value for --autonode. Currently only 'enabled' is supported  
  
E: Invalid IAM role ARN format: 'asdf'. Expected format: arn:aws:iam::<account-id>:role/<role-name>  
  
E: Cannot update IAM role ARN when AutoNode is not enabled. Enable AutoNode first with --autonode=enabled  
  
E: AutoNode is only supported for Hosted Control Plane clusters
