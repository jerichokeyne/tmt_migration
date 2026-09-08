# Test

## Step
Prepare a HCP cluster with " --external-auth-providers-enabled"

## Expect

## Step
Create break_glass_credential via interactive mode  
$rosa create break-glass-credential -c 2a83k03lilf22l1d4kqkkt96i0hfgpbr -i

## Expect
-Check the parameters are optional  
-Input the ? to check help message  
./rosa create break-glass-credential -c 2a83k03lilf22l1d4kqkkt96i0hfgpbr   
I: Enabling interactive mode  
? Username (optional):   
? Expiration duration (optional): 2h
