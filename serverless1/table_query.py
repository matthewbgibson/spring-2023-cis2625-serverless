import boto3
from boto3.dynamodb.conditions import Key, Attr
# Get the service resource.
dydb = boto3.resource('dynamodb')
# Instantiate a table resource object
table = dydb.Table('STUDENTS')
# retrieve items in a table using DynamoDB.Table.query()
response = table.query(
                  KeyConditionExpression=Key('SID').eq('700123456')
                    )
items = response['Items']
print(items)
