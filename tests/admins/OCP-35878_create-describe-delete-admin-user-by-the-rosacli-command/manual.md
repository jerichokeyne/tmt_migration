# Setup

Create a ROSA cluster.

# Test

## Step

Try to describe the cluster admin while no admin user exists.

```bash
rosa describe admin -c ${CLUSTER_ID}
```

## Expect

```
W: There is no 'cluster-admin' user on cluster '2ss7bulenrhb4cackpfsmoaliqocoleh'. To create it run the following command:
   rosa create admin -c 2ss7bulenrhb4cackpfsmoaliqocoleh
```

## Step

Try to describe the admin for a cluster that does not exist.

```bash
rosa describe admin -c invalid
```

## Expect

```
E: Failed to get cluster 'invalid': There is no cluster with identifier or name 'invalid'
```

## Step

Create an admin user by running `rosa create admin`.

```bash
rosa create admin -c ${CLUSTER_ID}
```

## Expect

```
I: Admin account has been added to cluster '2ss7bulenrhb4cackpfsmoaliqocoleh'.
I: Please securely store this generated password. If you lose this password you can delete and recreate the cluster admin user.
I: To login, run the following command:

   oc login https://api.k0g6p3p1h8e0z5y.iogw.s3.devshift.org:443 --username cluster-admin --password Dp3yj-5Iigy-xopLg-y3Kca

I: It may take several minutes for this access to become active.
```

- The `cluster-admin` is created successfully and the `oc login` command is prompted.
- One HTPasswd IDP named `cluster-admin` is created.

```
$ rosa list idps -c 2ss7bulenrhb4cackpfsmoaliqocoleh
NAME             TYPE
cluster-admin    HTPasswd
```

- One `cluster-admin` user is added to the `cluster-admins` group.

```
$ rosa list users -c 2ss7bulenrhb4cackpfsmoaliqocoleh
ID             GROUPS
cluster-admin  cluster-admins
```

## Step

Describe the admin.

```bash
rosa describe admin -c ${CLUSTER_ID}
```

## Expect

```
I: There is 'cluster-admin' user on cluster '2ss7bulenrhb4cackpfsmoaliqocoleh'. To login, run the following command:
   oc login https://api.k0g6p3p1h8e0z5y.iogw.s3.devshift.org:443 --username cluster-admin
```

## Step

Delete the admin user.

```bash
rosa delete admin -c ${CLUSTER_ID}
```

## Expect

```
? Are you sure you want to delete cluster-admin user on cluster 2ss7bulenrhb4cackpfsmoaliqocoleh? Yes
I: Admin user 'cluster-admin' has been deleted from cluster '2ss7bulenrhb4cackpfsmoaliqocoleh'
```

- The `cluster-admin` user is removed from the group.

```
$ rosa list users -c 2ss7bulenrhb4cackpfsmoaliqocoleh
I: There are no users configured for cluster '2ss7bulenrhb4cackpfsmoaliqocoleh'
```

- The HTPasswd IDP is deleted.

```
$ rosa list idps -c 2ss7bulenrhb4cackpfsmoaliqocoleh
I: There are no identity providers configured for cluster '2ss7bulenrhb4cackpfsmoaliqocoleh'
```

## Step

Create a HTPasswd IDP, then create a `cluster-admin`.

## Expect

- It succeeds without any error.
- One `cluster-admin` user is added to the `cluster-admins` group under the existing IDP but does not show in `rosa list user`.

## Step

Delete admin.

## Expect

- The `cluster-admin` user is removed from the group.
- The HTPasswd IDP is not deleted because the HTPasswd list is not empty.

## Step

Create another admin user by the command.

## Expect

- It fails with an error message:

```
User 'cluster-admin' already exists on group 'cluster-admins' for cluster
```

## Step

Try to delete the admin.

1. Delete the admin with the correct `cluster_id`.

```bash
rosa delete admin -c 1talhgv5kjfmite8pk5cmlr979t4vu38
```

2. Delete the admin with the incorrect `cluster_id`.

```bash
rosa delete admin -c aaa
```

## Expect

1. A confirmation prompt is displayed. Enter `y` to delete or `n` to cancel.

```
? Are you sure you want to delete cluster-admin user on cluster 1talhgv5kjfmite8pk5cmlr979t4vu38? Yes
I: Admin user 'cluster-admin' has been deleted from cluster '1talhgv5kjfmite8pk5cmlr979t4vu38'
```

2. The command fails for the incorrect cluster ID.

```
E: Failed to get cluster 'aaa': There is no cluster with identifier or name 'aaa'
```
