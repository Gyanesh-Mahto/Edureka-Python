'''
7.Please write a program which count and print the numbers of each character in a string input 
by console.
Example: If the following string is given as input to the program:
abcdefgabc
Then, the output of the program should be:
a,2
c,2
b,2
e,1
d,1
g,1
f,1
'''
str_1=input("Please enter a string: ")
list_str=list(str_1.strip())
#print(list_str)
res=[]
for i in list_str:
    if i not in res:
        res.append(i)
#print(res)
length=len(res)
for i in range(length):
    print(res[i],",",list_str.count(res[i]))

'''
I/P:Please enter a string: abcdefgabc
O/P:
a , 2
b , 2
c , 2
d , 1
e , 1
f , 1
g , 1
'''