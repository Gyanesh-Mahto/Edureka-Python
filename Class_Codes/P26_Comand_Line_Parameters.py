'''
It is possible to pass arguments to Python programs when they are executed.
The brackets which follow main are used for this purpose.
.argv refers to the number of arguments passed, and argv[] is a pointer array which points to each argument which is passed to main.
The python sys module provides access to any command-line arguments via the sys.argv. This serves two purposes:
-->1. sys.argv is the list of command-line arguments
-->2. len(sys.argv) is the number of command-line arguments
'''
import sys
print("Number of arguments: ", len(sys.argv), "arguments.")
print("Arguments list:",str(sys.argv))

'''
I/P: 
python .\P26_Comand_Line_Parameters.py arg1 arg2 arg3

O/P:
Number of arguments:  4 arguments.
Arguments list: ['.\\P26_Comand_Line_Parameters.py', 'arg1', 'arg2', 'arg3']
'''

