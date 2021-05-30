# TODO: when module is imported
#   - run env_setup.py, to ensure the configuration dependencies are met
#   - run ddb_init.py, to create the DDB table if doesn't exist
from .ddb_init import create_ddb
import logging
from .env_setup import check_aws_setup_files

logging.basicConfig(level=logging.INFO)

check_aws_setup_files()
create_ddb()
