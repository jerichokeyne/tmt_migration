# Test

## Step
```bash
rosa create machinepool --help
```

## Expect
Version option is displayed
--version string Version of OpenShift that will be used to install a machine pool for a hosted cluster, for example "4.12.4"

## Step
~~rosa edit machinepool --help~~

## Expect
~~Version option is displayed --version string Version of OpenShift that will be used to install a machine pool for a hosted cluster, for example "4.12.4"~~

## Step
Create hosted-cp rosa cluster
```bash
rosa create cluster --version 4.12.50 # Just assume that 4.12.50 exist for discussion
```

## Expect
Cluster is ready

## Step
```bash
rosa list machinepool -c <cluster-name>
```

## Expect
Version is shown

## Step
```bash
rosa create machinepool --version 4.12.25
```

## Expect
The nodepool created

## Step
NOTE: MachinePool versions **must** not be less than 2 minor versions behind the Control Plane version and same major version
As Hypershift is supported only from 4.12.0, not relevant currently - will need to update the TC after 4.13, 4.14, 4.15 releases
The new minimal version for HCP is 4.14.x, so the minimal version for node pool is 4.14.x.(toggle:hypershift-enable-additional-minimal-version)
4.12 is only used for IBM LH users

## Expect

## Step
~~Edit the nodepool version.id to another one~~

## Expect
~~The nodepool updated successfully~~
