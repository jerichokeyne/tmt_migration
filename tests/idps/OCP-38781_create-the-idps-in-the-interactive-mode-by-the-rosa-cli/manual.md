# Test

## Step
Log in with the rosa cli

## Expect

## Step
Create a GitHub IDP in interactive mode.

```bash
rosa create idp -c <clusrer_id>
rosa create idp -c <clusrer_id> -i
```

## Expect
NOET: It needs to cover the organizations and teams.
The idp should be created successfully and work well.
The help message in the interactive should be correct.
```
\# ./rosa create idp -c 1idjapicb4f98lign14em7ur6qk42s5c
? Type of identity provider: [Use arrows to move, type to filter]
> github
gitlab
google
ldap
openid
? Type of identity provider: github
? Restrict to members of: [Use arrows to move, type to filter, ? for more help]
> organizations
teams
? Restrict to members of: organizations
? GitHub organizations: [? for help] gorg
? GitHub organizations: gorg
? To use GitHub as an identity provider, you must first register the application:
- Open the following URL:
https://github.com/organizations/gorg/settings/applications/new?oauth_application%5Bcallback_url%5D=https%3A%2F%2Foauth-openshift.apps.yuwan-0124-sr1.w3l5.s2.devshift.org%2Foauth2callback%2Fgithub-1&oauth_application%5Bname%5D=yuwan-0124-sr1&oauth_application%5Burl%5D=https%3A%2F%2Fconsole-openshift-console.apps.yuwan-0124-sr1.w3l5.s2.devshift.org
- Click on 'Register application'
? Client ID: [? for help] aaa
? Client ID: aaa
? Client Secret: [? for help] ***
I: Configuring IDP for cluster '1idjapicb4f98lign14em7ur6qk42s5c'
I: Identity Provider 'github-1' has been created.
It will take up to 1 minute for this configuration to be enabled.
To add cluster administrators, see 'rosa grant user --help'.
To login into the console, open https://console-openshift-console.apps.yuwan-0124-sr1.w3l5.s2.devshift.org and click on github-1.
```

## Step
Create a GitLab IDP in interactive mode.

```bash
rosa create idp -c <clusrer_id>
rosa create idp -c <clusrer_id> -i
```

## Expect
The idp should be created successfully and work well.
The help message in the interactive should be correct.
```
\# ./rosa create idp -c 1idjapicb4f98lign14em7ur6qk42s5c
? Type of identity provider: [Use arrows to move, type to filter]
> github
gitlab
google
ldap
openid
? Type of identity provider: [Use arrows to move, type to filter]
github
> gitlab
google
ldap
openid
? Type of identity provider: gitlab
? URL: [? for help] (https://gitlab.com) https://aa.com
? URL: https://aa.com
? To use GitLab as an identity provider, register the application by opening:
- https://aa.com/profile/applications
? Then enter the following information:
- Name: yuwan-0124-sr1
- Redirect URI: https://oauth-openshift.apps.yuwan-0124-sr1.w3l5.s2.devshift.org/oauth2callback/gitlab-1
- Scopes: openid
? Application ID: [? for help] fff
? Application ID: fff
? Secret: [? for help] ***
I: Configuring IDP for cluster '1idjapicb4f98lign14em7ur6qk42s5c'
I: Identity Provider 'gitlab-1' has been created.
It will take up to 1 minute for this configuration to be enabled.
To add cluster administrators, see 'rosa grant user --help'.
To login into the console, open https://console-openshift-console.apps.yuwan-0124-sr1.w3l5.s2.devshift.org and click on gitlab-1.
```

## Step
Create a Google IDP in interactive mode.

```bash
rosa create idp -c <clusrer_id>
rosa create idp -c <clusrer_id> -i
```

