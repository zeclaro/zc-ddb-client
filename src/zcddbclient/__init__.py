# TODO: when module is imported
#   - run env_setup.py, to ensure the configuration dependencies are met
#   - run ddb_init.py, to create the DDB table if doesn't exist
from .ddb_init import create_ddb
import logging

logging.basicConfig(level=logging.INFO)

create_ddb()
