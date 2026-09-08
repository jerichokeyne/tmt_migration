# Test

## Step
Running "rosa list ocm-roles" will display a list of OCM roles with a column labeled "CONSOLE ACCESS"

## Expect
`❯ ./rosa list ocm-roles  
I: Fetching ocm roles  
ROLE NAME ROLE ARN LINKED ADMIN AWS Managed CONSOLE ACCESS  
rosacli-ocm-role-stage-OCM-Role-13849960 arn:aws:iam::090777400063:role/test/rosacli-ocm-role-stage-OCM-Role-13849960 No Yes No Yes`

## Step
Running "rosa list ocm-roles -o json" and "rosa list ocm-roles -o yaml" will display valid JSON/YAML results and include a field "NoConsole" which will be either "No" or "Yes"

## Expect
`❯ ./rosa list ocm-roles -o json  
I: Fetching ocm roles  
[  
{  
"RoleName": "rosacli-ocm-role-stage-OCM-Role-13849960",  
"RoleARN": "arn:aws:iam::090777400063:role/test/rosacli-ocm-role-stage-OCM-Role-13849960",  
"Linked": "No",  
"Admin": "Yes",  
"NoConsole": "No"  
}  
]  
  
❯ ./rosa list ocm-roles -o yaml  
I: Fetching ocm roles  
- Admin: "Yes"  
Linked: "No"  
NoConsole: "No"  
RoleARN: arn:aws:iam::090777400063:role/test/rosacli-ocm-role-stage-OCM-Role-13849960  
RoleName: rosacli-ocm-role-stage-OCM-Role-13849960`

## Step
Running "rosa create ocm-role" with "--no-console" will work, and the resulting IAM role will have a tag with the key "rosa_no_console_role" and value "true"

## Expect
`❯ ./rosa create ocm-role --mode auto -y --prefix 'jkeyne' --no-console  
I: Creating ocm role  
W: This OCM role cannot be used to provision clusters via console.redhat.com`  
I: Creating role using 'arn:aws:iam::090777400063:user/jkeyne'  
I: Attached trust policy to role 'jkeyne-OCM-Role-13849960(https://console.aws.amazon.com/iam/home?#/roles/jkeyne-OCM-Role-13849960)': {"Version": "2012-10-17", "Statement": [{"Action": ["sts:AssumeRole"], "Effect": "Allow", "Condition": {"StringEquals": {"sts:ExternalId": "1jlfDskrR39egznAq3T18Ul0Xxv"}}, "Principal": {"AWS": ["arn:aws:iam::644306948063:role/RH-Managed-OpenShift-Installer"]}}]}  
I: Created role 'jkeyne-OCM-Role-13849960' with ARN 'arn:aws:iam::090777400063:role/jkeyne-OCM-Role-13849960'  
I: Attached policy 'arn:aws:iam::090777400063:policy/jkeyne-OCM-Role-13849960-NoConsole-Policy' to role 'jkeyne-OCM-Role-13849960(https://console.aws.amazon.com/iam/home?#/roles/jkeyne-OCM-Role-13849960)'  
  
I: Linking OCM role  
I: Successfully linked role-arn 'arn:aws:iam::090777400063:role/jkeyne-OCM-Role-13849960' with organization account '1jlfDskrR39egznAq3T18Ul0Xxv'  
  
❯ ./rosa list ocm-roles  
I: Fetching ocm roles  
ROLE NAME ROLE ARN LINKED ADMIN AWS Managed CONSOLE ACCESS  
jkeyne-OCM-Role-13849960 arn:aws:iam::090777400063:role/jkeyne-OCM-Role-13849960 Yes No No No  
rosacli-ocm-role-stage-OCM-Role-13849960 arn:aws:iam::090777400063:role/test/rosacli-ocm-role-stage-OCM-Role-13849960 No Yes No Yes  
  
❯ aws iam get-role --role-name jkeyne-OCM-Role-13849960 --output json | jq -r '.Role.Tags[] | select(.Key == "rosa_no_console_role")'  
{  
"Key": "rosa_no_console_role",  
"Value": "true"  
}

## Step
Running "rosa create ocm-role -i" should prompt the user `? Create OCM role with minimal permissions (no console access): [? for help] (y/N)` and if they select yes, it should create the role the same as the previous step

## Expect
`❯ ./rosa create ocm-role -i  
I: Creating ocm role  
? Role prefix: jkeyne  
? Enable admin capabilities for the OCM role: No  
? Create OCM role with minimal permissions (no console access): Yes  
W: This OCM role cannot be used to provision clusters via console.redhat.com`  
? Permissions boundary ARN (optional):  
? Role Path (optional):  
? Role creation mode: auto  
I: Creating role using 'arn:aws:iam::090777400063:user/jkeyne'  
? Create the 'jkeyne-OCM-Role-13849960' role? Yes  
I: Attached trust policy to role 'jkeyne-OCM-Role-13849960(https://console.aws.amazon.com/iam/home?#/roles/jkeyne-OCM-Role-13849960)': {"Version": "2012-10-17", "Statement": [{"Action": ["sts:AssumeRole"], "Effect": "Allow", "Condition": {"StringEquals": {"sts:ExternalId": "1jlfDskrR39egznAq3T18Ul0Xxv"}}, "Principal": {"AWS": ["arn:aws:iam::644306948063:role/RH-Managed-OpenShift-Installer"]}}]}  
I: Created role 'jkeyne-OCM-Role-13849960' with ARN 'arn:aws:iam::090777400063:role/jkeyne-OCM-Role-13849960'  
I: Attached policy 'arn:aws:iam::090777400063:policy/jkeyne-OCM-Role-13849960-NoConsole-Policy' to role 'jkeyne-OCM-Role-13849960(https://console.aws.amazon.com/iam/home?#/roles/jkeyne-OCM-Role-13849960)'  
  
I: Linking OCM role  
? OCM Role ARN: arn:aws:iam::090777400063:role/jkeyne-OCM-Role-13849960  
? Link the 'arn:aws:iam::090777400063:role/jkeyne-OCM-Role-13849960' role with organization '1jlfDskrR39egznAq3T18Ul0Xxv'? Yes  
I: Successfully linked role-arn 'arn:aws:iam::090777400063:role/jkeyne-OCM-Role-13849960' with organization account '1jlfDskrR39egznAq3T18Ul0Xxv'  
  
❯ aws iam get-role --role-name jkeyne-OCM-Role-13849960 --output json | jq -r '.Role.Tags[] | select(.Key == "rosa_no_console_role")'  
{  
"Key": "rosa_no_console_role",  
"Value": "true"  
}
