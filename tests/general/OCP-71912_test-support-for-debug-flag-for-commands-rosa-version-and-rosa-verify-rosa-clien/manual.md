# Setup

```
$ rosa version
1.2.34 (Build: 7b4bd676)
```

# Test

## Step
Run `rosa version --debug`.

## Expect
The command should run successfully.

```
$ rosa version --debug
1.2.34 (Build: 7b4bd676)
time=2024-02-08T13:12:20+05:30 level=debug msg=Request method is GET
time=2024-02-08T13:12:20+05:30 level=debug msg=Request URL is 'https://mirror.openshift.com/pub/openshift-v4/clients/rosa/'
time=2024-02-08T13:12:21+05:30 level=debug msg=Response status is '200 OK'
time=2024-02-08T13:12:21+05:30 level=debug msg=Response header 'Cache-Control' is 'max-age=0'
time=2024-02-08T13:12:21+05:30 level=debug msg=Response header 'Content-Length' is '30493'
time=2024-02-08T13:12:21+05:30 level=debug msg=Response header 'Content-Type' is 'text/html'
........
I: Your ROSA CLI is up to date
```

The network requests made while running the command should be visible in the CLI.

## Step
Run `rosa verify rosa-client --debug`.

## Expect
The command should run successfully.

```
$ rosa verify rosa-client --debug
time=2024-02-08T13:06:32+05:30 level=debug msg=Request method is GET
time=2024-02-08T13:06:32+05:30 level=debug msg=Request URL is 'https://mirror.openshift.com/pub/openshift-v4/clients/rosa/'
time=2024-02-08T13:06:33+05:30 level=debug msg=Response status is '200 OK'
time=2024-02-08T13:06:33+05:30 level=debug msg=Response header 'Cache-Control' is 'max-age=0'
time=2024-02-08T13:06:33+05:30 level=debug msg=Response header 'Content-Length' is '30493'
........
I: Your ROSA CLI is up to date.
```

The network requests made while running the command should be visible in the CLI.
