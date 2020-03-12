'''
Lists: List is the most versatile datatype available in Python, which can be written as a list
of comma-separated values(items) between square brackets.

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



