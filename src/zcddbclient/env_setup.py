"""
Module to:
-validate ~/.aws/credentials and ~/.aws/config are present
- read the ~/.zc-ddb-client-rc file
    - target DDB
"""
import logging

# TODO: implement setup of AWS credentials
# cli if module running as main. Will just check and potentially raise exception if module is being imported.

# TODO: read ~/.zc-ddb-client-rc file
DDB_TABLE_NAME = "zc-measurements"
