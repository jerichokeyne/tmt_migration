# Test

## Step
Login to staging env with `ocm`

```bash
# login
ocm login --url staging --token ${ORG_MEMBER_TOKEN}

# check
ocm whoami
```

## Expect

## Step
Create a new domain via ROSA CLI

For example:

```bash
./rosa create dns-domain
./rosa create dnsdomain
```

## Expect
```
I: DNS domain ‘v8tv.s1.devshift.org’ has been created.
I: To view all DNS domains, run 'rosa list dns-domains
```

## Step
Check domain

```bash
ocm get /api/clusters_mgmt/v1/dns_domains/v8tv.s1.devshift.org
echo '{"user_defined": false`}' | ocm post /api/clusters_mgmt/v1/dns_domains
```

## Expect
```json
{
  "Kind": "DnsDomain",
  "id": "v8tv.s1.devshift.org",
  "href": "/api/clusters_mgmt/v1/dns_domains/v8tv.s1.devshift.org",
  "organization_link": {
    "kind": "OrganizationLink",
    "id": "1qTKNfyb6TkqyLkbLImy5Qwuhmz",
    "href": "/api/accounts_mgmt/v1/organizations/1qTKNfyb6TkqyLkbLImy5Qwuhmz"
  },
  "user_defined": true
}
```

## Step
Delete domain

```bash
./rosa delete dnsdomain v8tv.s1.devshift.org
```

## Expect
```
I: Successfully deleted dns domain 'v8tv.s1.devshift.org'
```

## Step
Repeat all above steps with setting `--hosted-cp` to create a DNS domain for a Hosted Control Plane cluster

## Expect
The result should be same. The DNS base domain for clusters with Cross Account VPC architecture is defined per environment:

- For HCP DNS domains, use `i3`, `s3`, and `p3` respectively for each environment.
- For classic clusters, use `i1`, `s1`, and `p1` respectively for each environment.

## Step
List all existing domains via ROSA CLI

For example:

```bash
./rosa list dns-domain
```

## Expect
```
yuwan@yuwan-mac rosa % ./rosa list dns-domain
ID CLUSTER ID RESERVED TIME USER DEFINED ARCHITECTURE
14lr.s1.devshift.org 2024-10-22T09:59:07Z Yes classic
fmjw.s1.devshift.org 2024-11-11T10:16:20Z Yes classic
k7pb.s1.devshift.org 2024-11-10T11:00:45Z Yes classic
ns4c.s1.devshift.org 2f5j95ub7120ofied2128mgr4ok9ft5k 2024-11-20T06:38:02Z Yes classic
oelv.s1.devshift.org 2024-10-16T10:31:21Z Yes classic
p4af.s1.devshift.org 2024-10-22T11:36:01Z Yes classic
r0hk.s3.devshift.org 0001-01-01T00:00:00Z Yes hcp
rlvd.s3.devshift.org 2024-11-15T07:17:39Z Yes hcp
x35h.s1.devshift.org 0001-01-01T00:00:00Z Yes classic
y2up.s1.devshift.org 2024-10-18T03:30:49Z Yes classic
z4w3.s3.devshift.org 0001-01-01T00:00:00Z Yes hcp
z7vh.s1.devshift.org 0001-01-01T00:00:00Z Yes classic

