#Scope of a Variable:
#Global Varables:
'''
The variables which are declared out of the function and can be accessed anywhere in the program
are called as Global Variables.
'''
#Local Variables:
'''
The variables which are declared inside of the function and can be accessed only inside the function
are called as Local Variables.
'''

a=50
def num():
    b=10
    print(a)    #50 - Global variable
    print(b)    #10  - Local variable

print(a)    #50 - Global Variable
num()

