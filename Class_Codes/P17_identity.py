'''
Identity Operators: 

is: Evalutes to TRUE if the variables on either side of the operator point to the same object and FALSE otherwise.

is not: Evalutes to FALSE if the variables on either side of the operator point to the same object and TRUE otherwise.

Identity/Membership operators always returns Boolean value(TRUE/FALSE).
'''

a=[1,2,3,4]
b=[1,2,3,4]
c=[4,5,6,7]
d=[3,2,1,4]

print(a is b)       #FALSE
print(a is c)       #FALSE
print(a is d)       #FALSE
print(b is c)       #FALSE
print(b is d)       #FALSE
print(c is d)       #FALSE

'''
Here everything is false because, all variables a, b, c, d are not same objects but they are different objects.
Even if elements in and b are same but they are not same objects. Hence, membership testing fails for a and b.
Let's verify our statement by checking the address of both variables.
'''
print(id(a))    #47859192
print(id(b))    #47860352
'''
Here address of both variables are different means they are not same objects.
'''
e = a
print(a is e)   #TRUE
print(id(a))    #47859192
print(id(e))    #47859192
'''
Here this statement is True because a and e are both same objects as we can confirm the same with the address of both variables.
'''

'''
But if a and b are compared with comparison operator, then it will be true. Because, comparison operator will check if the values are same or not. whereas,
is operator checks for memory reference.
'''
print(a == b)   #True

'''
NOTE: whenever you are trying to compare two elements or two objects which have been generated in different environments or in different segments of the codes
in different ways then we should not use 'MEMBERSHIP' operation.
'''

'''
Q] When e = a then what is it for?
Ans: Creating the new copy element e from existing element a where the address reference remains the same.

Q] What is the use of membership operation?
Ans: It is used to check whether a value is of certain type or not
'''

print(a[0])     #1
print(a[1])     #2
print(a[2])     #3
print(a[3])     #4

subset_a=a[1:3]
print(subset_a)     #[2, 3]
print(subset_a is a)    #False
print(id(a))        #28591608
print(id(subset_a)) #61379448

'''
is not: It is simply the opposite of is
'''
print(subset_a is a)    #False
print(subset_a is not a)    #True