...
```

## Step
List all DNS domains with the `--hosted-cp` flag

## Expect
```
yuwan@yuwan-mac rosa % ./rosa list dns-domain --hosted-cp
ID CLUSTER ID RESERVED TIME USER DEFINED ARCHITECTURE
r0hk.s3.devshift.org 0001-01-01T00:00:00Z Yes hcp
rlvd.s3.devshift.org 2024-11-15T07:17:39Z Yes hcp
z4w3.s3.devshift.org 0001-01-01T00:00:00Z Yes hcp
```

## Step
Print as JSON/YAML format

For example:

```bash
./rosa list dns-domain -o json
./rosa list dns-domain -o yaml
```

## Expect
Domain list in JSON/YAML format

## Step
List all existing domains in all organizations via ROSA CLI

For example:

```bash
./rosa list dns-domain -a
```

## Expect
There will be more domains listed than before.

```
❯ rosa list dns-domain -a
ID CLUSTER ID RESERVED TIME USER DEFINED ARCHITECTURE
005a.s1.devshift.org 2021-02-03T18:52:54Z No classic
00if.s1.devshift.org 2021-02-03T18:52:54Z No classic
00le.s1.devshift.org 2021-02-03T18:52:54Z No classic
00qw.s1.devshift.org 2021-02-03T18:52:54Z No classic
00rq.s1.devshift.org 2021-02-03T18:52:54Z No classic
00wu.s1.devshift.org 2021-02-03T18:52:54Z No classic
0103.s2.devshift.org 2021-02-03T18:52:54Z No
010r.s1.devshift.org 2021-02-03T18:52:54Z No classic
016k.s1.devshift.org 2021-02-03T18:52:54Z No classic
01ak.s1.devshift.org 2021-02-03T18:52:54Z No classic
01jd.s1.devshift.org 2021-02-03T18:52:54Z No classic
01jn.s2.devshift.org 2021-02-03T18:52:54Z No
01ne.s1.devshift.org 2021-02-03T18:52:54Z No classic
...
```

Also, if you output in JSON format, you can find all the organization IDs, and make sure that there's more than one.

```bash
rosa list dns-domain -a -o json | jq 'map(.organization.id) | unique'
```

```json
[
  null,
  "1GND9hMMlLa1wnrJCa499ihuzcE",
  "1H9RmeQvY7stKQUbhXibRV59Ixd",
  ...
  "2xMSdPCiTKnwxEU5ohBzTM6vKTe",
  "2y935ro1fkAHgHRGGweWTUQkqqu"
]
```

vs

```bash
rosa list dns-domain -o json | jq 'map(.organization.id) | unique'
```

```json
[
  "2wLZWMFZgGEBkd1MBfJPtHTFSJZ"
]
```

## Step
List all existing domains for only HCP clusters in all organizations via ROSA CLI

For example:

```bash
./rosa list dns-domain -a --hosted-cp
```

## Expect
There will be more domains listed than when you run just `rosa list dns-domain --hosted-cp`, and all the domains will have the architecture `hcp`.

```
❯ rosa list dns-domain -a --hosted-cp | head -n 30
ID CLUSTER ID RESERVED TIME USER DEFINED ARCHITECTURE
021i.s3.devshift.org 200mhtg3rtmbgn8lb44eklmk6nmo3hqp 2022-11-15T15:58:24Z No hcp
0b47.s3.devshift.org 2023-05-18T18:40:51Z No hcp
0e8w.s3.devshift.org 2025-03-24T15:41:51Z No hcp
0gcp.s3.devshift.org 2025-03-25T09:32:09Z No hcp
1gqz.s3.devshift.org 2023-05-21T18:33:12Z No hcp
1rr6.s3.devshift.org 2023-09-22T23:18:12Z No hcp
27qz.s3.devshift.org 2023-09-25T15:58:24Z No hcp
2ghp.s3.devshift.org 2025-04-10T21:10:57Z No hcp
30xd.s3.devshift.org 2023-09-25T11:53:02Z No hcp
38dk.s3.devshift.org 2023-05-04T11:28:57Z No hcp
3jy1.s3.devshift.org 2023-05-22T20:29:08Z No hcp
4ggs.s3.devshift.org 2025-07-07T18:07:46Z No hcp
4rj8.s3.devshift.org 2023-05-18T07:17:39Z No hcp
5vco.s3.devshift.org 2023-05-17T18:40:51Z No hcp
...
```

```bash
rosa list dns-domain -a -o json --hosted-cp | jq 'map(.organization.id) | unique'
```

```json
[
  "1H9SY60bJWyoynWMsZzZEvtLFdI",
  "1HAXGgCYqHpednsRDiwWsZBmDlA",
  ...
  "2wLZWMFZgGEBkd1MBfJPtHTFSJZ",
  "2wzWBh8nQg8PHvOdrR875c6fsnJ"
]
```

vs

```bash
rosa list dns-domain -o json --hosted-cp | jq 'map(.organization.id) | unique'
```

```json
[
  "2wLZWMFZgGEBkd1MBfJPtHTFSJZ"
]
```
