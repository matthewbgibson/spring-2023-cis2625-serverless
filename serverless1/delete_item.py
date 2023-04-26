import boto3
# Get the service resource.
dydb = boto3.resource('dynamodb')
# Instantiate a table resource object
table = dydb.Table('STUDENTS')
# delete the item using DynamoDB.Table.delete_item()
table.delete_item(
    Key={
        'SID': '700123456',
        'email': 'mxg81620@ucmo.edu'
    }
)

# Print out items in the table.
print(table.item_count)
