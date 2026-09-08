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

# Test

## Step
Login with rosacli

## Expect
The config file should be generated locate at <user_config_dir>/ocm/ocm.json

## Step
Check the help message of `rosa -h` and `rosa token -h`

## Expect
yuwan1-mac:1.2.36rc3 yuwan$ ./rosa token -h  
Uses the stored credentials to generate a token.  
  
  
Usage:  
rosa token [flags]  
  
  
Flags:  
--generate Generate a new token.  
--header Print the JSON header.  
-h, --help help for token  
-o, --output string Output format. Allowed formats are [json yaml]  
--payload Print the JSON payload.  
--refresh Print the refresh token instead of the access token.  
--signature Print the signature.  
  
  
Global Flags:  
--color string Surround certain characters with escape sequences to display them in color on the terminal. Allowed options are [auto never always] (default "auto")  
--debug Enable debug mode.  
yuwan1-mac:1.2.36rc3 yuwan$ ./rosa -h | grep token  
token Generates a token

## Step
`rosa token`

## Expect
The token should be display in the output.  
The token should be same with the access_token in the config file.

## Step
`rosa token --generate `

## Expect
New token should be generated and shown.  
The access_token field in the config file should be updated with the new generated token.

## Step
`rosa token --header `

## Expect
$ ./rosa token --header g  
{"alg":"RS256","typ" : "JWT","kid" : "-4elc_VdN_WsOUYf2G4Qxr8GcwIx_KtXUCitatLKlLw"}  
  
The JSON header of the token should be shown.  
It is decoded the access_token in the config file, below script to verify if it is parsed correctly:  
echo $test_token | cut -d '.' -f 1 | tr '_-' '/+' | base64 -D

## Step
`rosa token --payload`

## Expect
The JSON payload of the token should be shown.  
It is decoded the access_token in the config file, below script to verify if it is parsed correctly:  
echo $test_token | cut -d '.' -f 2| base64 -D

## Step
`rosa token --signature`

## Expect
The JSON signature of the token should be shown.  
It is decoded the access_token in the config file, below script to verify if it is parsed correctly:  
echo $test_token | cut -d '.' -f 3 | tr '_-' '/+' | base64 -D

## Step
Repeat step 3~7 adding '--refresh' flag

## Expect
The output should be shown with the refresh_token in the config file, It can verify with the same ways above.

## Step
copy the config file <user_config_dir>/ocm/ocm.json to $HOME/.ocm.json and delete <user_config_dir>/ocm/ocm.json. Then repeat step 3~8

## Expect
The result should be same

## Step
export env variable OCM_CONFIG with a file path, like ~/myconfig.  
copy the config file $HOME/.ocm.json to ~/myconfig and delete $HOME/.ocm.json.  
Then repeat step 3~8

## Expect
The result should be same

## Step
Check validations:  

  * If there is no config file in three path, see 'Setup'.
  * The config file with invalid format.NOTE: the config file is alway generated in most normal case, we still can edit the config file to test this step.

## Expect
- E: Failed to create OCM connection: Not logged in, run the 'rosa login' command  
- It should fail with readable error message.
