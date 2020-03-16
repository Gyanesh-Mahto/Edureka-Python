#Memory Address:
'''
-> To check memory address of a variable, id() is used
'''
a=10
b=10
print(id(a))
print(id(b))
#O/P:
#94179604211008
#94179604211008


'''
We know that a and b are two different variables, but they wil have the same address.

We have variables a and b having a value 10. It doesn't mean that there will be 2 copies 10s in 
memory. There will be only one 10 and the variables a and b will point to this value.
'''