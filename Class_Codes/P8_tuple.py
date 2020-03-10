'''
Apart from Numbers and string data types, Another data type which is immutable in nature in python is "Tuple".
Tuple: Tuple consists of a Number of values separated by comma.
Tuple is always represented by small bracket () as it is enclosed within paranthesis.

'''
tuple1=(1,2,3,4,5,6)
print(id(tuple1))
print(tuple1)

#O/P:
#49929608
#(1, 2, 3, 4, 5, 6)

'''
In Tuple we can have multiple data types unlike as an Arrays in C.
'''

tuple1=(1,2,3,'4',5.2,6j+2,"ab")
print(id(tuple1))
print(tuple1)

#O/P:
#49929888
#(1, 2, 3, '4', 5.2, (2+6j), 'ab')

'''
Here each and every data type has been properly identified and alloted by python inside a tuple.
Here both tuples are different since tuple is immtable data type. That we have confirmed with address of both tuples. First tuple is recycled
'''

'''
-->In Tuple, because Tuple is immutable in nature, If we want to access specific elements in a tuple and try to change that value then we get
TypeError.
'''
print(tuple1[1])
#O/P: 2
tuple1[1]=202
print(tuple1[1])
#O/P:
#TypeError: 'tuple' object does not support item assignment