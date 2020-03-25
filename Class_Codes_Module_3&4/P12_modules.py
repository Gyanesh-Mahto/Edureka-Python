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

import os

print(os.name)  #posix

print(os.environ)   #Environment

print(os.getppid())     #507: pep id

print(os.getcwd())  #Get Current Working Directory

print(os.chdir("/home/mga/Desktop/Edureka/Module_3_&_4/Class_Codes_Module_3&4"))    #Change current Working Directory

print(os.mkdir("/home/mga/Desktop/Edureka/Module_3_&_4/Demo_folder")) #Creates Demo_folder directory in given path

print(os.rmdir("/home/mga/Desktop/Edureka/Module_3_&_4/Demo_folder"))   #Deletes directory from a given path

'''
chdir, mkdir, rmdir are some of the most important commands of OS module.
'''
#os.path module:
print(os.path.join('/home/mga/Desktop','/home/mga/Downloads'))
# Takes one or more paths and joins them by using the current OS's path separator
#O/P: /home/mga/Downloads
print(os.path.abspath('/home/mga/Desktop/Edureka/Module_3_&_4/Class_Codes_Module_3&4'))
#Takes a relative pathname and returns the corresponding absolute pathname
#O/P: /home/mga/Desktop/Edureka/Module_3_&_4/Class_Codes_Module_3&4

print(os.path.normpath('/home/mga/Desktop/Edureka/Module_3_&_4/Class_Codes_Module_3&4'))
#Converts path names from nonstandard format to standard format
#O/P: /home/mga/Desktop/Edureka/Module_3_&_4/Class_Codes_Module_3&4

print(os.path.split('/home/mga/Desktop/Edureka/Module_3_&_4/Class_Codes_Module_3&4/P10_object_oriented_Programming.py'))
#Takes a pathname and returns it in two parts: the directory part and the filename
#('/home/mga/Desktop/Edureka/Module_3_&_4/Class_Codes_Module_3&4', 'P10_object_oriented_Programming.py')

print(os.path.exists('/home/mga/Desktop/Edureka/Module_3_&_4/Class_Codes_Module_3&4'))
#Takes a pathname and returns true if it exists
#True

print(os.path.isdir('/home/mga/Desktop/Edureka/Module_3_&_4/Class_Codes_Module_3&4'))
#Takes a pathname and returns true if it points to a directory
#O/P: True

print(os.path.isdir('/home/mga/Desktop/Edureka/Module_3_&_4/Class_Codes_Module_3&4/P10_object_oriented_Programming.py'))
#O/P: False since pathname is pointing to a file.

print(list(os.walk('/home/mga/Desktop/Edureka/Module_3_&_4/Class_Codes_Module_3&4')))
#O/P:
#[('/home/mga/Desktop/Edureka/Module_3_&_4/Class_Codes_Module_3&4', ['__pycache__'], 
# ['P9_06_Class_Variable_Instance_Variable.py', 'P9_07_Constructor_and_Destructor.py', 
# 'P2_one.py', 'P11_Modules_&_Handling_Exceptions.txt', 'P9_02_class.py', 'P4_0_lambda_functions.py', 
# 'P1_Functions.py', 'P7_Keyword_Arguments.py', 'P9_04_Attributes_in_class.py', 
# 'Functions_OOPs.txt', 'P9_05_Public_Protected_Private_Attributes.py', 
# 'P10_Object_oriented_Programming.py', 'P9_01_OOPs_vs_POP.txt', 'P2_concept_of_main.txt', 
# 'P12_modules.py', 'P8_Variable_length_arguments.py', 'P4_1_Map_Filter_Reduce.py', 
# 'P3_inbuilt_functions.txt', 'P3_enumerate.py', 'P6_Memory_Address.py', 
# 'P5_Scope_of_a_variable.py', 'P2_two.py', 'P9_03_Methods_within_class.py']), 
# ('/home/mga/Desktop/Edureka/Module_3_&_4/Class_Codes_Module_3&4/__pycache__', [], 
# ['P2_one.cpython-37.pyc'])]
'''
os.walk() will generate tuple of path, folders, files present in given path and will keep on
traversing the subfolders
'''

##Math-Theoretic Functions:
'''
This module is always available. It provides access to the mathematical functions
'''
import math
print(math.ceil(10.098))    #11
#Returns the ceiling of x as a integer

print(math.copysign(10,-1)) #-10.0
#Returns x with the sign of y. On a platform that supports signed zeros, copysign(1.0,-0.0)
#returns -1.0

print(math.fabs(-19.7))     #19.7
#Returns positive value of entered negative value

#math - power and logarithmic function
print(math.exp(5))  #148.4131591025766
#Returns e**x

print(math.expm1(2))    #6.38905609893065
#Returns e**x-1

print(math.log(10, 10))   #1.0
#With one argument, return the natural logarithm of x(to base 10)

#math - Trigonometric Functions
print(math.acos(0.5))   #1.0471975511965979
#Return the arc cosine (measured in radians) of x.

print(math.asin(0.5))   #0.5235987755982989
#Return the arc sine (measured in radians) of x.

print(math.atan(0.5))   #0.4636476090008061
#Return the arc tangent (measured in radians) of x.

print(math.cos(0.5))    #0.8775825618903728
#Return the cosine of x (measured in radians).

print(math.degrees(0.5))    #28.64788975654116
#Convert angle x from radians to degrees.

print(math.radians(0.5))    #0.008726646259971648
#Convert angle x from degrees to radians.
