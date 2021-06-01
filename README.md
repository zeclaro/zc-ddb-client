# DynamoDB Client for IoT Measurements

Python implementation of a DynamoDB client for a Measurements table.

The Measurements table will have the following columns:
- a unique identifier (Primary Key)
- date and time of measurement (Secondary Key)
- measurement qualifier (the thing being measured)
- measurement value
- measurement unit
- device id
- location

# Setup

## AWS config and credentials

This module uses boto3 to connect to DynamoDB. It requires the following AWS configuration files:

- `~/.aws/config`<br>
Example: <br>
```
[default]
    region=us-west-2
    output=json
```

<br>

- `~/.aws/credentials`<br>

Example: <br>
```
[default]
    aws_access_key_id=AKIAIOSFODNN7EXAMPLE
    aws_secret_access_key=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
```

You can create these files manually or use the AWS CLI `configure` command.
<br>
More information [here](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html) and [here](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html#configuration).
<br>

## Client config file

The following file is required to configure zc-dbb-client:
- `~/.zc-ddb-client/config.yml`<br>
Example:<br>

```yaml
dynamo-db:
  table-name: zc-measurements
```