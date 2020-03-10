'''
Membership Operators:

in: The ‘in’ operator is used to check if a value exists in a sequence or not.
Evaluates to true if it finds a variable in the specified sequence and false otherwise.

not in: Evaluates to true if it does not finds a variable in the specified sequence and false otherwise.
'''
a=[1,2,3,4]
b=[1,2,3,4]
c=[4,5,6,7]
d=[3,2,1,4]
e = a
print(a in b)       #FALSE
print(a in c)       #FALSE
print(a in d)       #FALSE
print(b in c)       #FALSE
print(b in d)       #FALSE
print(c in d)       #FALSE
print( a in e)

subset_a=a[1:3]

print(subset_a)     #[2, 3]
print(subset_a in a)    #False