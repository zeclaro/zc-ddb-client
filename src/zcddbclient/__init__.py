# TODO: when module is imported
#   - run env_setup.py, to ensure the configuration dependencies are met
#   - run ddb_init.py, to create the DDB table if doesn't exist
import env_setup
from ddb_init import create_ddb

create_ddb()
