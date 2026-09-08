# Test

## Step
~~ Assign label `capability.organization.create_cluster_proxy to the organization used for proxy testing`~~

## Expect

## Step
**Login via rosacli and check the help message of 'rosa create cluster -h'**

## Expect
~~--http-proxy string A proxy URL to use for creating HTTP connections outside the cluster. The URL scheme must be http. --https-proxy string A proxy URL to use for creating HTTPS connections outside the cluster. --additional-trust-bundle-file string A file contains a PEM-encoded X.509 certificate bundle that will be added to the nodes ' trusted certificate store. --no-proxy strings~~ A comma-separated list of destination domain names, domains, IP addresses or other network CIDRs to exclude proxying. Use "*" to bypass proxy for all destinations  
  
--http-proxy string A proxy URL to use for creating HTTP connections outside the cluster. The URL scheme must be http.  
--https-proxy string A proxy URL to use for creating HTTPS connections outside the cluster.  
--no-proxy strings A comma-separated list of destination domain names, domains, IP addresses or other network CIDRs to exclude proxying.  
--additional-trust-bundle-file string A file contains a PEM-encoded X.509 certificate bundle that will be added to the nodes' trusted certificate store.

## Step
Prepare existing subnets to use for testing  
[How to prepare AWS subnets for existed VPC testing](<https://docs.google.com/document/d/1-LKUxX4xA5g205er2HSZeP3FX7aYMQ5PhHrGmW9uQWw/edit>)   
Prepare MITM proxy server for testing  
[How to create MITM proxy server on AWS](<https://docs.google.com/document/d/17mhgm_3vYYTcctzqZeDok0KzZqn2KPv1QdvGvm0g2O8/edit#heading=h.tf7v93fsxoqn>)   
  
**A easier way to prepare VPC, subnets and proxy****  
** REPO**:** <https://github.com/openshift-qe/openshift-rosa-cli> **  
**  
**Create VPC, subnets using ocmqe**  
// create a vpc on the indicated region  
ocmqe create vpc --region us-west-2 --name <your-alias>-vpc  
  
// create a vpc on the dedicated region, if cannot find create it  
ocmqe create vpc --region us-west-2 --name <your-alias>-vpc --find-existing  
  
// create subnets  
ocmqe create subnets --region us-west-2 --zones a --vpc-id <vpc id, got from the above command's output>  
  
**Create proxy using ocmqe  
** // create a directory which store the generated files,  
ocmqe create proxy --region us-west-2 --vpc-id <vpc-id generated above> --zone <e.g. us-west-2a> --ca-file <ca file path, e.g. ~/proxy/ca-file> --keypair-name <a keypair name that not exists, e.g. dawang-proxy> --privatekey-path <the directory the generated files will store in, e.g. ~/proxy>

## Expect
**Succeed to create VPC, subnets using ocmqe  
** ocmqe create vpc --region us-west-2 --name dawang-west2-vpc  
INFO[2024-07-31 14:37:20] Going to prepare a vpc with name dawang-west2-vpc, on region us-west-2, with cidr 10.0.0.0/16 and subnets on zones  
INFO[2024-07-31 14:37:21] Going to create vpc and the follow resources on zones:  
INFO[2024-07-31 14:37:22] Create vpc success vpc-08c39a192f0b13a5d  
INFO[2024-07-31 14:37:22] Tag resource vpc-08c39a192f0b13a5d successfully  
INFO[2024-07-31 14:37:22] Created vpc with ID vpc-08c39a192f0b13a5d  
INFO[2024-07-31 14:37:22] VPC created on AWS with id: vpc-08c39a192f0b13a5d  
INFO[2024-07-31 14:37:23] Modify vpc dns attribute successvpc-08c39a192f0b13a5dDnsHostnames  
INFO[2024-07-31 14:37:23] VPC DNS Updated on AWS with id: vpc-08c39a192f0b13a5d  
INFO[2024-07-31 14:37:23] Create igw success: igw-0b3bd4415d34373a7  
INFO[2024-07-31 14:37:23] Attach igw success: igw-0b3bd4415d34373a7  
INFO[2024-07-31 14:37:23] Prepare vpc internetgateway for vpc vpc-08c39a192f0b13a5d  
INFO[2024-07-31 14:37:23] Create subnets successfully  
INFO[2024-07-31 14:37:23] Create vpc chain successfully. Enjoy it.  
INFO[2024-07-31 14:37:23] VPC ID: vpc-08c39a192f0b13a5d  
INFO[2024-07-31 14:37:23] VPC REGION: us-west-2  
INFO[2024-07-31 14:37:23] VPC NAME: dawang-west2-vpc  
  
ocmqe create subnets --region us-west-2 --zones a --vpc-id vpc-08c39a192f0b13a5d  
INFO[2024-07-31 14:37:50] Trying to list subnets of the vpc  
INFO[2024-07-31 14:37:50] Got 0 subnets  
INFO[2024-07-31 14:37:50] Got main association for rt rtb-030e5460ce7747a63  
INFO[2024-07-31 14:37:50] Going to prepare  
INFO[2024-07-31 14:37:50] Got no public subnet for current zone a, going to create one  
INFO[2024-07-31 14:37:51] Created subnet subnet-0b8e6c11e38b5152a for vpc vpc-08c39a192f0b13a5d  
INFO[2024-07-31 14:37:51] Created subnet with ID subnet-0b8e6c11e38b5152a  
INFO[2024-07-31 14:37:52] Associate route table success rtbassoc-0a199b3e049b097f9  
INFO[2024-07-31 14:37:53] Create route success for route table: rtb-05d49a44705023a2f  
INFO[2024-07-31 14:37:53] Tag resource subnet-0b8e6c11e38b5152a successfully  
INFO[2024-07-31 14:37:53] Got no proper private subnet for current zone a, going to create one  
INFO[2024-07-31 14:37:54] Created subnet subnet-0373b8e48a82355f2 for vpc vpc-08c39a192f0b13a5d  
INFO[2024-07-31 14:37:54] Created subnet with ID subnet-0373b8e48a82355f2  
INFO[2024-07-31 14:37:55] Associate route table success rtbassoc-0e22b489783296c57  
INFO[2024-07-31 14:37:55] Allocated EIP eipalloc-0ac161c9dd44f4ed2 with ip 35.82.188.204  
INFO[2024-07-31 14:37:56] Create nat success: nat-0508cbbaec79d22fc  
INFO[2024-07-31 14:39:50] Create route success for route table: rtb-05262242c025052a9  
INFO[2024-07-31 14:39:50] Tag resource subnet-0373b8e48a82355f2 successfully  
INFO[2024-07-31 14:39:50] ZONE a PUBLIC SUBNET: subnet-0b8e6c11e38b5152a  
INFO[2024-07-31 14:39:50] ZONE a PRIVATE SUBNET: subnet-0373b8e48a82355f2**  
  
Succeed to create proxy using ocmqe**  
ocmqe create proxy --region us-west-2 --vpc-id vpc-08c39a192f0b13a5d --zone us-west-2a --ca-file ~/proxy/ca-file.pem --keypair-name dawang-proxy --privatekey-path ~/proxy  
INFO[2024-07-31 15:09:13] Trying to list subnets of the vpc  
INFO[2024-07-31 15:09:13] Got 2 subnets  
INFO[2024-07-31 15:09:13] subnet-0b8e6c11e38b5152a 10.0.0.0/24 us-west-2a  
INFO[2024-07-31 15:09:13] subnet-0373b8e48a82355f2 10.0.1.0/24 us-west-2a  
INFO[2024-07-31 15:09:13] Got custom rt rtb-05d49a44705023a2f  
INFO[2024-07-31 15:09:13] Got main association for rt rtb-030e5460ce7747a63  
INFO[2024-07-31 15:09:13] Got custom rt rtb-05262242c025052a9  
INFO[2024-07-31 15:09:14] Create security group sg-01af18c79a84bd5fb success for vpc-08c39a192f0b13a5d  
INFO[2024-07-31 15:09:14] Tag resource sg-01af18c79a84bd5fb successfully  
INFO[2024-07-31 15:09:14] Created tagged security group with ID sg-01af18c79a84bd5fb  
INFO[2024-07-31 15:09:14] SG sg-01af18c79a84bd5fb created for vpc vpc-08c39a192f0b13a5d  
INFO[2024-07-31 15:09:15] Authorize security group success sg-01af18c79a84bd5fb  
INFO[2024-07-31 15:09:15] Authorize security group success sg-01af18c79a84bd5fb  
INFO[2024-07-31 15:09:15] Authorize SG sg-01af18c79a84bd5fb successfully for proxy.  
INFO[2024-07-31 15:09:15] Create key pair success: key-0090129389776e87a  
create key pair: key-0090129389776e87a successfully  
INFO[2024-07-31 15:09:16] Tag resource key-0090129389776e87a successfully  
INFO[2024-07-31 15:09:17] Waiting for below instances ready: i-0af8281344bd1cf79  
INFO[2024-07-31 15:09:17] Check instances status of i-0af8281344bd1cf79  
[{0x140004d60a0 [] 0x140004d6090 0x140004c13c0 0x140004c8fc0 <nil> 0x140004c8f90 {}}]  
INFO[2024-07-31 15:09:17] Instance ID i-0af8281344bd1cf79 is in status of not-applicable  
INFO[2024-07-31 15:09:17] Instance ID i-0af8281344bd1cf79 is in state of pending  
INFO[2024-07-31 15:10:17] Check instances status of i-0af8281344bd1cf79  
[{0x140004d61a0 [] 0x140004d6190 0x140004c1780 0x140004c92f0 <nil> 0x140004c9260 {}}]  
INFO[2024-07-31 15:10:17] Instance ID i-0af8281344bd1cf79 is in status of initializing  
INFO[2024-07-31 15:10:17] Instance ID i-0af8281344bd1cf79 is in state of running  
INFO[2024-07-31 15:10:17] All instances running  
INFO[2024-07-31 15:10:17] Launch proxy instance i-0af8281344bd1cf79 succeed  
INFO[2024-07-31 15:10:18] Tag resource i-0af8281344bd1cf79 successfully  
INFO[2024-07-31 15:10:18] Allocated EIP eipalloc-0ab81cc4aa786c626 with ip 100.20.61.242  
INFO[2024-07-31 15:10:18] Successfully allocated EIP: 100.20.61.242  
INFO[2024-07-31 15:10:19] Successfully allocated 100.20.61.242 with instance i-0af8281344bd1cf79.  
allocation id: eipalloc-0ab81cc4aa786c626, association id: eipassoc-0dcd58f6ad4454c3f  
INFO[2024-07-31 15:10:19] Prepare EIP successfully for the proxy preparation. Launch with IP: 100.20.61.242  
INFO[2024-07-31 15:12:24] HTTP PROXY: http://10.0.0.210:8080  
INFO[2024-07-31 15:12:24] HTTPs PROXY: https://10.0.0.210:8080  
INFO[2024-07-31 15:12:24] CA FILE PATH: /Users/dawang/proxy/ca-file.pem

## Step
**Create cluster with existing subnets, proxy set and ca-file(generate by creating proxy) via command**  
~~rosa create cluster --cluster-name yw-1029-t2 --version 4.8.14 --compute-nodes 2 --machine-cidr 10.0.0.0/16 --service-cidr 172.30.0.0/16 --pod-cidr 10.128.0.0/14 --host-prefix 23 --subnet-ids subnet-0c518f8745554ad64,subnet-0c2da2f8b694f6729 --http-proxy http://aa.com --https-proxy htpps://ss.com --additional-trust-bundle-file /root/workplace/rosa/additional_trust_bundle.ca --region us-east-1~~  
  
rosa create cluster --cluster-name dawang-hcp-proxy-rc3 --sts --create-admin-user --role-arn arn:aws:iam::301721915996:role/dawang-rosa-HCP-ROSA-Installer-Role --support-role-arn arn:aws:iam::301721915996:role/dawang-rosa-HCP-ROSA-Support-Role --worker-iam-role arn:aws:iam::301721915996:role/dawang-rosa-HCP-ROSA-Worker-Role --operator-roles-prefix dawang-hcp-proxy-rc3-n9j5 --oidc-config-id 2cqafguhtaep2jfof4lgqapnir2fbtqh --region us-west-2 --version 4.16.3 --ec2-metadata-http-tokens optional --replicas 2 --compute-machine-type m5.xlarge --machine-cidr 10.0.0.0/16 --service-cidr 172.30.0.0/16 --pod-cidr 10.128.0.0/14 --host-prefix 23 --subnet-ids subnet-0b8e6c11e38b5152a,subnet-0373b8e48a82355f2 **--http-proxy** http://10.0.0.210:8080 **--https-proxy** https://10.0.0.210:8080 **--no-proxy** example.com **--additional-trust-bundle-file** /Users/xxx/proxy/ca-file.pem --hosted-cp --billing-account 301721915996

## Expect
Cluster will be created successfully.  
It can get the correct proxy information through `rosa describe cluster -c <cluster id>`  
- proxy should show correctly in the response body  
- The proxy should show correctly in the cluster description  
.....  
Proxy:  
- HTTPProxy: http://10.0.0.210:8080  
- HTTPSProxy: https://10.0.0.210:8080  
- NoProxy: example.com  
Additional trust bundle: REDACTED   
.....

## Step
~~Repeat last step with account without the capability~~

## Expect
~~It should fail with some error message~~

## Step
~~Create another one with only http_proxy set Create another one with only https_proxy set with CA Check the install_config on HIVE~~

## Expect
~~The install config should match the settings - proxy should show correctly in the response body - The proxy should show correctly in the cluster description There is a syncset named 'proxy' that contains the proxy values~~

## Step
**Wait for cluster ready**

## Expect
Cluster should be ready in 2 hours

## Step
~~For no_proxy Create cluster with~~  
http_proxy + no_proxy set  
https_proxy+ no_proxy set with CA   
http_proxy and https_proxy + no_proxy set with CA   
no_proxy value format :hosts, IP addresses, or IP ranges in CIDR ,or a wildcard domain  
Example:`domain.example.com` `10.0.0.12` `10.0.0.0/24,.example.com``  
  
`Edit cluster for updating no_proxy`  
`Example: domain.example.com `10.0.0.12` `10.0.0.0/24,.example.com`

## Expect
~~The result is same to above~~  
All of the nodes should be updated with the updated proxy information.

## Step
~~Create machinepool to the cluster~~

## Expect

## Step
~~Launch cluster console~~

## Expect
~~The machinepool should be created successfully~~

## Step
~~Install add-on to the cluster~~

## Expect

## Step
~~Launch cluster console and check the service~~

## Expect
~~cluster addon service should use same proxy~~

## Step
~~Create IDP to the cluster and launch~~

## Expect
~~IDP will use same proxy~~

## Step
~~Upgrade the cluster~~

## Expect
~~Cluster will be upgraded successfully~~

## Step
~~Config networking additional ingress to the cluster~~

## Expect
~~Cluster ingress can be used successfully~~

## Step
~~Create cluster with --enable-proxy but without proxy setting~~

## Expect
~~The options of proxy should be prompted~~

## Step
~~Repeat above steps on sts cluster~~

## Expect
~~The cluster should be created successfully~~

## Step
~~Repeat above steps on different clusters(multi-az, private cluster....)~~

## Expect

## Step
~~Repeat all above steps via the interactive mode~~

## Expect
~~The proxy options are only prompted after choose 'Install into an existing VPC~~' yes.  
The clusters should be created successfully.  
The proxy config can be updated correctly when `rosa edit cluster -c xxx`  
- with valid value  
- when to remove any existing cluster-wide proxy value or an existing additional-trust-bundle value.
