'''
5.Please write a program which accepts a string from console and print the characters that have 
even indexes.
Example: If the following string is given as input to the program:
H1e2l3l4o5w6o7r8l9d
Then, the output of the program should be:Helloworld
'''
str_1=input("Please enter a string: ")
str_2=list(str_1.strip())
#print(str_2)
length=len(str_2)
#print(length)
for i in range(length):
    if i%2==0:
        print(str_2[i],end="")
print("\n")

'''
O/P: Helloworld
'''