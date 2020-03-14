'''
13. Please write a program to randomly generate a list with 5 numbers, which are divisible by 5 and 7 , between 1 and 1000 inclusive. 
'''
import random

new_list=[]
length=len(new_list)
for n in range(1001):
    rand_num=random.randrange(1,1001)
    if rand_num%5==0 and rand_num%7==0:
        new_list.append(rand_num)
        length+=1
    if length==5:
        break
print(new_list)

#O/P: [805, 175, 420, 945, 140]