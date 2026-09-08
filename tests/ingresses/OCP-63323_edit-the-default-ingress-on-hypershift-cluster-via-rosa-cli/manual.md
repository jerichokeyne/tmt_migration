# Test

## Step
Run command and check the help message  
$rosa edit ingress --help

## Expect
yuwan1-mac:rosa yuwan$ ./rosa edit ingress -h  
Edit the additional non-default application router for a cluster.  
  
Usage:  
rosa edit ingress ID [flags]  
  
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
-c, --cluster string Name or ID of the cluster.  
-h, --help help for ingress  
--label-match string Label match for ingress. Format should be a comma-separated list of 'key=value'. If no label is specified, all routes will be exposed on both routers.  
--private Restrict application route to direct, private connectivity.  
  
Global Flags:  
--color string Surround certain characters with escape sequences to display them in color on the terminal. Allowed options are [auto never always] (default "auto")  
--debug Enable debug mode.  
-i, --interactive Enable interactive mode.  
--profile string Use a specific AWS profile from your credential file.  
--region string Use a specific AWS region, overriding the AWS_REGION environment variable.

## Step
Run command to edit an default ingress with --label-match  
$ rosa edit ingress <ingress id> -c <cluster name> --private=true --label-match="aaa=bbb,ccc=ddd"

## Expect
- E: Updating route selectors is not supported for hosted cp clusters

## Step
Run command to edit an default ingress with --private  
$ rosa edit ingress <ingress id> -c <cluster name> --private=false   
$ rosa edit ingress <ingress id> -c <cluster name> --private  
--> Then list the ingress to check the 'PRIVATE' column

## Expect
- If no change, W: No need to update ingress as there are no changes is shown  
- Or I: Updated ingress 'j0j2' on cluster '23j0i3uboco0c12hddfmnknueblgnvpd'  
  
Check the output of `rosa list ingress`:  
- if --private works, 'PRIVATE' value is yes; if --private=false works, 'PRIVATE' value is no

## Step
Check the the interactive mode

## Expect
- Only 'Private ingress' question is shown, and it works well  
yuwan1-mac:rosa yuwan$ ./rosa edit ingress j0j2 -c 23j0i3uboco0c12hddfmnknueblgnvpd -i   
? Restrict application route to direct, private connectivity.  
? Private ingress (optional): (y/N)
