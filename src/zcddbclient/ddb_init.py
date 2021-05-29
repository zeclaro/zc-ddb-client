""" This module will create the DynamoDB table, if it doesn't exist """

import boto3
import logging
from .env_setup import DDB_TABLE_NAME
from .constants import AWS_REGION

boto3.setup_default_session(region_name=AWS_REGION)
dynamodb = boto3.client('dynamodb')


def create_ddb():
    logging.info(f"Creating DynamoDB table {DDB_TABLE_NAME}...")
    try:

        dynamodb.create_table(
            TableName=DDB_TABLE_NAME,
            AttributeDefinitions=[
                {
                    "AttributeName": "PK",
                    "AttributeType": "S"
                },
                {
                    "AttributeName": "SK",
                    "AttributeType": "S"
                }
            ],
            KeySchema=[
                {
                    "AttributeName": "PK",
                    "KeyType": "HASH"
                },
                {
                    "AttributeName": "SK",
                    "KeyType": "RANGE"
                }
            ],
            ProvisionedThroughput={
                "ReadCapacityUnits": 1,
                "WriteCapacityUnits": 1
            }
        )
        logging.info(f"Table {DDB_TABLE_NAME} created successfully.")
    except dynamodb.exceptions.ResourceInUseException as e:
        logging.info(f"Table {DDB_TABLE_NAME} already exists.")
