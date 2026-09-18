# Test

## Step

**Repeat all the steps of OCP-45502 via the interactive mode**

## Expect

The proxy options are only prompted after choose 'Install into an existing VPC' yes.
The clusters should be created successfully configuring cluster-wide proxy.
The proxy config can be updated correctly when `rosa edit cluster -c xxx`
- with valid value
- when to remove any existing cluster-wide proxy value or an existing additional-trust-bundle value.

**Known issue:**
OCM-10176
OCM-10030

## Step

**Check the node proxy**
```bash
rosa describe admin -c xxx
oc login https://api.xxx:443 --username cluster-admin
oc debug node/<node_name>
```
\# chroot /host
\# cat /etc/mco/proxy.env

## Expect

All of the nodes should be setup with the correct proxy information like below.
```
cat /etc/mco/proxy.env
\# Proxy environment variables will be populated in this file. Properly
\# url encoded passwords with special characters will use '%<HEX><HEX>'.
\# Systemd requires that any % used in a password be represented as
\# %% in a unit file since % is a prefix for macros; this restriction does not
\# apply for environment files. Templates that need the proxy set should use
\# 'EnvironmentFile=/etc/mco/proxy.env'.
HTTP_PROXY=http://10.0.0.147:8080
HTTPS_PROXY=https://10.0.0.147:8080
NO_PROXY=.cluster.local,.svc,.us-west-2.compute.internal,10.0.0.0/16,127.0.0.1,169.254.169.254,172.31.0.0/24,192.168.0.0/18,api-int.rosacli-ci-nkjt.zyqa.s1.devshift.org,localhost,quay.io,zyqa.s1.devshift.org
```

**// Debug for rosa classic cluster
\#############################**
// If there's no proxy information, pls check if there's proxy information of its output, if exist, then it means cms have submit its updates to ocp, and ocp may encountered issue. If not exist, then it means cms may encountered issue.

```bash
oc get proxy/cluster -oyaml
```

// if the above output contains proxy, then check if there's any error message
```bash
oc get co/network -o yaml | yq -y '.status' | head -10
oc get cm user-ca-bundle -n openshift-config -o yaml | yq -y '.data'
```

// It can view the updated status for mc pool, how many nodes has been updated
```bash
oc get mcp
```

// It will create a new mc when the proxy config (oc get proxy/cluster -oyaml) changed
```bash
oc get mc
```

**#############################**
