'''
9.With a given list [12,24,35,24,88,120,155,88,120,155], 
write a program to print this list after removing all duplicate values with original order 
reserved.
'''
list_1=[12,24,35,24,88,120,155,88,120,155]
list_2=[]
for i in list_1:
    if i not in list_2:
        list_2.append(i)

print(list_2)
'''
O/P: [12, 24, 35, 88, 120, 155]
'''