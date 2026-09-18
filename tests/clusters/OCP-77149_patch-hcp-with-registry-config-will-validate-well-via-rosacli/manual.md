# Test

## Step

patch  hcp with invalid value for --registry-config-allowed-registries-for-import flag
--registry-config-allowed-registries-for-import test.com:<not boolean type>

## Expect

-There should be readable error message.
```
E: Expected valid allowed registries for import values: invalid identifier 'test.com:tag' for 'allowed registries for import.' Should be in a <registry>:<boolean> format. The boolean indicates whether the registry is secure or not.
```

## Step

patch  hcp with --registry-config-blocked-registries and --registry-config-allowed-registries at same time

## Expect

-There should be readable error message.

## Step

patch registry config to a non-hcp cluster

## Expect

-There should be readable error message.
```
E: Setting the registry config is only supported for hosted clusters
```
