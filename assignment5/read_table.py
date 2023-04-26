import boto3

dydb = boto3.resource('dynamodb')
table = dydb.Table('STUDENTS')

response = table.get_item(
    Key={
        'username': 'mattgibson',
        'first_name': 'Matt',
        'last_name': 'Gibson',
        'phone': '660-123-4567',
        'age': 55
    })
item = response['Item']
print(item)