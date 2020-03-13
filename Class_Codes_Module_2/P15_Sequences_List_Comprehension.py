'''
List Comprehension is an easier and more readable way to create a list. 
'''
#1. Print n for n items in nums
#For Loops
nums=[1,2,3,4,5,6,7,8,9,10]
my_list=[]
for n in nums:
    my_list.append(n)
print(my_list)
#O/P: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#List Comprehension:
my_list_com=[n for n in nums]
print(my_list_com)
#O/P: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
'''
So, with list comprehension, for loop statement is simplified in single line
'''

#2. Print n*n for n items in nums:
#For loop:
my_list=[]
for n in nums:
    my_list.append(n*n)
print(my_list)
#O/P: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#List Comprehension:
my_list_c=[n*n for n in nums]
print(my_list_c)
#O/P: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#3. Print n only if it is even from nums list
#For Loop
my_list=[]
for n in nums:
    if n%2==0:
        my_list.append(n)
print(my_list)
#O/P: [2, 4, 6, 8, 10]

#List Comprehension:
my_list=[n for n in nums if n%2==0]
print(my_list)
#O/P: [2, 4, 6, 8, 10]
