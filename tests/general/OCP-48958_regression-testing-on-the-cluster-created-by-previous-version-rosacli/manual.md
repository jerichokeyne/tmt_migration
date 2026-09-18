# Test

## Step
Log in with the previous ROSA CLI version, create an advanced ROSA cluster, and wait for it to be ready.

Note: This needs to cover at least the n-1 and n-2 ROSA CLI versions.

## Expect

## Step
Have a smoke test including the following actions with the latest ROSA CLI version:

- Create resources
- Delete resources
- Upgrade cluster
- Edit resources

## Expect
It should work well

## Step
Repeat steps 1-2 on an STS cluster.

## Expect
It should work well

## Step
Create a 4.10.x STS cluster via a ROSA CLI version lower than v1.1.11.

Note: This case needs to cover all ROSA CLI versions lower than v1.1.11.

## Expect
It should fail with the following error message:

```
E: Failed to create cluster: Creating STS clusters on OpenShift openshift-v4.10.0-candidate requires ROSA 1.1.10 or higher. Go to https://console.redhat.com/openshift/downloads#tool-rosa to download the latest version.
```

## Step
Check if it uses cloudfront to create the OIDC with the rosacli version >= 1.2.7 when create STS cluster

## Expect
- The OIDC provider should use CloudFront, and the OIDC endpoint URL should contain `cloudfront.net`, if ROSA CLI version is >= 1.2.7 and the account's organization enables the `oidc-s3-cloudfront` toggle.
- Otherwise, the OIDC provider should not use CloudFront and the OIDC endpoint URL should contain `rh-oidc`.

From OCM-1540, new URL DNS CNAMEs should be in the URL:

- [oidc.op1.openshiftapps.com](http://oidc.op1.openshiftapps.com/) -> `dvbwgdztaeq9o.cloudfront.net`
- [oidc.os1.devshift.org](http://oidc.os1.devshift.org/) -> `d3gt1gce2zmg3d.cloudfront.net`
- [oidc.oi1.devshift.org](http://oidc.is1.devshift.org/) -> `d1b0cha94ris3q.cloudfront.net`
