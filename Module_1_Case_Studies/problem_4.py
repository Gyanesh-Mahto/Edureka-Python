'''
4. Write a program that accepts a sentence and calculate the number of letters and digits. 
Suppose if the entered string is: Python0325 
Then the output will be: 
LETTERS: 6 
DIGITS:4 
'''
str_1=input("Please enter a string: ")
sent_1=list(str_1.strip())
print(sent_1)
l=len(sent_1)
i=0
digits=0
letters=0
while i<l:
    if sent_1[i]>='a' and sent_1[i]<='z':
        letters+=1
    elif sent_1[i]>='A' and sent_1[i]<='Z':
        letters+=1
    elif sent_1[i]>='0' and sent_1[i]<='9':
        digits+=1
    i+=1

print("Letters: {}".format(letters))
print("Digits: {}".format(digits))
