'''
Lists: List is the most versatile datatype available in Python, which can be written as a list
of comma-separated values(items) between square brackets.

Lists are mutable in nature
'''
list1=['abc','def','ghi','jkl','mno']
'''
On this list we can do all sequence operation:
->Concatination
->Membership Testing
->Indexing
->Slicing
->Repitition
'''
print(list1)    #Prints entire list
#O/P:
#['abc', 'def', 'ghi', 'jkl', 'mno']
print(list1[1]) #Indexing to get 2nd value
#O/P:
#def
'''
Slicing:
Syntax:
sequence[start:stop+1:step]
So, if we are taking slice from 1 to 4 index then we have to write sequence as follows:
sequence[1:5]
O/P: 1234
'''
print(list1[:5])    #Slicing to get values from index 0 to 4
#O/P:
#['abc', 'def', 'ghi', 'jkl', 'mno']
print(list1[:3])    #Slicing to get values from index 0 to 2
#O/P:
#['abc', 'def', 'ghi']
print(list1[::2])   #Print element from 0 to n with the stepping of 2
#O/P:
#['abc', 'ghi', 'mno']

print(list1*2)      #Repitition of list
#O/P:
#['abc', 'def', 'ghi', 'jkl', 'mno', 'abc', 'def', 'ghi', 'jkl', 'mno']

print(list1[-1:])   #Printing last element
#O/P:
#['mno']
print(list1[-2:])   #Printing last two element
#O/P:
#['jkl', 'mno']
print(list1[0:-2])   #Printing all element except last two element
#O/P:
#['abc', 'def', 'ghi']

print(list1[::-1])   #Printing all element in Reverse
#O/P:
#['mno', 'jkl', 'ghi', 'def', 'abc']
print(list1[::-2])   #Printing all element in Reverse direction with stepping of 2
#O/P:
#['mno', 'ghi', 'abc']


print(list1)
#['abc', 'def', 'ghi', 'jkl', 'mno']

del(list1[2]) #del function will delete particular element from the list.
print(list1)
#O/P:
#['abc', 'def', 'jkl', 'mno']
'''
Due to del() 2nd element from the list has been deleted
'''

list1[2]='123'  #Updation - Updating the list
print(list1)
#O/P:
#['abc', 'def', '123', 'mno']
'''
Due to updation, list is updated with the new value provided overwriting old value at that particular index
'''

print(list1)
#['abc', 'def', '123', 'mno']
print(list1.pop(2))     #pop(index)
#123
print(list1)
#['abc', 'def', 'mno']
'''
pop(index) -> It pops out the particluar element from the list.
'''

print(list1)
#['abc', 'def', 'mno']
list1.remove('mno')     #remove(element)
print(list1)
#['abc', 'def']
'''
remove() -> It removes particluar object from the list.
'''

print(type(list1))      #type(list): It gives the datatype of the variable.
#<class 'list'>

print(list1)
#['abc', 'def']
list1.append("Hello")   #append(element): Adds an item at the end of the list
print(list1)
#['abc', 'def', 'Hello']

list1.extend('Namaste')     #extend(element): Inserts many items at the end of list.
print(list1)
#['abc', 'def', 'Hello', 'N', 'a', 'm', 'a', 's', 't', 'e']
'''
NOTE: extend() takes only 1 argument and it inserts char and string object as form of char only.
'''

list1.extend(['Hello'])
print(list1)
#['abc', 'def', 'Hello', 'N', 'a', 'm', 'a', 's', 't', 'e', 'Hello']
'''
Here, with extend function we can add list items in existing list.
'''

list1.insert(2,"Pranam")
print(list1)
#O/P:
#['abc', 'def', 'Pranam', 'Hello', 'N', 'a', 'm', 'a', 's', 't', 'e', 'Hello']
'''
insert(index, Value): Insert function inserts elements in a list at particular index.
'''

list1.remove('Hello')   #remove(element): It removes particular item from list
print(list1)
#O/P:
#['abc', 'def', 'Pranam', 'N', 'a', 'm', 'a', 's', 't', 'e', 'Hello']

print(sorted(list1))    #sorted(list)
#['Hello', 'N', 'Pranam', 'a', 'a', 'abc', 'def', 'e', 'm', 's', 't']
'''
sorted(list): It sorts elements in a list as per ASCII characters of the very first letter in a string.
'''

'''
Tuples inside a List:
'''

list2=[(1,2,3),("Hello", "Bye")]    #Tuples inside a list
print(list2)
#[(1, 2, 3), ('Hello', 'Bye')]
print(len(list2))   #Length of list inside a Tuple.
#2
print(list2[1][0:1])    #Printing 0st element from 1st tuple.
#('Hello',)
