# Test

## Step
Prepare account roles

## Expect
> rosa create account-roles --prefix ${account_role_prefix} -f --mode auto -y

## Step
Create cluster with `--compute-machine-type=m6g.xlarge`

## Expect
> rosa create cluster [...] --compute-machine-type=m6g.xlarge

## Step
Create operator-roles and oidc-provider

## Expect
> rosa create operator-roles -c ${CLUSTER_NAME}  
> rosa create oidc-provider -c ${CLUSTER_NAME}

## Step
Wait for cluster ready

## Expect

## Step
Wait for nodepool ready

## Expect

## Step
Wait for cluster operators ready

## Expect

## Step
Destroy cluster

## Expect
> terraform destroy
