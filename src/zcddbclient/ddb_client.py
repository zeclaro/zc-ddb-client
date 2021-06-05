""" Provides a DynamoDB client to handle operations against a measurements table. """
# TODO:
#   implement the other operations: read, delete, update

import boto3
import logging
from .env_setup import DDB_TABLE_NAME
from datetime import datetime
from .constants import UUID_GENERATION_ORIGIN_DATE, TIME_STAMP_FORMAT
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(DDB_TABLE_NAME)


def _generate_uuid(device_id: str):
    origin = datetime.strptime(UUID_GENERATION_ORIGIN_DATE, TIME_STAMP_FORMAT)
    now = datetime.now()
    microseconds = (now - origin).total_seconds() * 1000 * 1000
    return f"#{device_id}#{int(microseconds)}"


def write_item(*, qualifier: str, value: str, unit: str, device_id: str, location: str):
    item_uuid = _generate_uuid(device_id)
    logging.debug(f"Writing item {item_uuid} in table {DDB_TABLE_NAME}")
    now = datetime.now()

    check_float = isinstance(float(value), float)
    assert check_float is True

    item = dict()

    item["PK"] = item_uuid
    item["SK"] = now.strftime(TIME_STAMP_FORMAT)
    item["qualifier"] = qualifier
    item["value"] = value
    item["unit"] = unit
    item["device_id"] = device_id
    item["location"] = location

    response = table.put_item(Item=item)

    return response
