""" Constants used through the project """
from os.path import  expanduser

home = expanduser("~")

TIME_STAMP_FORMAT = "%d/%m/%Y %H:%M:%S"
UUID_GENERATION_ORIGIN_DATE = "11/06/2016 18:00:00"
AWS_CREDENTIALS_PATH = f"{home}/.aws/credentials"
AWS_CONFIG_PATH = f"{home}/.aws/config"
CONFIG_FILE_PATH = f"{home}/.zc-ddb-client/config.yml"
