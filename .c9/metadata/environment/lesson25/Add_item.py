{"filter":false,"title":"Add_item.py","tooltip":"/lesson25/Add_item.py","undoManager":{"mark":35,"position":35,"stack":[[{"start":{"row":0,"column":0},"end":{"row":15,"column":0},"action":"insert","lines":["import boto3","# Get the service resource.","dydb = boto3.resource('dynamodb')","# Instantiate a table resource object","table = dydb.Table('users')","# add new items to the table using DynamoDB.Table.put_item():","table.put_item(","   Item={","        'username': 'janedoe',","        'first_name': 'Jane',","        'last_name': 'Doe',","        'age': 25,","        'account_type': 'standard_user',","    }",")",""],"id":1}],[{"start":{"row":12,"column":40},"end":{"row":13,"column":0},"action":"insert","lines":["",""],"id":2},{"start":{"row":13,"column":0},"end":{"row":13,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":13,"column":8},"end":{"row":13,"column":10},"action":"insert","lines":["''"],"id":3}],[{"start":{"row":13,"column":9},"end":{"row":13,"column":10},"action":"insert","lines":["p"],"id":4},{"start":{"row":13,"column":10},"end":{"row":13,"column":11},"action":"insert","lines":["h"]},{"start":{"row":13,"column":11},"end":{"row":13,"column":12},"action":"insert","lines":["o"]},{"start":{"row":13,"column":12},"end":{"row":13,"column":13},"action":"insert","lines":["n"]},{"start":{"row":13,"column":13},"end":{"row":13,"column":14},"action":"insert","lines":["e"]}],[{"start":{"row":13,"column":15},"end":{"row":13,"column":16},"action":"insert","lines":[":"],"id":5}],[{"start":{"row":13,"column":16},"end":{"row":13,"column":17},"action":"insert","lines":[" "],"id":6}],[{"start":{"row":13,"column":17},"end":{"row":13,"column":19},"action":"insert","lines":["''"],"id":7}],[{"start":{"row":13,"column":18},"end":{"row":13,"column":19},"action":"insert","lines":["9"],"id":8},{"start":{"row":13,"column":19},"end":{"row":13,"column":20},"action":"insert","lines":["1"]},{"start":{"row":13,"column":20},"end":{"row":13,"column":21},"action":"insert","lines":["3"]}],[{"start":{"row":13,"column":21},"end":{"row":13,"column":22},"action":"insert","lines":["-"],"id":9},{"start":{"row":13,"column":22},"end":{"row":13,"column":23},"action":"insert","lines":["2"]}],[{"start":{"row":13,"column":23},"end":{"row":13,"column":24},"action":"insert","lines":["3"],"id":10},{"start":{"row":13,"column":24},"end":{"row":13,"column":25},"action":"insert","lines":["4"]},{"start":{"row":13,"column":25},"end":{"row":13,"column":26},"action":"insert","lines":["-"]},{"start":{"row":13,"column":26},"end":{"row":13,"column":27},"action":"insert","lines":["3"]}],[{"start":{"row":13,"column":27},"end":{"row":13,"column":28},"action":"insert","lines":["3"],"id":11},{"start":{"row":13,"column":28},"end":{"row":13,"column":29},"action":"insert","lines":["4"]},{"start":{"row":13,"column":29},"end":{"row":13,"column":30},"action":"insert","lines":["4"]}],[{"start":{"row":4,"column":24},"end":{"row":4,"column":25},"action":"remove","lines":["s"],"id":12},{"start":{"row":4,"column":23},"end":{"row":4,"column":24},"action":"remove","lines":["r"]},{"start":{"row":4,"column":22},"end":{"row":4,"column":23},"action":"remove","lines":["e"]},{"start":{"row":4,"column":21},"end":{"row":4,"column":22},"action":"remove","lines":["s"]},{"start":{"row":4,"column":20},"end":{"row":4,"column":21},"action":"remove","lines":["u"]}],[{"start":{"row":4,"column":20},"end":{"row":4,"column":21},"action":"insert","lines":["G"],"id":13},{"start":{"row":4,"column":21},"end":{"row":4,"column":22},"action":"insert","lines":["i"]},{"start":{"row":4,"column":22},"end":{"row":4,"column":23},"action":"insert","lines":["b"]},{"start":{"row":4,"column":23},"end":{"row":4,"column":24},"action":"insert","lines":["s"]},{"start":{"row":4,"column":24},"end":{"row":4,"column":25},"action":"insert","lines":["o"]},{"start":{"row":4,"column":25},"end":{"row":4,"column":26},"action":"insert","lines":["n"]}],[{"start":{"row":8,"column":27},"end":{"row":8,"column":28},"action":"remove","lines":["e"],"id":14},{"start":{"row":8,"column":26},"end":{"row":8,"column":27},"action":"remove","lines":["o"]},{"start":{"row":8,"column":25},"end":{"row":8,"column":26},"action":"remove","lines":["d"]},{"start":{"row":8,"column":24},"end":{"row":8,"column":25},"action":"remove","lines":["e"]},{"start":{"row":8,"column":23},"end":{"row":8,"column":24},"action":"remove","lines":["n"]},{"start":{"row":8,"column":22},"end":{"row":8,"column":23},"action":"remove","lines":["a"]},{"start":{"row":8,"column":21},"end":{"row":8,"column":22},"action":"remove","lines":["j"]}],[{"start":{"row":8,"column":21},"end":{"row":8,"column":22},"action":"insert","lines":["m"],"id":15},{"start":{"row":8,"column":22},"end":{"row":8,"column":23},"action":"insert","lines":["a"]},{"start":{"row":8,"column":23},"end":{"row":8,"column":24},"action":"insert","lines":["t"]},{"start":{"row":8,"column":24},"end":{"row":8,"column":25},"action":"insert","lines":["t"]},{"start":{"row":8,"column":25},"end":{"row":8,"column":26},"action":"insert","lines":["g"]},{"start":{"row":8,"column":26},"end":{"row":8,"column":27},"action":"insert","lines":["i"]},{"start":{"row":8,"column":27},"end":{"row":8,"column":28},"action":"insert","lines":["b"]},{"start":{"row":8,"column":28},"end":{"row":8,"column":29},"action":"insert","lines":["s"]},{"start":{"row":8,"column":29},"end":{"row":8,"column":30},"action":"insert","lines":["o"]},{"start":{"row":8,"column":30},"end":{"row":8,"column":31},"action":"insert","lines":["n"]}],[{"start":{"row":9,"column":26},"end":{"row":9,"column":27},"action":"remove","lines":["e"],"id":16},{"start":{"row":9,"column":25},"end":{"row":9,"column":26},"action":"remove","lines":["n"]},{"start":{"row":9,"column":24},"end":{"row":9,"column":25},"action":"remove","lines":["a"]},{"start":{"row":9,"column":23},"end":{"row":9,"column":24},"action":"remove","lines":["J"]}],[{"start":{"row":9,"column":23},"end":{"row":9,"column":24},"action":"insert","lines":["M"],"id":17},{"start":{"row":9,"column":24},"end":{"row":9,"column":25},"action":"insert","lines":["a"]},{"start":{"row":9,"column":25},"end":{"row":9,"column":26},"action":"insert","lines":["t"]},{"start":{"row":9,"column":26},"end":{"row":9,"column":27},"action":"insert","lines":["t"]}],[{"start":{"row":10,"column":24},"end":{"row":10,"column":25},"action":"remove","lines":["e"],"id":18},{"start":{"row":10,"column":23},"end":{"row":10,"column":24},"action":"remove","lines":["o"]},{"start":{"row":10,"column":22},"end":{"row":10,"column":23},"action":"remove","lines":["D"]}],[{"start":{"row":10,"column":22},"end":{"row":10,"column":23},"action":"insert","lines":["G"],"id":19},{"start":{"row":10,"column":23},"end":{"row":10,"column":24},"action":"insert","lines":["i"]},{"start":{"row":10,"column":24},"end":{"row":10,"column":25},"action":"insert","lines":["b"]},{"start":{"row":10,"column":25},"end":{"row":10,"column":26},"action":"insert","lines":["s"]},{"start":{"row":10,"column":26},"end":{"row":10,"column":27},"action":"insert","lines":["o"]},{"start":{"row":10,"column":27},"end":{"row":10,"column":28},"action":"insert","lines":["n"]}],[{"start":{"row":11,"column":16},"end":{"row":11,"column":17},"action":"remove","lines":["5"],"id":20}],[{"start":{"row":11,"column":16},"end":{"row":11,"column":17},"action":"insert","lines":["6"],"id":21}],[{"start":{"row":13,"column":29},"end":{"row":13,"column":30},"action":"remove","lines":["4"],"id":22},{"start":{"row":13,"column":28},"end":{"row":13,"column":29},"action":"remove","lines":["4"]},{"start":{"row":13,"column":27},"end":{"row":13,"column":28},"action":"remove","lines":["3"]},{"start":{"row":13,"column":26},"end":{"row":13,"column":27},"action":"remove","lines":["3"]}],[{"start":{"row":13,"column":26},"end":{"row":13,"column":27},"action":"insert","lines":["4"],"id":23},{"start":{"row":13,"column":27},"end":{"row":13,"column":28},"action":"insert","lines":["5"]},{"start":{"row":13,"column":28},"end":{"row":13,"column":29},"action":"insert","lines":["6"]},{"start":{"row":13,"column":29},"end":{"row":13,"column":30},"action":"insert","lines":["7"]}],[{"start":{"row":13,"column":24},"end":{"row":13,"column":25},"action":"remove","lines":["4"],"id":24},{"start":{"row":13,"column":23},"end":{"row":13,"column":24},"action":"remove","lines":["3"]},{"start":{"row":13,"column":22},"end":{"row":13,"column":23},"action":"remove","lines":["2"]}],[{"start":{"row":13,"column":22},"end":{"row":13,"column":23},"action":"insert","lines":["1"],"id":25},{"start":{"row":13,"column":23},"end":{"row":13,"column":24},"action":"insert","lines":["2"]},{"start":{"row":13,"column":24},"end":{"row":13,"column":25},"action":"insert","lines":["3"]}],[{"start":{"row":13,"column":20},"end":{"row":13,"column":21},"action":"remove","lines":["3"],"id":26},{"start":{"row":13,"column":19},"end":{"row":13,"column":20},"action":"remove","lines":["1"]},{"start":{"row":13,"column":18},"end":{"row":13,"column":19},"action":"remove","lines":["9"]}],[{"start":{"row":13,"column":18},"end":{"row":13,"column":19},"action":"insert","lines":["6"],"id":27},{"start":{"row":13,"column":19},"end":{"row":13,"column":20},"action":"insert","lines":["6"]},{"start":{"row":13,"column":20},"end":{"row":13,"column":21},"action":"insert","lines":["0"]}],[{"start":{"row":8,"column":16},"end":{"row":8,"column":17},"action":"remove","lines":["e"],"id":28},{"start":{"row":8,"column":15},"end":{"row":8,"column":16},"action":"remove","lines":["m"]},{"start":{"row":8,"column":14},"end":{"row":8,"column":15},"action":"remove","lines":["a"]},{"start":{"row":8,"column":13},"end":{"row":8,"column":14},"action":"remove","lines":["n"]},{"start":{"row":8,"column":12},"end":{"row":8,"column":13},"action":"remove","lines":["r"]},{"start":{"row":8,"column":11},"end":{"row":8,"column":12},"action":"remove","lines":["e"]},{"start":{"row":8,"column":10},"end":{"row":8,"column":11},"action":"remove","lines":["s"]},{"start":{"row":8,"column":9},"end":{"row":8,"column":10},"action":"remove","lines":["u"]}],[{"start":{"row":8,"column":9},"end":{"row":8,"column":10},"action":"insert","lines":["S"],"id":29},{"start":{"row":8,"column":10},"end":{"row":8,"column":11},"action":"insert","lines":["I"]},{"start":{"row":8,"column":11},"end":{"row":8,"column":12},"action":"insert","lines":["D"]}],[{"start":{"row":13,"column":13},"end":{"row":13,"column":14},"action":"remove","lines":["e"],"id":30},{"start":{"row":13,"column":12},"end":{"row":13,"column":13},"action":"remove","lines":["n"]},{"start":{"row":13,"column":11},"end":{"row":13,"column":12},"action":"remove","lines":["o"]},{"start":{"row":13,"column":10},"end":{"row":13,"column":11},"action":"remove","lines":["h"]},{"start":{"row":13,"column":9},"end":{"row":13,"column":10},"action":"remove","lines":["p"]}],[{"start":{"row":13,"column":9},"end":{"row":13,"column":10},"action":"insert","lines":["e"],"id":31},{"start":{"row":13,"column":10},"end":{"row":13,"column":11},"action":"insert","lines":["m"]},{"start":{"row":13,"column":11},"end":{"row":13,"column":12},"action":"insert","lines":["a"]},{"start":{"row":13,"column":12},"end":{"row":13,"column":13},"action":"insert","lines":["i"]},{"start":{"row":13,"column":13},"end":{"row":13,"column":14},"action":"insert","lines":["l"]}],[{"start":{"row":13,"column":29},"end":{"row":13,"column":30},"action":"remove","lines":["7"],"id":32},{"start":{"row":13,"column":28},"end":{"row":13,"column":29},"action":"remove","lines":["6"]},{"start":{"row":13,"column":27},"end":{"row":13,"column":28},"action":"remove","lines":["5"]},{"start":{"row":13,"column":26},"end":{"row":13,"column":27},"action":"remove","lines":["4"]},{"start":{"row":13,"column":25},"end":{"row":13,"column":26},"action":"remove","lines":["-"]},{"start":{"row":13,"column":24},"end":{"row":13,"column":25},"action":"remove","lines":["3"]},{"start":{"row":13,"column":23},"end":{"row":13,"column":24},"action":"remove","lines":["2"]},{"start":{"row":13,"column":22},"end":{"row":13,"column":23},"action":"remove","lines":["1"]},{"start":{"row":13,"column":21},"end":{"row":13,"column":22},"action":"remove","lines":["-"]},{"start":{"row":13,"column":20},"end":{"row":13,"column":21},"action":"remove","lines":["0"]},{"start":{"row":13,"column":19},"end":{"row":13,"column":20},"action":"remove","lines":["6"]},{"start":{"row":13,"column":18},"end":{"row":13,"column":19},"action":"remove","lines":["6"]}],[{"start":{"row":13,"column":18},"end":{"row":13,"column":19},"action":"insert","lines":["m"],"id":33},{"start":{"row":13,"column":19},"end":{"row":13,"column":20},"action":"insert","lines":["x"]},{"start":{"row":13,"column":20},"end":{"row":13,"column":21},"action":"insert","lines":["g"]},{"start":{"row":13,"column":21},"end":{"row":13,"column":22},"action":"insert","lines":["8"]},{"start":{"row":13,"column":22},"end":{"row":13,"column":23},"action":"insert","lines":["1"]},{"start":{"row":13,"column":23},"end":{"row":13,"column":24},"action":"insert","lines":["6"]},{"start":{"row":13,"column":24},"end":{"row":13,"column":25},"action":"insert","lines":["2"]},{"start":{"row":13,"column":25},"end":{"row":13,"column":26},"action":"insert","lines":["0"]}],[{"start":{"row":13,"column":26},"end":{"row":13,"column":27},"action":"insert","lines":["@"],"id":34},{"start":{"row":13,"column":27},"end":{"row":13,"column":28},"action":"insert","lines":["u"]},{"start":{"row":13,"column":28},"end":{"row":13,"column":29},"action":"insert","lines":["c"]},{"start":{"row":13,"column":29},"end":{"row":13,"column":30},"action":"insert","lines":["m"]},{"start":{"row":13,"column":30},"end":{"row":13,"column":31},"action":"insert","lines":["o"]},{"start":{"row":13,"column":31},"end":{"row":13,"column":32},"action":"insert","lines":["."]},{"start":{"row":13,"column":32},"end":{"row":13,"column":33},"action":"insert","lines":["e"]},{"start":{"row":13,"column":33},"end":{"row":13,"column":34},"action":"insert","lines":["d"]},{"start":{"row":13,"column":34},"end":{"row":13,"column":35},"action":"insert","lines":["u"]}],[{"start":{"row":8,"column":25},"end":{"row":8,"column":26},"action":"remove","lines":["n"],"id":35},{"start":{"row":8,"column":24},"end":{"row":8,"column":25},"action":"remove","lines":["o"]},{"start":{"row":8,"column":23},"end":{"row":8,"column":24},"action":"remove","lines":["s"]},{"start":{"row":8,"column":22},"end":{"row":8,"column":23},"action":"remove","lines":["b"]},{"start":{"row":8,"column":21},"end":{"row":8,"column":22},"action":"remove","lines":["i"]},{"start":{"row":8,"column":20},"end":{"row":8,"column":21},"action":"remove","lines":["g"]},{"start":{"row":8,"column":19},"end":{"row":8,"column":20},"action":"remove","lines":["t"]},{"start":{"row":8,"column":18},"end":{"row":8,"column":19},"action":"remove","lines":["t"]},{"start":{"row":8,"column":17},"end":{"row":8,"column":18},"action":"remove","lines":["a"]},{"start":{"row":8,"column":16},"end":{"row":8,"column":17},"action":"remove","lines":["m"]}],[{"start":{"row":8,"column":16},"end":{"row":8,"column":17},"action":"insert","lines":["7"],"id":36},{"start":{"row":8,"column":17},"end":{"row":8,"column":18},"action":"insert","lines":["0"]},{"start":{"row":8,"column":18},"end":{"row":8,"column":19},"action":"insert","lines":["0"]},{"start":{"row":8,"column":19},"end":{"row":8,"column":20},"action":"insert","lines":["1"]},{"start":{"row":8,"column":20},"end":{"row":8,"column":21},"action":"insert","lines":["2"]},{"start":{"row":8,"column":21},"end":{"row":8,"column":22},"action":"insert","lines":["3"]},{"start":{"row":8,"column":22},"end":{"row":8,"column":23},"action":"insert","lines":["4"]},{"start":{"row":8,"column":23},"end":{"row":8,"column":24},"action":"insert","lines":["5"]},{"start":{"row":8,"column":24},"end":{"row":8,"column":25},"action":"insert","lines":["6"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":9,"column":29},"end":{"row":9,"column":29},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1682022470192,"hash":"2291a391a2aaa04458b076caa2bea7dc7d556bed"}