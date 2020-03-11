import sys
import os   #This module supports file system

newfile=open("Test_File",'w+')  #This command 'w+' creates new file and opens it

name=input("Please enter your name: ")
subject=input("Please enter subject: ")
marks=int(input("Please enter your marks: "))
str1="Hello {}, In subject {}, you have scored {} marks".format(name,subject,marks)

newfile.write(str1)     #This code writes str1 date in newfile.
newfile.close()     #After completing the code we need to close the file.

'''
I/P:
Please enter your name: Gyanesh
Please enter subject: Maths
Please enter your marks: 99

O/P:
Creates a newfile "Test_File" in same directory and stores data as follows:
Hello Gyanesh, In subject Maths, you have scored 99 marks
'''
'''
Please NOTE: If we use w+ and again run the same file with different input, then data will be
overwritten in same file.
'''
