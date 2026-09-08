# Test

## Step
note: cannot create additional ingress on staging/int env since the "managed-ingress-support" is toggled on for all users on staging/int env from now (09/18)  
Edit/Delete additional ingress should work if it is present  
Edit default ingress is not changed.  
  
Launch rosa cli to staging env

## Expect

## Step
Prepare a ready rosa cluster

## Expect

## Step
Run command and check the help message of ingress creation:  
$rosa edit ingress --help

## Expect
- The help message will show correctly  
[xueli@xueli-work tmp]$ rosa edit ingress -h  
Edit the additional non-default application router for a cluster.  
  
  
Usage:  
rosa edit ingress [flags]  
  
  
Aliases:  
ingress, route  
  
  
Examples:  
\# Make additional ingress with ID 'a1b2' private on a cluster named 'mycluster'  
rosa edit ingress --private --cluster=mycluster a1b2  
  
  
\# Update the router selectors for the additional ingress with ID 'a1b2'  
rosa edit ingress --label-match=foo=bar --cluster=mycluster a1b2  
  
  
\# Update the default ingress using the sub-domain identifier  
rosa edit ingress --private=false --cluster=mycluster apps  
  
  
Flags:  
-c, --cluster string Name or ID of the cluster to add the ingress to (required).  
-h, --help help for ingress  
--label-match string Label match for ingress. Format should be a comma-separated list of 'key=value'. If no label is specified, all routes will be exposed on both routers.  
--private Restrict application route to direct, private connectivity.  
  
  
Global Flags:  
--debug Enable debug mode.  
-i, --interactive Enable interactive mode.  
--profile string Use a specific AWS profile from your credential file.  
-v, --v Level log level for V logs

## Step
Run command to edit an default ingress  
$ rosa edit ingress <ingress id> -c <cluster name> --private=true --label-match="aaa=bbb,ccc=ddd"

## Expect
- There is no error output

## Step
Repeat with the step to the additional ingress

## Expect
There is no error output  
It shows the updating succeeded.

## Step
Run command:  
$ rosa list ingress -c <cluster name>

## Expect
- The new updated ingress is listed  
- The updated value displayed in rout selectors  
[xueli@xueli-work tmp]$ rosa list ingress -c xueli-rosa  
ID APPLICATION ROUTER PRIVATE DEFAULT ROUTE SELECTORS  
u6x8 https://apps.xueli-rosa.r2th.s1.devshift.org yes yes   
p3s7 https://apps2.xueli-rosa.r2th.s1.devshift.org yes no aaa=bbb, ccc=ddd
