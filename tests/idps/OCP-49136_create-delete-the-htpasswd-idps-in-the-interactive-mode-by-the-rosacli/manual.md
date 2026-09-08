# Test

## Step
Log in with the rosa cli

## Expect

## Step
Create HTPasswd IDP in the interactive mode.  
\#rosa create idp -c <clusrer_id>  
\#rosa create idp -c <clusrer_id> -i

## Expect
- It allows to create multi users in the interactive mode.  
- The help message should be shown after input '?'  
- Query the idp by OCM API, the result should be shown correctly  
- The cluster console can be logged with the username and password  
yuwan1-mac:rosa yuwan$ ./rosa create idp -c 252jb43vlb7c01ieo7rbsbboc0qtojn6 -i   
I: Interactive mode enabled.  
Any optional fields can be left empty and a default will be selected.  
? Type of identity provider: htpasswd  
? Identity provider name: da  
? Configure users from HTPasswd file (optional): /Users/yuwan/workplace/rosa/yw0719htpasswdfile1  
I: Configuring IDP for cluster '252jb43vlb7c01ieo7rbsbboc0qtojn6'  
I: Identity Provider 'da' has been created.  
It may take several minutes for this access to become active.  
To add cluster administrators, see 'rosa grant user --help'.  
- There is an option "? Configure users from HTPasswd file (optional):" to input the path of the htpasswd idp file. It will continue to ask "? Add another user" after add by file.   
- If the file cannot be found by the path, it will return error; If the user name is existed in some file, it will return error  
  
I: To log in to the console, open https://console-openshift-console.apps.yuwan-jntsr1.ck80.s1.devshift.org and click on 'da'.  
? Add another user (optional): Yes  
? Username: test4  
? Password: [? for help] *********************  
I: User 'test4' added  
? Add another user (optional): No  
yuwan1-mac:rosa yuwan$

## Step
Try to create admin via `rosa create admin`

## Expect
- There should be one more item in the response of retrieving HTPasswd idp by OCM API  
- There is a cluster-admin user in the cluster-admins group, it can be retrieved by OCM API  
- The cluster console can be logged with the username and password created by `rosa create admin`

## Step
Try to create another HTPasswd idp.

## Expect
The another HTPasswd idp should be created successfully.

## Step
Delete the idp

## Expect
- The idp with all users including the cluster-admin user are deleted.

## Step
Create admin firstly via `rosa create admin`

## Expect
- There should be one item in the response of retrieving HTPasswd idp by OCM API  
- There is a cluster-admin user in the cluster-admins group, it can be retrieved by OCM API  
- The cluster console can be logged with the username and password created by `rosa create admin`

## Step
Repeat step2 to create one HTPasswd idp with multi users

## Expect
- A new htpasswd idp will be created  
- Query the idp by OCM API, the result should be shown correctly  
- The cluster console can be logged with the username and password

## Step
Revoke the admin

## Expect
- Query the idp by OCM API, the result should has no cluster-admin user  
- The cluster-admin user is removed from the cluster-admins group

## Step
Repeat the steps on Windows/MacOS/Linux

## Expect
- The function should work well  
- The output should display well
