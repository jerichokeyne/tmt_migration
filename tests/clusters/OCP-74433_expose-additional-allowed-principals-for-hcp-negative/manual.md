# Test

## Step

1. Verify failed creation of HCP cluster using the --additional-allowed-principals flag and invalid formatted arn
```bash
rosa create cluster --cluster-name $name --hosted-cp --additional-allowed-principals $account_role_arn
```

## Expect

```
E: Expected valid ARNs for additional allowed principals list: Invalid ARN: arn: invalid prefix
```

## Step

Verify failed creation of classic cluster using the --additional-allowed-principals flag

## Expect

```
E: Additional Allowed Principals is supported only for Hosted Control Planes
```

## Step

2. Get root aws arn (login as super admin)
```bash
ocm get /api/clusters_mgmt/v1/clusters/<id>/resources/live|jq -r .resources |grep "root"
```

## Expect

serviceNetwork: - cidr: 172.30.0.0/16 olmCatalogPlacement: management platform: aws: additionalAllowedPrincipals: - arn:aws:iam::301721915996:role/jf-HCP-ROSA-Installer-Role - arn:aws:iam::644306948063:root cloudProviderConfig: subnet: id: subnet-0ec7f73b8f66518a2

## Step

3. Verify failed creation of HCP cluster using the --additional-allowed-principals flag and protected arn
```bash
rosa create cluster --cluster-name $name --hosted-cp --additional-allowed-principals $root_arn
```

## Expect

```
E: Failed to create cluster: Additional allowed principals list containing 'arn:aws:iam::644306948063:root'
```
