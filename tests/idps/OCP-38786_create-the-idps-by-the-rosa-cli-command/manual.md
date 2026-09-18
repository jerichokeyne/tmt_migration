# Test

## Step
Log in with the rosa cli

## Expect

## Step
Create Github IDP by the command.

## Expect
NOET: It needs to cover the organizations and teams.
The idp should be created successfully and work well.
```
\# ./rosa create idp -c 1idjapicb4f98lign14em7ur6qk42s5c --type github --name github-test --mapping-method claim --client-id ccc --client-secret sss --ca sss.cert --hostname https://aa.com --organizations org
I: Configuring IDP for cluster '1idjapicb4f98lign14em7ur6qk42s5c'
I: Identity Provider 'github-test' has been created.
It will take up to 1 minute for this configuration to be enabled.
To add cluster administrators, see 'rosa grant user --help'.
To login into the console, open https://console-openshift-console.apps.yuwan-0124-sr1.w3l5.s2.devshift.org and click on github-test.
```

## Step
Create Github IDP by the command with some ,but not all,required parameter.

## Expect
The interactive mode will be called up.
The parameter already input in the command should be treated as the default value.
```
\# ./rosa create idp -c 1idjapicb4f98lign14em7ur6qk42s5c --type github --mapping-method claim --client-secret sss --teams org/myteam
? To use GitHub as an identity provider, you must first register the application:
- Open the following URL:
https://github.com/organizations/org/settings/applications/new?oauth_application%5Bcallback_url%5D=https%3A%2F%2Foauth-openshift.apps.yuwan-0124-sr1.w3l5.s2.devshift.org%2Foauth2callback%2Fgithub-2&oauth_application%5Bname%5D=yuwan-0124-sr1&oauth_application%5Burl%5D=https%3A%2F%2Fconsole-openshift-console.apps.yuwan-0124-sr1.w3l5.s2.devshift.org
- Click on 'Register application'
? Client ID: [? for help] cc
? Client ID: cc
I: Configuring IDP for cluster '1idjapicb4f98lign14em7ur6qk42s5c'
I: Identity Provider 'github-2' has been created.
It will take up to 1 minute for this configuration to be enabled.
To add cluster administrators, see 'rosa grant user --help'.
To login into the console, open https://console-openshift-console.apps.yuwan-0124-sr1.w3l5.s2.devshift.org and click on github-2.

\# ./rosa create idp -c 1idjapicb4f98lign14em7ur6qk42s5c --type github --name github-test-1 --mapping-method claim --client-id ccc --organizations org
? To use GitHub as an identity provider, you must first register the application:
- Open the following URL:
https://github.com/organizations/org/settings/applications/new?oauth_application%5Bcallback_url%5D=https%3A%2F%2Foauth-openshift.apps.yuwan-0124-sr1.w3l5.s2.devshift.org%2Foauth2callback%2Fgithub-test-1&oauth_application%5Bname%5D=yuwan-0124-sr1&oauth_application%5Burl%5D=https%3A%2F%2Fconsole-openshift-console.apps.yuwan-0124-sr1.w3l5.s2.devshift.org
- Click on 'Register application'
? Client ID: [? for help] (ccc)
? Client ID: ccc
? Client Secret: [? for help] ***
I: Configuring IDP for cluster '1idjapicb4f98lign14em7ur6qk42s5c'
I: Identity Provider 'github-test-1' has been created.
It will take up to 1 minute for this configuration to be enabled.
To add cluster administrators, see 'rosa grant user --help'.
To login into the console, open https://console-openshift-console.apps.yuwan-0124-sr1.w3l5.s2.devshift.org and click on github-test-1.
```

## Step
Create Gitlab IDP by the command.

## Expect
The idp should be created successfully and work well.
```
\# ./rosa create idp -c 1idjapicb4f98lign14em7ur6qk42s5c --type gitlab --name gitlab-test --mapping-method claim --client-id ccc --client-secret sss --ca sss.cert --host-url https://mygitlab.com
I: Configuring IDP for cluster '1idjapicb4f98lign14em7ur6qk42s5c'
I: Identity Provider 'gitlab-test' has been created.
It will take up to 1 minute for this configuration to be enabled.
To add cluster administrators, see 'rosa grant user --help'.
To login into the console, open https://console-openshift-console.apps.yuwan-0124-sr1.w3l5.s2.devshift.org and click on gitlab-test.
```

