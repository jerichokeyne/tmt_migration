# Test

## Step
Prepare one hosted-cp cluster.

## Expect

## Step
Check the help message about image mirrors.

```bash
rosa create -h | grep image-mirror
rosa edit -h | grep image-mirror
rosa delete -h | grep image-mirror
rosa list -h | grep image-mirror
```

## Expect
```
image-mirror           Create image mirror for a cluster
image-mirror    Edit image mirror for a cluster
image-mirror           Delete image mirror from a cluster
image-mirrors           List cluster image mirrors
```

All subcommand help messages should be clear and correct.

## Step
Create an image mirror with the `--type`, `-c`, `--source`, and `--mirrors` flags.

- `--mirrors` supports multiple values.

```bash
rosa create image-mirror -c 2lbbrpgkocgajphhqee7vku1pgd4qsge --source www.registry/hco --mirrors my.registry.com/nginx,testing.org/nginx,22 --type digest
```

## Expect
```
I: Image mirror with ID '8f57c878-9b6e-4965-9d8f-a545c80f6aba' has been created on cluster '2lbbrpgkocgajphhqee7vku1pgd4qsge'
I: Source: www.registry/hco
I: Mirrors: [my.registry.com/nginx testing.org/nginx 22]
```

- It should succeed and display the image mirror details.

## Step
List image mirrors.

```bash
rosa list image-mirror -c 2lbbrpgkocgajphhqee7vku1pgd4qsge
```

## Expect
```
ID TYPE SOURCE MIRRORS
383fa117-cb7f-479d-8812-85b8e7ac161d digest www.registry/rosa 11, 22
7d80c104-dd42-43c4-b400-84b494d8b731 digest www.registry/ocm 11, 22
8f57c878-9b6e-4965-9d8f-a545c80f6aba digest www.registry/hco my.registry.com/nginx, testing.org/nginx, 22
```

- It should return the created image mirror with `ID`, `TYPE`, `SOURCE`, and `MIRRORS` fields.

## Step
Validate `rosa create image-mirror`.

- No cluster ID is set.
- No source is set.
- No mirrors are set.
- The cluster ID does not exist.
- A duplicate source exists on the cluster.
- An unsupported type is set; currently, the only supported type value is `digest`.

## Expect
```
Failed to execute root command: required flag(s) "cluster" not set
Failed to execute root command: required flag(s) "source" not set
Failed to execute root command: required flag(s) "mirrors" not set

E: There is no cluster with identifier or name '2lbbrpgkocgajphhqee7vk'
E: Failed to create image mirror: status is 400, identifier is '400', code is 'CLUSTERS-MGMT-400', at '2025-09-16T08:50:07Z' and operation identifier is '6e6db802-05c4-4163-81c1-c3cd8eaee553': Image mirror for source 'www.registry/hco' already exists for cluster '2lbbrpgkocgajphhqee7vku1pgd4qsge'

E: Failed to create image mirror: status is 400, identifier is '400', code is 'CLUSTERS-MGMT-400', at '2025-09-16T08:56:56Z' and operation identifier is '8f3cd54d-fe3a-4357-b646-df6087ebed06': Image mirror type must be 'digest' if specified
```

## Step
Edit an image mirror.

- `--mirrors` supports multiple values.

```bash
rosa edit image-mirror -c 2lbbrpgkocgajphhqee7vku1pgd4qsge --id 7d80c104-dd42-43c4-b400-84b494d8b731 --mirrors ff,kk
```

## Expect
```
I: Image mirror '7d80c104-dd42-43c4-b400-84b494d8b731' has been updated on cluster '2lbbrpgkocgajphhqee7vku1pgd4qsge'
I: Source: www.registry/ocm
I: Updated mirrors: [ff kk]
```

- It should succeed and display the updated image mirror details as an INFO message.
- `rosa list image-mirror` output should update with the new value.

## Step
Validate `rosa edit image-mirror`.

- No cluster ID is set.
- No mirrors are set.
- No image mirror ID is set.
- The image mirror ID does not exist.
- The cluster ID does not exist.

## Expect
```
Failed to execute root command: required flag(s) "cluster" not set
Failed to execute root command: required flag(s) "mirrors" not set

E: Image mirror ID is required. Specify it as an argument or use the --id flag
E: Failed to edit image mirror: status is 404, identifier is '404', code is 'CLUSTERS-MGMT-404', at '2025-09-16T09:05:03Z' and operation identifier is '65396383-24ad-4034-a35e-0dfdb9c792dc': Image mirror ID '7d80c104-dd' for cluster '2lbbrpgkocgajphhqee7vku1pgd4qsge' not found

E: There is no cluster with identifier or name '2lbbrpgkocg'
```

## Step
Delete image mirrors.

```bash
rosa delete image-mirror -c 2lbbrpgkocgajphhqee7vku1pgd4qsge --id 383fa117-cb7f-479d-8812-85b8e7ac161d
rosa delete image-mirror -c 2lbbrpgkocgajphhqee7vku1pgd4qsge --id 8f57c878-9b6e-4965-9d8f-a545c80f6aba -y
```

## Expect
```
? Are you sure you want to delete image mirror '383fa117-cb7f-479d-8812-85b8e7ac161d' on cluster '2lbbrpgkocgajphhqee7vku1pgd4qsge'?: Yes
I: Image mirror '383fa117-cb7f-479d-8812-85b8e7ac161d' has been deleted from cluster '2lbbrpgkocgajphhqee7vku1pgd4qsge'
I: Image mirror '8f57c878-9b6e-4965-9d8f-a545c80f6aba' has been deleted from cluster '2lbbrpgkocgajphhqee7vku1pgd4qsge'
```

- It should be deleted successfully with `-y`.
- It should ask for confirmation when deleting without `-y`.
- After deletion, the item should be removed from `rosa list image-mirror` output.

## Step
Validate `rosa delete image-mirror`.

- No cluster ID is set.
- The cluster ID does not exist.
- No image mirror ID is set.
- The image mirror ID does not exist.

## Expect
```
Failed to execute root command: required flag(s) "cluster" not set
E: There is no cluster with identifier or name 'aa'

E: Image mirror ID is required. Specify it as an argument or use the --id flag
E: Failed to get image mirror 'aaa': status is 404, identifier is '404', code is 'CLUSTERS-MGMT-404', at '2025-09-16T09:07:30Z' and operation identifier is '2dd9ae05-3788-4b82-99d4-1c8e3736a914': Image mirror ID 'aaa' for cluster '2lbbrpgkocgajphhqee7vku1pgd4qsge' not found
```

## Step
Check all functions on a non-hosted-cp cluster.

## Expect
```
E: Image mirrors are only supported on Hosted Control Plane clusters
```
