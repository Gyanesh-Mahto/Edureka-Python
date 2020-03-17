'''
Variable-length Arguments: When we need to process a function for more arguments than you have specified while defining the function, 
So, variable-length arguments can be used.
'''
def myFunction(arg1, arg2, arg3, *args, **kwargs):
    print("First Normal Argument: "+str(arg1))
    print("Second Normal Argument: "+str(arg2))
    print("Third Normal Argument: "+str(arg3))
    print("Non-Keyworded Argument: "+str(args))
    print("Keyworded Argument: "+str(kwargs))

myFunction(1,2,3,4,5, name="Mandar", country="India", age=25)   #When a dictionary is passed in function, then it is collected in function using **kwargs
'''
O/P:
First Normal Argument: 1
Second Normal Argument: 2
Third Normal Argument: 3
Non-Keyworded Argument: (4, 5)
Keyworded Argument: {'name': 'Mandar', 'country': 'India', 'age': 25}
'''

'''
def info(user, *users):
    print("Users of Python:")
    print(user)
    for var in users:
        print("Users of Python")
        print(var)
        return()

info("Annie")           #Single variable or multiple variables can be passed as an arguments to the same function.
info("Annie", "Dave")
'''
'''
O/P:
Users of Python:
Annie
Users of Python:
Annie
Users of Python
Dave
'''