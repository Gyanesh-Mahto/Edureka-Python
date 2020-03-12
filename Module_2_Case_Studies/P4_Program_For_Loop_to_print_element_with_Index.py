'''
4.Write a for loop that prints all elements of a list and their position in the list.
a = [4,7,3,2,5,9]
Hint: Use Loop to iterate through list elements
'''
a = [4,7,3,2,5,9]
length=len(a)
#print(length)
for i in range(length):
    print(a[i],"->Index",i)

'''
O/P:
4 ->Index 0
7 ->Index 1
3 ->Index 2
2 ->Index 3
5 ->Index 4
9 ->Index 5
'''