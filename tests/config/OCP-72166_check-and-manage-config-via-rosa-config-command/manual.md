# Setup

The config loaded and used by this feature has three locations. ROSA CLI sequentially detects the following paths for the config:

1. The config file full path is defined by the `OCM_CONFIG` environment variable.
2. The config file is located at `$HOME/.ocm.json`.
3. The config file is located at `<user_config_dir>/ocm/ocm.json`.

The user config directory differs by operating system. See the following code, which determines the user directory (a function of the `os` package):

```go
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
```

Config structure:

```go
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
```

# Test

## Step

Log in with ROSA CLI.

## Expect

- The config file is generated at `<user_config_dir>/ocm/ocm.json`.

## Step

Check the help messages of `rosa -h`, `rosa token -h`, `rosa config get -h`, and `rosa config set -h`.

```bash
rosa -h
rosa token -h
rosa config get -h
rosa config set -h
```

## Expect

```
....
config get or set configuration variables
```

- In the `rosa config -h` output, check the config location at `Currently using: ...`.

```bash
rosa config -h
```

```
Get or set variables from a configuration file.

The location of the configuration file is gleaned from the 'OCM_CONFIG' environment variable,
or ~/.ocm.json if that variable is unset. Currently using: /home/jkeyne/.config/ocm/ocm.json

The following variables are supported:

	access_token   Bearer access token.
	client_id      OpenID client identifier.
	client_secret  OpenID client secret.
	insecure       Enables insecure communication with the server.
	refresh_token  Offline or refresh token.
	scopes         OpenID scope.
	token_url      OpenID token URL.
	url            URL of the API gateway.
	user_agent     OCM client UserAgent. Default value is used if not set.
	version        OCM client version. Default value is used if not set.
	fedramp        Indicates FedRAMP.

Note that "rosa config get access_token" gives whatever the file contains - may be missing or expired;
you probably want "rosa token" command instead which will obtain a fresh token if needed.

If 'OCM_KEYRING' is set, the configuration file is ignored and the keyring is used instead. The
following backends are supported for the keyring:

- macOS: keychain, pass
- Linux: secret-service, pass
- Windows: wincred

Available Keyrings on your OS: secret-service, pass

Usage:
  rosa config [command]

Available Commands:
  get         Prints the value of a config variable
  set         Sets the variable's value

Flags:
  -h, --help   help for config

Global Flags:
      --color string   Surround certain characters with escape sequences to display them in color on the terminal. Allowed options are [auto never always] (default "auto")
      --debug          Enable debug mode.

Use "rosa config [command] --help" for more information about a command.
```

## Step

Run `rosa config get <supported variables>`.

The following variables are supported:

- `access_token`: Bearer access token.
- `client_id`: OpenID client identifier.
- `client_secret`: OpenID client secret.
- `insecure`: Enables insecure communication with the server.
- `refresh_token`: Offline or refresh token.
- `scopes`: OpenID scope.
- `token_url`: OpenID token URL.
- `url`: URL of the API gateway.
- `fedramp`: Indicates FedRAMP.

To test all supported variables, edit the config file to add all supported variables. See the config structure in Setup.

## Expect

- All variables are shown correctly and match the config file.
- If a field is not in the config file, it returns the JSON default value. For `bool`, it returns `true`; other field types return empty values.

## Step

Set variables using `rosa config set <variable>`.

## Expect

- The new value is set by the command. Run `rosa config get <variable>` to verify it.
- The value in the config file is updated accordingly.
- Setting `scopes` fails with `Setting scopes is unsupported`.

## Step

Delete the config file in the default user config path, then set config with `rosa config set <variable>`.

## Expect

- It is set successfully. Run `rosa config get <variable>` to verify it.
- A new config file is created in the user config directory. See Setup.

## Step

Get and set an unsupported variable with the above commands.

## Expect

- The commands fail with an error.

```bash
rosa config set not_suuport aaa
rosa config get not_suuport
```

```
E: 'not_suuport' is not a supported setting

E: 'not_suuport' is not a supported setting
```

## Step

Run `rosa login`, then copy the config file from `<user_config_dir>/ocm/ocm.json` to `$HOME/.ocm.json` and delete `<user_config_dir>/ocm/ocm.json`. Then repeat steps 3 through 5.

## Expect

- The result is the same.

## Step

Run `rosa login`, then export the `OCM_CONFIG` environment variable with a file path such as `~/myconfig`. Copy the config file from `$HOME/.ocm.json` to `~/myconfig` and delete `$HOME/.ocm.json`. Then repeat steps 3 through 5.

## Expect

- The result is the same.

## Step

Delete the config file to ensure no config file is in any of the three locations described in Setup. Then try to get one config variable.

## Expect

```
E: Config file '/Users/yuwan/Library/Application Support/ocm/ocm.json' does not exist
```
