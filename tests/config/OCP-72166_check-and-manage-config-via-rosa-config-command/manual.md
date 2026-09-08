# Setup
the config loaded and used by this feature has three locations, rosacli sequentially detects the bellow three path for the config:  
  

  1. The config file full path is defined by "OCM_CONFIG" env.
  2. The config file located at home dir, "$HOME/.ocm.json"
  3. The config file located at user config dir,<user_config_dir>/ocm/ocm.json

  
The use config dir are different for different OS, see bellow code to determine the user dir(that is a function of os package):  
`  
func UserConfigDir() (string, error) {  
var dir string  
switch runtime.GOOS {  
case "windows":  
dir = Getenv("AppData")  
if dir == "" {  
return "", errors.New("%AppData% is not defined")  
}  
case "darwin", "ios":  
dir = Getenv("HOME")  
if dir == "" {  
return "", errors.New("$HOME is not defined")  
}  
dir += "/Library/Application Support"  
case "plan9":  
dir = Getenv("home")  
if dir == "" {  
return "", errors.New("$home is not defined")  
}  
dir += "/lib"  
default: // Unix  
dir = Getenv("XDG_CONFIG_HOME")  
if dir == "" {  
dir = Getenv("HOME")  
if dir == "" {  
return "", errors.New("neither $XDG_CONFIG_HOME nor $HOME are defined")  
}  
dir += "/.config"  
}  
}  
return dir, nil  
}  
  
`  
  
  
Config Struction is as bellow:  
type Config struct {  
AccessToken string `json:"access_token,omitempty" doc:"Bearer access token."`  
ClientID string `json:"client_id,omitempty" doc:"OpenID client identifier."`  
ClientSecret string `json:"client_secret,omitempty" doc:"OpenID client secret."`  
Insecure bool `json:"insecure,omitempty" doc:"Enables insecure communication with the server."`  
RefreshToken string `json:"refresh_token,omitempty" doc:"Offline or refresh token."`  
Scopes []string `json:"scopes,omitempty" doc:"OpenID scope."`  
TokenURL string `json:"token_url,omitempty" doc:"OpenID token URL."`  
URL string `json:"url,omitempty" doc:"URL of the API gateway."`  
FedRAMP bool `json:"fedramp,omitempty" doc:"Indicates FedRAMP."`  
}

# Test

## Step
Login with rosacli

## Expect
The config file should be generated locate at <user_config_dir>/ocm/ocm.json

## Step
Check the help message of `rosa -h` and `rosa token -h` and `rosa config get -h` and `rosa config set -h`

## Expect
$ ./rosa -h   
....  
config get or set configuration variables  
  
  
- In the output `rosa config -h` , check the config location at ''Currently using: ..."  
$ ./rosa config -h   
Get or set variables from a configuration file.  
  
  
The location of the configuration file is gleaned from the 'OCM_CONFIG' environment variable,  
or ~/.ocm.json if that variable is unset. Currently using: /Users/yuwan/workplace/temp/myocmconfig  
  
  
The following variables are supported:  
  
  
access_token Bearer access token.  
client_id OpenID client identifier.  
client_secret OpenID client secret.  
insecure Enables insecure communication with the server.  
refresh_token Offline or refresh token.  
scopes OpenID scope.  
token_url OpenID token URL.  
url URL of the API gateway.  
fedramp Indicates FedRAMP.  
  
  
Note that "rosa config get access_token" gives whatever the file contains - may be missing or expired;  
you probably want "rosa token" command instead which will obtain a fresh token if needed.  
  
  
Usage:  
rosa config [command]  
  
  
Available Commands:  
get Prints the value of a config variable  
set Sets the variable's value  
  
  
Flags:  
-h, --help help for config  
  
  
Global Flags:  
--color string Surround certain characters with escape sequences to display them in color on the terminal. Allowed options are [auto never always] (default "auto")  
--debug Enable debug mode.

## Step
Run `rosa config get <supported variables>` command.  
  
The following variables are supported:  
  
  
access_token Bearer access token.  
client_id OpenID client identifier.  
client_secret OpenID client secret.  
insecure Enables insecure communication with the server.  
refresh_token Offline or refresh token.  
scopes OpenID scope.  
token_url OpenID token URL.  
url URL of the API gateway.  
fedramp Indicates FedRAMP  
  
To testing all the supported variables, we can edit the config file adding all supported variables., see the config struction in 'Setup' part.

## Expect
All variables can be shown correctly, same with the one in the config file.  
If one field is not in the config file, It will return the json default value. For bool, return true and other type field return empty.

## Step
Set varibles using `rosa config set <variable>` command.

## Expect
The new value should be set by the command, run `rosa config get <variable>` to check if it works.  
The value in the config file should be updated accordingly.  
It should fail with error "Setting scopes is unsupported" when set scopes variable.

## Step
Delete the config file in the default use config path, the set some config via `rosa config set <variable>` command.

## Expect
It should be set successfully, run `rosa config get <variable>` to check if it works.  
New config file will be created in the user config dir.(See 'Setup' part)

## Step
Get and set an not-support varible via above command.

## Expect
It will fail with error:  
$ ./rosa config set not_suuport aaa  
E: 'not_suuport' is not a supported setting  
  
  
$ ./rosa config get not_suuport   
E: 'not_suuport' is not a supported setting

## Step
Run `rosa login` then  
copy the config file <user_config_dir>/ocm/ocm.json to $HOME/.ocm.json and delete <user_config_dir>/ocm/ocm.json. Then repeat 3~5

## Expect
The result should be same

## Step
Run `rosa login` then  
export env variable OCM_CONFIG with a file path, like ~/myconfig.  
copy the config file $HOME/.ocm.json to ~/myconfig and delete $HOME/.ocm.json.  
Then repeat step 3~5

## Expect
The result should be same

## Step
Delete the config file to make sure no config file in the three location, see 'Setup' part. Then try to get one config variable.

## Expect
E: Config file '/Users/yuwan/Library/Application Support/ocm/ocm.json' does not exist
