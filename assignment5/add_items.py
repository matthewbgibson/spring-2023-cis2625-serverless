import boto3

dydb = boto3.resource('dynamodb')

table = dydb.Table('properties')


item ={
        'str_address': '1880 Rainbow Road',
        'zip': '64037',
        'city': 'Higginsville',
        'state': 'MO',
    }

table.put_item(Item=item)
    