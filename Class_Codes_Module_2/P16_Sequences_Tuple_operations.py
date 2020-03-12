'''
Tuple: A Tuple is a sequence of immutable Python objects. Tuples are sequences, just like lists.

tuple=("Hello","Bye")

Following methods are supported in Tuples:
-> Slicing
-> Updating Tuple
-> Delete Tuple
-> Tuple Length
-> Concatination
-> Repetition

Tuples are similar to list except that Tuples are immutable in nature.

A Tuple is a collection of constant vales and speed of execution of Tuple is fast as compared to other sequences.

Difference between lists and tuples:
1. Tuples are immutable whereas list is mutable.
'''

tup1=("Hi", "Hello", "Bye")
print(len(tup1))    #Prints length of tup1
#3

print(max(tup1))    #Prints element as per ASCII value
#Hi

print(min(tup1))    #Prints element as per ASCII value, Here min is Bye because B will come before H.
#Bye
'''
min and max are elements first and last respectively. But it applicable only for tuple of same data type. Otherwise it will throw error
'''

print(tup1*2)       #Repetition of tup1
#('Hi', 'Hello', 'Bye', 'Hi', 'Hello', 'Bye')

print("Hello" in tup1)      #Membership testing in tuple
#True

tup2=("John", "Wick", "Rocks")

print(tup1+tup2)        #Concatination of tuples
#('Hi', 'Hello', 'Bye', 'John', 'Wick', 'Rocks')

del(tup2)       #Deletes tuple tup2
#print(tup2)
'''
O/P:
NameError: name 'tup2' is not defined<----Since, del(tuple) deletes the tuple
del() comes with the base package. It is not attribute of tuple.
'''

print(sorted(tup1))     #Prints sorted tuple tup1 based on first ASCII characters of words.
#['Bye', 'Hello', 'Hi']

print(tup1)
#('Hi', 'Hello', 'Bye')
print(tup1[::-1])       #Reverses tuples tup1
#('Bye', 'Hello', 'Hi')

list_1=list(tup1)   #Typecastes tuple in list
print(list_1)
#['Hi', 'Hello', 'Bye']

print(dir(tup1))
'''
dir - contains inbuilt python attributes or inbuilt modules ("__attributes__") and attributes or functions specific to tuple objects("function").

['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', 
'__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__',
'__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 
'index']
'''

print(tup1.index("Hello"))      #index(element) to find indexes of elements.
#1

tup1=("Hello", "Namaste", "Pranam", "Sakhshat", "Hi", "Bye", "Namaste")
print(tup1.count("Namaste"))      #count(element) counts the number of times element is present in a tuple.
#2

list_1=list(tup1)   #Typecastes tuple in list
print(list_1)
#O/P:
#['Hello', 'Namaste', 'Pranam', 'Sakhshat', 'Hi', 'Bye', 'Namaste']

print(dir(list_1))
'''
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', 
'__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', 
'__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', 
'__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

Since, list is mutable object, it has many attributes like 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 
'reverse', 'sort'
But as tuple is immutable object, it has only 2 functions: count and index
'''

list_inside_tuple=([1,2,3],[4,5,6],["Hello", "Bye"])     #List inside a tuple.
print(list_inside_tuple)
#([1, 2, 3], [4, 5, 6], ['Hello', 'Bye'])

tuple_inside_list=[(1,2,3),(4,5,6),("Hello", "Bye")]    #Tuple inside a list
print(tuple_inside_list)
#[(1, 2, 3), (4, 5, 6), ('Hello', 'Bye')]

print(dir(list_inside_tuple))
'''
It is tuple since only count and index are present:

['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', 
'__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__',
'__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 
'index']
'''

print(dir(list_inside_tuple[0]))