## Step
Create Gitlab IDP by the command with some ,but not all,required parameter.

## Expect
The interactive mode will be called up.
The parameter already input in the command should be treated as the default value.

## Step
Create Google IDP by the command.

## Expect
The idp should be created successfully and work well.
```
[root@yuwan moactl]# ./rosa create idp -c 1idjapicb4f98lign14em7ur6qk42s5c --type google --name google-test --mapping-method claim --client-id ccc --client-secret sss --hosted-domain https://mygoogle.com
I: Configuring IDP for cluster '1idjapicb4f98lign14em7ur6qk42s5c'
I: Identity Provider 'google-test' has been created.
It will take up to 1 minute for this configuration to be enabled.
To add cluster administrators, see 'rosa grant user --help'.
To login into the console, open https://console-openshift-console.apps.yuwan-0124-sr1.w3l5.s2.devshift.org and click on google-test.
```

## Step
Create Google IDP by the command with some ,but not all,required parameter.

## Expect
The interactive mode will be called up.
The parameter already input in the command should be treated as the default value.

## Step
Create Ldap IDP by the command.

## Expect
The idp should be created successfully and work well.
It needs to cover '--insecure'.
```
\# ./rosa create idp -c 1idjapicb4f98lign14em7ur6qk42s5c --type ldap --name ldap-test --mapping-method claim --url ldap://myldap.com --bind-dn dn --bind-password bp --id-attributes id --username-attributes ua --name-attributes na --email-attributes email --ca sss.cert
I: Configuring IDP for cluster '1idjapicb4f98lign14em7ur6qk42s5c'
I: Identity Provider 'ldap-test' has been created.
It will take up to 1 minute for this configuration to be enabled.
To add cluster administrators, see 'rosa grant user --help'.
To login into the console, open https://console-openshift-console.apps.yuwan-0124-sr1.w3l5.s2.devshift.org and click on ldap-test.

\# ./rosa create idp -c 1idjapicb4f98lign14em7ur6qk42s5c --type ldap --name ldap-test-1 --mapping-method claim --url ldap://myldap.com --bind-dn dn --bind-password bp --id-attributes id --username-attributes ua --name-attributes na --email-attributes email --insecure
I: Configuring IDP for cluster '1idjapicb4f98lign14em7ur6qk42s5c'
I: Identity Provider 'ldap-test-1' has been created.
It will take up to 1 minute for this configuration to be enabled.
To add cluster administrators, see 'rosa grant user --help'.
To login into the console, open https://console-openshift-console.apps.yuwan-0124-sr1.w3l5.s2.devshift.org and click on ldap-test-1.
```

## Step
Create LDAP IDP by the command with some ,but not all,required parameter.

## Expect
The interactive mode will be called up.
The parameter already input in the command should be treated as the default value.

## Step
Create OpenID IDP by the command.

## Expect
The idp should be created successfully and work well.
```
\# ./rosa create idp -c 1idjapicb4f98lign14em7ur6qk42s5c --type openid --name openid-test --mapping-method claim --client-id ccc --client-secret sss --issuer-url https://myopenid.com --email-claims email --groups-claims g1,g2 --name-claims nc --username-claims uc --extra-scopes s1,s2
I: Configuring IDP for cluster '1idjapicb4f98lign14em7ur6qk42s5c'
I: Identity Provider 'openid-test' has been created.
It will take up to 1 minute for this configuration to be enabled.
To add cluster administrators, see 'rosa grant user --help'.
To login into the console, open https://console-openshift-console.apps.yuwan-0124-sr1.w3l5.s2.devshift.org and click on openid-test.
```

## Step
Create Openid IDP by the command with some ,but not all,required parameter.

## Expect
The interactive mode will be called up.
The parameter already input in the command should be treated as the default value.

## Step
Repeat the steps on Windows/MacOS/Linux

## Expect
- The function should work well
- The output should display well
