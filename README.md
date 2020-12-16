# service-now-api
Example Python code for manipulating incidents in ServiceNOW

## Set Up

### Required Software
- Install version Python 3.6 or later
- Install the requests library

### Required Configuration
- set environment variable `SNOW_USER` to `admin`
- set environment variable `SNOW_PWD` to admin password
- set environment variable `SNOW_INSTANCE` to admin password

## Creating an Incident with a Caller Id

```
$ ./incident-create.py david.gwartney@kore.com
```
