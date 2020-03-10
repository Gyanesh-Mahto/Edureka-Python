#Immutable Data Types - 1. Numbers

var_1=101   #<class 'int'>
var_1=202.2  #<class 'float'> 
print("The address of var_1 is {} and the data type is {}".format(id(var_1), type(var_1)))
print("The address of var_1 is {} and the data type is {}".format(id(var_1), type(var_1)))

#O/P:
#The address of var_1 is 93833785540768 and the data type is <class 'int'>
#The address of var_1 is 139753337581928 and the data type is <class 'float'>
#139753337581928

'''
Here after updating new value to variable var_1, the old address is junked out and the 
variable var_1 is allocated with new memory when new value is assigned to it. 
'''

var_1=101   #<class 'int'>
var_2=202.2  #<class 'float'> 
var_3=30j+9     # <class 'complex'>
print(var_1)
print("The address of var_1 is {} and the data type is {}".format(id(var_1), type(var_1)))
print(var_2)
print("The address of var_2 is {} and the data type is {}".format(id(var_2), type(var_2)))
print(var_3)
print("The address of var_3 is {} and the data type is {}".format(id(var_3), type(var_3)))

#O/P:
#101
#The address of var_1 is 94809548624032 and the data type is <class 'int'>
#202.2
#The address of var_2 is 139914869928296 and the data type is <class 'float'>
#(9+30j)<------Here first real part is stored in system and then imaginary part
#The address of var_3 is 139914869397712 and the data type is <class 'complex'>

'''
Please remember the keyword which we have to use is only j for complex numbers. Other Letters then
j will give syntactical error
Here var_3=30j+9, In which:
30j-->Imaginary Number
9-->Real Number
'''