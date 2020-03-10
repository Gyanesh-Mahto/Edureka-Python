'''
Dictionaries contain key value pairs. Each key is separated from its value by a colon(:), the items are
separated by comma, and th whole thing is enclosed within curly braces.

Syntax:
dict1={key1:value1, key2:value2,.........,keyn:valuen,}
'''

dict1={'Team':['India', 'USA', 'SA', 'Australia', 'Oman'],
'Rank':[1,15,5,21,6]}
print(dict1)

#O/P:
#{'Team': ['India', 'USA', 'SA', 'Australia', 'Oman'], 'Rank': [1, 15, 5, 21, 6]}

'''
Note: This dictionary has a key and value combination. The key here is Team as well as Rank and the values are in the form of lists
'''
'''
dir command: It will give all the attributes, properties and functions associated with that kind of variable of particular data type.
__term__<---It is defined by python
'''
print(dir(dict1))
'''
O/P:
['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
'''
print(dict1.keys())     #It gives keys of dict1, keys()<---It is function
#O/P: dict_keys(['Team', 'Rank'])
print(dict1.values())   #It gives values of dict1
#O/P:
#dict_values([['India', 'USA', 'SA', 'Australia', 'Oman'], [1, 15, 5, 21, 6]])

print(dict1.keys)   #<---It is method
#<built-in method keys of dict object at 0x00685570>

print(dict1.values) #<---It is also a method
#<built-in method values of dict object at 0x00685570>