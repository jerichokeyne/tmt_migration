# Test

## Step
Log in with the rosa cli

## Expect

## Step
Check the help message of 'rosa create idp -h'

## Expect
\# ./rosa create idp -h  
Add an Identity providers to determine how users log into the cluster.  
  
Usage:  
rosa create idp [flags]  
  
Examples:  
\# Add a GitHub identity provider to a cluster named "mycluster"  
rosa create idp --type=github --cluster=mycluster  
  
\# Add an identity provider following interactive prompts  
rosa create idp --cluster=mycluster --interactive  
  
Flags:  
-c, --cluster string Name or ID of the cluster to add the IdP to (required).  
-t, --type string Type of identity provider. Options are [github gitlab google ldap openid].  
--name string Name for the identity provider.  
  
--mapping-method string Specifies how new identities are mapped to users when they log in. (default "claim")  
--client-id string Client ID from the registered application.  
--client-secret string Client Secret from the registered application.  
--ca string Path to PEM-encoded certificate file to use when making requests to the server.  
  
--hostname string GitHub: Optional domain to use with a hosted instance of GitHub Enterprise.  
--organizations string GitHub: Only users that are members of at least one of the listed organizations will be allowed to log in.  
--teams string GitHub: Only users that are members of at least one of the listed teams will be allowed to log in. The format is <org>/<team>.  
  
--host-url string GitLab: The host URL of a GitLab provider. (default "https://gitlab.com")  
--hosted-domain string Google: Restrict users to a Google Apps domain.  
  
--url string LDAP: An RFC 2255 URL which specifies the LDAP search parameters to use.  
--insecure LDAP: Do not make TLS connections to the server.  
--bind-dn string LDAP: DN to bind with during the search phase.  
--bind-password string LDAP: Password to bind with during the search phase.  
--id-attributes string LDAP: The list of attributes whose values should be used as the user ID. (default "dn")  
--username-attributes string LDAP: The list of attributes whose values should be used as the preferred username. (default "uid")  
--name-attributes string LDAP: The list of attributes whose values should be used as the display name. (default "cn")  
--email-attributes string LDAP: The list of attributes whose values should be used as the email address.  
  
--issuer-url string OpenID: The URL that the OpenID Provider asserts as the Issuer Identifier. It must use the https scheme with no URL query parameters or fragment.  
--email-claims string OpenID: List of claims to use as the email address.  
--name-claims string OpenID: List of claims to use as the display name.  
--username-claims string OpenID: List of claims to use as the preferred username when provisioning a user.  
--groups-claims string OpenID: List of claims to use as the groups names.  
--extra-scopes string OpenID: List of scopes to request, in addition to the 'openid' scope, during the authorization token request.  
  
-h, --help help for idp  
  
Global Flags:  
--debug Enable debug mode.  
-i, --interactive Enable interactive mode.  
--profile string Use a specific AWS profile from your credential file.  
-v, --v Level log level for V logs  
-y, --yes Automatically answer yes to confirm operation.

## Step
Check the validation for the Github idp creation  
1.invalid format of teams  
2. All required parameter shouldnot be empty(org/teams,client_id,client_secret)

## Expect
1.E: Failed to add IDP to cluster '1iekajbm5j6ps8hh5ddjdpe64880c1q6': 'team' 'jojo' in not in format <org/team>  
2.X Sorry, your reply was invalid: Value is required(in red)

## Step
Check the validation for the Gitlab idp creation in the interactive mode.  
1.All required parameter shouldnot be empty(url,client_id,client_secret)  
2.invalid ca file path

## Expect
1.For the client_id and client_secret , there should be "X Sorry, your reply was invalid: Value is required(in red)" error message  
2. For the url, there is a default value for it

## Step
Check the validation for the Google idp creation in the interactive mode.  
1.All required parameter shouldnot be empty(host_domain,client_id,client_secret)  
2.invalid ca file path

## Expect
1.there should be "X Sorry, your reply was invalid: Value is required(in red)" error message

## Step
Check the validation for the LDAP idp creation in the interactive mode.  
1.All required parameter shouldnot be empty(ldap_url)  
2.bind_dn and bind_password must be input at the same time. and if not input, it is empty as default  
3. The ldap url with incorrect format  
4. For the ldap attributes, it will use the default values if they are not input  
5. ca and insecure cannot be set at the same time

## Expect
1.there should be "X Sorry, your reply was invalid: Value is required(in red)" error message

## Step
Check the validation for the Openid idp creation in the interactive mode.  
1.All required parameter shouldnot be empty(issuer_url,client_id,client_secret)  
2.invalid ca file path

## Expect
1.there should be "X Sorry, your reply was invalid: Value is required(in red)" error message

## Step
Repeat the steps on Windows/MacOS/Linux

## Expect
- The function should work well  
- The output should display well
