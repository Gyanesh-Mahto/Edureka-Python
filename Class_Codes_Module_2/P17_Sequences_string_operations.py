'''
Strings:
We can create them simply by enclosing characters in quotes

Example:
string="Python"

Following operations can be performed on string:
-> Slicing: string[range]
-> Updating: string[range]+'x'
-> Concatenation: string 1+ string 2
-> Repitition: string_1*2
-> Membership: in, not in
-> Reverse: string[::-1]
'''

str1='Welcome'
str2="to"
str3="""Edureka"""

print(str1)
#Welcome
print(str2)
#to
print(str3)
#Edureka

string="Python"
print(string)
#Python
print(len(string))
#6
print(string[1:3])
#yt
print('t' in string)
#True

print("Welcome to %s"%("Python"))
#Welcome to Python
print("My name is %s and my age is %d"%("Gyanesh",24))
#My name is Gyanesh and my age is 24

print(dir(str1))
'''
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', 
'__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', 
'__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', 
'__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', 
'__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 
'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 
'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 
'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 
'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 
'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 
'title', 'translate', 'upper', 'zfill']
'''

str1='edureka'
print(str1.capitalize())
#Edureka

print(str1.count("ka"),0,len(str1))
#1 0 7  (1: No. of times "ka" present in string, 0: Begin, 7: len(str1))

s=str1.encode('utf-8', 'strict')
print(s)
#b'edureka'

print(max(str1))
#u
print(min(str1))
#a

print(str1.replace('e','--E--',1))
#--E--dureka
print(str1.replace('e','--E--',2))
#--E--dur--E--ka
print(str1.upper())
#EDUREKA
print(str1.index('k'))
#5

str1="Happy Learning"
print(str1[::-1])
#gninraeL yppaH

print(str1[2:7])
#ppy L