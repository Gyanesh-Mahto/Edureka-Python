'''
JSON Module:
-->The json module provides an easy way to encode and decode data in json.
-->It is useful when dealing with web data.
'''
import json
data={"name":"Ace", "shares":100, "price":540}
json_str=json.dumps(data)
print(json_str)
#{"name": "Ace", "shares": 100, "price": 540}