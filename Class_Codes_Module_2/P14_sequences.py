#Sequence Operation on various sequences:
##############################################################################################
#List:
item_1=[1,2,3,4,5,'a','b','c','d','e']
item_2=[6,7,8,9,0,'f','g','h','i','j']

print(item_1+item_2)    #Concatination

#O/P:
#[1, 2, 3, 4, 5, 'a', 'b', 'c', 'd', 'e', 6, 7, 8, 9, 0, 'f', 'g', 'h', 'i', 'j']
'''
Here sequences got concatinated due to '+' operator.
'''

item_1=[1,2,3,4,5]
item_2=[6,7,8,9,0]

print(item_1+item_2)    #Concatination

#O/P:
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
'''
Here also sequences got concatinated due to '+' operator even if values are integers instead of
adding values.
'''

print(item_1 * 2)   #Repetition

#O/P:
#[1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
'''
NOTE: For sequences, * operator will act as Repetition operator.
'''

print(1 in item_1)  #Membership Testing

#O/P:
#True

print(1 not in item_1)  #Membership Testing

#O/P:
#False

print(item_1[2])    #Indexing
#O/P: 3
'''
Indexing will give element present at specific index.
'''
print(item_2[1:4])  #Slicing[start, stop-1]
#O/P:
#[7,8,9]
#########################################################################################
#Tuples:

item_1=(1,2,3,4,5,'a','b','c','d','e')
item_2=(6,7,8,9,0,'f','g','h','i','j')

print(item_1+item_2)    #Concatination

#O/P:
#(1, 2, 3, 4, 5, 'a', 'b', 'c', 'd', 'e', 6, 7, 8, 9, 0, 'f', 'g', 'h', 'i', 'j')
'''
Here sequences got concatinated due to '+' operator.
'''

item_1=(1,2,3,4,5)
item_2=(6,7,8,9,0)

print(item_1+item_2)    #Concatination

#O/P:
#(1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
'''
Here also sequences got concatinated due to '+' operator even if values are integers instead of
adding values.
'''

print(item_1 * 2)   #Repetition

#O/P:
#(1, 2, 3, 4, 5, 1, 2, 3, 4, 5)
'''
NOTE: For sequences, * operator will act as Repetition operator.
'''

print(1 in item_1)  #Membership Testing

#O/P:
#True

print(1 not in item_1)  #Membership Testing

#O/P:
#False

print(item_1[2])    #Indexing
#O/P: 3
'''
Indexing will give element present at specific index.
'''
print(item_2[1:4])  #Slicing[start, stop-1]
#O/P:
#[7,8,9]
############################################################################################

