'''
Sets: Set is an unordered collection of unique items. Set is defined by values separated by comma inside
braces {}
Sets can also be created by calling the built-in function:
x=set("Welcome To Edureka")
print(x)

Operations on Sets:
-> Intersection: Intersection of set A and set B are elements which are common in both sets.
                 Intersection is performed using & operator.
-> Union: Union of set A and set B are set of all elements which are present in both sets.
          Union is performed using | operator.
-> Difference: Difference of set A and set B are set of elements from set A which are not present
               in set B. Difference is performed using - operator.
'''
x=set("Welcome To Edureka")
print(x)
#{'E', 'l', 'o', ' ', 'T', 'u', 'W', 'c', 'm', 'e', 'a', 'r', 'k', 'd'}
print(x)
#{'E', 'd', 'r', ' ', 'e', 'm', 'W', 'k', 'c', 'a', 'o', 'l', 'T', 'u'}
'''
Here each and every character is unique but in unorder collection
'''
'''
Q. When to use sets?
->If we wish to collect unique strings or integers from a sequence then we should use sets.

Example:
College administration is facing problem, because during information feeding, many students are
entering same password and ID
As we know, Sets supports unique elements. So, we can convert the lists of IDs and passwords
into sets and can get only Unique ones.
'''

A={1,2,3,4}
B={3,4,5,6}
print(A & B)    #Intersection:
#{3, 4}
print(A | B)    #Union
#{1, 2, 3, 4, 5, 6}

s={'a','b','c','d','e','f','o','v'}
set1={'a','b','d','o','v'}  #Subset of s
set2={'a','c','d','o','e'}  #Subset of s
print(set1 | set2)    #Union
#{'e', 'a', 'b', 'c', 'd', 'o', 'v'}
print(set1 & set2)    #Intersection
#{'a', 'o', 'd'}
print(set1 - set2)      #Difference
#{'b', 'v'}
print(set2 - set1)      #Difference
#('c', 'e')
'''
In Difference of sets, only those element is returned from first set which are not present in 
second set.
'''
s={'a','b','c','d','e','f','o','v','a','b','c','d','e','f','o','v','a','b','c','d','e','f','o','v'}
print(s)
#{'d', 'f', 'a', 'o', 'b', 'e', 'c', 'v'}
'''
Here only unique elements are present in set s
'''

s={1,2,3,'a','b'}   #Superset
set1={1,'a','b'}    #Subset
print(1 in s)
#True
print(5 not in s)
#true
print(s.issuperset(set1))   #Report whether this set contains another set.
#True
print(s.union(set1))    #Return the union of sets as a new set.
#{1, 2, 3, 'a', 'b'}
print(s.intersection(set1))     #Return the intersection of two sets as a new set.
#{1, 'a', 'b'}
print(s.difference(set1))   #Return the difference of two or more sets as a new set.
#{2,3}
print(s.symmetric_difference(set1))     #Return the symmetric difference of two sets as a new set.
#{2,3}

print(s)   
#1,2,3,'a','b'}
s.add('c')      #Add an element to a set. This has no effect if the element is already present.
print(s)
#{1, 2, 3, 'b', 'a', 'c'}

s.remove(1)     ##Remove an element from a set; it must be a member.
print(s)
#{2, 3, 'b', 'a', 'c'}

s.remove('a')   #Remove an element from a set; it must be a member.
print(s)
#{2, 3, 'b', 'c'}

s.discard(3)    #Remove an element from a set if it is a member. If the element is not a member, do nothing.
print(s)
#{2, 'b', 'c'}

s.pop()     #Remove and return an arbitrary set element. Raises KeyError if the set is empty.
print(s)
#{'b', 'c'}

s.clear()   #clear(): Removes all elements from set
print(s)
#set() <-----------Empty set