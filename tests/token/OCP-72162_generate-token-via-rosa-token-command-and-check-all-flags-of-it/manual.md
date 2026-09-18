# Setup
The configuration loaded and used by this feature has three locations. ROSA CLI sequentially detects the following paths:

1. The full config-file path defined by the `OCM_CONFIG` environment variable.
2. The config file in the home directory: `$HOME/.ocm.json`.
3. The config file in the user config directory: `<user_config_dir>/ocm/ocm.json`.

The user config directory differs by operating system. Use the following `os` package function to determine it:

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

# Test

## Step
Log in with ROSA CLI.

## Expect
The config file is generated at `<user_config_dir>/ocm/ocm.json`.

## Step
Check the help message for `rosa -h` and `rosa token -h`.

## Expect
```
Uses the stored credentials to generate a token.

Usage:
  rosa token [flags]

Flags:
      --generate    Generate a new token.
      --header      Print the JSON header.
  -h, --help        help for token
      --payload     Print the JSON payload.
      --refresh     Print the refresh token instead of the access token.
      --signature   Print the signature.

Global Flags:
      --color string   Surround certain characters with escape sequences to display them in color on the terminal. Allowed options are [auto never always] (default "auto")
      --debug          Enable debug mode.
```

```
token       Generates a token
```

## Step
```bash
rosa token
```

## Expect
- The token is displayed in the output.
- The token matches the `access_token` in the config file.

## Step
```bash
rosa token --generate
```

## Expect
- A new token is generated and displayed.
- The `access_token` field in the config file is updated with the newly generated token.

## Step
```bash
rosa token --header
```

## Expect
```
{"alg":"RS256","typ" : "JWT","kid" : "-4elc_VdN_WsOUYf2G4Qxr8GcwIx_KtXUCitatLKlLw"}
```

The JSON header of the token is displayed. It decodes the `access_token` in the config file; use the following script to verify that it is parsed correctly:

```bash
echo $test_token | cut -d '.' -f 1 | tr '_-' '/+' | base64 -D
```

## Step
```bash
rosa token --payload
```

## Expect
The JSON payload of the token is displayed. It decodes the `access_token` in the config file; use the following script to verify that it is parsed correctly:

```bash
echo $test_token | cut -d '.' -f 2| base64 -D
```

## Step
```bash
rosa token --signature
```

## Expect
The JSON signature of the token is displayed. It decodes the `access_token` in the config file; use the following script to verify that it is parsed correctly:

```bash
echo $test_token | cut -d '.' -f 3 | tr '_-' '/+' | base64 -D
```

## Step
Repeat steps 3 through 7 with the `--refresh` flag.

## Expect
The output matches the `refresh_token` in the config file and can be verified using the methods above.

## Step
Copy `<user_config_dir>/ocm/ocm.json` to `$HOME/.ocm.json` and delete `<user_config_dir>/ocm/ocm.json`. Then repeat steps 3 through 8.

## Expect
The result is the same.

## Step
Export `OCM_CONFIG` with a file path, such as `~/myconfig`. Copy `$HOME/.ocm.json` to `~/myconfig` and delete `$HOME/.ocm.json`. Then repeat steps 3 through 8.

## Expect
The result is the same.

## Step
Check validations:

- There is no config file in the three paths. See Setup.
- The config file has an invalid format. The config file is always generated in most normal cases, so edit it to test this step.

## Expect
- ```
  E: Failed to create OCM connection: Not logged in, run the 'rosa login' command
  ```
- It fails with a readable error message.
