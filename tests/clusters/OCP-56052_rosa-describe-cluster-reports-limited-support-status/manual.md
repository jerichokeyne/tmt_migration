# Test

## Step
Create the cluster  
> rosa install cluster -c am-verify

## Expect
the cluster created

## Step
Check the limited support templates  
> ocm get /api/clusters_mgmt/v1/limited_support_reason_templates

## Expect
{  
"kind": "LimitedSupportReasonTemplateList",  
"page": 1,  
"size": 2,  
"total": 2,  
"items": [  
{  
"kind": "LimitedSupportReasonTemplate",  
"id": "7bc43fa6-3014-4da6-b262-e85d093c1117",  
"href": "/api/clusters_mgmt/v1/limited_support_reason_templates/7bc43fa6-3014-4da6-b262-e85d093c1117",  
"summary": "Unsupported cluster configuration",  
"details": "Red Hat has identified that your cluster is running a configuration that is inhibiting normal operation. Please see the service log for more details, or contact Red Hat support for more information."  
},  
{  
"kind": "LimitedSupportReasonTemplate",  
"id": "90a884a3-7482-4a1e-a9f2-ee1ed205feb8",  
"href": "/api/clusters_mgmt/v1/limited_support_reason_templates/90a884a3-7482-4a1e-a9f2-ee1ed205feb8",  
"summary": "Unsupported cloud provider configuration",  
"details": "Red Hat has identified that the cloud provider account hosting your cluster is running a configuration that is inhibiting normal operation. Please see the service log for more details, or contact Red Hat support for more information."  
}  
]  
}

## Step
Create limited support reasons via API with template ID without details/summary  
$ ocm post /api/clusters_mgmt/v1/clusters/<cluster id>/limited_support_reasons --body   
{  
"summary":"<summary>",  
"details":"<details>",  
"detection_type":"<manual/auto>",  
"template":{"id":"<template id>"}  
}

## Expect
{  
"kind": "LimitedSupportReason",  
"id": "9ec5e13a-64cc-11ed-93ec-0a580a831994",  
"href": "/api/clusters_mgmt/v1/clusters/1vsisll25ttafc75v8vg4veo36cr0hp8/limited_support_reasons/9ec5e13a-64cc-11ed-93ec-0a580a831994",  
"summary": "limitedTest",  
"details": "limitedTest",  
"template": {  
"id": "7bc43fa6-3014-4da6-b262-e85d093c1117",  
"href": "/api/clusters_mgmt/v1/clusters/1vsisll25ttafc75v8vg4veo36cr0hp8/limited_support_reasons/7bc43fa6-3014-4da6-b262-e85d093c1117"  
},  
"creation_timestamp": "2022-11-15T10:02:31.822778175Z"  
}

## Step
Check that the limited support reason added  
> ocm get /api/clusters_mgmt/v1/clusters/1vsisll25ttafc75v8vg4veo36cr0hp8/limited_support_reasons

## Expect
{  
"kind": "LimitedSupportReasonList",  
"page": 1,  
"size": 1,  
"total": 1,  
"items": [  
{  
"kind": "LimitedSupportReason",  
"id": "9ec5e13a-64cc-11ed-93ec-0a580a831994",  
"href": "/api/clusters_mgmt/v1/clusters/1vsisll25ttafc75v8vg4veo36cr0hp8/limited_support_reasons/9ec5e13a-64cc-11ed-93ec-0a580a831994",  
"summary": "limitedTest",  
"details": "limitedTest",  
"template": {  
"id": "7bc43fa6-3014-4da6-b262-e85d093c1117",  
"href": "/api/clusters_mgmt/v1/clusters/1vsisll25ttafc75v8vg4veo36cr0hp8/limited_support_reasons/7bc43fa6-3014-4da6-b262-e85d093c1117"  
},  
"creation_timestamp": "2022-11-15T10:02:31.822778Z"  
}  
]  
}

## Step
Verify the 'rosa describe' output  
> rosa describe cluster -c am-verify

