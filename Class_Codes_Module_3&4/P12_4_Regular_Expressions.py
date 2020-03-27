#Regular Expressions:
#--------------------#
'''
A Regular Expression is a special text string for describing a search pattern.
-->Regular Expression in itself is a programming language which deals with only and only strings.
Example:
Can you identify the pattern to get the Name and Age:
Nameage=""
Janice is 22 and Theon is 33
Gabriel is 44 and Joey is 21

{"Janice":"22", "Theon":"33",
"Gabriel":"44", "Joey":"21"}

First letter of all the Names is an uppercase letter and Age is represented by Numbers.
'''
#Regular Expression Operations:
'''
Find a word in a string
Generate an iterator
Match one of any of several letters
Match series of range of characters
Replace String
Match a Single character
'''
'''
The replace method of strings is used to replace all occurences of one string with another, and
the index method is used to find the first occurence of a substring in a string. But sometimes you
need to do a more sophisticated search or replace then Regular Expression is used.
'''
import re
print(re.sub(r'[ad]', '*', 'abcde abcedf abcdef'))
'''
We can use square brackets to indicate that we only want to match certain letters. It replaces
every a and d with asterisks.
'''
#O/P: *bc*e *bce*f *bc*ef

print(re.sub(r'abc', '*', 'abcdef abcdef')) #Replaces all occurrences of abc with *
#O/P: *def *def


