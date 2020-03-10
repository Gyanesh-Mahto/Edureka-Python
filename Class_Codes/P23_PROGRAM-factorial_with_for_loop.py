#WAP for finding factorial of a number using FOR loop

num=int(input("Please enter you number: "))
n=1
fact=1
'''
while num>1:
    fact=fact*num
    num=num-1
'''
'''
for n in range(num):
    fact=fact*num
    num=num-1
'''

for k in range(1,num+1):
    fact=fact*k

print(fact)