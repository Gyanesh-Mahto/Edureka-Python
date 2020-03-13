'''
8.With   two   given   lists   [1,3,6,78,35,55]   and   [12,24,35,24,88,120,155],
write   a program to make a list whose elements are intersection of the above given lists.
'''
list_1=[1,3,6,78,35,55]
list_2=[12,24,35,24,88,120,155]

set_list_1=set(list_1)
set_list_2=set(list_2)

set_list_3=set_list_1 & set_list_2  #Intersection

list_3=list(set_list_3)
print(list_3)

#O/P: [35]