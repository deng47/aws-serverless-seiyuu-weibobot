#!/usr/bin/env python3

import boto3
from boto3.dynamodb.conditions import Key, Attr

class MyTable():
    def __init__(self, table):
        dynamodb = boto3.resource('dynamodb')
        self.table = dynamodb.Table(table)

    def put_data(self, data):
        self.table.put_item(Item=data)

    def remove_data(self, data):
        self.table.delete_item(Key=data)

    def update_data(self, key, tag, column, data):
        response = self.table.update_item(Key={key:tag},AttributeUpdates={column:{ 'Action': 'PUT', 'Value': data}},ReturnValues='UPDATED_NEW')
        return response['ResponseMetadata']['HTTPStatusCode'] == 200

    def get_data(self, tag, data):
        response = self.table.query(KeyConditionExpression=Key(tag).eq(data))
        return response['Items']

