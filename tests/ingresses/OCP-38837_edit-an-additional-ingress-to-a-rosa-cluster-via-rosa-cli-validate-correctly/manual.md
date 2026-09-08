# Test

## Step
note: cannot create additional ingress on staging/int env since the "managed-ingress-support" is toggled on for all users on staging/int env from now (09/18)  
Edit/Delete additional ingress should work if it is present  
Edit default ingress is not changed.  
  
Launch rosa cli to staging env

## Expect

## Step
Prepare a ready rosa cluster

## Expect

## Step
Run command to record the ingress:  
$ rosa list ingress -c <cluster name>

## Expect

## Step
Run command to edit ingress with invalid label:  
$ rosa edit ingress <ingress id> -c <cluster name> --label-match "aaa,"

## Expect
- There will be error message returned E: Expected key=value format for label-match  
- Ingress not updated

## Step
Run command with non-allowed flag  
$ rosa edit ingress <ingress id> --nonallowed

## Expect
- The help message should show  
- Error message : Error: unknown flag: --nonallowed

## Step
Run command without cluster indicated  
$ rosa edit ingress <ingress id>

## Expect
- Error message: Error: required flag(s) "cluster" not set  
- The help usage should show

## Step
Run command with all of the flags in the help message

## Expect
- All of flags should be meaningful and can work correctly
