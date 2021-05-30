"""
Module to:
- validate files ~/.aws/credentials and ~/.aws/config are present
- read the ~/.zc-ddb-client-rc file
    - DDB table name
"""
from .constants import AWS_CREDENTIALS_PATH, AWS_CONFIG_PATH
import logging
from pathlib import Path
import errno
import os


def check_aws_setup_files():
    aws_credentials_file = Path(AWS_CREDENTIALS_PATH)
    aws_config_file = Path(AWS_CONFIG_PATH)
    if not(aws_credentials_file.is_file()):
        logging.error(f"Make sure that file {AWS_CREDENTIALS_PATH} exists and is correctly configured.")
        raise FileNotFoundError(
            errno.ENOENT, os.strerror(errno.ENOENT), AWS_CREDENTIALS_PATH)

    if not(aws_config_file.is_file()):
        logging.error(f"Make sure that file {AWS_CONFIG_PATH} exists and is correctly configured.")
        raise FileNotFoundError(
            errno.ENOENT, os.strerror(errno.ENOENT), AWS_CONFIG_PATH)


# TODO: read ~/.zc-ddb-client-rc file
DDB_TABLE_NAME = "zc-measurements"
