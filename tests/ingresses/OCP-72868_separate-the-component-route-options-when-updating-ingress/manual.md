# Test

## Step
Prepare one ready ROSA cluster

## Expect

## Step
Verify the --help/-h statement for rosa edit ingress  
  
rosa edit ingress --help  
  
OR   
  
rosa edit ingress -h

## Expect
Edit a cluster ingress for a cluster.  
  
Usage:  
rosa edit ingress ID [flags]  
  
Flags:  
-c, --cluster string Name or ID of the cluster.  
--component-routes string Component routes settings. Available keys [oauth, console, downloads]. For each key a pair of hostname and tlsSecretRef is expected to be supplied. Format should be a comma separate list 'oauth: hostname=example-hostname;tlsSecretRef=example-secret-ref,downloads:...

## Step
List the ingresses of the cluster: rosa list ingresses cluster_identifier

## Expect

## Step
Verify the ability to simultaneously set custom hostname, certificate secrets for oauth, downloads and console routes by using the following: rosa edit ingress -c cluster_identifier ingress_identifier --component-routes "oauth: hostname=<hostname>;tlsSecretRef=<secret-ref>,downloads: hostname=<hostname>;tlsSecretRef=<secret-ref>,console: hostname=<hostname>;tlsSecretRef=<secret-ref>"

## Expect
You should get the following output: I: Updated ingress 'id' on cluster 'cluster_name'

## Step
Verify the same changes in the interactive mode: rosa edit ingress -i

## Expect

## Step
Verify the update: rosa list ingresses cluster_identifier

## Expect
Call “/api/clusters_mgmt/v1/clusters/<cluster_id>/ingresses” with a get request: Oauth, downloads, and console routes reflect the respective custom values

## Step
Confirm that error is return when not all required component routes are specified in the command

## Expect
E: An error occurred whilst parsing the supplied component routes: the expected amount of component routes is 3, but 1 have been supplied

## Step
Test updating all component routes with new certificate secrets using rosa edit ingress

## Expect
Should be updated successfully (rosa list ingresses cluster_identifier, call the api with a get request)

## Step
Test setting individual hostnames and secrets to each route

## Expect
Should be updated successfully (rosa list ingresses cluster_identifier, call the api with a get request)

## Step
Verify the behaviour if you do not supply the correct syntax etc for the parameters:  
[valeriiashapoval@fedora rosa-1.2.37.rc4]$ rosa edit ingress -c vshapova-7047 m9s9 --component-routes "oauth: hostname:custom1;tlsSecretRef=custom1,downloads: hostname=custom2;tlsSecretRef=custom2,console: hostname=custom3;tlsSecretRef=custom3"E: An error occurred whilst parsing the supplied component routes: only the name of the component should be followed by ':'[valeriiashapoval@fedora rosa-1.2.37.rc4]$ rosa edit ingress -c vshapova-7047 m9s9 --component-routes "oauth: hostname=custom1;tlsSecretRef=custom1,downloads: hostname:custom2;tlsSecretRef:custom2,console: hostname=custom3;tlsSecretRef=custom3"E: An error occurred whilst parsing the supplied component routes: only the name of the component should be followed by ':'[valeriiashapoval@fedora rosa-1.2.37.rc4]$ rosa edit ingress -c vshapova-7047 m9s9 --component-routes "oauth: hostname=custom1;tlsSecretRef=custom1,downloads: hostname=custom2;tlsSecretRef=custom2,console: hostname:custom3;tlsSecretRef=custom3"E: An error occurred whilst parsing the supplied component routes: only the name of the component should be followed by ':'[valeriiashapoval@fedora rosa-1.2.37.rc4]$ rosa edit ingress -c vshapova-7047 m9s9 --component-routes "oauth= hostname=custom1;tlsSecretRef=custom1,downloads: hostname=custom2;tlsSecretRef=custom2,console: hostname=custom3;tlsSecretRef=custom3"E: An error occurred whilst parsing the supplied component routes: only the name of the component should be followed by ':'[valeriiashapoval@fedora rosa-1.2.37.rc4]$ rosa edit ingress -c vshapova-7047 m9s9 --component-routes "oauth: hostname=custom1;tlsSecretRef=custom1,downloads= hostname=custom2;tlsSecretRef=custom2,console: hostname=custom3;tlsSecretRef=custom3"E: An error occurred whilst parsing the supplied component routes: only the name of the component should be followed by ':'[valeriiashapoval@fedora rosa-1.2.37.rc4]$ rosa edit ingress -c vshapova-7047 m9s9 --component-routes "oauth: hostname=custom1;tlsSecretRef=custom1,downloads: hostname=custom2;tlsSecretRef=custom2,console= hostname=custom3;tlsSecretRef=custom3"E: An error occurred whilst parsing the supplied component routes: only the name of the component should be followed by ':'[valeriiashapoval@fedora rosa-1.2.37.rc4]$ rosa edit ingress -c vshapova-7047 m9s9 --component-routes "oauth: hostname=custom1;tlsSecretRef=custom1,downloads: hostname=custom2;tlsSecretRef=custom2,console:= hostname=custom3;tlsSecretRef=custom3"E: An error occurred whilst parsing the supplied component routes: '' is not a valid parameter for a component route. Expected include [hostname, tlsSecretRef]

## Expect
Call the API with a GET request, verify that no changes have been made (/api/clusters_mgmt/v1/clusters/<cluster_id>/ingresses)

## Step
Repeat the steps on a hosted CP cluster.

## Expect
