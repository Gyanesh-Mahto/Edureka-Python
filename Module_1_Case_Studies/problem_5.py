'''
5. Design a code which will find the given number is Palindrome number or not.   
Hint: Use built-in functions of string. 
'''
num=int(input("Please enter a number: "))
temp=num
rev=0
while temp:
    rev=rev*10+temp%10
    temp=temp//10
if rev==num:
    print("Palindrome")
else:
    print("Not Palindrome")