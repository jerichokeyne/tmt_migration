# Test

## Step
Log in with the rosa cli

## Expect

## Step
Check the validation for the common parameter by the command.  
1. invalid type  
2. invalid mapping method (this validation is removed for htpasswd idp's)  
~~3. invalid ca file path~~

## Expect
1.E: Expected a valid IDP type. Options are [github gitlab google ldap openid]  
2.E: Failed to add IDP to cluster '1iekajbm5j6ps8hh5ddjdpe64880c1q6': Only claim/add/generate/lookup is supported in the 'mapping_method' field  
3.E: Failed to create IDP for cluster '1iekajbm5j6ps8hh5ddjdpe64880c1q6': Expected a valid certificate bundle: open ssss: no such file or directory

## Step
Check the validation for the Github idp creation in the command mode.  
1.invalid format of teams

## Expect
1.E: Failed to add IDP to cluster '1iekajbm5j6ps8hh5ddjdpe64880c1q6': 'team' 'jojo' in not in format <org/team>  
2.If not all required parameter is inputed, the interactive mode will be called up and the parameter already inputed in the command will be treated as the default value

## Step
Check the validation for the Gitlab idp creation in the command mode.  
1. invalid type  
2. invalid mapping method  
3. invalid ca file path

## Expect
1.Some with the step3  
2. If not all required parameter is inputed, the interactive mode will be called up and the parameter already inputed in the command will be treated as the default value

## Step
Check the validation for the Google idp creation in the command mode.  
1. invalid type  
2. invalid mapping method  
~~3. invalid ca file path~~

## Expect
1.Some with the step3  
2.If not all required parameter is inputed, the interactive mode will be called up and the parameter already inputed in the command will be treated as the default value

## Step
Check the validation for the LDAP idp creation in the command mode.  
1.bind_dn and bind_password must be input at the same time. and if not input, it is empty as default  
2. The ldap url with incorrect format  
3. For the ldap attributes, it will use the default values if they are not input  
4. ca and insecure cannot be set at the same time

## Expect
1.If not all required parameter is inputed, the interactive mode will be called up and the parameter already inputed in the command will be treated as the default value  
2.E: Failed to create IDP for cluster '1iekajbm5j6ps8hh5ddjdpe64880c1q6': Expected LDAP URL to have an ldap:// or ldaps:// scheme  
3.E: Failed to create IDP for cluster '1iekajbm5j6ps8hh5ddjdpe64880c1q6': Cannot use certificate bundle with an insecure connection

## Step
Check the validation for the Openid idp creation in the command mode.  
1. invalid type  
2. invalid mapping method  
3. invalid ca file path  
4. the groups item includes 'dedicated-admins','cluster-admins' or both  
5. add idp with the groups-claim on the cluster which version is lower than 4.10.0

## Expect
Same with the step3.  
- E: Failed to add IDP to cluster 'yuwan-sts4': Claim groups name cannot be one of 'dedicated-admins','cluster-admins'  
E: Failed to add IDP to cluster '1si79jfoflh9vn0rp0dhbd5nsbdlpj71': Cannot set OpenID identity provider groups claim for cluster version older than '4.10.0'

## Step
Repeat the steps on Windows/MacOS/Linux

## Expect
- The function should work well  
- The output should display well
