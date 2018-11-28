#!/usr/bin/env python3

import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.create_table(
    TableName='weibo',
    KeySchema=[
        {
            'AttributeName': 'source', 
            'KeyType': 'HASH'
        }
    ], 
    AttributeDefinitions=[
        {
            'AttributeName': 'source', 
            'AttributeType': 'S'
        } 
    ], 
    ProvisionedThroughput={
        'ReadCapacityUnits': 1, 
        'WriteCapacityUnits': 1
    }
)

