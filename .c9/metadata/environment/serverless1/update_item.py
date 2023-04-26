{"filter":false,"title":"update_item.py","tooltip":"/lesson25/update_item.py","ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":16,"column":0},"end":{"row":16,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"hash":"506897d0b6218283645d0d6b76ae05e05cae1a9d","mime":"text/x-script.python","undoManager":{"mark":17,"position":17,"stack":[[{"start":{"row":0,"column":0},"end":{"row":16,"column":0},"action":"insert","lines":["import boto3","# Get the service resource.","dydb = boto3.resource('dynamodb')","# Instantiate a table resource object","table = dydb.Table('users')","# update attributes of the item in the table using DynamoDB.Table.update_item()","table.update_item(","    Key={","        'username': 'janedoe',","        'last_name': 'Doe'","    },","    UpdateExpression='SET age = :val1',","    ExpressionAttributeValues={","        ':val1': 27","    }",")",""],"id":1}],[{"start":{"row":13,"column":18},"end":{"row":13,"column":19},"action":"remove","lines":["7"],"id":2}],[{"start":{"row":13,"column":18},"end":{"row":13,"column":19},"action":"insert","lines":["6"],"id":3}],[{"start":{"row":4,"column":24},"end":{"row":4,"column":25},"action":"remove","lines":["s"],"id":4},{"start":{"row":4,"column":23},"end":{"row":4,"column":24},"action":"remove","lines":["r"]},{"start":{"row":4,"column":22},"end":{"row":4,"column":23},"action":"remove","lines":["e"]},{"start":{"row":4,"column":21},"end":{"row":4,"column":22},"action":"remove","lines":["s"]},{"start":{"row":4,"column":20},"end":{"row":4,"column":21},"action":"remove","lines":["u"]}],[{"start":{"row":4,"column":20},"end":{"row":4,"column":21},"action":"insert","lines":["S"],"id":5},{"start":{"row":4,"column":21},"end":{"row":4,"column":22},"action":"insert","lines":["T"]},{"start":{"row":4,"column":22},"end":{"row":4,"column":23},"action":"insert","lines":["U"]},{"start":{"row":4,"column":23},"end":{"row":4,"column":24},"action":"insert","lines":["D"]},{"start":{"row":4,"column":24},"end":{"row":4,"column":25},"action":"insert","lines":["E"]},{"start":{"row":4,"column":25},"end":{"row":4,"column":26},"action":"insert","lines":["N"]},{"start":{"row":4,"column":26},"end":{"row":4,"column":27},"action":"insert","lines":["T"]},{"start":{"row":4,"column":27},"end":{"row":4,"column":28},"action":"insert","lines":["S"]}],[{"start":{"row":8,"column":27},"end":{"row":8,"column":28},"action":"remove","lines":["e"],"id":6},{"start":{"row":8,"column":26},"end":{"row":8,"column":27},"action":"remove","lines":["o"]},{"start":{"row":8,"column":25},"end":{"row":8,"column":26},"action":"remove","lines":["d"]},{"start":{"row":8,"column":24},"end":{"row":8,"column":25},"action":"remove","lines":["e"]},{"start":{"row":8,"column":23},"end":{"row":8,"column":24},"action":"remove","lines":["n"]},{"start":{"row":8,"column":22},"end":{"row":8,"column":23},"action":"remove","lines":["a"]},{"start":{"row":8,"column":21},"end":{"row":8,"column":22},"action":"remove","lines":["j"]}],[{"start":{"row":8,"column":21},"end":{"row":8,"column":22},"action":"insert","lines":["m"],"id":7},{"start":{"row":8,"column":22},"end":{"row":8,"column":23},"action":"insert","lines":["a"]},{"start":{"row":8,"column":23},"end":{"row":8,"column":24},"action":"insert","lines":["t"]},{"start":{"row":8,"column":24},"end":{"row":8,"column":25},"action":"insert","lines":["t"]},{"start":{"row":8,"column":25},"end":{"row":8,"column":26},"action":"insert","lines":["g"]},{"start":{"row":8,"column":26},"end":{"row":8,"column":27},"action":"insert","lines":["i"]},{"start":{"row":8,"column":27},"end":{"row":8,"column":28},"action":"insert","lines":["b"]},{"start":{"row":8,"column":28},"end":{"row":8,"column":29},"action":"insert","lines":["s"]},{"start":{"row":8,"column":29},"end":{"row":8,"column":30},"action":"insert","lines":["o"]},{"start":{"row":8,"column":30},"end":{"row":8,"column":31},"action":"insert","lines":["n"]}],[{"start":{"row":9,"column":24},"end":{"row":9,"column":25},"action":"remove","lines":["e"],"id":8},{"start":{"row":9,"column":23},"end":{"row":9,"column":24},"action":"remove","lines":["o"]},{"start":{"row":9,"column":22},"end":{"row":9,"column":23},"action":"remove","lines":["D"]}],[{"start":{"row":9,"column":22},"end":{"row":9,"column":23},"action":"insert","lines":["G"],"id":9},{"start":{"row":9,"column":23},"end":{"row":9,"column":24},"action":"insert","lines":["i"]},{"start":{"row":9,"column":24},"end":{"row":9,"column":25},"action":"insert","lines":["b"]},{"start":{"row":9,"column":25},"end":{"row":9,"column":26},"action":"insert","lines":["s"]},{"start":{"row":9,"column":26},"end":{"row":9,"column":27},"action":"insert","lines":["o"]},{"start":{"row":9,"column":27},"end":{"row":9,"column":28},"action":"insert","lines":["n"]}],[{"start":{"row":8,"column":16},"end":{"row":8,"column":17},"action":"remove","lines":["e"],"id":10},{"start":{"row":8,"column":15},"end":{"row":8,"column":16},"action":"remove","lines":["m"]},{"start":{"row":8,"column":14},"end":{"row":8,"column":15},"action":"remove","lines":["a"]},{"start":{"row":8,"column":13},"end":{"row":8,"column":14},"action":"remove","lines":["n"]},{"start":{"row":8,"column":12},"end":{"row":8,"column":13},"action":"remove","lines":["r"]},{"start":{"row":8,"column":11},"end":{"row":8,"column":12},"action":"remove","lines":["e"]},{"start":{"row":8,"column":10},"end":{"row":8,"column":11},"action":"remove","lines":["s"]},{"start":{"row":8,"column":9},"end":{"row":8,"column":10},"action":"remove","lines":["u"]}],[{"start":{"row":8,"column":9},"end":{"row":8,"column":10},"action":"insert","lines":["S"],"id":11},{"start":{"row":8,"column":10},"end":{"row":8,"column":11},"action":"insert","lines":["I"]},{"start":{"row":8,"column":11},"end":{"row":8,"column":12},"action":"insert","lines":["D"]}],[{"start":{"row":9,"column":17},"end":{"row":9,"column":18},"action":"remove","lines":["e"],"id":12},{"start":{"row":9,"column":16},"end":{"row":9,"column":17},"action":"remove","lines":["m"]},{"start":{"row":9,"column":15},"end":{"row":9,"column":16},"action":"remove","lines":["a"]},{"start":{"row":9,"column":14},"end":{"row":9,"column":15},"action":"remove","lines":["n"]},{"start":{"row":9,"column":13},"end":{"row":9,"column":14},"action":"remove","lines":["_"]},{"start":{"row":9,"column":12},"end":{"row":9,"column":13},"action":"remove","lines":["t"]},{"start":{"row":9,"column":11},"end":{"row":9,"column":12},"action":"remove","lines":["s"]},{"start":{"row":9,"column":10},"end":{"row":9,"column":11},"action":"remove","lines":["a"]},{"start":{"row":9,"column":9},"end":{"row":9,"column":10},"action":"remove","lines":["l"]}],[{"start":{"row":9,"column":9},"end":{"row":9,"column":10},"action":"insert","lines":["e"],"id":13},{"start":{"row":9,"column":10},"end":{"row":9,"column":11},"action":"insert","lines":["m"]},{"start":{"row":9,"column":11},"end":{"row":9,"column":12},"action":"insert","lines":["a"]},{"start":{"row":9,"column":12},"end":{"row":9,"column":13},"action":"insert","lines":["i"]},{"start":{"row":9,"column":13},"end":{"row":9,"column":14},"action":"insert","lines":["l"]}],[{"start":{"row":9,"column":23},"end":{"row":9,"column":24},"action":"remove","lines":["n"],"id":14},{"start":{"row":9,"column":22},"end":{"row":9,"column":23},"action":"remove","lines":["o"]},{"start":{"row":9,"column":21},"end":{"row":9,"column":22},"action":"remove","lines":["s"]},{"start":{"row":9,"column":20},"end":{"row":9,"column":21},"action":"remove","lines":["b"]},{"start":{"row":9,"column":19},"end":{"row":9,"column":20},"action":"remove","lines":["i"]},{"start":{"row":9,"column":18},"end":{"row":9,"column":19},"action":"remove","lines":["G"]}],[{"start":{"row":9,"column":18},"end":{"row":9,"column":19},"action":"insert","lines":["m"],"id":15},{"start":{"row":9,"column":19},"end":{"row":9,"column":20},"action":"insert","lines":["x"]},{"start":{"row":9,"column":20},"end":{"row":9,"column":21},"action":"insert","lines":["g"]},{"start":{"row":9,"column":21},"end":{"row":9,"column":22},"action":"insert","lines":["8"]},{"start":{"row":9,"column":22},"end":{"row":9,"column":23},"action":"insert","lines":["1"]},{"start":{"row":9,"column":23},"end":{"row":9,"column":24},"action":"insert","lines":["6"]},{"start":{"row":9,"column":24},"end":{"row":9,"column":25},"action":"insert","lines":["2"]},{"start":{"row":9,"column":25},"end":{"row":9,"column":26},"action":"insert","lines":["0"]}],[{"start":{"row":9,"column":26},"end":{"row":9,"column":27},"action":"insert","lines":["@"],"id":16},{"start":{"row":9,"column":27},"end":{"row":9,"column":28},"action":"insert","lines":["u"]},{"start":{"row":9,"column":28},"end":{"row":9,"column":29},"action":"insert","lines":["c"]},{"start":{"row":9,"column":29},"end":{"row":9,"column":30},"action":"insert","lines":["m"]},{"start":{"row":9,"column":30},"end":{"row":9,"column":31},"action":"insert","lines":["o"]},{"start":{"row":9,"column":31},"end":{"row":9,"column":32},"action":"insert","lines":["."]},{"start":{"row":9,"column":32},"end":{"row":9,"column":33},"action":"insert","lines":["e"]},{"start":{"row":9,"column":33},"end":{"row":9,"column":34},"action":"insert","lines":["d"]},{"start":{"row":9,"column":34},"end":{"row":9,"column":35},"action":"insert","lines":["u"]}],[{"start":{"row":8,"column":25},"end":{"row":8,"column":26},"action":"remove","lines":["n"],"id":17},{"start":{"row":8,"column":24},"end":{"row":8,"column":25},"action":"remove","lines":["o"]},{"start":{"row":8,"column":23},"end":{"row":8,"column":24},"action":"remove","lines":["s"]},{"start":{"row":8,"column":22},"end":{"row":8,"column":23},"action":"remove","lines":["b"]},{"start":{"row":8,"column":21},"end":{"row":8,"column":22},"action":"remove","lines":["i"]},{"start":{"row":8,"column":20},"end":{"row":8,"column":21},"action":"remove","lines":["g"]},{"start":{"row":8,"column":19},"end":{"row":8,"column":20},"action":"remove","lines":["t"]},{"start":{"row":8,"column":18},"end":{"row":8,"column":19},"action":"remove","lines":["t"]},{"start":{"row":8,"column":17},"end":{"row":8,"column":18},"action":"remove","lines":["a"]},{"start":{"row":8,"column":16},"end":{"row":8,"column":17},"action":"remove","lines":["m"]}],[{"start":{"row":8,"column":16},"end":{"row":8,"column":17},"action":"insert","lines":["7"],"id":18},{"start":{"row":8,"column":17},"end":{"row":8,"column":18},"action":"insert","lines":["0"]},{"start":{"row":8,"column":18},"end":{"row":8,"column":19},"action":"insert","lines":["0"]},{"start":{"row":8,"column":19},"end":{"row":8,"column":20},"action":"insert","lines":["1"]},{"start":{"row":8,"column":20},"end":{"row":8,"column":21},"action":"insert","lines":["2"]},{"start":{"row":8,"column":21},"end":{"row":8,"column":22},"action":"insert","lines":["3"]},{"start":{"row":8,"column":22},"end":{"row":8,"column":23},"action":"insert","lines":["4"]},{"start":{"row":8,"column":23},"end":{"row":8,"column":24},"action":"insert","lines":["5"]},{"start":{"row":8,"column":24},"end":{"row":8,"column":25},"action":"insert","lines":["6"]}]]},"timestamp":1682022443736}