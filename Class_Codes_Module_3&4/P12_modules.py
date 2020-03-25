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
From import statement allows you to import specific attribute from a specific module into the
current namespace.
'''
#example:
from math import sqrt
print(sqrt(4))  #2.0
'''
This statement does not import the entire module, it just imports required files in the
module.
'''

#From import * statement
'''
The from...import * allows you to import all the attributes from the required module.
This provides an easy way to import all the items from a module into the current namespaces.
'''
#from math import *

#The Reload Function:
'''
When the module is imported into a script, the code in the top-level portion of a module is
executed only once. Therefore, if you want to re-execute the top-level code in a module, 
you can use the reload function. The reload function imports a previously imported module again.
'''

##Important Modules used in python:
'''
Modules:
-> sys
-> os
-> math
-> datetime
-> random
-> json
'''

#sys module:
#-----------#
'''
-> This module provides access to some variables used or maintained by the interpreter and to
functions that interact strongly with the interpreter. It is always available because when we
install python, then this module is installed.
'''
import sys
print(sys.argv)    #['P12_modules.py'] (stores any command line argument passed)
#print(sys.exit())   #It informs the python interpreter to quit.

print(not sys)
#Returns False if module is imported, else True
print(sys.flags)
#Returns the struct sequence flags and exposes the status of command line flags
print(sys.prefix)
#Returns a string giving the site-specific directory prefix where the platform independent python
#files are installed
'''
O/P:
False
sys.flags(debug=0, inspect=0, interactive=0, optimize=0, dont_write_bytecode=0, no_user_site=0, no_site=0, ignore_environment=0, verbose=0, bytes_warning=0, quiet=0, hash_randomization=1, isolated=0, dev_mode=False, utf8_mode=0)
/home/mga/anaconda3
'''

##os module:
#-----------#
'''
os module:
-----------
-> The os module includes code that lets Python work with your operating system and run some
operating system commands.
'''
import os
print(os.getcwd())

print(os.chdir("~/Desktop/Edureka"))

print(os.mkdir("test"))

print(os.rmdir("~/Desktop/Edureka/test"))
