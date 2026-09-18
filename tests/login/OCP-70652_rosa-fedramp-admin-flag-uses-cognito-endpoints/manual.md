# Setup
- Tester must be FedRAMP onboarded.
- Must be connected to the FedRAMP environment using AppGate VPN.
- Must have credentials in Cognito.
- Rosa CLI must be `1.2.24` or higher.
- AWS GovCloud CLI access must be set up.
- Do not use a proxy.

# Test

## Step
1. Ensure the user can log into the production environment using the admin flag.

Capture a token from `https://api-admin.openshiftusgov.com/auth`.

Log into production using the token:

```bash
rosa login --env production --govcloud --admin --token <TOKEN>
```

## Expect
- Login should be successful and show the api-admin URL.

```
I: Logged in as 'ccrum' on 'https://api-admin.openshiftusgov.com'
```

## Step
2. Ensure the rosa command in production is successful.

```bash
rosa whoami
```

## Expect
```
AWS ARN: arn:aws-us-gov:iam::asdasd
AWS Account ID: asd
AWS Default Region: us-gov-east-1
OCM API: https://api.int.openshiftusgov.com
OCM Account Email: asf
OCM Account ID: asf
OCM Account Name: TEst Test
OCM Account Username: chad.crum@openshiftusgov.com
OCM Organization External ID: 2222
OCM Organization ID: asdasdasdasddsa
OCM Organization Name: qe-idp
```

## Step
3. Ensure the user can log into the integration environment using the admin flag.

Capture a token from `https://api-admin.int.openshiftusgov.com/auth`.

Log into integration using the token:

```bash
rosa login --env integration --govcloud --admin --token <TOKEN>
```

## Expect
- Login should be successful and show the api-admin URL.

```
I: Logged in as 'ccrum' on 'https://api-admin.integration.openshiftusgov.com'
```

## Step
4. Ensure the rosa command in integration is successful.

```bash
rosa whoami
```

## Expect
```
AWS ARN: arn:aws-us-gov:iam::asdasd
AWS Account ID: asd
AWS Default Region: us-gov-east-1
OCM API: https://api.int.openshiftusgov.com
OCM Account Email: asf
OCM Account ID: asf
OCM Account Name: TEst Test
OCM Account Username: chad.crum@openshiftusgov.com
OCM Organization External ID: 2222
OCM Organization ID: asdasdasdasddsa
OCM Organization Name: qe-idp
```

## Step
5. Ensure the user can log into the stage environment using the admin flag.

Capture a token from `https://api-admin.stage.openshiftusgov.com/auth`.

Log into stage using the token:

```bash
rosa login --env stage --govcloud --admin --token <TOKEN>
```

## Expect
- Login should be successful and show the api-admin URL.

```
I: Logged in as 'ccrum' on 'https://api-admin.stage.openshiftusgov.com'
```

## Step
6. Ensure the rosa command in stage is successful.

```bash
rosa whoami
```

## Expect
```
AWS ARN: arn:aws-us-gov:iam::asdasd
AWS Account ID: asd
AWS Default Region: us-gov-east-1
OCM API: https://api.int.openshiftusgov.com
OCM Account Email: asf
OCM Account ID: asf
OCM Account Name: TEst Test
OCM Account Username: chad.crum@openshiftusgov.com
OCM Organization External ID: 2222
OCM Organization ID: asdasdasdasddsa
OCM Organization Name: qe-idp
```
