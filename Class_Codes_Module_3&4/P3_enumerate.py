'''
enumerate():
-Return an enumerate object. The iterable must be a sequence, an iterator, or some other object
which supports iteration.
'''
grocery=['bread', 'milk', 'butter'] #Creating a list of grocery
enumerate_grocery=enumerate(grocery)
#Since, list is a sequence, enumerate object(enumerate_grocery) is created.
print(enumerate_grocery)            #<enumerate object at 0x7f4d0b5f3120>
print(type(enumerate_grocery))      #<class 'enumerate'>

#Converting to a list:
print(list(enumerate_grocery))      #[(0, 'bread'), (1, 'milk'), (2, 'butter')]
#For every item in grocery list, it has added an index value. And it is returning that in form of a tuple.
#Changing the default counter:
enumerate_grocery=enumerate(grocery, 10)
print(list(enumerate_grocery))      #[(10, 'bread'), (11, 'milk'), (12, 'butter')]

#Enumerate returns the list of tuples. Tuples consists index values and items from the list.
