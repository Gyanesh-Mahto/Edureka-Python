import sys
import os

newfile=open("Test_File","r+")

name=input("Please enter your name: ")
subject=input("Please enter your subject: ")
marks=int(input("Please enter your marks: "))

str1="Hello {}, You have scored {} marks in {} subject".format(name,marks,subject)

print(newfile.read())   #It will read pre-existing data in a newfile which is "Test_File"

newfile.write(str1)
print(newfile.read())
newfile.close()
'''
NOTE: r+ command is used to read and write data in a file. New data will be appended in file.

I/P:
Please enter your name: Gyanesh
Please enter your subject: Maths
Please enter your marks: 99

O/P:
Hello Gyanesh, You have scored 99 marks in Maths subject    #Pre-existing data in Test_File
Hello Gyanesh, You have scored 98 marks in Physics subject  #New data is appended after old data
 in Test_File
'''