""" This module will create the DynamoDB table, if it doesn't exist """

import boto3
from botocore.exceptions import ClientError
import logging
from .env_setup import DDB_TABLE_NAME

dynamodb = boto3.resource('dynamodb')


def create_ddb():
    """ Creates the DDB table, if it doesn't already exists. """
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
    # except dynamodb.client.exceptions.ResourceInUseException as e:
    except ClientError as e:
        if e.response['Error']['Code'] == "ResourceInUseException":
            logging.info(f"Table {DDB_TABLE_NAME} already exists.")
        else:
            logging.error(e)
