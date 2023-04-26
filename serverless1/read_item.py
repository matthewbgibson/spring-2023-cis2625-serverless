import boto3
# Get the service resource.
dydb = boto3.resource('dynamodb')
# Instantiate a table resource object
table = dydb.Table('STUDENTS')
# retrieve a table item using DynamoDB.Table.get_item()
response = table.get_item(
    Key={
        'SID': '700123456',
        'email': 'mxg81620@ucmo.edu'
    })
# print(type(response))
# print(response)
item = response['Item']
print(item)
