""" Provides functionality to read, write and delete records from the DynamoDB table. """
import boto3
import logging
from .env_setup import DDB_TABLE_NAME
from datetime import datetime
from .constants import UUID_ORIGIN_DATE, TIME_STAMP_FORMAT

dynamodb = boto3.client('dynamodb')
pass

def _generate_uuid(device_id: str):
    origin = datetime.strptime(UUID_ORIGIN_DATE, TIME_STAMP_FORMAT)
    now = datetime.now()
    microseconds = (now - origin).total_seconds() * 1000 * 1000
    return f"#{device_id}#{int(microseconds)}"


def write_item(*, qualifier: str, value: float, unit: str, device_id: str, location: str):

    now = datetime.now()
    item = dict()

    item["item_id"] = _generate_uuid(device_id)
    item["timestamp"] = now.strftime(TIME_STAMP_FORMAT)
    item["qualifier"] = qualifier
    item["value"] = value
    item["unit"] = unit
    item["device_id"] = device_id
    item["location"] = location

    response = table.put_item(item)

    return response
