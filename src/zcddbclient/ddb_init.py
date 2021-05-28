""" This module will create the DynamoDB table, if it doesn't exist """

import boto3
import logging
from env_setup import DDB_TABLE_NAME

dynamodb = boto3.client('dynamodb')


def create_ddb():
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
    except Exception as e:
        logging.error("Could not create table. Error:")
        logging.error(e)
