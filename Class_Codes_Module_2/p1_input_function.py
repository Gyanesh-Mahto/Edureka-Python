'''
input function: The input function is a function which tells the program that at this particular
moment you need to take some information from the console which is being used by the user.

So, whenever the program wants to take some information from the user or the console, we make
use of the input function.
'''
'''
Reading Keyboard Input:
-Python provides a built-in function to read a line of text from the standard function: input
-->Input function will take input in form of string.
'''
import sys

name=input("Please enter your name: ")

subject=input("Please enter your subject: ")

print("Hello {}, in this subject {}, you have obtained {} marks".format(name, subject, sys.argv[1]))
'''
Here while running the program we need to enter the marks as command line argument.
'''
#marks=int(input("Please enter your marks"))

'''
I/P: python p1_input_function.py  78
O/P: 
Please enter your name: Rakshat
Please enter your subject: Physics
Hello Rakshat, in this subject Physics, you have obtained 78 marks
'''
print(sys.argv)
#O/P:
#['p1_input_function.py', '78']

name=input("Please enter your name: ")
subject=input("Please enter your subject: ")
marks=int(input("Please enter your marks: "))
'''
Since input function will take all input in form of string, we need to typecast it into integer.
'''
print("Hello {}, in this subject {}, you have obtained {} marks".format(name, subject, marks))
'''
I/P:
Please enter your name: Gyanesh
Please enter your subject: History
Please enter your marks: 98
O/P:
Hello Gyanesh, in this subject History, you have obtained 98 marks
'''