## Expect
The idp should be created successfully and work well.
The help message in the interactive should be correct.
```
\# ./rosa create idp -c 1idjapicb4f98lign14em7ur6qk42s5c
? Type of identity provider: [Use arrows to move, type to filter]
github
gitlab
> google
ldap
openid
? Type of identity provider: google
? To use Google as an identity provider, you must first register the application:
- Open the following URL:
https://console.developers.google.com/projectcreate
- Follow the instructions to register your application
- When creating the OAuth client ID, use the following URL for the Authorized redirect URI:
https://oauth-openshift.apps.yuwan-0124-sr1.w3l5.s2.devshift.org/oauth2callback/google-1
? Client ID: [? for help] aa
? Client ID: aa
? Client Secret: [? for help] **
? Hosted domain: [? for help] https://cc.com
? Hosted domain: https://cc.com
I: Configuring IDP for cluster '1idjapicb4f98lign14em7ur6qk42s5c'
I: Identity Provider 'google-1' has been created.
It will take up to 1 minute for this configuration to be enabled.
To add cluster administrators, see 'rosa grant user --help'.
To login into the console, open https://console-openshift-console.apps.yuwan-0124-sr1.w3l5.s2.devshift.org and click on google-1.
```

## Step
Create an LDAP IDP in interactive mode.

```bash
rosa create idp -c <clusrer_id>
rosa create idp -c <clusrer_id> -i
```

## Expect
The idp should be created successfully and work well.
The help message in the interactive should be correct.
```
\# ./rosa create idp -c 1idjapicb4f98lign14em7ur6qk42s5c
? Type of identity provider: [Use arrows to move, type to filter]
github
gitlab
google
> ldap
openid
? Type of identity provider: ldap
? To use LDAP as an identity provider, you must first register the application:
- Open the following URL:
https://docs.openshift.com/dedicated/4/authentication/identity_providers/configuring-ldap-identity-provider.html
- Follow the instructions to register your application
? LDAP URL: [? for help] ldap://aa.com
? LDAP URL: ldap://aa.com
I: Configuring IDP for cluster '1idjapicb4f98lign14em7ur6qk42s5c'
I: Identity Provider 'ldap-1' has been created.
It will take up to 1 minute for this configuration to be enabled.
To add cluster administrators, see 'rosa grant user --help'.
To login into the console, open https://console-openshift-console.apps.yuwan-0124-sr1.w3l5.s2.devshift.org and click on ldap-1.
```

## Step
Create an OpenID IDP in interactive mode.

```bash
rosa create idp -c <clusrer_id>
rosa create idp -c <clusrer_id> -i
```

## Expect
The idp should be created successfully and work well.
The help message in the interactive should be correct.
```
\# ./rosa create idp -c 1idjapicb4f98lign14em7ur6qk42s5c
? Type of identity provider: [Use arrows to move, type to filter]
github
gitlab
google
ldap
> openid
? Type of identity provider: openid
? To use OpenID as an identity provider, you must first register the application:
- Open the following URL:
https://docs.openshift.com/dedicated/4/authentication/identity_providers/configuring-oidc-identity-provider.html
- Follow the instructions to register your application
- When creating the OpenID, use the following URL for the Authorized redirect URI:
https://oauth-openshift.apps.yuwan-0124-sr1.w3l5.s2.devshift.org/oauth2callback/openid-1
? Client ID: [? for help] ggg
? Client ID: ggg
? Client Secret: [? for help] ***
? Issuer URL: [? for help] https://ss.com
? Issuer URL: https://ss.com
? You can indicate which claims to use as the user’s preferred user name, display name, and email address.
At least one claim must be configured to use as the user’s identity. Enter multiple values separated by commas.
? Email (optional): [? for help] e
? Email (optional): e
? Name (optional): [? for help]
? Name (optional):
? Preferred username (optional): [? for help]
? Preferred username (optional):
? OpenID: List of claims to use as the groups names.
? Groups (optional):
I: Configuring IDP for cluster '1idjapicb4f98lign14em7ur6qk42s5c'
I: Identity Provider 'openid-1' has been created.
It will take up to 1 minute for this configuration to be enabled.
To add cluster administrators, see 'rosa grant user --help'.
To login into the console, open https://console-openshift-console.apps.yuwan-0124-sr1.w3l5.s2.devshift.org and click on openid-1.
```

## Step
Repeat the steps on Windows/MacOS/Linux

## Expect
- The function should work well.
- The output should display well
