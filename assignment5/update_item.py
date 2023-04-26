import boto3
# Get the service resource.
dydb = boto3.resource('dynamodb')
# Instantiate a table resource object
table = dydb.Table('STUDENTS')
# update attributes of the item in the table using DynamoDB.Table.update_item()
table.update_item(
    Key={
        'username': 'mattgibson',
        'last_name': 'Gibson'
    },
    UpdateExpression='SET age = :val1',
    ExpressionAttributeValues={
        ':val1': 26
    }
)