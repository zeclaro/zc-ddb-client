from .ddb_init import create_ddb
import logging
from .env_setup import check_aws_setup_files_exist, get_ddb_table_name

logging.basicConfig(level=logging.INFO)

check_aws_setup_files_exist()
get_ddb_table_name()
create_ddb()
