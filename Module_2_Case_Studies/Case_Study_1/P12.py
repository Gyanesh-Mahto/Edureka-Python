'''
12. By using list comprehension, please write a program to print the list 
after removing delete numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155]. 
'''
list_1=[12,24,35,70,88,120,155]
new_list=[n for n in list_1 if n%5==0 and n%7==0]
print(new_list)

#O/P: [35, 70]

