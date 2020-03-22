#Moudles:
'''
Modules:
- A modules allows you to logically organize the code.
- Python Moudules are nothing but python files with .py extension
- A module is a file contaning Python definitions and statements.
'''
#Import:
'''
Use "import" to load a module in python. When the interpretor encounters an import statement,
it imports the module, if the module is present in the search path.
Example: import math

-Whenever we are using import statement, each and every piece of code there which is not defined
inside a function is executed. So, the codes which are global in nature is executed.
'''

#dir:
'''
A dir is a built in function which returns the list of strings containing the name defined by the
module. It gives the list of variables, functions defined in that module.
'''
import math
print(dir(math))
'''
['__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 
'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 
'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 
'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 
'log1p', 'log2', 'modf', 'nan', 'pi', 'pow', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 
'tan', 'tanh', 'tau', 'trunc']
'''

#from import statement:
'''

'''