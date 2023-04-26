{"filter":false,"title":"update_item.py","tooltip":"/assignment5/update_item.py","undoManager":{"mark":8,"position":8,"stack":[[{"start":{"row":0,"column":0},"end":{"row":4,"column":17},"action":"insert","lines":["'username': 'mattgibson',","        'first_name': 'Matt',","        'last_name': 'Gibson',","        'phone': '660-123-4567',","        'age': 55"],"id":1}],[{"start":{"row":0,"column":0},"end":{"row":4,"column":17},"action":"remove","lines":["'username': 'mattgibson',","        'first_name': 'Matt',","        'last_name': 'Gibson',","        'phone': '660-123-4567',","        'age': 55"],"id":2}],[{"start":{"row":0,"column":0},"end":{"row":15,"column":1},"action":"insert","lines":["import boto3","# Get the service resource.","dydb = boto3.resource('dynamodb')","# Instantiate a table resource object","table = dydb.Table('users')","# update attributes of the item in the table using DynamoDB.Table.update_item()","table.update_item(","    Key={","        'username': 'janedoe',","        'last_name': 'Doe'","    },","    UpdateExpression='SET age = :val1',","    ExpressionAttributeValues={","        ':val1': 26","    }",")"],"id":3}],[{"start":{"row":4,"column":24},"end":{"row":4,"column":25},"action":"remove","lines":["s"],"id":4},{"start":{"row":4,"column":23},"end":{"row":4,"column":24},"action":"remove","lines":["r"]},{"start":{"row":4,"column":22},"end":{"row":4,"column":23},"action":"remove","lines":["e"]},{"start":{"row":4,"column":21},"end":{"row":4,"column":22},"action":"remove","lines":["s"]},{"start":{"row":4,"column":20},"end":{"row":4,"column":21},"action":"remove","lines":["u"]}],[{"start":{"row":4,"column":20},"end":{"row":4,"column":21},"action":"insert","lines":["S"],"id":5},{"start":{"row":4,"column":21},"end":{"row":4,"column":22},"action":"insert","lines":["T"]},{"start":{"row":4,"column":22},"end":{"row":4,"column":23},"action":"insert","lines":["U"]},{"start":{"row":4,"column":23},"end":{"row":4,"column":24},"action":"insert","lines":["D"]},{"start":{"row":4,"column":24},"end":{"row":4,"column":25},"action":"insert","lines":["E"]},{"start":{"row":4,"column":25},"end":{"row":4,"column":26},"action":"insert","lines":["N"]},{"start":{"row":4,"column":26},"end":{"row":4,"column":27},"action":"insert","lines":["T"]},{"start":{"row":4,"column":27},"end":{"row":4,"column":28},"action":"insert","lines":["S"]}],[{"start":{"row":8,"column":27},"end":{"row":8,"column":28},"action":"remove","lines":["e"],"id":6},{"start":{"row":8,"column":26},"end":{"row":8,"column":27},"action":"remove","lines":["o"]},{"start":{"row":8,"column":25},"end":{"row":8,"column":26},"action":"remove","lines":["d"]},{"start":{"row":8,"column":24},"end":{"row":8,"column":25},"action":"remove","lines":["e"]},{"start":{"row":8,"column":23},"end":{"row":8,"column":24},"action":"remove","lines":["n"]},{"start":{"row":8,"column":22},"end":{"row":8,"column":23},"action":"remove","lines":["a"]},{"start":{"row":8,"column":21},"end":{"row":8,"column":22},"action":"remove","lines":["j"]}],[{"start":{"row":8,"column":21},"end":{"row":8,"column":22},"action":"insert","lines":["m"],"id":7},{"start":{"row":8,"column":22},"end":{"row":8,"column":23},"action":"insert","lines":["a"]},{"start":{"row":8,"column":23},"end":{"row":8,"column":24},"action":"insert","lines":["t"]},{"start":{"row":8,"column":24},"end":{"row":8,"column":25},"action":"insert","lines":["t"]},{"start":{"row":8,"column":25},"end":{"row":8,"column":26},"action":"insert","lines":["g"]},{"start":{"row":8,"column":26},"end":{"row":8,"column":27},"action":"insert","lines":["i"]},{"start":{"row":8,"column":27},"end":{"row":8,"column":28},"action":"insert","lines":["b"]},{"start":{"row":8,"column":28},"end":{"row":8,"column":29},"action":"insert","lines":["s"]},{"start":{"row":8,"column":29},"end":{"row":8,"column":30},"action":"insert","lines":["o"]},{"start":{"row":8,"column":30},"end":{"row":8,"column":31},"action":"insert","lines":["n"]}],[{"start":{"row":9,"column":24},"end":{"row":9,"column":25},"action":"remove","lines":["e"],"id":8},{"start":{"row":9,"column":23},"end":{"row":9,"column":24},"action":"remove","lines":["o"]},{"start":{"row":9,"column":22},"end":{"row":9,"column":23},"action":"remove","lines":["D"]}],[{"start":{"row":9,"column":22},"end":{"row":9,"column":23},"action":"insert","lines":["G"],"id":9},{"start":{"row":9,"column":23},"end":{"row":9,"column":24},"action":"insert","lines":["i"]},{"start":{"row":9,"column":24},"end":{"row":9,"column":25},"action":"insert","lines":["b"]},{"start":{"row":9,"column":25},"end":{"row":9,"column":26},"action":"insert","lines":["s"]},{"start":{"row":9,"column":26},"end":{"row":9,"column":27},"action":"insert","lines":["o"]},{"start":{"row":9,"column":27},"end":{"row":9,"column":28},"action":"insert","lines":["n"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":14,"column":5},"end":{"row":14,"column":5},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1682020550091,"hash":"57d66b3bd84915ce0de4670f31d671cd978d288c"}