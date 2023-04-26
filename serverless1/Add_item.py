import boto3
# Get the service resource.
dydb = boto3.resource('dynamodb')
# Instantiate a table resource object
table = dydb.Table('Gibson')
# add new items to the table using DynamoDB.Table.put_item():
table.put_item(
   Item={
        'SID': '700123456',
        'first_name': 'Matt',
        'last_name': 'Gibson',
        'age': 26,
        'account_type': 'standard_user',
        'email': 'mxg81620@ucmo.edu'
    }
)
