# Test

## Step

note: cannot create additional ingress now since the "managed-ingress-support" is toggled on for all users

1. check the output of list ingress cli
```bash
rosa list ingress -c xxxx
```

## Expect

should see "LB TYPE"
ID APPLICATION ROUTER PRIVATE DEFAULT ROUTE SELECTORS LB-TYPE
i5a4 https://apps.xxx.org no yes classic

## Step

2. check the help message for ingress cli
~~$ rosa create ingress -h~~
```bash
rosa edit ingress -h
```

## Expect

should see flags "--lb-type"
```
Flags:
<...>
--lb-type string Type of Load Balancer. Options are classic,nlb.**
```

**

## Step

3. update default ingress to use nlb
```bash
rosa edit ingress --lb-type nlb -c xxxx
```
I: Updated ingress 'j3t6' on cluster 'xxxx'

## Expect

succeed

## Step

~~4. create the second ingress to use nlb~~
~~$ rosa create ingress -c xxxxx --lb-type nlb I: Ingress has been created on cluster 'xxxxx'. I: To view all ingresses, run 'rosa list ingresses -c xxxxx' note: should use classic by default if without "--lb-type"~~

## Expect

succeed

```bash
rosa list ingress -c xxxxxx
```
ID APPLICATION ROUTER PRIVATE DEFAULT ROUTE SELECTORS LB-TYPE
j3t6 https://apps.xxx.org no yes nlb
r9v9 https://apps2.xxxx.org no no nlb

## Step

5. (optional) change ingress lb type back to classic

## Expect

succeed
