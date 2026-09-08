# Setup
You need a HCP cluster on at least OCP version 4.19. You also need the "capability.organization.rosa_hcp_allow_autonode" capability enabled on your organization

# Test

## Step
Edit autonode config in the interactive mode  
  
rosa edit cluster -c $CLUSTER_NAME -i

## Expect
`**?` Update AutoNode IAM role ARN (current: arn:aws:iam::090777400063:role/jkeyne-HCP-ROSA-Installer-Role):  
?** New AutoNode IAM role ARN: [? for help] (arn:aws:iam::090777400063:role/jkeyne-HCP-ROSA-Installer-Role)  
  
It should succeed, and can describe the change:  
The output will contain a section describing the auto node configuration**  
  
`...`  
`AutoNode:`  
Mode: enabled**  
IAM Role ARN: arn:aws:iam::090777400063:role/jkeyne-HCP-ROSA-Installer-Role  
...

## Step
Verify that when editing the cluster interactively, it checks that the IAM role is a valid IAM role

## Expect
`**?` Update AutoNode IAM role ARN (current: arn:aws:iam::090777400063:role/jkeyne-HCP-ROSA-Installer-Role):** Yes   
X Sorry, your reply was invalid: '' does not match regular expression ^arn:aws[\w-]*:iam::\d{12}:role(?:\/+[\w+=,.@-]+)+$   
**?** **New AutoNode IAM role ARN:** [? for help] (arn:aws:iam::090777400063:role/jkeyne-HCP-ROSA-Installer-Role)

## Step
Verify that you can't enable the feature on classic clusters  
rosa edit cluster -c $CLUSTER_NAME --autonode 'enabled' --autonode-iam-role-arn $IAM_ROLE_ARN

## Expect
`E:` AutoNode is only supported for Hosted Control Plane clusters
