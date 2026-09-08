# Setup
KMS key   
{  
"Version": "2012-10-17",  
"Id": "key-rosa-policy-1",  
"Statement": [  
{  
"Sid": "Enable IAM User Permissions",  
"Effect": "Allow",  
"Principal": {  
"AWS": "arn:aws:iam::${AWS_ACCOUNT_ID}:root"  
},  
"Action": "kms:*",  
"Resource": "*"  
},  
{  
"Sid": "Installer Permissions",  
"Effect": "Allow",  
"Principal": {  
"AWS": "arn:aws:iam::${AWS_ACCOUNT_ID}:role/ManagedOpenShift-HCP-ROSA-Installer-Role"  
},  
"Action": [  
"kms:CreateGrant",  
"kms:DescribeKey",  
"kms:GenerateDataKeyWithoutPlaintext"  
],  
"Resource": "*"  
},  
{  
"Sid": "ROSA KubeControllerManager Permissions",  
"Effect": "Allow",  
"Principal": {  
"AWS": "arn:aws:iam::${AWS_ACCOUNT_ID}:role/<operator_role_prefix>-kube-system-kube-controller-manager"  
  
  
},  
"Action": "kms:DescribeKey",  
"Resource": "*"  
},  
{  
"Sid": "ROSA KMS Provider Permissions",  
"Effect": "Allow",  
"Principal": {  
"AWS": "arn:aws:iam::${AWS_ACCOUNT_ID}:role/<operator_role_prefix>-kube-system-kms-provider"  
},  
"Action": [  
"kms:Encrypt",  
"kms:Decrypt",  
"kms:DescribeKey"  
],  
"Resource": "*"  
},  
{  
"Sid": "ROSA NodeManager Permissions",  
"Effect": "Allow",  
"Principal": {  
"AWS": "arn:aws:iam::${AWS_ACCOUNT_ID}:role/<operator_role_prefix>-kube-system-capa-controller-manager"  
},  
"Action": [  
"kms:DescribeKey",  
"kms:GenerateDataKeyWithoutPlaintext",  
"kms:CreateGrant"  
],  
"Resource": "*"  
}  
]  
}

# Test

## Step
Prepare kms key by aws client.  
1. create KMS key and add the tag  
KMS_ARN=$(aws kms create-key --region $AWS_REGION --description 'Custom ROSA Encryption Key' --tags TagKey=red-hat,TagValue=true --query KeyMetadata.Arn --output text)  
2.Add the ARN for the account-wide installer role and operator roles to the `Statement.Principal.AWS` section in the file. (Example is in Setup)  
Reference: <https://docs.openshift.com/rosa/rosa_hcp/rosa-hcp-creating-cluster-with-aws-kms-key.html>

## Expect

## Step
Check the help message of 'rosa create cluster -h'

## Expect
--etcd-encryption Add etcd encryption. By default etcd data is encrypted at rest. This option configures etcd encryption on top of existing storage encryption.  
--etcd-encryption-kms-arn string The etcd encryption kms key ARN is the key used to encrypt etcd. If set it will override etcd-encryption flag to true. It is a unique, fully qualified identifier for the CMK. A key ARN includes the AWS account, Region, and the key ID.

## Step
Create one hypershift cluster with the KMS encryption by command.  
\# rosa create cluster -c <cluster_name> --etcd-encryption --etcd-encryption-kms-arn

## Expect
1. The cluster should be created successfully.

## Step
Create one hypershift cluster with the KMS encryption by command.  
\# rosa create cluster -c <cluster_name> --etcd-encryption-kms-arn

## Expect
1. The cluster should be created successfully.

## Step
~~Create one cluster the KMS encryption via the interactive mode. # rosa create cluster -i(Interactive mode should be merged to other test case or separate it to a new TC)~~

## Expect
1. There should be bellow items prompted in the interactive mode.  
? Encrypt etcd data: Yes  
? Etcd encryption KMS ARN: arn:aws:kms:us-east-1:301721915996:key/3ead7012-a878-4bc5-a14e-7962d8d5d540  
  
2. The cluster should be created successfully.

## Step
[OCM-9804] Describe HCP cluster with configuring both the KMS and etcd encryption   
rosa describe cluster -c <cluster-name>

## Expect
It should contain the corresponding encryption information as below.  
// rosa describe cluster -c <cluster-name>  
Etcd Encryption: Enabled  
Etcd KMS key ARN: <KMS key arn>  
  
// rosa describe cluster -c <cluster-name> -ojson  
"aws": {  
...  
"etcd_encryption": {  
"kms_key_arn": "KMS key arn"  
},  
"kms_key_arn": "KMS key arn",  
}

## Step
[OCM-9804] Create a HCP cluster only configuring etcd encryption

## Expect

## Step
[OCM-9804] Describe HCP cluster with only configuring etcd encryption  
rosa describe cluster -c <cluster-name>

## Expect
It should contain the corresponding encryption information as below.  
// rosa describe cluster -c <cluster-name>  
Etcd Encryption: Enabled  
Etcd KMS key ARN: <KMS key arn>  
  
// rosa describe cluster -c <cluster-name> -ojson  
"aws": {  
...  
"etcd_encryption": {  
"kms_key_arn": "KMS key arn"  
},  
"kms_key_arn": "KMS key arn",  
}

## Step
[OCM-9804] Create a HCP cluster without configuring etcd encryption  
rosa create cluster

## Expect

## Step
[OCM-9804] Describe a HCP cluster without configuring etcd encryption  
rosa describe cluster -c <cluster-name>

## Expect
It should contain the corresponding encryption information as below.  
// rosa describe cluster -c <cluster-name>  
Etcd Encryption: Disabled  
  
// rosa describe cluster -c <cluster-name> -ojson  
...  
"etcd_encryption": false,  
...
