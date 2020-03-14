'''
11. By using list comprehension, please write a program to print the list after removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155].
'''
list_1=[12,24,35,70,88,120,155]
new_list=[n for n in list_1 if n!=list_1[0] and n!=list_1[4] and n!=list_1[5]]
print(new_list)

#O/P: [24, 35, 70, 155]