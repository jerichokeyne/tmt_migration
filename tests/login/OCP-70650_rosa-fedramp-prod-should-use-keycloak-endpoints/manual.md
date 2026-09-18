# Setup
- Tester must be FedRAMP onboarded.
- Rosa CLI must be `1.2.33` or higher.
- AWS GovCloud CLI access must be set up.
- Do not use a proxy.

# Test

## Step
1. Rosa client uses FedRAMP Keycloak endpoints when connecting to the FedRAMP production environment.

Browse to the production environment and get a token:

`https://console.openshiftusgov.com/openshift/token`

Use the token with the non-aliased endpoint:

```bash
rosa login --govcloud --token <token>
```

## Expect
- Login should be successful.

```
II: Logged in as 'chad.crum@openshiftusgov.com' on 'https://api.openshiftusgov.com'
```

## Step
2. Ensure the rosa command is successful.

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
