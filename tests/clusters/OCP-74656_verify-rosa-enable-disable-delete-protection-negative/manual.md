# Setup
Create a classic and HCP cluster

# Test

## Step

Verify invalid argument fails as expected
```bash
rosa edit cluster -c jf-hcp-57094 --enable-delete-protection=aaaa
rosa edit cluster -c jf-hcp-57094 --enable-delete-protection=
```

## Expect

```
Error: invalid argument "aaaa" for "--enable-delete-protection" flag: strconv.ParseBool: parsing "aaaa": invalid syntax
Error: invalid argument "" for "--enable-delete-protection" flag: strconv.ParseBool: parsing "": invalid syntax
```
