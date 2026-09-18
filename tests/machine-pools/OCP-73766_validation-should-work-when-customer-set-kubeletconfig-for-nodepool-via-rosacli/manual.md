# Test

## Step
Prepare a hosted cluster

## Expect

## Step
Create machinepool with multiple kubelet config ids
```bash
rosa create machinepool --kubelet-configs kube1,kube2 --replicas 0 --name multikube
```

## Expect
It will fail with only 1 supported

## Step
Create machinepool with not existing kubeletconfig name
```bash
rosa create machinepool --kubelet-configs notexisting --replicas 0 --name not existing
```

## Expect
It will fail with error message the kubeletconfig not existing

## Step
Create a machinepool with existing kubeletconfig

## Expect
It will succeed

## Step
Delete the kubeletconfig

## Expect
It will fail that it is in using

## Step
Edit the kubeletconfig

## Expect
It will fail that it is in using

## Step
Edit machinepool with multiple kubelet config ids

## Expect
It will fail with only 1 supported

## Step
Edit machinepool with not existing kubeletconfig name

## Expect
It will fail with error message the kubeletconfig not existing