## Expect
Limited support chapter added  
  
  
```  
Name: am-verify  
ID: 1vsisll25ttafc75v8vg4veo36cr0hp8  
External ID: 87b3989a-ef2c-45f5-9610-f6172264b4fd  
Control Plane: Customer hosted  
OpenShift Version: 4.11.12  
Channel Group: stable  
DNS: am-verify.f541.s1.devshift.org  
AWS Account: 425464789085  
API URL: https://api.am-verify.f541.s1.devshift.org:6443  
Console URL: https://console-openshift-console.apps.eldar-verify.f541.s1.devshift.org  
Region: us-west-2  
Multi-AZ: false  
Nodes:  
- Control plane: 3  
- Infra: 2  
- Compute: 2  
Network:  
- Type: OVNKubernetes  
- Service CIDR: 172.30.0.0/16  
- Machine CIDR: 10.0.0.0/16  
- Pod CIDR: 10.128.0.0/16  
- Host Prefix: /23  
STS Role ARN: arn:aws:iam::425464789085:role/chaoli-Installer-Role  
Support Role ARN: arn:aws:iam::425464789085:role/chaoli-Support-Role  
Instance IAM Roles:  
- Control plane: arn:aws:iam::425464789085:role/chaoli-ControlPlane-Role  
- Worker: arn:aws:iam::425464789085:role/chaoli-Worker-Role  
Operator IAM Roles:  
- arn:aws:iam::425464789085:role/am-verify-f57w-openshift-cluster-csi-drivers-ebs-cloud-creden  
- arn:aws:iam::425464789085:role/am-verify-f57w-openshift-cloud-network-config-controller-clou  
- arn:aws:iam::425464789085:role/am-verify-f57w-openshift-machine-api-aws-cloud-credentials  
- arn:aws:iam::425464789085:role/am-verify-f57w-openshift-cloud-credential-operator-cloud-cred  
- arn:aws:iam::425464789085:role/am-verify-f57w-openshift-image-registry-installer-cloud-crede  
- arn:aws:iam::425464789085:role/am-verify-f57w-openshift-ingress-operator-cloud-credentials  
State: ready   
Private: No  
Created: Nov 9 2022 10:09:30 UTC  
Details Page: https://qaprodauth.console.redhat.com/openshift/details/s/2HJ1rMX9thdiHZfFlSVWazEniLF  
OIDC Endpoint URL: https://rh-oidc-staging.s3.us-east-1.amazonaws.com/1vsisll25ttafc75v8vg4veo36cr0hp8  
**Limited Support:  
- Summary: limitedTest  
- Details: limitedTest**  
```

## Step
Create additional limited support reason to the cluster  
$ ocm post /api/clusters_mgmt/v1/clusters/<cluster id>/limited_support_reasons --body   
{  
"summary":"<summary>",  
"details":"<details>",  
"detection_type":"<manual/auto>",  
"template":{"id":"<template id>"}  
}

## Expect
{  
"kind": "LimitedSupportReason",  
"id": "59fabb80-64d6-11ed-93ec-0a580a831994",  
"href": "/api/clusters_mgmt/v1/clusters/1vsisll25ttafc75v8vg4veo36cr0hp8/limited_support_reasons/59fabb80-64d6-11ed-93ec-0a580a831994",  
"summary": "limitedTest2",  
"details": "limitedTest2",  
"template": {  
"id": "90a884a3-7482-4a1e-a9f2-ee1ed205feb8",  
"href": "/api/clusters_mgmt/v1/clusters/1vsisll25ttafc75v8vg4veo36cr0hp8/limited_support_reasons/90a884a3-7482-4a1e-a9f2-ee1ed205feb8"  
},  
"creation_timestamp": "2022-11-15T11:12:11.373658242Z"  
}

## Step
Check that the limited support reason added  
> ocm get /api/clusters_mgmt/v1/clusters/<cluster id>/limited_support_reasons

## Expect
{  
"kind": "LimitedSupportReasonList",  
"page": 1,  
"size": 2,  
"total": 2,  
"items": [  
{  
"kind": "LimitedSupportReason",  
"id": "59fabb80-64d6-11ed-93ec-0a580a831994",  
"href": "/api/clusters_mgmt/v1/clusters/1vsisll25ttafc75v8vg4veo36cr0hp8/limited_support_reasons/59fabb80-64d6-11ed-93ec-0a580a831994",  
"summary": "limitedTest2",  
"details": "limitedTest2",  
"template": {  
"id": "90a884a3-7482-4a1e-a9f2-ee1ed205feb8",  
"href": "/api/clusters_mgmt/v1/clusters/1vsisll25ttafc75v8vg4veo36cr0hp8/limited_support_reasons/90a884a3-7482-4a1e-a9f2-ee1ed205feb8"  
},  
"creation_timestamp": "2022-11-15T11:12:11.373658Z"  
},  
{  
"kind": "LimitedSupportReason",  
"id": "9ec5e13a-64cc-11ed-93ec-0a580a831994",  
"href": "/api/clusters_mgmt/v1/clusters/1vsisll25ttafc75v8vg4veo36cr0hp8/limited_support_reasons/9ec5e13a-64cc-11ed-93ec-0a580a831994",  
"summary": "limitedTest",  
"details": "limitedTest",  
"template": {  
"id": "7bc43fa6-3014-4da6-b262-e85d093c1117",  
"href": "/api/clusters_mgmt/v1/clusters/1vsisll25ttafc75v8vg4veo36cr0hp8/limited_support_reasons/7bc43fa6-3014-4da6-b262-e85d093c1117"  
},  
"creation_timestamp": "2022-11-15T10:02:31.822778Z"  
}  
]  
}

## Step
Verify the 'rosa describe' output  
> rosa describe cluster -c am-verify

## Expect
...  
  
OIDC Endpoint URL: https://rh-oidc-staging.s3.us-east-1.amazonaws.com/1vsisll25ttafc75v8vg4veo36cr0hp8  
Limited Support:  
- Summary: limitedTest2  
- Details: limitedTest2  
- Summary: limitedTest  
- Details: limitedTest  
```

## Step
Delete limited support reasons one-by-one  
> ocm delete /api/clusters_mgmt/v1/clusters/<cluster id>/limited_support_reasons/<limited_support_reason>

## Expect
limited support reasons are deleted
