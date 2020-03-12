'''
Dictionary: Dictionary is an unordered collection of key-value pairs. It is generally used when
we have a huge amiunt of data.
Example: dict={1:"C", 2:"C++", 3:"Python"}

Operations that can be performed on Dictionaries:
-> Length
-> del d[K]
-> Membership Testing

Q. When to use Dictionaries?
->When one has to create some huge records with name and ID then we can use Dictionaries.
'''
dict_1={1:"C", 2:"C++", 3:"Python"}     #Creating a Dictionary
print(dict_1)
#{1: 'C', 2: 'C++', 3: 'Python'}
print(dict_1[1])    #Accessing Values in Dictionary
#C
print(dict_1[2])
#C++
print(dict_1[3])
#Python

employees={
    'emp_id':[1,2,3,4,5], 
    'name':["Arvind","John","Wick","Mark","Vladimir"]
}

print(employees)
#{'emp_id': [1, 2, 3, 4, 5], 'name': ['Arvind', 'John', 'Wick', 'Mark', 'Vladimir']}

print(dir(employees))
'''
['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', 
'__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', 
'__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', 
'__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', 
'__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 
'popitem', 'setdefault', 'update', 'values']
'''
'''
'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 
'values' <--------------------These functions and attributes we can use for various dictionary
operations
'''

print(employees.keys())
#dict_keys(['emp_id', 'name'])
print(employees.values())
#dict_values([[1, 2, 3, 4, 5], ['Arvind', 'John', 'Wick', 'Mark', 'Vladimir']])
print(employees.items())
#dict_items([('emp_id', [1, 2, 3, 4, 5]), ('name', ['Arvind', 'John', 'Wick', 'Mark', 'Vladimir'])])
print(employees.get(1))
#None
print(employees.get('emp_id'))  #It will give all emp_id
#[1, 2, 3, 4, 5]
print(employees.get('name'))    #It will give all names
#['Arvind', 'John', 'Wick', 'Mark', 'Vladimir']

'''
Q. How to check if a character is in a set?
'''
name_set=set(employees.get('name'))
print(name_set)
#{'Arvind', 'Vladimir', 'Mark', 'John', 'Wick'}
print('Mark' in name_set)
#True
print('M' in employees.get('name')[3])
#True

#Updating Dictionary
print(dict_1)
#{1: 'C', 2: 'C++', 3: 'Python'}
dict_1[1]="Advanced C"      #Updation
print(dict_1)
#{1: 'Advanced C', 2: 'C++', 3: 'Python'}

#Deleting Dictionary
del (dict_1[3])     #Deletion
print(dict_1)
#{1: 'Advanced C', 2: 'C++'}

#length of Dinctionary:
print(len(dict_1))
#2

#Type checking
print(type(dict_1))
#<class 'dict'>

#Sorting Dictionary:
dict_1={
    1:'C',3:'Python',2:'C++'
}
print(dict_1)
#{1: 'C', 3: 'Python', 2: 'C++'}
list_dict=list(dict_1.keys())
print(list_dict)
#[1, 3, 2]
sorted_list_dict=sorted(list_dict)
print(sorted_list_dict)
#[1, 2, 3]
for key in sorted_list_dict:
    print(key,'->',dict_1[key])
'''
1 -> C
2 -> C++
3 -> Python
'''

#Tuple in Dinctionary:
dict_1={
    'emp_id':(1,2,3,4,5),
    'name': ("Abhinav","Himmer", "Yuyutsu", "Satyavrat", "Bindra")
}
print(dict_1)
#{'emp_id': (1, 2, 3, 4, 5), 'name': ('Abhinav', 'Himmer', 'Yuyutsu', 'Satyavrat', 'Bindra')}
print(dict_1['emp_id'][1])
#2
print(type(dict_1['emp_id']))
#<class 'tuple'>

#List in Dictionary:
dict_1={
    'emp_id':[1,2,3,4,5],
    'name': ["Abhinav","Himmer", "Yuyutsu", "Satyavrat", "Bindra"]
}
print(dict_1)
#{'emp_id': [1, 2, 3, 4, 5], 'name': ['Abhinav', 'Himmer', 'Yuyutsu', 'Satyavrat', 'Bindra']}
print(dict_1['emp_id'][1])
#2
print(type(dict_1['emp_id']))
#<class 'list'>